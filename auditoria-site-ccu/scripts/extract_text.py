#!/usr/bin/env python3
"""Extrai texto visível do HTML SSR do Wix, por página."""
import re, os, html, glob, json

RAW = "/projects/sandbox/audit-ccu/raw"
OUT = "/projects/sandbox/audit-ccu/text"
os.makedirs(OUT, exist_ok=True)

def visible_text(s):
    # isola o body
    m = re.search(r"<body.*?>(.*)</body>", s, re.I | re.S)
    body = m.group(1) if m else s
    # remove script/style/noscript/svg
    body = re.sub(r"<script.*?</script>", " ", body, flags=re.I | re.S)
    body = re.sub(r"<style.*?</style>", " ", body, flags=re.I | re.S)
    body = re.sub(r"<noscript.*?</noscript>", " ", body, flags=re.I | re.S)
    body = re.sub(r"<svg.*?</svg>", " ", body, flags=re.I | re.S)
    # quebra de linha em blocos
    body = re.sub(r"</(p|div|h[1-6]|li|tr|section|button|a|span)>", "\n", body, flags=re.I)
    body = re.sub(r"<br\s*/?>", "\n", body, flags=re.I)
    body = re.sub(r"<[^>]+>", " ", body)
    body = html.unescape(body)
    body = body.replace("\xa0", " ")
    lines = [re.sub(r"[ \t]+", " ", l).strip() for l in body.split("\n")]
    out, prev = [], None
    for l in lines:
        if l and l != prev:
            out.append(l)
            prev = l
    return "\n".join(out)

summary = []
for f in sorted(glob.glob(os.path.join(RAW, "*.html"))):
    name = os.path.basename(f)[:-5]
    s = open(f, encoding="utf-8", errors="replace").read()
    t = visible_text(s)
    open(os.path.join(OUT, name + ".txt"), "w", encoding="utf-8").write(t)
    words = len(t.split())
    summary.append((name, len(t), words, t.count("\n") + 1))

print(f"{'PAGINA':<44} {'CHARS':>7} {'PALAVRAS':>9} {'LINHAS':>7}")
print("-" * 74)
for n, c, w, l in sorted(summary, key=lambda x: x[2]):
    print(f"{n:<44} {c:>7} {w:>9} {l:>7}")
