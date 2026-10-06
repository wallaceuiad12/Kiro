"""
Verifica a consistência do gabarito gerado por gerar_provas_pdf.py.

Checagens:
  1. Soma dos pontos de cada alínea == total declarado no título da alínea.
  2. Soma das alíneas == total declarado no título da questão.
  3. Cada questão tem os cinco blocos do gabarito.
  4. Soma das três questões de cada prova == 100 pontos.

Lê o Markdown gerado (que vem da mesma fonte que o PDF), de modo que o que se
verifica é exatamente o que foi publicado.

Uso: python3 verificar_gabarito.py
Código de saída 0 se tudo confere, 1 caso contrário.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(ROOT, 'provas-dissertativas-gabarito-completo.md')

# Os títulos podem vir seguidos do sufixo "[acrescentado]", por isso não se
# exige o fechamento do negrito logo após o rótulo.
BLOCOS = {
    'o que pede': r'\*\*O que a questão pede',
    'distribuição': r'Distribuição dos pontos',
    'resposta-modelo': r'Resposta-modelo',
    'erros': r'\*\*Erros? que mais custa(?:m)? nota',
    'diferenciação': r'\*\*Pontos de diferenciação',
}


def carregar_gabaritos(texto):
    """Fatia o Markdown em {prova: {questão: (total_declarado, trecho)}}."""
    # Só a Parte II interessa; a Parte I repete os enunciados.
    parte2 = texto.split('## Parte II — Gabaritos', 1)[1]
    parte2 = parte2.split('## Apêndice A', 1)[0]

    provas = {}
    for bloco_prova in re.split(r'\n## Gabarito — ', parte2)[1:]:
        nome = bloco_prova.splitlines()[0].strip()
        questoes = {}
        for bloco_q in re.split(r'\n### ', bloco_prova)[1:]:
            cab = bloco_q.splitlines()[0].strip()
            m = re.match(r'(Questão \d+) \((\d+) pontos\)', cab)
            if m:
                questoes[m.group(1)] = (int(m.group(2)), bloco_q)
        provas[nome] = questoes
    return provas


def somar_alineas(trecho):
    """[(rótulo, total_declarado, soma_real)] para cada 'Distribuição dos pontos'."""
    resultados = []
    linhas = trecho.splitlines()
    for i, linha in enumerate(linhas):
        m = re.match(r'#### (?:([a-c])\) )?Distribuição dos pontos \((\d+)\)', linha.strip())
        if not m:
            continue
        rotulo = m.group(1) or 'único'
        declarado = int(m.group(2))
        soma = 0
        for seguinte in linhas[i + 1:]:
            s = seguinte.strip()
            if s.startswith('####') or s.startswith('###') or s.startswith('##'):
                break
            if not s.startswith('|'):
                continue
            celulas = [c.strip() for c in s.strip('|').split('|')]
            ultima = celulas[-1].replace('**', '')
            if ultima.isdigit():
                soma += int(ultima)
        resultados.append((rotulo, declarado, soma))
    return resultados


def main():
    if not os.path.exists(MD):
        print('Markdown não encontrado. Rode antes: python3 gerar_provas_pdf.py')
        return 1

    with open(MD, encoding='utf-8') as f:
        texto = f.read()

    provas = carregar_gabaritos(texto)
    falhas = []
    print(f'Verificando {MD}\n')

    for prova, questoes in provas.items():
        print(f'=== {prova} ===')
        total_prova = 0
        for questao, (declarado_q, trecho) in questoes.items():
            alineas = somar_alineas(trecho)
            soma_alineas = 0
            detalhes = []
            for rotulo, declarado, soma in alineas:
                ok = declarado == soma
                detalhes.append(f'{rotulo}: {soma}/{declarado}' + ('' if ok else '  <-- ERRO'))
                if not ok:
                    falhas.append(f'{prova} · {questao} · alínea {rotulo}: '
                                  f'soma {soma} ≠ declarado {declarado}')
                soma_alineas += declarado

            ok_q = soma_alineas == declarado_q
            if not ok_q:
                falhas.append(f'{prova} · {questao}: alíneas somam {soma_alineas} '
                              f'≠ total {declarado_q}')
            total_prova += declarado_q

            faltando = [nome for nome, padrao in BLOCOS.items()
                        if not re.search(padrao, trecho)]
            if faltando:
                falhas.append(f'{prova} · {questao}: bloco(s) ausente(s) — '
                              f'{", ".join(faltando)}')

            marca = 'ok' if (ok_q and not faltando) else 'FALHA'
            print(f'  {questao} ({declarado_q} pts) [{marca}]  '
                  f'{" | ".join(detalhes)}'
                  + (f'  blocos ausentes: {faltando}' if faltando else ''))

        if total_prova != 100:
            falhas.append(f'{prova}: as três questões somam {total_prova} ≠ 100')
        print(f'  total da prova: {total_prova}/100\n')

    if falhas:
        print('FALHAS:')
        for f_ in falhas:
            print('  -', f_)
        return 1

    print('Tudo confere: somas corretas e os cinco blocos presentes em todas as questões.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
