# Logo — Processo Trainee 2026.2 (CCU)

Logo do Processo Trainee derivada da identidade visual da logo do **Prep4Consulting
2026.1**, para substituí-la nos materiais do processo.

![Logo Processo Trainee 2026.2](logo-processo-trainee-2026-2.png)

> A arte é branca com fundo transparente — feita para fundos escuros
> (o tema da apresentação usa `#161616`). Em fundo claro ela fica ilegível.

## O que foi mantido da logo original

| Elemento | Original (Prep4Consulting) | Aqui |
| --- | --- | --- |
| Vermelho da marca | `#C1272D` | igual (é o `dk1` do tema da apresentação) |
| Texto | branco `#FFFFFF` | igual |
| 1ª linha | `Prep` + bloco vermelho com o “4” | `Processo` + bloco vermelho sólido |
| Régua vermelha | na base da 1ª linha, até a borda do bloco | igual |
| 2ª linha | `Consulting`, palavra dominante | `Trainee`, palavra dominante |
| `CCU` | corpo pequeno, aninhado sob a 2ª linha | igual |
| Selo do semestre | contorno arredondado, último dígito em vermelho | `2026.2`, mesmo tratamento |
| Proporção da arte | 914 × 435 (2.101:1) | igual, renderizada em 1828 × 870 |

O bloco vermelho entra como âncora geométrica, sem glifo: na original ele carrega
o “4” de *Prep **4** Consulting* (“prep **for** consulting”), e “Processo Trainee”
não tem essa palavra de ligação.

## Tipografia

- **Trirong Bold** — logotipo. Serifa geométrica de serifas finas e retas, `g` de
  uma barriga com cauda aberta e ápice do `t` chanfrado; é a que reproduz os
  desenhos das letras da logo original.
- **Kanit Bold** — numerais do selo. O **Kanit já é uma das fontes embarcadas na
  apresentação**, e as duas são da mesma superfamília da Cadson Demak.

Ambas são [SIL Open Font License](https://openfontlicense.org/).

## Como regerar

```bash
pip install Pillow
python3 gerar_logo_trainee.py logo-processo-trainee-2026-2.png
```

As fontes são baixadas do repositório do Google Fonts na primeira execução (vão
para `./fonts`). Se você já as tem localmente:

```bash
FONT_DIR=/caminho/para/as/fontes python3 gerar_logo_trainee.py saida.png
```

A composição é montada em unidades proporcionais e só no fim é recortada no
*ink* e normalizada para 1828 × 870 — então para ajustar o desenho mexa nas
constantes do topo do script (`LINE1_RATIO`, `BADGE_W_R`, `CCU_CAP_R`, etc.) em
vez de coordenadas absolutas.
