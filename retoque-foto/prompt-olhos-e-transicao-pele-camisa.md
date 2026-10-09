# Prompts de retoque, olhos naturais e transição pele/camisa

Objetivo, corrigir duas áreas que denunciam geração por IA na foto do elevador.

1. Olhos com aspecto artificial, simétricos demais, saturados e sem textura de íris.
2. Transição entre pele do pescoço e colarinho da camisa social sem textura de tecido, sem sombra de contato e sem costura visível.

Os prompts abaixo funcionam em editores que aceitam instrução em linguagem natural com imagem de referência, por exemplo Nano Banana, Flux Kontext, Seedream, Qwen Image Edit, Adobe Firefly e Generative Fill do Photoshop.

---

## 1. Prompt principal, versão em inglês

Editores de imagem respondem melhor em inglês. Esta é a versão recomendada.

```
Photorealistic retouch of this portrait. Keep the subject's identity, face
structure, pose, framing, lighting direction and background completely
unchanged. Do not restyle or beautify. The goal is documentary photographic
realism, as if shot on a smartphone camera.

EYES
Rebuild the eyes to match the attached reference camera photos of the same
person. Preserve the exact original iris color, iris size, eye shape, eyelid
crease and interpupillary distance from the reference. Add fine radial iris
fiber texture with visible crypts and subtle color variation across the
stroma. Soften the limbal ring so it fades gradually instead of forming a hard
dark outline. Introduce natural asymmetry between left and right eye, slightly
different eyelid aperture and lash direction, since perfectly mirrored eyes
read as synthetic. Add a single specular catchlight per eye, positioned
consistently with the existing light source in the photo, small and soft, not
a bright white dot. Render the sclera slightly off white with faint warm
vascular detail near the tear duct and a subtle shadow from the upper lid, not
pure white. Keep lower lash line visible but sparse. Add a thin moist
highlight along the lower waterline. Preserve natural tear duct anatomy.
Reduce overall eye sharpening so eye detail does not exceed the sharpness of
the surrounding skin.

NECK TO SHIRT TRANSITION
Rebuild the junction between neck skin and the dress shirt collar as a real
photograph. Add a soft contact shadow under the jaw and inside the collar
opening, with density consistent with the ambient light in the scene. Give the
collar correct structural behavior, defined collar leaf, visible interlining
stiffness, realistic fold where the collar meets the neck, and a slight gap on
one side. Add visible fabric texture, woven cotton poplin with fine warp and
weft threads, subtle sheen, micro wrinkles radiating from the collar seam and
natural drape over the shoulders. Add visible topstitching along the collar
edge and the placket, with slightly irregular stitch spacing. Where the zip
neck layer appears, render knitted texture with visible stitch loops, ribbed
collar structure, and the zipper with metal teeth, puller and fabric tape
correctly aligned, following the body contour.

SKIN
Restore skin micro detail on neck, throat and jaw, visible pores, fine vellus
hair, slight tonal unevenness, natural redness variation, subtle tendon and
clavicle definition under the skin. Avoid smooth plastic or waxy skin.

GLOBAL CONSISTENCY
Match color temperature, white balance, exposure and contrast across all
edited regions to the rest of the photograph. Apply uniform luminance noise
and grain so the edited areas match the sensor noise of the original capture.
Match lens characteristics, same depth of field and same slight softness at
the edges. No seams, no blur halos, no mismatched sharpness between regions.
```

### Negative prompt

Para ferramentas que aceitam prompt negativo.

```
plastic skin, waxy skin, airbrushed, oversmoothed, beauty filter, glowing
eyes, oversaturated iris, hard black limbal ring, perfectly symmetrical eyes,
doll eyes, anime eyes, pure white sclera, double catchlight, enlarged pupils,
fake eyelashes, flat fabric, textureless cloth, painted collar, floating
collar, missing contact shadow, visible compositing seam, blur halo, mismatched
sharpness, HDR glow, 3d render, cgi, illustration, overexposed highlights,
identity change, different face
```

---

## 2. Prompt principal, versão em português

Para ferramentas que aceitam português, por exemplo Firefly em pt-BR.

```
Retoque fotorrealista deste retrato. Mantenha a identidade, a estrutura do
rosto, a pose, o enquadramento, a direção da luz e o fundo exatamente iguais.
Não embeleze e não estilize. O objetivo é realismo fotográfico documental, como
se a foto tivesse sido feita com a câmera de um celular.

OLHOS
Reconstrua os olhos com base nas fotos de referência da câmera da mesma pessoa.
Preserve a cor exata da íris, o tamanho da íris, o formato dos olhos, a prega
da pálpebra e a distância entre as pupilas conforme a referência. Acrescente
textura radial fina de fibras da íris, com criptas visíveis e variação suave de
cor. Suavize o anel limbal para que ele dissolva aos poucos em vez de formar um
contorno escuro duro. Introduza assimetria natural entre o olho esquerdo e o
direito, abertura de pálpebra levemente diferente e direção de cílios
diferente, porque olhos perfeitamente espelhados parecem sintéticos. Coloque um
único reflexo especular por olho, alinhado com a fonte de luz existente na
foto, pequeno e suave, não um ponto branco forte. Renderize a esclera em branco
levemente quebrado, com vascularização discreta perto do canto lacrimal e
sombra suave da pálpebra superior, nunca branco puro. Mantenha a linha de
cílios inferiores visível e esparsa. Acrescente um brilho úmido fino na borda
inferior da pálpebra. Reduza a nitidez geral dos olhos para que não fiquem mais
definidos que a pele ao redor.

TRANSIÇÃO PESCOÇO E CAMISA
Reconstrua a junção entre a pele do pescoço e o colarinho da camisa social como
uma fotografia real. Acrescente sombra de contato suave sob o maxilar e dentro
da abertura do colarinho, com densidade coerente com a luz do ambiente. Dê ao
colarinho comportamento estrutural correto, pontas definidas, rigidez de
entretela visível, dobra realista no encontro com o pescoço e uma leve folga de
um dos lados. Acrescente textura de tecido visível, popeline de algodão com
fios de trama e urdume finos, brilho discreto, microrrugas saindo da costura do
colarinho e caimento natural sobre os ombros. Acrescente pesponto visível na
borda do colarinho e na carcela, com espaçamento de pontos levemente irregular.
Onde aparecer a camada de zip neck, renderize textura de malha com laçadas
visíveis, colarinho canelado e o zíper com dentes metálicos, puxador e fita de
tecido corretamente alinhados, acompanhando o contorno do corpo.

PELE
Recupere microdetalhe de pele no pescoço, na garganta e no maxilar, poros
visíveis, pelos finos, leve irregularidade de tom, variação natural de
vermelhidão e definição discreta de tendões e clavícula sob a pele. Evite pele
plástica ou com aparência de cera.

CONSISTÊNCIA GERAL
Iguale temperatura de cor, balanço de branco, exposição e contraste de todas as
regiões editadas ao restante da fotografia. Aplique ruído de luminância e
granulação uniformes para que as áreas editadas combinem com o ruído de sensor
da captura original. Iguale as características de lente, mesma profundidade de
campo e mesma leve suavidade nas bordas. Sem emendas, sem halos de desfoque e
sem diferença de nitidez entre regiões.
```

---

## 3. Prompts curtos por região, para Generative Fill do Photoshop

O Generative Fill trabalha melhor com seleção pequena e instrução curta. Faça
uma área por vez.

**Seleção, apenas os dois olhos**

```
realistic human eyes, fine radial iris fiber texture, soft limbal ring,
slightly off white sclera with faint vessels near tear duct, single small soft
catchlight, natural asymmetry, sparse lower lashes, documentary photo, matching
grain
```

**Seleção, colarinho e 2 cm de pele ao redor**

```
woven cotton poplin dress shirt collar, visible warp and weft threads,
topstitched edge, interlining structure, micro wrinkles from seam, soft contact
shadow under jaw, realistic drape, natural skin pores on neck, photographic
grain
```

**Seleção, área do zip neck**

```
knitted merino zip neck, visible stitch loops, ribbed collar, metal zipper with
teeth and puller, fabric zipper tape, natural fold and drape, soft shadow at
neckline, photographic texture
```

**Seleção, faixa estreita exatamente na linha pele e tecido**

```
seamless photographic transition between skin and fabric, soft contact shadow,
matching sharpness, matching sensor noise, no halo
```

---

## 4. Como usar as duas fotos da câmera como referência

As fotos de referência valem mais que qualquer descrição de texto, porque
carregam a cor real da íris e o padrão real da sua pele.

1. Suba a foto do elevador como imagem principal a ser editada.
2. Suba as duas fotos da câmera como imagem de referência, em ferramentas com
   múltipla entrada, por exemplo Nano Banana e Flux Kontext.
3. Acrescente esta linha ao início do prompt.

```
Use image 2 and image 3 as ground truth references for the eyes, iris color,
eye shape and skin texture of the same person. Transfer that exact eye anatomy
and skin micro texture into image 1 without changing image 1 pose, lighting,
framing or clothing shape.
```

4. Rode em força de edição baixa, algo entre 0,25 e 0,40 de denoise ou
   strength, para não perder a semelhança. Força alta troca o rosto.

---

## 5. Checklist de verificação do resultado

Marque cada item antes de considerar a foto pronta.

- [ ] Os olhos não estão espelhados, há diferença real entre eles.
- [ ] Existe apenas um reflexo de luz por olho, e ele aponta para a mesma
      direção da luz da cena.
- [ ] A esclera não é branco puro.
- [ ] A nitidez dos olhos não é maior que a nitidez da pele do rosto.
- [ ] Existe sombra de contato embaixo do maxilar.
- [ ] O colarinho tem costura visível e trama de tecido.
- [ ] O tecido tem rugas coerentes com a posição dos ombros.
- [ ] O grão da área editada é igual ao grão do fundo da foto.
- [ ] Ampliando em 200 por cento, não aparece linha de emenda entre pele e
      tecido.

Se qualquer item falhar, rode outra passada apenas naquela região em vez de
regerar a imagem inteira.
