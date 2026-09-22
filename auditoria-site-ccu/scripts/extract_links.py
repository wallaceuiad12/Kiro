#!/usr/bin/env python3
"""Mapeia links internos/externos e o menu real do CCU."""
import re, os, html, glob, json
from collections import defaultdict

RAW = "/projects/sandbox/audit-ccu/raw"
DOM = "consultoriaunicamp.com"

def links_of(s):
    out = []
    for m in re.finditer(r"<a\b([^>]*)>(.*?)</a>", s, re.I | re.S):
        attrs, inner = m.group(1), m.group(2)
        h = re.search(r'href=["\'](.*?)["\']', attrs, re.I)
        if not h:
            continue
        href = html.unescape(h.group(1)).strip()
        label = html.unescape(re.sub(r"<[^>]+>", " ", inner))
        label = re.sub(r"\s+", " ", label).strip()
        out.append((href, label))
    return out

# menu real: extrai do primeiro nav/menu container da home
home = open(os.path.join(RAW, "HOME.html"), encoding="utf-8", errors="replace").read()
print("=== MENU + TODOS OS LINKS DA HOME (em ordem) ===")
seen = set()
for href, label in links_of(home):
    k = (href, label)
    if k in seen:
        continue
    seen.add(k)
    print(f"  {label[:52]:<54} -> {href}")

# inbound link graph
inbound = defaultdict(set)
external = defaultdict(set)
for f in sorted(glob.glob(os.path.join(RAW, "*.html"))):
    name = os.path.basename(f)[:-5]
    src = "/" if name == "HOME" else "/" + name.replace("__", "/")
    s = open(f, encoding="utf-8", errors="replace").read()
    for href, label in links_of(s):
        if href.startswith("#") or href.startswith("mailto") or href.startswith("tel"):
            continue
        if DOM in href:
            path = re.sub(r"^https?://[^/]+", "", href).split("?")[0].split("#")[0]
            path = path if path else "/"
            inbound[path.rstrip("/") or "/"].add(src)
        elif href.startswith("http"):
            external[re.sub(r"^https?://([^/]+).*", r"\1", href)].add(src)

json.dump({k: sorted(v) for k, v in inbound.items()},
          open("/projects/sandbox/audit-ccu/inbound.json", "w"), ensure_ascii=False, indent=1)

print("\n\n=== LINKS DE ENTRADA (inbound) POR PAGINA ===")
allpages = []
for f in sorted(glob.glob(os.path.join(RAW, "*.html"))):
    n = os.path.basename(f)[:-5]
    allpages.append("/" if n == "HOME" else "/" + n.replace("__", "/"))
for p in sorted(allpages):
    key = p.rstrip("/") or "/"
    src = inbound.get(key, set())
    # remove auto-link (footer/menu presente em todas)
    tag = "ORFA" if not src else f"{len(src)} origens"
    print(f"{p:<48} {tag:<12} {sorted(src)[:6] if src else ''}")

print("\n\n=== DOMINIOS EXTERNOS REFERENCIADOS ===")
for d, srcs in sorted(external.items(), key=lambda x: -len(x[1])):
    print(f"{d:<44} {len(srcs):>3} paginas  ex: {sorted(srcs)[:3]}")
