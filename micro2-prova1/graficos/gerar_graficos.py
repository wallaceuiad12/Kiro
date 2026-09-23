"""
Gera as figuras do resumo da Prova 1 de Microeconomia II (CE-362 / Unicamp).
Todos os parametros numericos vem do material da disciplina:
  - Caixa de Edgeworth: Lista 1, Questao 1 (U = x1*x2, wA=(4,2), wB=(1,3))
  - Onus do monopolio: excedente.pdf (P = 100 - 2Q, CMg = 10 + 3Q)
  - Monopolio com custo quadratico: Revisao_EGeMONO.pdf (p = 100 - y, C = y^2/2 + 10)
Uso: python3 gerar_graficos.py
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.dirname(os.path.abspath(__file__))
plt.rcParams.update({
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
    "figure.dpi": 130,
    "savefig.bbox": "tight",
    "savefig.facecolor": "white",
})

AZUL, VERM, VERDE, CINZA, LARANJA = "#1f4e79", "#c00000", "#2e7d32", "#555555", "#ef6c00"


# ----------------------------------------------------------------------------
# 1. Caixa de Edgeworth - Lista 1, Q1
# ----------------------------------------------------------------------------
def fig_edgeworth():
    fig, ax = plt.subplots(figsize=(7.4, 6.6))
    L = 5.0
    x = np.linspace(0.05, L - 0.05, 600)

    # Curvas de indiferenca de A (origem em baixo-esquerda): x1*x2 = u
    for u, est, lw, lab in [(8, "-", 2.2, r"$U_A = 8$ (passa por $W$)"),
                            (9, "-", 2.6, r"$U_A = 9$ (passa por $E$)"),
                            (6, ":", 1.2, None), (11, ":", 1.2, None)]:
        ax.plot(x, u / x, est, color=VERM, lw=lw, zorder=3, label=lab)
    # Curvas de indiferenca de B (origem em cima-direita): (5-x1)(5-x2) = u
    for u, est, lw, lab in [(3, "-", 2.2, r"$U_B = 3$ (passa por $W$)"),
                            (4, "-", 2.6, r"$U_B = 4$ (passa por $E$)"),
                            (2, ":", 1.2, None), (6, ":", 1.2, None)]:
        ax.plot(x, L - u / (L - x), est, color=AZUL, lw=lw, zorder=3, label=lab)

    # Curva de contrato (diagonal): x2A = x1A
    ax.plot([0, L], [0, L], color=VERDE, lw=3, zorder=4,
            label="Curva de contrato  $x_2^A = x_1^A$")

    # Nucleo das trocas (trecho da curva de contrato dentro da lente)
    lo, hi = np.sqrt(8), L - np.sqrt(3)
    ax.plot([lo, hi], [lo, hi], color=VERDE, lw=8, alpha=0.35, zorder=2,
            label=f"Núcleo (trocas aceitas): [{lo:.2f}; {hi:.2f}]")

    # Lente de trocas mutuamente beneficas
    xx = np.linspace(lo - 0.4, hi + 0.4, 400)
    sup = np.minimum(L - 3 / (L - xx), L)
    inf = np.maximum(8 / xx, 0)
    m = sup > inf
    ax.fill_between(xx[m], inf[m], sup[m], color="#ffd54f", alpha=0.55, zorder=1,
                    label="Lente: ganhos mútuos de troca")

    # Reta orcamentaria: p1/p2 = 1 passando por W  =>  x2 = 6 - x1
    ax.plot(x, 6 - x, "--", color=CINZA, lw=2, zorder=3,
            label=r"Reta orçamentária  $p_1/p_2 = 1$")

    # Pontos
    ax.plot(4, 2, "o", ms=11, color="black", zorder=6)
    ax.annotate(r"$W$ = dotação" "\n" r"A=(4,2), B=(1,3)", (4, 2), (2.62, 0.72),
                fontsize=9.6, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="black", lw=1.3))
    ax.plot(3, 3, "*", ms=22, color=LARANJA, mec="black", mew=0.8, zorder=6)
    ax.annotate(r"$E$ = equilíbrio walrasiano" "\n" r"A=(3,3), B=(2,2)" "\n"
                r"$TMS_A = TMS_B = p_1/p_2 = 1$", (3, 3), (0.18, 0.75),
                fontsize=9.5, fontweight="bold",
                bbox=dict(boxstyle="round", fc="#fff9c4", ec=CINZA, alpha=0.95),
                arrowprops=dict(arrowstyle="->", color="black", lw=1.3))

    # Caixa e eixos duplos
    ax.set_xlim(0, L); ax.set_ylim(0, L)
    ax.set_xlabel(r"Bem 1 do agente A  $\longrightarrow$", fontsize=11)
    ax.set_ylabel(r"Bem 2 do agente A  $\longrightarrow$", fontsize=11)
    ax.text(-0.34, -0.36, r"$0_A$", fontsize=13, fontweight="bold")
    ax.text(L + 0.15, L + 0.17, r"$0_B$", fontsize=13, fontweight="bold")
    sec_x = ax.secondary_xaxis("top"); sec_y = ax.secondary_yaxis("right")
    sec_x.set_xlabel(r"$\longleftarrow$  Bem 1 do agente B", fontsize=11)
    sec_y.set_ylabel(r"$\longleftarrow$  Bem 2 do agente B", fontsize=11)
    sec_x.set_ticks([0, 1, 2, 3, 4, 5], labels=["5", "4", "3", "2", "1", "0"])
    sec_y.set_ticks([0, 1, 2, 3, 4, 5], labels=["5", "4", "3", "2", "1", "0"])

    ax.set_title("Caixa de Edgeworth — troca pura, $U_i = x_1 x_2$  (Lista 1, Q1)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.11), ncol=2,
              fontsize=8.8, framealpha=0.95)
    ax.grid(alpha=0.15)
    fig.savefig(f"{OUT}/01-caixa-edgeworth.png")
    plt.close(fig)


# ----------------------------------------------------------------------------
# 2. Demanda linear e Receita Marginal
# ----------------------------------------------------------------------------
def fig_demanda_rmg():
    fig, ax = plt.subplots(figsize=(7.2, 5.2))
    a, b = 100.0, 2.0
    q = np.linspace(0, a / b, 400)
    ax.plot(q, a - b * q, color=AZUL, lw=2.6, label=r"Demanda  $p(y) = a - by$")
    qr = np.linspace(0, a / (2 * b), 400)
    ax.plot(qr, a - 2 * b * qr, color=VERM, lw=2.6, label=r"$RMg(y) = a - 2by$")
    ax.plot(np.linspace(a / (2 * b), a / b, 100),
            a - 2 * b * np.linspace(a / (2 * b), a / b, 100), "--", color=VERM, lw=1.6)
    ax.axhline(0, color="black", lw=1)

    ax.axvline(a / (2 * b), color=CINZA, ls=":", lw=1.5)
    ax.annotate(r"$|\epsilon| = 1$" "\n" r"$RMg = 0$", (a / (2 * b), 8), (29, 30),
                fontsize=10, fontweight="bold",
                arrowprops=dict(arrowstyle="->", lw=1.2))
    ax.fill_between([0, a / (2 * b)], -40, 100, color="#c8e6c9", alpha=0.45)
    ax.fill_between([a / (2 * b), a / b], -40, 100, color="#ffcdd2", alpha=0.45)
    ax.text(10, 88, "REGIÃO ELÁSTICA\n" r"$|\epsilon| > 1$, $RMg > 0$",
            fontsize=9.5, color=VERDE, fontweight="bold")
    ax.text(33, -28, "REGIÃO INELÁSTICA — o monopolista\n"
                     r"NUNCA opera aqui ($RMg < 0$)",
            fontsize=9.5, color=VERM, fontweight="bold")
    ax.annotate("", (a / (2 * b), -14), (a / b, -14),
                arrowprops=dict(arrowstyle="<->", color=VERM, lw=1.6))
    ax.text(31.5, -10, r"metade do intercepto: $\frac{a}{2b}$ vs $\frac{a}{b}$",
            fontsize=9.5, color=VERM)

    ax.set_xlim(0, a / b + 2); ax.set_ylim(-40, 105)
    ax.set_xlabel("quantidade  $y$"); ax.set_ylabel("$p$,  $RMg$")
    ax.set_title("Demanda linear × Receita Marginal: a RMg tem o dobro da inclinação")
    ax.set_xticks([0, 25, 50]); ax.set_xticklabels(["0", r"$a/2b$", r"$a/b$"])
    ax.set_yticks([0, 100]); ax.set_yticklabels(["0", "$a$"])
    ax.legend(loc="upper right", fontsize=9.5)
    ax.grid(alpha=0.15)
    fig.savefig(f"{OUT}/02-demanda-rmg.png")
    plt.close(fig)


# ----------------------------------------------------------------------------
# 3. Equilibrio do monopolista com lucro (exemplo dos slides)
# ----------------------------------------------------------------------------
def fig_monopolio_equilibrio():
    fig, ax = plt.subplots(figsize=(7.2, 5.4))
    q = np.linspace(0.6, 100, 700)
    p = 100 - q                      # demanda inversa
    rmg = 100 - 2 * q                # receita marginal
    cmg = q                          # C(y) = y^2/2 + 10  =>  CMg = y
    cme = q / 2 + 10 / q             # CMe

    ym, pm = 100 / 3, 200 / 3
    cme_m = ym / 2 + 10 / ym

    ax.plot(q, p, color=AZUL, lw=2.6, label=r"Demanda  $p = 100 - y$")
    ax.plot(q[q <= 50], rmg[q <= 50], color=VERM, lw=2.6, label=r"$RMg = 100 - 2y$")
    ax.plot(q, cmg, color=VERDE, lw=2.6, label=r"$CMg = y$")
    ax.plot(q, cme, color=LARANJA, lw=2.2, ls="--", label=r"$CMe = y/2 + 10/y$")

    # Retangulo de lucro
    ax.fill_between([0, ym], cme_m, pm, color="#ffd54f", alpha=0.6,
                    label=fr"Lucro $\approx$ {(pm - cme_m) * ym:,.0f}".replace(",", "."))
    ax.plot([ym, ym], [0, pm], ":", color=CINZA, lw=1.6)
    ax.plot([0, ym], [pm, pm], ":", color=CINZA, lw=1.6)
    ax.plot(ym, pm, "*", ms=20, color="black", zorder=6)
    ax.plot(ym, ym, "o", ms=8, color=VERDE, zorder=6)
    ax.annotate(r"$RMg = CMg$" "\n" r"$y_m = 100/3$", (ym, ym), (46, 12),
                fontsize=10, fontweight="bold",
                arrowprops=dict(arrowstyle="->", lw=1.3))
    ax.annotate(r"$p_m = 200/3 \approx 66{,}7$", (ym, pm), (40, 84),
                fontsize=10, fontweight="bold",
                arrowprops=dict(arrowstyle="->", lw=1.3))

    # Benchmark competitivo: p = CMg
    ax.plot(50, 50, "s", ms=9, color="#6a1b9a", zorder=6)
    ax.annotate(r"C. perfeita: $p = CMg$" "\n" r"$y_c = 50,\ p_c = 50$", (50, 50), (57, 62),
                fontsize=9.5, color="#6a1b9a", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#6a1b9a", lw=1.3))

    ax.set_xlim(0, 85); ax.set_ylim(0, 105)
    ax.set_xlabel("quantidade  $y$"); ax.set_ylabel("$p$,  custos,  $RMg$")
    ax.set_title("Equilíbrio do monopolista:  $p = 100 - y$,  $C(y) = y^2/2 + 10$")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=3, fontsize=9)
    ax.grid(alpha=0.15)
    fig.savefig(f"{OUT}/03-monopolio-equilibrio.png")
    plt.close(fig)


# ----------------------------------------------------------------------------
# 4. Onus do monopolio - excedente.pdf: P = 100 - 2Q, CMg = 10 + 3Q
# ----------------------------------------------------------------------------
def fig_onus_monopolio():
    fig, ax = plt.subplots(figsize=(7.6, 5.8))
    Qc, Pc = 18.0, 64.0
    Qm, Pm = 90 / 7, 520 / 7
    CMgm = 10 + 3 * Qm                      # 340/7
    q = np.linspace(0, 26, 500)

    ax.plot(q, 100 - 2 * q, color=AZUL, lw=2.6, label=r"Demanda  $P = 100 - 2Q$")
    ax.plot(q, 10 + 3 * q, color=VERDE, lw=2.6, label=r"Oferta = $CMg = 10 + 3Q$")
    qr = np.linspace(0, 25, 300)
    ax.plot(qr, 100 - 4 * qr, color=VERM, lw=2.4, ls="-", label=r"$RMg = 100 - 4Q$")

    # EC do monopolio (triangulo acima de Pm)
    ax.fill([0, 0, Qm], [Pm, 100, Pm], color="#90caf9", alpha=0.85,
            label=r"$EC_m = 165{,}31$")
    # EP do monopolio: retangulo + triangulo
    ax.fill([0, Qm, Qm, 0], [Pm, Pm, CMgm, 10], color="#a5d6a7", alpha=0.85,
            label=r"$EP_m = 578{,}57$")
    # Perda de peso morto (triangulo entre Qm e Qc)
    ax.fill([Qm, Qc, Qm], [Pm, Pc, CMgm], color="#ef5350", alpha=0.75,
            label=r"PPM $= 66{,}12$")

    # Transferencia EC -> EP
    ax.plot([0, Qm], [Pc, Pc], ":", color=CINZA, lw=1.5)
    ax.annotate(r"Transferência EC$\to$EP" "\n" r"$= 132{,}24$", (Qm / 2, (Pm + Pc) / 2),
                (1.0, 40), fontsize=9.5, fontweight="bold",
                arrowprops=dict(arrowstyle="->", lw=1.2))

    for (Q, P, lab, cor, off) in [(Qc, Pc, r"$E$ competitivo" "\n" r"$Q_c=18,\ P_c=64$",
                                   "#6a1b9a", (19.2, 40)),
                                  (Qm, Pm, r"$M$ monopólio" "\n" r"$Q_m\approx12{,}86$" "\n" r"$P_m\approx74{,}29$",
                                   "black", (15.8, 84))]:
        ax.plot(Q, P, "*", ms=19, color=cor, zorder=7)
        ax.annotate(lab, (Q, P), off, fontsize=9.5, color=cor, fontweight="bold",
                    arrowprops=dict(arrowstyle="->", color=cor, lw=1.3))
    ax.plot([Qm, Qm], [0, Pm], ":", color=CINZA, lw=1.4)
    ax.plot([Qc, Qc], [0, Pc], ":", color=CINZA, lw=1.4)

    ax.set_xlim(0, 26); ax.set_ylim(0, 103)
    ax.set_xlabel("quantidade  $Q$"); ax.set_ylabel("preço  $P$")
    ax.set_title("Ônus do monopólio — bem-estar:  $P = 100 - 2Q$,  $CMg = 10 + 3Q$")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=3,
              fontsize=8.8, framealpha=0.95)
    ax.grid(alpha=0.15)
    fig.savefig(f"{OUT}/04-onus-monopolio.png")
    plt.close(fig)


# ----------------------------------------------------------------------------
# 5. Discriminacao de precos: 1o, 2o e 3o graus
# ----------------------------------------------------------------------------
def fig_discriminacao():
    fig, axes = plt.subplots(1, 3, figsize=(15.5, 4.7))

    # --- 1o grau (mesma economia da Fig. 4, para comparacao direta) --------
    ax = axes[0]
    q = np.linspace(0, 24, 300)
    ax.plot(q, 100 - 2 * q, color=AZUL, lw=2.6, label="Demanda $P = 100 - 2Q$")
    ax.plot(q, 10 + 3 * q, color=VERDE, lw=2.6, label="$CMg = 10 + 3Q$")
    Qs = 18.0
    ax.fill([0, 0, Qs], [10, 100, 10 + 3 * Qs], color="#a5d6a7", alpha=0.8,
            label="EP = excedente TOTAL = 810")
    ax.plot(Qs, 10 + 3 * Qs, "*", ms=17, color="black", zorder=6)
    ax.axvline(Qs, ls=":", color=CINZA)
    ax.annotate(r"produz até $p = CMg$:" "\n" r"$Q = 18$ (EFICIENTE)", (Qs, 64), (7.5, 20),
                fontsize=8.8, fontweight="bold",
                arrowprops=dict(arrowstyle="->", lw=1.2))
    ax.set_title("1º grau (perfeita)\nEC = 0,  PPM = 0,  $Q$ eficiente")
    ax.text(0.8, 78, "Cobra de cada consumidor\nexatamente a sua\ndisposição a pagar.\n"
                     "Quantidade eficiente,\nmas a firma fica com\n"
                     "TODO o excedente\n(810 em vez de 578,57).", fontsize=8.4,
            va="top", bbox=dict(boxstyle="round", fc="#fff9c4", ec=CINZA, alpha=0.9))
    ax.set_xlim(0, 24); ax.set_ylim(0, 103)
    ax.set_xlabel("$Q$"); ax.set_ylabel("$P$")
    ax.legend(fontsize=7.8, loc="lower right"); ax.grid(alpha=0.15)

    # --- 2o grau (exemplo dos slides) -------------------------------------
    ax = axes[1]
    tipoA = [30, 20, 10]
    tipoB = [20, 10]
    ax.bar([0.8, 1.8, 2.8], tipoA, width=0.38, color="#1f4e79",
           label="Tipo A: 30, 20, 10")
    ax.bar([1.2, 2.2], tipoB, width=0.38, color="#c00000",
           label="Tipo B: 20, 10")
    ax.axhline(0, color="black", lw=1)
    ax.set_xticks([1, 2, 3]); ax.set_xticklabels(["1ª unid.", "2ª unid.", "3ª unid."])
    ax.set_ylabel("disposição a pagar (R$)")
    ax.set_title("2º grau (por quantidade / versão)\n"
                 "disposição a pagar por unidade — exemplo dos slides")
    ax.text(1.62, 37.5, "Pacote 1: 2 un. por R\\$ 30\n"
                        r"   $\rightarrow$ captura o Tipo B (20+10)" "\n"
                        "Pacote 2: 3 un. por R\\$ 60\n"
                        r"   $\rightarrow$ captura o Tipo A (30+20+10)",
            fontsize=8.4, va="top",
            bbox=dict(boxstyle="round", fc="#fff9c4", ec=CINZA))
    ax.set_ylim(0, 44); ax.legend(fontsize=8.5, loc="upper left"); ax.grid(alpha=0.15, axis="y")

    # --- 3o grau: calibrado para eps1 = -2 e eps2 = -4 no otimo (Lista 1, Q6)
    # D1: p = 60 - 2Q   -> RMg1 = 60 - 4Q = 20 => Q1 = 10, p1 = 40, eps1 = -2
    # D2: p = 100/3 - Q/2 -> RMg2 = 100/3 - Q = 20 => Q2 = 40/3, p2 = 80/3, eps2 = -4
    ax = axes[2]
    q = np.linspace(0, 32, 400)
    cmg = 20.0
    ax.plot(q, 60 - 2 * q, color=AZUL, lw=2.4, label=r"$D_1$: $p = 60 - 2Q$")
    ax.plot(q, 60 - 4 * q, "--", color=AZUL, lw=1.6, label=r"$RMg_1 = 60 - 4Q$")
    ax.plot(q, 100 / 3 - 0.5 * q, color=VERM, lw=2.4, label=r"$D_2$: $p = \frac{100}{3} - \frac{Q}{2}$")
    ax.plot(q, 100 / 3 - 1.0 * q, "--", color=VERM, lw=1.6, label=r"$RMg_2 = \frac{100}{3} - Q$")
    ax.axhline(cmg, color=VERDE, lw=2.6, label=r"$CMg = 20$")

    q1, p1 = 10.0, 40.0          # eps1 = -(1/2)(40/10) = -2
    q2, p2 = 40 / 3, 80 / 3      # eps2 = -(2)(26,67/13,33) = -4
    for (qq, pp, cor, lab) in [(q1, p1, AZUL, r"$p_1 = 40$" "\n" r"$|\epsilon_1| = 2$"),
                               (q2, p2, VERM, r"$p_2 = 80/3 \approx 26{,}7$" "\n" r"$|\epsilon_2| = 4$")]:
        ax.plot(qq, pp, "*", ms=17, color=cor, zorder=6)
        ax.plot([qq, qq], [0, pp], ":", color=cor, lw=1.3)
        ax.plot([0, qq], [pp, pp], ":", color=cor, lw=1.3)
        ax.annotate(lab, (qq, pp), (qq + 1.4, pp + 3.5), fontsize=9,
                    color=cor, fontweight="bold")
    ax.annotate(r"$\dfrac{p_1}{p_2} = \dfrac{40}{80/3} = 1{,}5$" "\n"
                r"(e NÃO 2,5 — ver Lista 1, Q6)", (2.2, 6.0), fontsize=9.5,
                fontweight="bold",
                bbox=dict(boxstyle="round", fc="#fff9c4", ec=CINZA))
    ax.set_title("3º grau (por grupos)\n"
                 r"$RMg_1 = RMg_2 = CMg$  →  $p$ maior onde $|\epsilon|$ é menor")
    ax.set_xlim(0, 28); ax.set_ylim(0, 65)
    ax.set_xlabel("$Q$ em cada mercado"); ax.set_ylabel("$P$")
    ax.legend(fontsize=7.8, loc="upper right"); ax.grid(alpha=0.15)

    fig.suptitle("Discriminação de preços — os três graus", fontsize=15, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.90))
    fig.savefig(f"{OUT}/05-discriminacao-precos.png")
    plt.close(fig)


# ----------------------------------------------------------------------------
# 6. Lei de Walras / demanda excedente agregada (exemplo dos slides)
# ----------------------------------------------------------------------------
def fig_walras():
    fig, ax = plt.subplots(figsize=(7.2, 5.0))
    # Slides: U_A = x1 (x2)^2, w_A=(10,10); U_B = (x1)^2 x2, w_B=(20,20); p1 = 1
    p2 = np.linspace(0.25, 2.2, 400)
    x1A = 10 * (1 + p2) / 3
    x1B = 40 * (1 + p2) / 3
    z1 = x1A + x1B - 30                     # demanda excedente do bem 1
    x2A = 20 * (1 + p2) / (3 * p2)
    x2B = 20 * (1 + p2) / (3 * p2)
    z2 = x2A + x2B - 30                     # demanda excedente do bem 2

    ax.plot(p2, z1, color=AZUL, lw=2.6, label=r"$z_1(p_2)$ — demanda excedente do bem 1")
    ax.plot(p2, z2, color=VERM, lw=2.6, label=r"$z_2(p_2)$ — demanda excedente do bem 2")
    ax.axhline(0, color="black", lw=1.2)
    ax.axvline(0.8, color=VERDE, ls="--", lw=2,
               label=r"$p_2^* = 0{,}8$  $\Rightarrow$  $z_1 = z_2 = 0$")
    ax.plot(0.8, 0, "o", ms=11, color=VERDE, zorder=6)
    ax.annotate("Lei de Walras: basta zerar UM mercado —\n"
                "o outro zera automaticamente.\n"
                r"Só o preço RELATIVO $p_2/p_1$ é determinado.",
                (0.8, 0), (0.95, -9), fontsize=9.5, fontweight="bold",
                arrowprops=dict(arrowstyle="->", lw=1.3))
    ax.fill_between(p2, 0, z1, where=(z1 > 0), color="#ffcdd2", alpha=0.5)
    ax.text(1.02, 9.0, r"$p_2$ alto demais:  $z_1 > 0$ e $z_2 < 0$" "\n"
                       "excesso de demanda do bem 1,\n"
                       "excesso de oferta do bem 2\n"
                       r"$\Rightarrow$ leiloeiro REDUZ $p_2$",
            fontsize=8.6, color=VERM)
    ax.text(0.285, 4.0, r"$p_2$ baixo demais:" "\n" r"$z_1 < 0$ e $z_2 > 0$" "\n"
                        r"$\Rightarrow$ leiloeiro AUMENTA $p_2$",
            fontsize=8.6, color=AZUL)

    ax.set_xlim(0.25, 2.2); ax.set_ylim(-22, 16)
    ax.set_xlabel(r"preço do bem 2  ($p_1 = 1$ como numerário)")
    ax.set_ylabel(r"demanda excedente agregada  $z_i$")
    ax.set_title("Tâtonnement e Lei de Walras — exemplo dos slides\n"
                 r"$U_A = x_1(x_2)^2,\ w_A=(10,10)$;  $U_B = (x_1)^2 x_2,\ w_B=(20,20)$",
                 fontsize=11.5)
    ax.legend(fontsize=9, loc="lower left")
    ax.grid(alpha=0.15)
    fig.savefig(f"{OUT}/06-lei-de-walras.png")
    plt.close(fig)


if __name__ == "__main__":
    fig_edgeworth()
    fig_demanda_rmg()
    fig_monopolio_equilibrio()
    fig_onus_monopolio()
    fig_discriminacao()
    fig_walras()
    print("Figuras geradas em:", OUT)
    for f in sorted(os.listdir(OUT)):
        if f.endswith(".png"):
            print("  -", f)
