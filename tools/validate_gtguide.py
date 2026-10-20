"""Validates the GuideME guide gtc:gtguide. Run: python -I tools/validate_gtguide.py
Checks: front matter is valid YAML with known keys; every item id in front matter and tags exists (GTCEu / AE2 /
Cataclysm / other mod jars in mods/, vanilla list from tools/gtguide_facts.json); every page is reachable from
index.md through navigation.parent; links between pages resolve; ImportStructure files exist, parse and are used
(no orphan structures); annotation coordinates fall inside the imported structure; RecipeFor ids have a
crafting-table recipe in the facts snapshot; Ponder copies of structures match."""
import glob, gzip, io, json, re, struct, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDE = ROOT / "kubejs/assets/gtc/guides/gtc/gtguide"
PONDER = ROOT / "kubejs/assets/gtc/ponder"
FACTS = json.loads((ROOT / "tools/gtguide_facts.json").read_text(encoding="utf-8"))
err, warn = [], []

try:
    import yaml
except Exception:  # minimal fallback parser for the restricted front matter this guide uses
    yaml = None


def parse_yaml(txt):
    if yaml:
        return yaml.safe_load(txt)
    data, cur = {}, None
    for line in txt.splitlines():
        if not line.strip():
            continue
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if m:
            k, v = m.groups()
            if v == "":
                data[k] = [] if k == "item_ids" else {}
                cur = k
            else:
                data[k] = v
            continue
        m = re.match(r"^  (\w+):\s*(.*)$", line)
        if m and isinstance(data.get(cur), dict):
            v = m.group(2)
            data[cur][m.group(1)] = json.loads(v) if v.startswith('"') else v
            continue
        m = re.match(r"^  - (\S+)$", line)
        if m and isinstance(data.get(cur), list):
            data[cur].append(m.group(1))
            continue
        raise ValueError("unparseable front matter line: " + line)
    return data


# ---------------------------------------------------------------- known ids
MODS = ROOT / "mods"
if "--mods" in sys.argv:
    MODS = Path(sys.argv[sys.argv.index("--mods") + 1]).resolve()


def known_ids():
    ids, mats = set(), set()
    jars = glob.glob(str(MODS / "*.jar"))
    if not jars:
        print(f"ERROR no mod jars in {MODS} - run `java -jar pakku.jar -y fetch` first or pass --mods <dir>")
        sys.exit(1)
    for j in jars:
        try:
            z = zipfile.ZipFile(j)
        except Exception:
            continue
        names = z.namelist()
        for n in names:
            m = re.match(r"assets/([^/]+)/models/item/(.+)\.json$", n)
            if m:
                ids.add(f"{m.group(1)}:{m.group(2)}")
        for n in names:
            m = re.match(r"assets/([^/]+)/lang/en_us\.json$", n)
            if not m:
                continue
            try:
                lang = json.loads(z.read(n))
            except Exception:
                continue
            for k in lang:
                mm = re.match(r"(?:item|block)\.([^.]+)\.(.+)$", k)
                if mm and not k.endswith(".tooltip") and ".tooltip" not in k:
                    ids.add(f"{mm.group(1)}:{mm.group(2)}")
                mm = re.match(r"material\.([^.]+)\.(.+)$", k)
                if mm:
                    mats.add(mm.group(2))
    for v in FACTS.get("vanilla_items", []):
        ids.add("minecraft:" + v)
    return ids, mats


KNOWN, MATS = known_ids()
SIZES = "single|double|quadruple|octal|hex"
PATS = [r"{m}_(ingot|dust|nugget|plate|gem|block|ore|foil|rod|ring|gear|rotor|bolt|screw|lens|spring)", r"(crushed|purified|refined)_{m}_ore",
        r"(impure|pure|small|tiny)_{m}_dust", r"{m}_(" + SIZES + r")_(cable|wire)", r"fine_{m}_wire", r"double_{m}_plate",
        r"{m}_(tiny|small|normal|large|huge|quadruple|nonuple)_fluid_pipe", r"(raw|hot)_{m}_(ingot|ore)", r"{m}_(" + SIZES + r")_cable"]


def exists(i):
    if i in KNOWN:
        return True
    ns, _, p = i.partition(":")
    if ns != "gtceu":
        return False
    for pat in PATS:
        m = re.fullmatch(pat.replace("{m}", "(?P<m>[a-z0-9_]+)"), p)
        if m and m.group("m") in MATS:
            return True
    return False


# ---------------------------------------------------------------- NBT (gzip) minimal reader
def nbt_read(path):
    f = io.BytesIO(gzip.decompress(path.read_bytes()))

    def s():
        return f.read(struct.unpack(">H", f.read(2))[0]).decode()

    def pay(t):
        if t in (1, 2, 3, 4, 5, 6):
            return struct.unpack(">" + "bhiqfd"[t - 1], f.read([1, 2, 4, 8, 4, 8][t - 1]))[0]
        if t == 7:
            return f.read(struct.unpack(">i", f.read(4))[0])
        if t == 8:
            return s()
        if t == 9:
            et = f.read(1)[0]
            n = struct.unpack(">i", f.read(4))[0]
            return [pay(et) for _ in range(n)]
        if t == 10:
            d = {}
            while True:
                tt = f.read(1)[0]
                if tt == 0:
                    return d
                k = s()
                d[k] = pay(tt)
        if t == 11:
            n = struct.unpack(">i", f.read(4))[0]
            return list(struct.unpack(f">{n}i", f.read(4 * n)))
        if t == 12:
            n = struct.unpack(">i", f.read(4))[0]
            return list(struct.unpack(f">{n}q", f.read(8 * n)))
        raise ValueError(t)

    assert f.read(1)[0] == 10
    s()
    return pay(10)


# ---------------------------------------------------------------- pages
pages = {}
for p in sorted(GUIDE.glob("*.md")):
    txt = p.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.S)
    if not m:
        err.append(f"{p.name}: missing front matter")
        continue
    try:
        fm = parse_yaml(m.group(1))
    except Exception as e:
        err.append(f"{p.name}: front matter is not valid YAML ({e})")
        continue
    if not isinstance(fm, dict) or not isinstance(fm.get("navigation"), dict):
        err.append(f"{p.name}: front matter needs a navigation mapping")
        continue
    nav = fm["navigation"]
    for k in nav:
        if k not in ("title", "icon", "parent", "position"):
            err.append(f"{p.name}: unknown navigation key {k}")
    for k in fm:
        if k not in ("navigation", "item_ids"):
            err.append(f"{p.name}: unknown front matter key {k}")
    if not isinstance(nav.get("title"), str) or not nav["title"]:
        err.append(f"{p.name}: navigation.title missing")
    if "position" in nav and not isinstance(nav["position"], int):
        err.append(f"{p.name}: navigation.position must be an int")
    pages[p.name] = dict(fm=fm, nav=nav, body=m.group(2))

if "index.md" not in pages:
    err.append("index.md missing")

# reachability
for name, pg in pages.items():
    seen, cur = {name}, name
    while True:
        par = pages[cur]["nav"].get("parent")
        if not par:
            break
        if par not in pages:
            err.append(f"{name}: parent {par} does not exist")
            break
        if par in seen:
            err.append(f"{name}: parent cycle")
            break
        seen.add(par)
        cur = par
    if cur != "index.md" and name != "index.md" and not any(e.startswith(f"{name}: parent") for e in err):
        err.append(f"{name}: not reachable from index.md (chain ends at {cur})")

# ids
TAG_ID = re.compile(r"<(ItemImage|ItemIcon|ItemLink|RecipeFor|Block)\b[^>]*?\bid=\"([^\"]+)\"")
CRAFTED = set(FACTS["crafted"])
used_structs = {}
for name, pg in pages.items():
    ids = list(pg["fm"].get("item_ids") or [])
    if pg["nav"].get("icon"):
        ids.append(pg["nav"]["icon"])
    for m in TAG_ID.finditer(pg["body"]):
        ids.append(m.group(2))
        if m.group(1) == "RecipeFor" and m.group(2) not in CRAFTED:
            err.append(f"{name}: RecipeFor {m.group(2)} has no crafting-table recipe in the facts snapshot")
    for i in ids:
        if not re.fullmatch(r"[a-z0-9_.-]+:[a-z0-9_/.-]+", str(i)):
            err.append(f"{name}: malformed id {i}")
        elif not exists(i):
            err.append(f"{name}: unknown item/block id {i}")
    # links
    for m in re.finditer(r"\]\(([^)#]+\.md)(?:#[^)]*)?\)", pg["body"]):
        if m.group(1) not in pages:
            err.append(f"{name}: link to missing page {m.group(1)}")
    # tag balance
    for tag in ("GameScene", "ItemGrid", "BlockAnnotation", "BoxAnnotation", "DiamondAnnotation", "LineAnnotation"):
        o = len(re.findall(rf"<{tag}\b(?![^>]*/>)", pg["body"]))
        c = len(re.findall(rf"</{tag}>", pg["body"]))
        if o != c:
            err.append(f"{name}: unbalanced <{tag}> ({o} open, {c} close)")
    # tables
    lines = pg["body"].splitlines()
    for i, l in enumerate(lines):
        if l.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[-| ]+\|$", lines[i + 1]):
            n = l.count("|")
            j = i
            while j < len(lines) and lines[j].startswith("|"):
                if lines[j].count("|") != n:
                    err.append(f"{name}: table row with wrong column count: {lines[j][:60]}")
                j += 1
    # scenes
    for sc in re.finditer(r"<GameScene\b.*?</GameScene>", pg["body"], re.S):
        txt = sc.group(0)
        sm = re.search(r"<ImportStructure\b[^>]*\bsrc=\"([^\"]+)\"", txt)
        size = None
        if sm:
            f = GUIDE / sm.group(1)
            used_structs.setdefault(f.resolve(), []).append(name)
            if not f.exists():
                err.append(f"{name}: ImportStructure file missing: {sm.group(1)}")
            else:
                try:
                    d = nbt_read(f)
                    size = d["size"]
                    pal = [b["Name"] for b in d["palette"]]
                    for b in pal:
                        if b != "minecraft:air" and not exists(b) and not b.startswith("minecraft:"):
                            err.append(f"{sm.group(1)}: unknown block {b}")
                except Exception as e:
                    err.append(f"{sm.group(1)}: not a readable structure NBT ({e})")
        elif "<Block " not in txt:
            err.append(f"{name}: GameScene without Block or ImportStructure")
        if size:
            for a in re.finditer(r"<BlockAnnotation\b[^>]*\bx=\"(-?\d+)\"[^>]*\by=\"(-?\d+)\"[^>]*\bz=\"(-?\d+)\"", txt):
                x, y, z = map(int, a.groups())
                if not (0 <= x < size[0] and 0 <= y < size[1] and 0 <= z < size[2]):
                    err.append(f"{name}: BlockAnnotation {x},{y},{z} outside structure {size}")
            for a in re.finditer(r"<BoxAnnotation\b[^>]*\bmin=\"([^\"]+)\"[^>]*\bmax=\"([^\"]+)\"", txt):
                mn = list(map(float, a.group(1).split()))
                mx = list(map(float, a.group(2).split()))
                if any(mn[k] < 0 or mx[k] > size[k] or mn[k] >= mx[k] for k in range(3)):
                    err.append(f"{name}: BoxAnnotation {a.group(1)} -> {a.group(2)} outside structure {size}")

# structures: orphans, ponder copies
sdir = GUIDE / "structures"
for f in sorted(sdir.glob("*.nbt")) if sdir.exists() else []:
    if f.resolve() not in used_structs:
        err.append(f"orphan structure (no page uses it): {f.name}")
    pf = PONDER / f.name
    if not pf.exists():
        warn.append(f"no Ponder copy of {f.name}")
    elif pf.read_bytes() != f.read_bytes():
        warn.append(f"Ponder copy of {f.name} differs")

print(f"{len(pages)} pages, {len(used_structs)} structures used, {len(KNOWN)} known base ids, {len(MATS)} materials")
for w in warn:
    print("WARN", w)
if err:
    print("\n".join("ERROR " + e for e in err))
    sys.exit(1)
print("VALID")
