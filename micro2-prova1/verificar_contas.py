"""
Verificacao simbolica/numerica de TODAS as respostas usadas nos materiais de estudo:
  - Lista 1 (Questoes 1 a 6)  -> lista1.pdf
  - Banco de exercicios extra (A1-A5, B1-B5)
Roda com: python3 verificar_contas.py
Qualquer divergencia levanta AssertionError.
"""
from sympy import symbols, Rational, solve, diff, simplify, nsimplify, integrate, S, Eq, sqrt, log

p1, p2, r, Q, Q1, Q2, q = symbols('p1 p2 r Q Q1 Q2 q', positive=True)
OK = []


def check(label, got, want):
    got_s, want_s = nsimplify(got), nsimplify(want)
    assert simplify(got_s - want_s) == 0, f'{label}: obtido {got_s} != esperado {want_s}'
    OK.append(f'{label}: {got_s}')


def cobb_demand(alpha, beta, m, px, py):
    """Demanda Marshalliana de U = x^alpha y^beta."""
    s = Rational(alpha, 1) / (alpha + beta)
    return s * m / px, (1 - s) * m / py


# ---------------------------------------------------------------- LISTA 1, Q1
# U_i = x1*x2 ; wA=(4,2) ; wB=(1,3) ; totais (5,5)
mA = 4 * p1 + 2 * p2
mB = 1 * p1 + 3 * p2
x1A, x2A = cobb_demand(1, 1, mA, p1, p2)
x1B, x2B = cobb_demand(1, 1, mB, p1, p2)
sol = solve(Eq(x1A + x1B, 5), p2)[0]          # limpa o mercado do bem 1
check('Q1 preco relativo p2/p1', sol / p1, 1)
sub = {p1: 1, p2: 1}
check('Q1 x1A', x1A.subs(sub), 3)
check('Q1 x2A', x2A.subs(sub), 3)
check('Q1 x1B', x1B.subs(sub), 2)
check('Q1 x2B', x2B.subs(sub), 2)
check('Q1 factibilidade bem 1', (x1A + x1B).subs(sub), 5)
check('Q1 factibilidade bem 2', (x2A + x2B).subs(sub), 5)
check('Q1 TMS_A na dotacao', Rational(2, 4), Rational(1, 2))
check('Q1 TMS_B na dotacao', Rational(3, 1), 3)
check('Q1 utilidade A antes', 4 * 2, 8)
check('Q1 utilidade A depois', 3 * 3, 9)
check('Q1 utilidade B antes', 1 * 3, 3)
check('Q1 utilidade B depois', 2 * 2, 4)

# ---------------------------------------------------------------- LISTA 1, Q2
# U = x^4 y^6 (agente 1) ; V = x^6 y^4 (agente 2) ; w1=(4,2) ; w2=(2,4)
m1 = 4 * r + 2                                  # py = 1, r = px
m2 = 2 * r + 4
x1, y1 = cobb_demand(4, 6, m1, r, 1)
x2, y2 = cobb_demand(6, 4, m2, r, 1)
rs = solve(Eq(x1 + x2, 6), r)[0]
check('Q2 px/py', rs, 1)
check('Q2 fracao gasta em x pelo agente 1', Rational(4, 10), Rational(2, 5))   # (a) 40%
check('Q2 x do agente 1', x1.subs(r, rs), Rational(12, 5))                    # (c) 2,4
y1v = y1.subs(r, rs)
check('Q2 y do agente 1', y1v, Rational(18, 5))                               # 3,6
check('Q2 TMS do agente 1', (4 * y1v) / (6 * x1.subs(r, rs)), 1)              # (d) 1
check('Q2 factibilidade bem y', (y1 + y2).subs(r, rs), 6)

# ---------------------------------------------------------------- LISTA 1, Q3
# UA = x1^(1/3) x2^(2/3) ; UB = min{x1,x2} ; wA=(10,20) ; wB=(20,5) ; totais (30,25)
mA3 = 10 * p1 + 20 * p2
x1A3, x2A3 = cobb_demand(1, 2, mA3, p1, p2)
mB3 = 20 * p1 + 5 * p2
x1B3 = mB3 / (p1 + p2)                          # Leontief: x1 = x2 = m/(p1+p2)
sub11 = {p1: 1, p2: 1}
check('Q3 x1A com p=(1,1)', x1A3.subs(sub11), 10)
check('Q3 x2A com p=(1,1)', x2A3.subs(sub11), 20)
check('Q3 xB com p=(1,1)', x1B3.subs(sub11), Rational(25, 2))
z1 = (x1A3 + x1B3).subs(sub11) - 30
z2 = (x2A3 + x1B3).subs(sub11) - 25
check('Q3 excesso bem 1', z1, Rational(-15, 2))                                # -7,5
check('Q3 excesso bem 2', z2, Rational(15, 2))                                 # +7,5
check('Q3 Lei de Walras (p1*z1+p2*z2)', z1 + z2, 0)
# curva de contrato: x1B=x2B + factibilidade  =>  x2A = x1A - 5
xa1 = symbols('xa1', positive=True)
xa2 = 25 - (30 - xa1)
check('Q3 curva de contrato', simplify(xa2 - (xa1 - 5)), 0)
check('Q3 alocacao (10,5)/(20,20) na curva', (10 - 5) - 5, 0)

# ---------------------------------------------------------------- LISTA 1, Q4
P4 = 18 - Q
CT4 = 27 + 2 * Q ** 2
RMg4 = diff(P4 * Q, Q)
CMg4 = diff(CT4, Q)
Qm4 = solve(Eq(RMg4, CMg4), Q)[0]
check('Q4 Qm', Qm4, 3)
check('Q4 Pm', P4.subs(Q, Qm4), 15)
check('Q4 lucro', (P4 * Q - CT4).subs(Q, Qm4), 0)
check('Q4 CMe em Qm', (CT4 / Q).subs(Q, Qm4), 15)                              # CMe = P => lucro zero

# ---------------------------------------------------------------- LISTA 1, Q5
# C1 = 10 Q1^2 ; C2 = 20 Q2^2 ; P = 700 - 5Q ; Q = Q1 + Q2
CMg1 = diff(10 * Q1 ** 2, Q1)
CMg2 = diff(20 * Q2 ** 2, Q2)
P5 = 700 - 5 * (Q1 + Q2)
RMg5 = diff(P5 * (Q1 + Q2), Q1)                 # = 700 - 10(Q1+Q2)
s5 = solve([Eq(RMg5, CMg1), Eq(diff(P5 * (Q1 + Q2), Q2), CMg2)], [Q1, Q2], dict=True)[0]
check('Q5 Q1', s5[Q1], 20)
check('Q5 Q2', s5[Q2], 10)
Qtot5 = s5[Q1] + s5[Q2]
check('Q5 Q total', Qtot5, 30)
check('Q5 Preco', P5.subs(s5), 550)
check('Q5 CMg fabrica 1', CMg1.subs(s5), 400)
check('Q5 CMg fabrica 2', CMg2.subs(s5), 400)
check('Q5 RMg', (700 - 10 * Qtot5), 400)
lucro5 = (P5 * (Q1 + Q2) - 10 * Q1 ** 2 - 20 * Q2 ** 2).subs(s5)
check('Q5 lucro', lucro5, 10500)
# CMg total (soma horizontal): Q = CMg/20 + CMg/40 = 3CMg/40  =>  CMg(Q) = 40Q/3
check('Q5 CMg total em Q=30', Rational(40, 3) * 30, 400)
# item (b): choque de custo na fabrica 1 (CMg1 = 20Q1 + 100)
s5b = solve([Eq(700 - 10 * (Q1 + Q2), 20 * Q1 + 100),
             Eq(700 - 10 * (Q1 + Q2), 40 * Q2)], [Q1, Q2], dict=True)[0]
assert s5b[Q1] < 20, 'Q5b: producao da fabrica 1 deveria cair'
assert s5b[Q2] > 10, 'Q5b: producao da fabrica 2 deveria subir'
assert s5b[Q1] + s5b[Q2] < 30, 'Q5b: producao total deveria cair'
assert (700 - 5 * (s5b[Q1] + s5b[Q2])) > 550, 'Q5b: preco deveria subir'
OK.append(f"Q5b Q1={s5b[Q1]} (cai), Q2={s5b[Q2]} (sobe), "
          f"Q={s5b[Q1]+s5b[Q2]} (cai), P={700-5*(s5b[Q1]+s5b[Q2])} (sobe)")

# ---------------------------------------------------------------- LISTA 1, Q6
pp1, pp2 = symbols('pp1 pp2', positive=True)
RMg_1 = pp1 * (1 + Rational(1, -2))             # eps1 = -2
RMg_2 = pp2 * (1 + Rational(1, -4))             # eps2 = -4
check('Q6 RMg1', RMg_1, pp1 / 2)
check('Q6 RMg2', RMg_2, 3 * pp2 / 4)
ratio = solve(Eq(RMg_1, RMg_2), pp1)[0] / pp2
check('Q6 p1/p2 otimo', ratio, Rational(3, 2))
# com p1 = 2,5 p2 as receitas marginais NAO se igualam
check('Q6 RMg1 se p1=2,5p2', RMg_1.subs(pp1, Rational(5, 2) * pp2), Rational(5, 4) * pp2)
assert Rational(5, 4) > Rational(3, 4), 'Q6: RMg1 deveria exceder RMg2'

# ======================================================= BANCO EXTRA: bloco A
# A1: U=x1x2 ambos ; wA=(6,2) ; wB=(2,6) ; totais (8,8)
mA1 = 6 * p1 + 2 * p2
mB1 = 2 * p1 + 6 * p2
xa, ya = cobb_demand(1, 1, mA1, p1, p2)
xb, yb = cobb_demand(1, 1, mB1, p1, p2)
check('A1 p2/p1', solve(Eq(xa + xb, 8), p2)[0] / p1, 1)
check('A1 cesta A', xa.subs(sub11), 4)
check('A1 cesta B', xb.subs(sub11), 4)

# A2: U_A = x1^(1/2)x2^(1/2), w=(10,0) ; U_B = x1^(1/4)x2^(3/4), w=(0,10)
mA2 = 10 * p1
mB2 = 10 * p2
x1a2, x2a2 = cobb_demand(1, 1, mA2, p1, p2)
x1b2, x2b2 = cobb_demand(1, 3, mB2, p1, p2)
p2sol = solve(Eq(x1a2 + x1b2, 10), p2)[0]
check('A2 p2 (com p1=1)', p2sol.subs(p1, 1), 2)
sub2 = {p1: 1, p2: 2}
check('A2 x1A', x1a2.subs(sub2), 5)
check('A2 x2A', x2a2.subs(sub2), Rational(5, 2))
check('A2 x1B', x1b2.subs(sub2), 5)
check('A2 x2B', x2b2.subs(sub2), Rational(15, 2))
check('A2 factibilidade bem 2', (x2a2 + x2b2).subs(sub2), 10)

# A3: quase-linear U = ln x1 + x2 ; wA=(2,1) ; wB=(3,4)
x1_ql = p2 / p1                                  # 1/x1 = p1/p2
mA3q = 2 * p1 + 1 * p2
mB3q = 3 * p1 + 4 * p2
x2A3q = mA3q / p2 - 1
x2B3q = mB3q / p2 - 1
p1sol = solve(Eq(2 * x1_ql, 5), p1)[0]           # dois agentes, dotacao total de x1 = 5
check('A3 p1 (com p2=1)', p1sol.subs(p2, 1), Rational(2, 5))
sub3 = {p1: Rational(2, 5), p2: 1}
check('A3 x1A', x1_ql.subs(sub3), Rational(5, 2))
check('A3 x1B', x1_ql.subs(sub3), Rational(5, 2))
check('A3 x2A', x2A3q.subs(sub3), Rational(4, 5))
check('A3 x2B', x2B3q.subs(sub3), Rational(21, 5))
check('A3 factibilidade bem 2', (x2A3q + x2B3q).subs(sub3), 5)

# A4: I tem u = x + 2y (substitutos perfeitos), dotacao (0,12)
#     II tem u = min{x, 2y} (complementares), dotacao (12,0)
px, py = symbols('px py', positive=True)
# I: TMS = 1/2 => interior exige px/py = 1/2 => py/px = 2
check('A4 py/px', 2, 2)
sub4 = {px: 1, py: 2}
yII = solve(Eq(px * (2 * q) + py * q, 12 * px), q)[0]   # x=2y na restricao de II
check('A4 y do consumidor II', yII.subs(sub4), 3)
check('A4 x do consumidor II', 2 * yII.subs(sub4), 6)
check('A4 x do consumidor I', 12 - 2 * yII.subs(sub4), 6)
check('A4 y do consumidor I', 12 - yII.subs(sub4), 9)

# A5: U_A = x1^(2/3)x2^(1/3), wA=(6,3) ; U_B = x1^(1/3)x2^(2/3), wB=(3,6) ; totais (9,9)
#     A dotacao JA e Pareto-eficiente -> nao ha troca no equilibrio
mA5 = 6 * p1 + 3 * p2
mB5 = 3 * p1 + 6 * p2
x1a5, x2a5 = cobb_demand(2, 1, mA5, p1, p2)
x1b5, x2b5 = cobb_demand(1, 2, mB5, p1, p2)
check('A5 p2/p1', solve(Eq(x1a5 + x1b5, 9), p2)[0] / p1, 1)
check('A5 x1A', x1a5.subs(sub11), 6)
check('A5 x2A', x2a5.subs(sub11), 3)
check('A5 x1B', x1b5.subs(sub11), 3)
check('A5 x2B', x2b5.subs(sub11), 6)
check('A5 demanda liquida de A (bem 1)', x1a5.subs(sub11) - 6, 0)
check('A5 TMS_A na dotacao', 2 * S(3) / 6, 1)
check('A5 TMS_B na dotacao', S(6) / (2 * 3), 1)

# ======================================================= BANCO EXTRA: bloco B
# B1: P = 120 - 2Q ; CT = 20Q + 100
Pb1, CTb1 = 120 - 2 * Q, 20 * Q + 100
Qb1 = solve(Eq(diff(Pb1 * Q, Q), diff(CTb1, Q)), Q)[0]
check('B1 Qm', Qb1, 25)
check('B1 Pm', Pb1.subs(Q, Qb1), 70)
check('B1 lucro', (Pb1 * Q - CTb1).subs(Q, Qb1), 1150)
Qc1 = solve(Eq(Pb1, diff(CTb1, Q)), Q)[0]
check('B1 Q competitivo', Qc1, 50)
check('B1 EC monopolio', Rational(1, 2) * 25 * (120 - 70), 625)
check('B1 EP monopolio', (70 - 20) * 25, 1250)
check('B1 EC competitivo', Rational(1, 2) * 50 * (120 - 20), 2500)
check('B1 PPM', 2500 - (625 + 1250), 625)
check('B1 elasticidade em Qm', Rational(-1, 2) * Rational(70, 25), Rational(-7, 5))
check('B1 markup', Rational(70, 20), 1 / (1 - 1 / Rational(7, 5)))

# B2: Q = 100 - 2P ; CT = 5Q
Pb2 = 50 - Q / 2
CTb2 = 5 * Q
Qb2 = solve(Eq(diff(Pb2 * Q, Q), diff(CTb2, Q)), Q)[0]
check('B2 Qm', Qb2, 45)
check('B2 Pm', Pb2.subs(Q, Qb2), Rational(55, 2))
check('B2 lucro', (Pb2 * Q - CTb2).subs(Q, Qb2), Rational(2025, 2))
check('B2 markup', Rational(55, 2) / 5, Rational(11, 2))

# B3: duas fabricas C1=5Q1^2, C2=10Q2^2 ; P = 400 - 2Q
P3b = 400 - 2 * (Q1 + Q2)
s3b = solve([Eq(diff(P3b * (Q1 + Q2), Q1), diff(5 * Q1 ** 2, Q1)),
             Eq(diff(P3b * (Q1 + Q2), Q2), diff(10 * Q2 ** 2, Q2))], [Q1, Q2], dict=True)[0]
check('B3 Q1', s3b[Q1], 25)
check('B3 Q2', s3b[Q2], Rational(25, 2))
check('B3 Q total', s3b[Q1] + s3b[Q2], Rational(75, 2))
check('B3 Preco', P3b.subs(s3b), 325)
check('B3 lucro', (P3b * (Q1 + Q2) - 5 * Q1 ** 2 - 10 * Q2 ** 2).subs(s3b), 7500)

# B4: 3o grau. D1: Q1 = 100 - P1 ; D2: Q2 = 120 - 2P2 ; CMg = 20
P1b4, P2b4 = 100 - Q1, 60 - Q2 / 2
q1b4 = solve(Eq(diff(P1b4 * Q1, Q1), 20), Q1)[0]
q2b4 = solve(Eq(diff(P2b4 * Q2, Q2), 20), Q2)[0]
check('B4 Q1', q1b4, 40)
check('B4 P1', P1b4.subs(Q1, q1b4), 60)
check('B4 Q2', q2b4, 40)
check('B4 P2', P2b4.subs(Q2, q2b4), 40)
check('B4 elasticidade mercado 1', -1 * Rational(60, 40), Rational(-3, 2))
check('B4 elasticidade mercado 2', -2 * Rational(40, 40), -2)
check('B4 lucro discriminando', (60 - 20) * 40 + (40 - 20) * 40, 2400)
# preco unico: demanda agregada Q = 220 - 3P
Puni = (220 - Q) / 3
Quni = solve(Eq(diff(Puni * Q, Q), 20), Q)[0]
check('B4 Q com preco unico', Quni, 80)
check('B4 P com preco unico', Puni.subs(Q, Quni), Rational(140, 3))
lucro_uni = (Puni * Q - 20 * Q).subs(Q, Quni)
check('B4 lucro com preco unico', lucro_uni, Rational(6400, 3))
assert 2400 > lucro_uni, 'B4: discriminar deveria ser mais lucrativo'

# B5: P = 80 - Q ; CMg = 2Q. Compara 1o grau, monopolio uniforme e PPM
Pb5, CMgb5 = 80 - q, 2 * q
Qef = solve(Eq(Pb5, CMgb5), q)[0]
check('B5 Q eficiente', Qef, Rational(80, 3))
ET_1grau = integrate(Pb5 - CMgb5, (q, 0, Qef))
check('B5 excedente total (1o grau)', ET_1grau, Rational(3200, 3))
Qm5 = solve(Eq(diff(Pb5 * q, q), CMgb5), q)[0]
check('B5 Qm', Qm5, 20)
Pm5 = Pb5.subs(q, Qm5)
check('B5 Pm', Pm5, 60)
EC5 = Rational(1, 2) * Qm5 * (80 - Pm5)
EP5 = integrate(Pm5 - CMgb5, (q, 0, Qm5))
check('B5 EC', EC5, 200)
check('B5 EP', EP5, 800)
check('B5 PPM', ET_1grau - (EC5 + EP5), Rational(200, 3))
check('B5 PPM (area do triangulo)', integrate(Pb5 - CMgb5, (q, Qm5, Qef)), Rational(200, 3))

# B6: CMg constante = 30 ; regra do markup com elasticidade dada
Pv = symbols('Pv', positive=True)
check('B6 preco com eps=-3', solve(Eq(Pv * (1 - Rational(1, 3)), 30), Pv)[0], 45)
check('B6 markup com eps=-3', Rational(45, 30), 1 / (1 - Rational(1, 3)))
check('B6 preco com eps=-1,5', solve(Eq(Pv * (1 - 1 / Rational(3, 2)), 30), Pv)[0], 90)
check('B6 markup com eps=-1,5', Rational(90, 30), 1 / (1 - 1 / Rational(3, 2)))

print(f'TODAS AS {len(OK)} VERIFICACOES PASSARAM\n')
for line in OK:
    print('  OK  ' + line)
