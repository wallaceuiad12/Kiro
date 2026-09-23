"""
Figuras adicionais para a Lista 1 resolvida e para o banco de exercicios extra.
Todos os numeros conferidos por verificar_contas.py.
Uso: python3 gerar_graficos_lista1.py
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.dirname(os.path.abspath(__file__))
plt.rcParams.update({
    "font.size": 11, "axes.titlesize": 12.5, "axes.titleweight": "bold",
    "figure.dpi": 130, "savefig.bbox": "tight", "savefig.facecolor": "white",
})
AZUL, VERM, VERDE, CINZA, LARANJA = "#1f4e79", "#c00000", "#2e7d32", "#555555", "#ef6c00"
ROXO = "#6a1b9a"


# ---------------------------------------------------------------------------
# Q5 — monopolista com duas fabricas (o diagrama que o enunciado pede)
# C1 = 10Q1^2 -> CMg1 = 20Q1 ; C2 = 20Q2^2 -> CMg2 = 40Q2 ; P = 700 - 5Q
# CMg total (soma HORIZONTAL): Q = CMg/20 + CMg/40 = 3CMg/40 -> CMg(Q) = 40Q/3
# Otimo: Q1 = 20, Q2 = 10, Q = 30, P = 550, CMg = RMg = 400
# ---------------------------------------------------------------------------
def fig_duas_fabricas():
    fig, ax = plt.subplots(figsize=(8.6, 5.9))
    q = np.linspace(0, 70, 500)

    ax.plot(q, 700 - 5 * q, color=AZUL, lw=2.8,
            label=r"Demanda = Receita Média:  $P = 700 - 5Q$")
    qr = np.linspace(0, 70, 500)
    ax.plot(qr, 700 - 10 * qr, color=VERM, lw=2.6,
            label=r"$RMg = 700 - 10Q$")
    ax.plot(q, 20 * q, color=VERDE, lw=2.2, ls="--",
            label=r"$CMg_1 = 20Q_1$  (Fábrica 1)")
    ax.plot(q, 40 * q, color=LARANJA, lw=2.2, ls="--",
            label=r"$CMg_2 = 40Q_2$  (Fábrica 2)")
    ax.plot(q, (40 / 3) * q, color=ROXO, lw=3.0,
            label=r"$CMg_{total} = \frac{40}{3}Q$  (soma horizontal)")
    ax.axhline(400, color=CINZA, ls=":", lw=1.8)
    ax.text(58, 412, r"$CMg_1 = CMg_2 = RMg = 400$", fontsize=9.5,
            color=CINZA, fontweight="bold")

    # pontos otimos
    for (qq, yy, cor, lab, off) in [
        (20, 400, VERDE, r"$Q_1 = 20$", (21.5, 300)),
        (10, 400, LARANJA, r"$Q_2 = 10$", (2.0, 300)),
        (30, 400, ROXO, r"$Q = 30$", (31.5, 200)),
    ]:
        ax.plot(qq, yy, "o", ms=10, color=cor, zorder=6)
        ax.plot([qq, qq], [0, yy], ":", color=cor, lw=1.5)
        ax.annotate(lab, (qq, 0), off, fontsize=10, color=cor, fontweight="bold",
                    arrowprops=dict(arrowstyle="->", color=cor, lw=1.4))

    ax.plot(30, 550, "*", ms=22, color="black", zorder=7)
    ax.annotate(r"$P = 700 - 5(30) = 550$", (30, 550), (33, 640),
                fontsize=10.5, fontweight="bold",
                arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.plot([0, 30], [550, 550], ":", color="black", lw=1.4)

    ax.annotate(r"Lucro $= 550(30) - 10(20)^2 - 20(10)^2 = \mathbf{10\,500}$",
                (36, 100), fontsize=10.5, fontweight="bold",
                bbox=dict(boxstyle="round", fc="#fff9c4", ec=CINZA))

    ax.set_xlim(0, 70); ax.set_ylim(0, 720)
    ax.set_xlabel("quantidade (da fábbrica ou total, conforme a curva)".replace("fábbrica", "fábrica"))
    ax.set_ylabel("R$")
    ax.set_title("Lista 1, Q5 — monopolista com duas fábricas:  $CMg_1 = CMg_2 = RMg$")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2, fontsize=8.8)
    ax.grid(alpha=0.15)
    fig.savefig(f"{OUT}/07-q5-duas-fabricas.png")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Q5(b) — choque de custo na Fabrica 1 (CMg1 = 20Q1 + 100)
# Novo otimo: Q1 = 115/7 ~ 16,43 ; Q2 = 75/7 ~ 10,71 ; Q = 190/7 ~ 27,14 ; P ~ 564,29
# ---------------------------------------------------------------------------
def fig_duas_fabricas_choque():
    fig, ax = plt.subplots(figsize=(8.0, 5.2))
    q = np.linspace(0, 45, 400)
    ax.plot(q, 700 - 10 * q, color=VERM, lw=2.6, label=r"$RMg = 700 - 10Q$")
    ax.plot(q, (40 / 3) * q, color=ROXO, lw=2.4, ls="--",
            label=r"$CMg_{total}$ antes")
    # Apos o choque: Q = (CMg-100)/20 + CMg/40 = 3CMg/40 - 5  ->  CMg = 40(Q+5)/3
    ax.plot(q, (40 / 3) * (q + 5), color=ROXO, lw=3.0,
            label=r"$CMg_{total}$ depois (desloca para cima)")

    for (Qv, cor, lab, dy) in [(30, CINZA, r"antes: $Q=30$, $P=550$", 0),
                               (190 / 7, "black", r"depois: $Q\approx27{,}14$, $P\approx564{,}29$", 0)]:
        cm = 700 - 10 * Qv
        ax.plot(Qv, cm, "*", ms=19, color=cor, zorder=6)
        ax.plot([Qv, Qv], [0, cm], ":", color=cor, lw=1.4)
    ax.annotate(r"antes: $Q=30$" "\n" r"$P=550$", (30, 400), (31.5, 300),
                fontsize=9.8, fontweight="bold",
                arrowprops=dict(arrowstyle="->", lw=1.3))
    ax.annotate(r"depois: $Q\approx27{,}1$" "\n" r"$P\approx564{,}3$", (190 / 7, 700 - 1900 / 7),
                (14.0, 250), fontsize=9.8, fontweight="bold",
                arrowprops=dict(arrowstyle="->", lw=1.3))

    ax.annotate("$Q_1$ CAI (16,43)   |   $Q_2$ SOBE (10,71)\n"
                "$Q$ total CAI   |   $P$ SOBE",
                (2.0, 620), fontsize=10.5, fontweight="bold",
                bbox=dict(boxstyle="round", fc="#e8f5e9", ec=VERDE))

    ax.set_xlim(0, 45); ax.set_ylim(0, 720)
    ax.set_xlabel("quantidade total  $Q$"); ax.set_ylabel("R$")
    ax.set_title("Lista 1, Q5(b) — alta do custo de mão de obra apenas na Fábrica 1")
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(alpha=0.15)
    fig.savefig(f"{OUT}/08-q5b-choque-custo.png")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Q3 — caixa de Edgeworth com um agente Leontief
# UA = x1^(1/3) x2^(2/3), wA=(10,20) ; UB = min{x1,x2}, wB=(20,5) ; caixa 30 x 25
# Curva de contrato: x2A = x1A - 5
# ---------------------------------------------------------------------------
def fig_edgeworth_leontief():
    fig, ax = plt.subplots(figsize=(7.8, 6.4))
    LX, LY = 30.0, 25.0

    # Curva de contrato
    xc = np.linspace(5, 30, 200)
    ax.plot(xc, xc - 5, color=VERDE, lw=3.2, zorder=4,
            label=r"Curva de contrato:  $x_2^A = x_1^A - 5$")

    # Curva de indiferenca de A pela dotacao: x1^(1/3) x2^(2/3) = u
    uA = 10 ** (1 / 3) * 20 ** (2 / 3)
    x = np.linspace(0.6, LX, 600)
    ax.plot(x, np.clip(uA ** 1.5 / np.sqrt(x), 0, LY * 1.4), color=VERM, lw=2.4,
            zorder=3, label=r"$U_A$ pela dotação ($\approx 15{,}87$)")

    # Curva de indiferenca de B (Leontief) pela dotacao: canto em A-coords (25,20)
    ax.plot([0, 25], [20, 20], color=AZUL, lw=2.4, zorder=3,
            label=r"$U_B = \min\{x_1,x_2\} = 5$ pela dotação")
    ax.plot([25, 25], [0, 20], color=AZUL, lw=2.4, zorder=3)
    ax.plot(25, 20, "o", ms=7, color=AZUL, zorder=5)

    # Pontos
    ax.plot(10, 20, "o", ms=12, color="black", zorder=7)
    ax.annotate(r"$W$: A=(10,20), B=(20,5)", (10, 20), (0.8, 22.9),
                fontsize=9.8, fontweight="bold",
                arrowprops=dict(arrowstyle="->", lw=1.3))
    ax.plot(10, 5, "s", ms=11, color=LARANJA, mec="black", zorder=7)
    ax.annotate(r"item (a): A=(10,5), B=(20,20)" "\n"
                r"satisfaz $x_1^B = x_2^B$ $\Rightarrow$ EFICIENTE",
                (10, 5), (1.0, 7.4), fontsize=9.2, fontweight="bold",
                bbox=dict(boxstyle="round", fc="#ffe0b2", ec=LARANJA),
                arrowprops=dict(arrowstyle="->", lw=1.3))

    # Item (d): com p=(1,1) o agente A demanda EXATAMENTE sua dotacao
    ax.text(13.2, 1.2,
            "item (d) com $p=(1,1)$:\n"
            r"A demanda $(10,20)$ = sua própria dotação $\Rightarrow e^A=(0,0)$" "\n"
            r"B demanda $(12{,}5;12{,}5) \Rightarrow e^B=(-7{,}5;\ +7{,}5)$" "\n"
            r"logo  $z = (-7{,}5;\ +7{,}5)$",
            fontsize=8.8, color=ROXO, fontweight="bold", va="bottom",
            bbox=dict(boxstyle="round", fc="#f3e5f5", ec=ROXO))

    ax.set_xlim(0, LX); ax.set_ylim(0, LY)
    ax.set_xlabel(r"bem 1 de A  $\longrightarrow$")
    ax.set_ylabel(r"bem 2 de A  $\longrightarrow$")
    ax.text(-1.9, -2.0, r"$0_A$", fontsize=13, fontweight="bold")
    ax.text(LX + 0.55, LY + 0.75, r"$0_B$", fontsize=13, fontweight="bold")
    sx = ax.secondary_xaxis("top"); sy = ax.secondary_yaxis("right")
    sx.set_xlabel(r"$\longleftarrow$  bem 1 de B")
    sy.set_ylabel(r"$\longleftarrow$  bem 2 de B")
    sx.set_ticks([0, 10, 20, 30], labels=["30", "20", "10", "0"])
    sy.set_ticks([0, 5, 15, 25], labels=["25", "20", "10", "0"])
    ax.set_title("Lista 1, Q3 — caixa de Edgeworth com agente Leontief (caixa 30 × 25)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.11), ncol=2, fontsize=8.6)
    ax.grid(alpha=0.15)
    fig.savefig(f"{OUT}/09-q3-edgeworth-leontief.png")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Q4 — monopolio com lucro zero: P = 18 - Q, CT = 27 + 2Q^2
# Qm = 3, Pm = 15, CMe(3) = 15 -> lucro exatamente zero
# ---------------------------------------------------------------------------
def fig_q4_lucro_zero():
    fig, ax = plt.subplots(figsize=(7.4, 5.3))
    q = np.linspace(0.45, 9, 600)
    ax.plot(q, 18 - q, color=AZUL, lw=2.7, label=r"Demanda  $P = 18 - Q$")
    qr = np.linspace(0, 9, 300)
    ax.plot(qr, 18 - 2 * qr, color=VERM, lw=2.5, label=r"$RMg = 18 - 2Q$")
    ax.plot(q, 4 * q, color=VERDE, lw=2.5, label=r"$CMg = 4Q$")
    ax.plot(q, 27 / q + 2 * q, color=LARANJA, lw=2.5, ls="--",
            label=r"$CMe = 27/Q + 2Q$")

    ax.plot(3, 12, "o", ms=9, color=VERDE, zorder=6)
    ax.annotate(r"$RMg = CMg$:  $18-2Q=4Q \Rightarrow Q_m=3$", (3, 12), (3.4, 6.0),
                fontsize=9.8, fontweight="bold",
                arrowprops=dict(arrowstyle="->", lw=1.3))
    ax.plot(3, 15, "*", ms=21, color="black", zorder=7)
    ax.plot([3, 3], [0, 15], ":", color=CINZA, lw=1.5)
    ax.plot([0, 3], [15, 15], ":", color=CINZA, lw=1.5)
    ax.annotate(r"$P_m = 15$  e  $CMe(3) = 15$" "\n"
                r"$\Rightarrow$ LUCRO = 0" "\n"
                r"(o preço apenas cobre o custo médio)",
                (3, 15), (4.55, 16.9), fontsize=9.4, fontweight="bold",
                bbox=dict(boxstyle="round", fc="#ffe0b2", ec=LARANJA),
                arrowprops=dict(arrowstyle="->", lw=1.4))

    ax.set_xlim(0, 9); ax.set_ylim(0, 27)
    ax.set_xlabel("quantidade  $Q$"); ax.set_ylabel("R$")
    ax.set_title("Lista 1, Q4 — monopolista com lucro zero:  $P=18-Q$,  $CT=27+2Q^2$")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=4, fontsize=8.8)
    ax.grid(alpha=0.15)
    fig.savefig(f"{OUT}/10-q4-lucro-zero.png")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Extra A3 — preferencias quase-lineares: U = ln(x1) + x2
# Curva de contrato VERTICAL em x1 = 2,5 ; equilibrio A=(2,5; 0,8), B=(2,5; 4,2)
# ---------------------------------------------------------------------------
def fig_quaselinear():
    fig, ax = plt.subplots(figsize=(7.2, 6.0))
    L = 5.0
    ax.axvline(2.5, color=VERDE, lw=3.2, zorder=4,
               label=r"Curva de contrato: RETA VERTICAL  $x_1^A = 2{,}5$")

    x = np.linspace(0.18, L - 0.05, 500)
    uA = np.log(2) + 1
    ax.plot(x, uA - np.log(x), color=VERM, lw=2.4, zorder=3,
            label=r"$U_A = \ln 2 + 1$ pela dotação")
    vB = np.log(3) + 4
    ax.plot(x, 5 - vB + np.log(np.clip(L - x, 1e-6, None)), color=AZUL, lw=2.4, zorder=3,
            label=r"$U_B = \ln 3 + 4$ pela dotação")

    ax.plot(2, 1, "o", ms=12, color="black", zorder=7)
    ax.annotate(r"$W$: A=(2,1), B=(3,4)", (2, 1), (0.42, 1.62),
                fontsize=9.6, fontweight="bold",
                arrowprops=dict(arrowstyle="->", lw=1.3))
    ax.plot(2.5, 0.8, "*", ms=22, color=LARANJA, mec="black", zorder=7)
    ax.annotate(r"$E$: A=(2,5; 0,8), B=(2,5; 4,2)" "\n" r"$p_1/p_2 = 2/5$",
                (2.5, 0.8), (2.92, 1.78), fontsize=9.4, fontweight="bold",
                bbox=dict(boxstyle="round", fc="#fff9c4", ec=CINZA),
                arrowprops=dict(arrowstyle="->", lw=1.3))

    ax.set_xlim(0, L); ax.set_ylim(0, L)
    ax.set_xlabel(r"bem 1 de A  $\longrightarrow$")
    ax.set_ylabel(r"bem 2 de A  $\longrightarrow$")
    ax.text(-0.36, -0.36, r"$0_A$", fontsize=13, fontweight="bold")
    ax.text(L + 0.14, L + 0.17, r"$0_B$", fontsize=13, fontweight="bold")
    sx = ax.secondary_xaxis("top"); sy = ax.secondary_yaxis("right")
    sx.set_xlabel(r"$\longleftarrow$  bem 1 de B")
    sy.set_ylabel(r"$\longleftarrow$  bem 2 de B")
    sx.set_ticks([0, 1, 2, 3, 4, 5], labels=["5", "4", "3", "2", "1", "0"])
    sy.set_ticks([0, 1, 2, 3, 4, 5], labels=["5", "4", "3", "2", "1", "0"])
    ax.set_title("Exercício A3 — preferências quase-lineares $U=\\ln x_1 + x_2$\n"
                 "a curva de contrato é uma reta VERTICAL", fontsize=11.5)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.11), ncol=1, fontsize=8.8)
    ax.grid(alpha=0.15)
    fig.savefig(f"{OUT}/11-a3-quaselinear.png")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Extra B1 — bem-estar com CMg constante: P = 120 - 2Q, CMg = 20
# Qm=25, Pm=70 ; Qc=50, Pc=20 ; EC_m=625, EP_m=1250, PPM=625
# ---------------------------------------------------------------------------
def fig_b1_bem_estar():
    fig, ax = plt.subplots(figsize=(7.6, 5.4))
    q = np.linspace(0, 58, 400)
    ax.plot(q, 120 - 2 * q, color=AZUL, lw=2.7, label=r"Demanda  $P = 120 - 2Q$")
    ax.plot(q, 120 - 4 * q, color=VERM, lw=2.5, label=r"$RMg = 120 - 4Q$")
    ax.axhline(20, color=VERDE, lw=2.7, label=r"$CMg = CMe = 20$")

    ax.fill([0, 0, 25], [70, 120, 70], color="#90caf9", alpha=0.85,
            label=r"$EC_m = 625$")
    ax.fill([0, 25, 25, 0], [70, 70, 20, 20], color="#a5d6a7", alpha=0.85,
            label=r"$EP_m = 1\,250$")
    ax.fill([25, 50, 25], [70, 20, 20], color="#ef5350", alpha=0.78,
            label=r"PPM $= 625$")

    for (Qv, Pv, lab, cor, off) in [(25, 70, r"$M$: $Q_m=25$, $P_m=70$", "black", (27, 92)),
                                    (50, 20, r"$E$: $Q_c=50$, $P_c=20$", ROXO, (43, 44))]:
        ax.plot(Qv, Pv, "*", ms=19, color=cor, zorder=7)
        ax.annotate(lab, (Qv, Pv), off, fontsize=9.8, color=cor, fontweight="bold",
                    arrowprops=dict(arrowstyle="->", color=cor, lw=1.3))
    ax.plot([25, 25], [0, 70], ":", color=CINZA, lw=1.4)

    ax.annotate(r"$|\epsilon|$ em $Q_m$ = 1,4  |  markup $P/CMg = 3{,}5 = \frac{1}{1-1/1{,}4}$",
                (1.2, 6.0), fontsize=9.6, fontweight="bold",
                bbox=dict(boxstyle="round", fc="#fff9c4", ec=CINZA))

    ax.set_xlim(0, 58); ax.set_ylim(0, 125)
    ax.set_xlabel("quantidade  $Q$"); ax.set_ylabel("preço  $P$")
    ax.set_title("Exercício B1 — bem-estar com custo marginal constante")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=3, fontsize=8.6)
    ax.grid(alpha=0.15)
    fig.savefig(f"{OUT}/12-b1-bem-estar.png")
    plt.close(fig)


if __name__ == "__main__":
    fig_duas_fabricas()
    fig_duas_fabricas_choque()
    fig_edgeworth_leontief()
    fig_q4_lucro_zero()
    fig_quaselinear()
    fig_b1_bem_estar()
    print("Figuras geradas:")
    for f in sorted(os.listdir(OUT)):
        if f.endswith(".png"):
            print("  -", f)
