# Prompt de ajuste de bigode, cavanhaque e sobrancelha

Para refinar os pelos faciais de uma imagem ja gerada, sem mexer no resto.

Use em Nano Banana Pro (gemini.google.com) ou Qwen Image Edit (chat.qwen.ai).
Modelos de edicao preservam melhor o que voce nao pediu para mudar.

## Como usar

Anexe na mesma mensagem, nesta ordem:

1. A foto gerada do elevador, que e a imagem a ser corrigida.
2. `SaveClip.App_768786532_2111405923054638_1391361679216671953_n.jpg`, a colagem, como referencia real dos pelos.

Cole o prompt. Gere 4 variacoes, porque pelo facial varia muito entre seeds.

## Prompt de ajuste (ingles, recomendado)

```
Edit IMAGE 1 only in the facial hair and eyebrows. Use IMAGE 2 (the six-photo collage) as the ground truth for how this man's real hair actually grows.

Change NOTHING else. Preserve the exact same face, bone structure, skin tone and texture, pose, framing, expression, eye direction, hair on the head, clothing, elevator background and lighting. This is a local retouch, not a regeneration.

MOUSTACHE:
Thin and dark, following the natural upper lip line, narrow in height and never bushy. Keep the slight thinning at the philtrum, in the centre under the nose, exactly as it appears in the reference. Individual hairs should read as separate strands, not as a solid painted block.

CONNECT THE MOUSTACHE TO THE GOATEE — this is the main change:
Extend the moustache downward from both corners, running past the corners of the mouth and down along the sides of the chin, so that it joins the chin patch and closes into a continuous ring of hair framing the mouth. The connecting strips should be narrow and natural, slightly sparser than the moustache itself, with soft irregular edges rather than sharp razor lines. The result should look grown in, not stencilled.

GOATEE / CHIN PATCH:
Keep it compact and centred on the chin, matching the width and depth seen in the reference. Slightly denser at the centre of the chin and fading out toward the jaw. Do not turn it into a full beard and do not extend it down the neck.

JAWLINE:
Keep the stubble along the jaw sparse and light, just a faint shadow of growth, exactly as in the reference. Do not thicken it.

EYEBROWS:
Dark brown, straight and fairly flat with only a very slight arch toward the outer third, medium thickness. Match the reference exactly, including the natural asymmetry between the two brows and the slightly thinner, tapering outer tails. Keep the original spacing and the natural gap above the bridge of the nose. Do not shape, darken, thicken or arch them into a styled or groomed look.

DENSITY AND REALISM:
All facial hair must follow his real growth pattern and density, which is fine and moderately sparse, not thick. Respect the exact proportions of his face. Keep visible skin between hairs, keep the natural variation in hair direction, and keep the real skin texture and pores underneath. No airbrushing, no smoothing, no symmetry correction, no beautification.
```

## Prompt curto, para Qwen Image Edit

Modelos de edicao mais leves respondem melhor a instrucao curta.

```
Keep everything in this photo identical. Only adjust the facial hair and eyebrows.
Connect the thin dark moustache down past both corners of the mouth to join the chin goatee, forming a continuous narrow ring of hair around the mouth. Keep the connecting strips thin, slightly sparse and naturally grown, not sharply shaved lines.
Keep the goatee compact and centred on the chin. Keep the jaw stubble very light.
Keep the eyebrows straight, dark brown and medium thickness, with their natural asymmetry, not groomed or arched.
Match the real growth density from the reference photos, which is fine and moderately sparse. Preserve skin texture and pores. Do not change the face, pose, clothing, background or lighting.
```

## Se o resultado sair errado

Problema mais comum e o modelo transformar a conexao em barba cheia.
Rode o ajuste corretivo:

```
The connecting hair came out too thick and reads as a full beard. Thin it down so it is a narrow strip on each side of the mouth, noticeably sparser than the moustache, with soft irregular edges. Keep clear skin visible on the cheeks and along the jaw.
```

Se a sobrancelha ficar desenhada demais:

```
The eyebrows look groomed and artificial. Restore their natural irregular edges, the slight asymmetry between left and right, and the thinner tapering outer tails. Remove any sharp outline.
```

## Para eu calibrar melhor

Suba no repo a foto gerada do elevador e as fotos de camera de perto do rosto.
Com elas eu ajusto a descricao dos pelos para o seu padrao exato de crescimento,
em vez de depender so da colagem, que e de resolucao baixa.
