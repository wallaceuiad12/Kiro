#!/usr/bin/env python3
"""Quantifica caos tipográfico e de cor a partir do HTML/CSS do Wix."""
import re, glob, os, json
from collections import Counter

RAW = "/projects/sandbox/audit-ccu/raw"
CCU = [f for f in glob.glob(os.path.join(RAW, "*.html"))
       if "event-details" not in f and "service-page" not in f]

fsize, ffam, colors, themes = Counter(), Counter(), Counter(), Counter()
inline_spans = 0

for f in CCU:
    s = open(f, encoding="utf-8", errors="replace").read()
    fsize.update(re.findall(r"font-size:\s*(\d+)px", s))
    ffam.update(re.findall(r"font-family:\s*([^;\"'}]+)", s))
    for c in re.findall(r"color:\s*(#[0-9A-Fa-f]{3,6}|rgba?\([^)]*\))", s):
        colors[c.lower().replace(" ", "")] += 1
    themes.update(re.findall(r'class="[^"]*\b(font_\d+)\b', s))
    inline_spans += len(re.findall(r'<span style="[^"]*font-', s))

print("=== TAMANHOS DE FONTE inline (px) usados nas paginas do CCU ===")
sizes = sorted(((int(k), v) for k, v in fsize.items()))
print(f"total de tamanhos distintos: {len(sizes)}")
print("  " + "  ".join(f"{k}px({v})" for k, v in sizes))

print("\n=== FAMILIAS DE FONTE referenciadas ===")
fam = Counter()
for k, v in ffam.items():
    for part in k.split(","):
        p = part.strip().strip("'\"").lower()
        if p and not p.startswith("var(") and p not in ("sans-serif", "serif", "monospace", "inherit"):
            fam[p] += v
print(f"total distintas: {len(fam)}")
for k, v in fam.most_common(30):
    print(f"  {k:<48} {v}")

print("\n=== TEMAS DE TEXTO DO WIX (font_N) em uso ===")
print(f"distintos: {len(themes)}  ->  {dict(sorted(themes.items(), key=lambda x: -x[1]))}")

print(f"\n=== SPANS COM ESTILO DE FONTE INLINE (formatacao manual) ===")
print(f"total de <span style=...font-...> nas paginas do CCU: {inline_spans}")

print("\n=== CORES declaradas (top 25) ===")
for k, v in colors.most_common(25):
    print(f"  {k:<24} {v}")
json.dump({"sizes": dict(fsize), "fams": dict(fam), "colors": dict(colors)},
          open("/projects/sandbox/audit-ccu/style.json", "w"), indent=1)
