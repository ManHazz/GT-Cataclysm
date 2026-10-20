#!/usr/bin/env python3
"""Unpack a Modrinth .mrpack into a client game dir: download client files, copy overrides."""
import argparse, hashlib, json, os, shutil, sys, urllib.request, zipfile


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("mrpack")
    ap.add_argument("dest", help="game directory (e.g. run)")
    a = ap.parse_args()
    dest = os.path.abspath(a.dest)
    os.makedirs(dest, exist_ok=True)
    z = zipfile.ZipFile(a.mrpack)
    idx = json.loads(z.read("modrinth.index.json"))
    bad = 0
    for f in idx["files"]:
        if (f.get("env") or {}).get("client") == "unsupported":
            continue
        out = os.path.abspath(os.path.join(dest, f["path"]))
        if not out.startswith(dest + os.sep):
            sys.exit("unsafe path " + f["path"])
        os.makedirs(os.path.dirname(out), exist_ok=True)
        data = None
        for url in f["downloads"]:
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "gt-cataclysm-ci"})
                data = urllib.request.urlopen(req, timeout=120).read()
                if hashlib.sha512(data).hexdigest() == f["hashes"]["sha512"]:
                    break
                data = None
            except Exception as e:
                print(f"warn: {url}: {e}", file=sys.stderr)
        if data is None:
            print(f"::error::failed to download {f['path']}")
            bad += 1
            continue
        with open(out, "wb") as fh:
            fh.write(data)
    for prefix in ("overrides/", "client-overrides/"):
        for n in z.namelist():
            if n.startswith(prefix) and not n.endswith("/"):
                out = os.path.abspath(os.path.join(dest, n[len(prefix):]))
                if not out.startswith(dest + os.sep):
                    sys.exit("unsafe path " + n)
                os.makedirs(os.path.dirname(out), exist_ok=True)
                with z.open(n) as src, open(out, "wb") as dst:
                    shutil.copyfileobj(src, dst)
    print(f"unpacked {len(idx['files'])} indexed files into {dest}; {bad} failures")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
