#!/usr/bin/env python3
"""Extrai metadados SEO reais do HTML bruto baixado."""
import re, os, html, json, glob

RAW = "/projects/sandbox/audit-ccu/raw"

def get(pat, s, flags=re.I | re.S):
    m = re.search(pat, s, flags)
    return html.unescape(m.group(1)).strip() if m else ""

rows = []
for f in sorted(glob.glob(os.path.join(RAW, "*.html"))):
    name = os.path.basename(f)[:-5]
    url = "/" if name == "HOME" else "/" + name.replace("__", "/")
    s = open(f, encoding="utf-8", errors="replace").read()
    title = get(r"<title[^>]*>(.*?)</title>", s)
    desc = get(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']', s)
    robots = get(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'](.*?)["\']', s)
    canon = get(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\'](.*?)["\']', s)
    ogtitle = get(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\'](.*?)["\']', s)
    # H1s
    h1 = re.findall(r"<h1[^>]*>(.*?)</h1>", s, re.I | re.S)
    h1 = [re.sub(r"<[^>]+>", "", x).strip() for x in h1]
    h1 = [html.unescape(x) for x in h1 if x.strip()]
    rows.append(dict(url=url, title=title, tlen=len(title), desc=desc,
                     dlen=len(desc), robots=robots, canonical=canon,
                     ogtitle=ogtitle, h1=h1, h1count=len(h1), bytes=len(s)))

json.dump(rows, open("/projects/sandbox/audit-ccu/meta.json", "w"),
          ensure_ascii=False, indent=1)

print(f"{'URL':<48} {'LEN':>4} TITLE")
print("-" * 120)
for r in rows:
    print(f"{r['url']:<48} {r['tlen']:>4} {r['title']}")

print("\n\n=== META DESCRIPTION ===")
for r in rows:
    d = r["desc"] if r["desc"] else "*** VAZIA ***"
    print(f"{r['url']:<48} ({r['dlen']:>3}) {d[:110]}")

print("\n\n=== ROBOTS / CANONICAL / H1 ===")
for r in rows:
    print(f"{r['url']:<48} robots={r['robots'] or '-':<28} h1s={r['h1count']} {r['h1'][:3]}")
