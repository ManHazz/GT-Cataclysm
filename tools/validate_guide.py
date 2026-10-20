"""Validates patchouli_books/gtc_guide. Run: python -I tools/validate_guide.py"""
import json, re, zipfile, glob
from pathlib import Path
R = Path(__file__).resolve().parent.parent
B = R / "patchouli_books" / "gtc_guide"
TYPES = {"text","spotlight","crafting","smelting","image","link","relations","quest","entity","empty","multiblock","network_recipe"}
TEXTKEYS = ("text",)
err = []
json.loads((B/"book.json").read_text(encoding="utf-8"))
cats = {p.stem for p in (B/"en_us"/"categories").glob("*.json")}
for p in (B/"en_us"/"categories").glob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    if "parent" in d and ":" not in d["parent"]: err.append(f"{p.name}: unqualified parent")
def ids():
    s = set(); langs = {}
    for j in glob.glob(str(R/"mods"/"*.jar")):
        try: z = zipfile.ZipFile(j)
        except Exception: continue
        for n in z.namelist():
            m = re.match(r"assets/([^/]+)/(?:models/item|lang)/(.+)\.json$", n)
            if m and n.startswith(f"assets/{m.group(1)}/models/item/"):
                s.add(f"{m.group(1)}:{m.group(2)}")
            if "/lang/en_us.json" in n:
                try:
                    for k in json.loads(z.read(n)):
                        mm = re.match(r"item\.([^.]+)\.(.+)$", k) or re.match(r"block\.([^.]+)\.(.+)$", k)
                        if mm: s.add(f"{mm.group(1)}:{mm.group(2)}")
                except Exception: pass
    return s
VANILLA = {"book","barrier","raw_iron","writable_book","map","tnt"}
mats = set()
for j in glob.glob(str(R/"mods"/"gtceu*.jar")) + glob.glob(str(R/"mods"/"gregtech*.jar")):
    z = zipfile.ZipFile(j)
    for k in json.loads(z.read("assets/gtceu/lang/en_us.json")):
        if k.startswith("material.gtceu."): mats.add(k[15:])
def ok_dyn(it):
    ns, nm = it.split(":", 1)
    if ns == "minecraft": return nm in VANILLA
    if ns == "gtceu":
        m = re.fullmatch(r"(.+?)_(ingot|single_cable)", nm)
        return bool(m and m.group(1) in mats)
    return False
known = ids()
n = 0
for p in (B/"en_us"/"entries").rglob("*.json"):
    n += 1
    d = json.loads(p.read_text(encoding="utf-8"))
    c = d.get("category", "")
    if not re.fullmatch(r"[a-z0-9_.-]+:[a-z0-9_/.-]+", c) or c.split(":",1)[1] not in cats:
        err.append(f"{p.name}: bad category {c!r}")
    for k in ("advancement",):
        if k in d and ":" not in d[k]: err.append(f"{p.name}: unqualified {k}")
    items = [d.get("icon")]
    for i, pg in enumerate(d["pages"]):
        t = pg.get("type", "").replace("patchouli:", "")
        if t not in TYPES: err.append(f"{p.name} p{i}: bad type {pg.get('type')}")
        if "advancement" in pg and ":" not in pg["advancement"]: err.append(f"{p.name} p{i}: unqualified advancement")
        if len(pg.get("text", "")) > 350: err.append(f"{p.name} p{i}: text {len(pg['text'])} chars")
        if "item" in pg: items.append(pg["item"])
        if t == "link" and ":" not in pg.get("entry", "x:"): err.append(f"{p.name} p{i}: unqualified link")
    for it in items:
        if it and it not in known and not ok_dyn(it): err.append(f"{p.name}: unknown item {it}")
print(n, "entries,", len(cats), "categories,", len(known), "known item ids")
print("\n".join(err) if err else "VALID")
