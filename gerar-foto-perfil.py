#!/usr/bin/env python3
"""
Gera a foto de perfil de WhatsApp via API do Gemini (Nano Banana Pro).

Uso:
    GEMINI_API_KEY=sua_chave python3 gerar-foto-perfil.py

Chave gratuita em https://aistudio.google.com/apikey

Envia as duas imagens de referencia (colagem de rosto + foto do elevador)
junto com o prompt, e salva o resultado em foto-perfil-gerada.png
"""

import base64
import json
import mimetypes
import os
import sys
import urllib.error
import urllib.request

ROSTO = "SaveClip.App_768786532_2111405923054638_1391361679216671953_n.jpg"
ROUPA = "47f32fd624290921c816d241cf5973c2.jpg"
SAIDA = "foto-perfil-gerada.png"

MODELOS = ["gemini-3-pro-image", "gemini-3-pro-image-preview", "gemini-2.5-flash-image"]

PROMPT = """Use IMAGE 1 (the six-photo collage) as the strict identity reference for the face.
Use IMAGE 2 (the elevator mirror photo) as the reference for wardrobe, lighting and setting ONLY. Do not copy that man's face.

Create a photorealistic square portrait of the SAME young man from IMAGE 1, for use as a WhatsApp profile picture.

FACE - replicate exactly, this is the top priority:
Young adult man in his early twenties, Brazilian, olive / light-tan skin with warm undertones.
Elongated oval face, narrow through the cheeks, with high and clearly defined cheekbones and a clean angular jawline. Slim neck, slender build.
Dark brown wavy-to-curly hair of medium length, with volume on top and loose curls falling at the temples, swept back off the forehead.
Dark brown almond-shaped eyes, moderately deep-set, with straight and fairly thick dark eyebrows.
Narrow straight nose with a slightly defined tip.
Medium-full lips, natural resting mouth.
Thin dark moustache with a small chin patch and sparse light stubble along the jawline, exactly as in the reference.
Keep every facial proportion, every asymmetry and the real skin texture with visible pores. Do NOT beautify, slim, widen or smooth the face. Do NOT change his age. He must be instantly recognisable as the man in IMAGE 1.

WARDROBE - copy from IMAGE 2:
Navy blue ribbed-knit quarter-zip sweater in lambswool, zip pulled roughly a third of the way up, soft natural drape with visible knit texture and ribbed cuffs and hem.
Underneath, a crisp cotton oxford shirt with thin blue and white vertical stripes, its collar worn out over the sweater's collar.
Light grey tailored wool trousers with a pressed front crease.
A watch with a dark leather strap on the left wrist.

POSE AND FRAMING:
Upper-body portrait, chest and head, framed from mid-torso up. Face fully visible and unobstructed, no phone, no mirror selfie.
Body angled very slightly off-centre, shoulders relaxed, head facing close to the camera. Calm confident expression with a subtle closed-mouth smile. Eyes looking directly into the lens.
Left hand relaxed in the trouser pocket so the shoulder line stays natural.

SETTING AND LIGHT:
Brushed stainless steel elevator interior, softly out of focus, with the horizontal handrail visible behind him and the warm metallic reflections of the panels.
Overhead lighting softened into flattering directional light on the face, gentle falloff under the jaw, catchlights in both eyes, no harsh shadows and no blown-out highlights.

TECHNICAL:
Shot on a 85mm portrait lens at f/2.0, shallow depth of field with the face tack sharp.
1:1 square aspect ratio, high resolution, natural colour grading, neutral white balance.
Authentic photography, natural skin, not a render, not an illustration, not plastic or over-retouched. No text, no watermark, no logo."""


def parte_imagem(caminho):
    if not os.path.exists(caminho):
        sys.exit(f"ERRO: imagem de referencia nao encontrada -> {caminho}")
    tipo = mimetypes.guess_type(caminho)[0] or "image/jpeg"
    with open(caminho, "rb") as fh:
        dados = base64.b64encode(fh.read()).decode()
    return {"inline_data": {"mime_type": tipo, "data": dados}}


def chamar(modelo, chave, corpo):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent"
    req = urllib.request.Request(
        url,
        data=json.dumps(corpo).encode(),
        headers={"Content-Type": "application/json", "x-goog-api-key": chave},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=300) as resp:
        return json.load(resp)


def main():
    chave = os.environ.get("GEMINI_API_KEY", "").strip()
    if not chave:
        sys.exit(
            "ERRO: defina GEMINI_API_KEY.\n"
            "Pegue uma chave gratuita em https://aistudio.google.com/apikey\n"
            "Depois rode: GEMINI_API_KEY=sua_chave python3 gerar-foto-perfil.py"
        )

    corpo = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": "IMAGE 1 (identity reference for the face):"},
                    parte_imagem(ROSTO),
                    {"text": "IMAGE 2 (wardrobe, lighting and setting reference):"},
                    parte_imagem(ROUPA),
                    {"text": PROMPT},
                ],
            }
        ],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    }

    erros = []
    for modelo in MODELOS:
        print(f"-> tentando modelo {modelo} ...", flush=True)
        try:
            resposta = chamar(modelo, chave, corpo)
        except urllib.error.HTTPError as exc:
            detalhe = exc.read().decode(errors="replace")[:400]
            erros.append(f"{modelo} HTTP {exc.code} {detalhe}")
            continue
        except Exception as exc:  # noqa: BLE001
            erros.append(f"{modelo} {exc}")
            continue

        for cand in resposta.get("candidates", []):
            for parte in cand.get("content", {}).get("parts", []):
                blob = parte.get("inlineData") or parte.get("inline_data")
                if blob and blob.get("data"):
                    with open(SAIDA, "wb") as fh:
                        fh.write(base64.b64decode(blob["data"]))
                    tam = os.path.getsize(SAIDA)
                    print(f"OK: imagem salva em {SAIDA} ({tam} bytes), modelo {modelo}")
                    return
        erros.append(f"{modelo} respondeu sem imagem -> {json.dumps(resposta)[:300]}")

    print("FALHOU em todos os modelos:", file=sys.stderr)
    for e in erros:
        print("  -", e, file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
