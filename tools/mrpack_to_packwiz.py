#!/usr/bin/env python3
"""Convert a Modrinth .mrpack into a packwiz pack (pack.toml, index.toml, *.pw.toml, plain files).

Usage: python -I tools/mrpack_to_packwiz.py <file.mrpack> <outdir>

Formats follow https://packwiz.infra.link/reference/pack-format/ . Output is
deterministic (sorted, no timestamps). outdir is emptied first.

Limitation: the packwiz index has no per-file side for plain files, so
client-overrides/ and server-overrides/ are NOT included (a warning is printed).
Only overrides/ is shipped, to every side.
"""
import hashlib
import json
import posixpath
import re
import shutil
import sys
import zipfile
from pathlib import Path

EXCLUDE_NAME = re.compile(r"^(packwiz\.json|packwiz-installer.*\.jar)$", re.I)


def q(s):
    return json.dumps(s)  # valid TOML basic string


def sha(data, algo):
    return hashlib.new(algo, data).hexdigest()


def side_of(env):
    env = env or {}
    if env.get("client") == "unsupported":
        return "server"
    if env.get("server") == "unsupported":
        return "client"
    return "both"


def safe_rel(p):
    p = posixpath.normpath(p.replace("\\", "/"))
    if p.startswith("/") or p == ".." or p.startswith("../") or re.match(r"^[A-Za-z]:", p):
        raise ValueError("unsafe path: " + p)
    return p


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    mrpack, out = Path(sys.argv[1]), Path(sys.argv[2])
    z = zipfile.ZipFile(mrpack)
    idx = json.loads(z.read("modrinth.index.json"))
    deps = idx["dependencies"]
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    index_entries = []  # (file, hash, metafile)

    def emit(rel, data, meta):
        dest = out / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        index_entries.append((rel, sha(data, "sha256"), meta))

    stats = {"metafiles": 0, "plain": 0, "client": 0, "server": 0, "both": 0, "skipped": 0}
    used = set()
    for f in sorted(idx["files"], key=lambda f: f["path"]):
        path = safe_rel(f["path"])
        base = posixpath.basename(path)
        if EXCLUDE_NAME.match(base):
            stats["skipped"] += 1
            continue
        side = side_of(f.get("env"))
        stem = re.sub(r"\.[^.]+$", "", base)
        slug = re.sub(r"[^A-Za-z0-9._+-]", "_", stem)
        meta_rel = posixpath.join(posixpath.dirname(path), slug + ".pw.toml")
        if meta_rel in used:
            raise SystemExit("metafile name collision: " + meta_rel)
        used.add(meta_rel)
        h = f["hashes"]
        fmt = "sha512" if "sha512" in h else "sha1"
        body = (
            f"name = {q(stem)}\n"
            f"filename = {q(base)}\n"
            f"side = {q(side)}\n"
            "\n[download]\n"
            f"url = {q(f['downloads'][0])}\n"
            f"hash-format = {q(fmt)}\n"
            f"hash = {q(h[fmt])}\n"
        )
        emit(meta_rel, body.encode(), True)
        stats["metafiles"] += 1
        stats[side] += 1

    for name in sorted(z.namelist()):
        if name.endswith("/"):
            continue
        if name.startswith(("client-overrides/", "server-overrides/")):
            stats["skipped"] += 1
            print("WARNING: sided override not supported by packwiz index, skipped: " + name, file=sys.stderr)
            continue
        if not name.startswith("overrides/"):
            continue
        rel = safe_rel(name[len("overrides/"):])
        if EXCLUDE_NAME.match(posixpath.basename(rel)):
            stats["skipped"] += 1
            continue
        emit(rel, z.read(name), False)
        stats["plain"] += 1

    index_entries.sort()
    lines = ['hash-format = "sha256"\n']
    for rel, h, meta in index_entries:
        lines.append(f"\n[[files]]\nfile = {q(rel)}\nhash = {q(h)}\n" + ("metafile = true\n" if meta else ""))
    index_bytes = "".join(lines).encode()
    (out / "index.toml").write_bytes(index_bytes)

    versions = ['minecraft = ' + q(deps["minecraft"])]
    for k in ("forge", "fabric-loader", "quilt-loader", "neoforge"):
        if k in deps:
            versions.append(f"{'fabric' if k == 'fabric-loader' else 'quilt' if k == 'quilt-loader' else k} = {q(deps[k])}")
    pack = (
        f"name = {q(idx['name'])}\n"
        f"version = {q(idx['versionId'])}\n"
        'pack-format = "packwiz:1.1.0"\n'
        "\n[index]\n"
        'file = "index.toml"\n'
        'hash-format = "sha256"\n'
        f"hash = {q(sha(index_bytes, 'sha256'))}\n"
        "\n[versions]\n" + "\n".join(versions) + "\n"
    )
    (out / "pack.toml").write_text(pack, newline="\n")
    print(json.dumps(stats))


if __name__ == "__main__":
    main()
