#!/usr/bin/env python3
"""Audit Forge mod jars: duplicate modIds, missing mandatory deps, forge/minecraft ranges."""
import io, re, sys, zipfile, glob, os
try:
    import tomllib
except ImportError:
    print("Python 3.11+ required (tomllib)"); sys.exit(2)

FORGE, MC = (47, 4, 13), (1, 20, 1)
IGNORE = {"minecraft", "forge", "java"}

def vtuple(s):
    return tuple(int(x) for x in re.findall(r"\d+", s))

def nested_ids(jar):
    out = set()
    with zipfile.ZipFile(jar) as z:
        for n in z.namelist():
            if n.startswith("META-INF/jarjar/") and n.endswith(".jar"):
                try:
                    with zipfile.ZipFile(io.BytesIO(z.read(n))) as nz:
                        if "META-INF/mods.toml" in nz.namelist():
                            t = tomllib.loads(nz.read("META-INF/mods.toml").decode("utf-8", "replace"))
                            out.update(m["modId"] for m in t.get("mods", []) if "modId" in m)
                except Exception:
                    pass
    return out

def in_range(rng, v):
    """Maven version range; supports comma-separated intervals. Empty/none = any."""
    rng = (rng or "").strip()
    if not rng:
        return True
    if not rng[0] in "[(":
        return True  # bare version = soft requirement
    for m in re.finditer(r"([\[(])([^,\])]*)(?:,([^\])]*))?([\])])", rng):
        lo_b, lo, hi, hi_b = m.group(1), m.group(2).strip(), m.group(3), m.group(4)
        if hi is None:
            if vtuple(lo)[:len(v)] == v or vtuple(lo) == v: return True
            continue
        hi = hi.strip()
        ok = True
        if lo:
            t = vtuple(lo); ok &= v > t if lo_b == "(" else v >= t
        if hi:
            t = vtuple(hi); ok &= v < t if hi_b == ")" else v <= t
        if ok: return True
    return False

def main(d):
    problems = []
    provided = set()
    mods = {}      # modId -> [jar]
    deps = []      # (jar, modId, depId, range)
    for jar in sorted(glob.glob(os.path.join(d, "*.jar"))):
        name = os.path.basename(jar)
        try:
            with zipfile.ZipFile(jar) as z:
                if "META-INF/mods.toml" not in z.namelist():
                    print(f"note: {name} has no META-INF/mods.toml"); continue
                data = tomllib.loads(z.read("META-INF/mods.toml").decode("utf-8", "replace"))
        except Exception as e:
            problems.append(f"{name}: cannot read mods.toml ({e})"); continue
        ids = [m.get("modId") for m in data.get("mods", []) if m.get("modId")]
        provided.update(nested_ids(jar))  # Jar-in-jar mods satisfy deps
        for i in ids: mods.setdefault(i, []).append(name)
        for owner, dl in data.get("dependencies", {}).items():
            for dep in dl:
                req = dep.get("mandatory") is True or str(dep.get("type", "")).lower() == "required"
                if req:
                    deps.append((name, owner, dep.get("modId"), dep.get("versionRange", "")))
    for i, js in mods.items():
        if len(js) > 1: problems.append(f"duplicate modId '{i}': {', '.join(js)}")
    for jar, owner, dep, rng in deps:
        if dep in IGNORE:
            if dep == "forge" and not in_range(rng, FORGE):
                problems.append(f"{jar}: forge range {rng} excludes 47.4.13")
            if dep == "minecraft" and not in_range(rng, MC):
                problems.append(f"{jar}: minecraft range {rng} excludes 1.20.1")
        elif dep not in mods and dep not in provided:
            problems.append(f"{jar}: missing mandatory dep '{dep}' {rng}")
    for p in problems: print("PROBLEM:", p)
    print(f"{len(mods)} modIds from {sum(len(v) for v in mods.values())} jars; {len(problems)} problem(s)")
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "mods"))
