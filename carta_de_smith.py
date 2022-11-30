import matplotlib.pyplot as plt
from numpy import arange


def executar_grafico(R, zl, zd1, zd2):
    figure, axes = plt.subplots(figsize=(12, 8))
    axes.set_aspect(1)
    axes.set_xlim(left=-1, right=1)
    axes.set_ylim(bottom=-1, top=1)
    axes.set_aspect(1)
    real_circules(axes)
    Imag_circules(axes)
    circulo_taul(R, axes)
    pontos(zl, zd1, zd2, axes)
    plt.title('Carta de Smith')
    plt.show()
    plt.close()


def real_circules(axes):
    # para desenhar os circulos, o matplot precisa apenas dos pontos do centro e do raio
    # o centro é dado por c= (r/(r+1),0) e o raio dado por R= (1/(r+1))
    # onde r é o valor de impedancia do circulo
    res = arange(0, 4, 0.2)

    for r in res:
        cx = r/(r+1)
        R = 1/(r+1)
        circulo = plt.Circle((cx, 0), R, fill=False)
        axes.add_artist(circulo)


def Imag_circules(axes):
    # o centro é dado por c= (1,1/x) e o raio dado por R= (1/x)
    # onde r é o valor de impedancia do circulo
    xes = arange(0.1, 4, 0.2)
    for x in xes:
        yx = 1/x
        R = 1/x
        circulo = plt.Circle((1, yx), R, fill=False)
        axes.add_artist(circulo)
        circulo = plt.Circle((1, -yx), R, fill=False)
        axes.add_artist(circulo)


def circulo_taul(R, axes):
    # está no centro, então xc = 0 e yc = 0
    # x² +y² = R²
    tau_l = plt.Circle((0, 0), R, fill=False, color="blue", label="Tau L")
    axes.add_artist(tau_l)
    plt.legend()


def pontos(zl, zd1, zd2, axes):
    axes.scatter(zl.real, zl.imag, label="Zl", color="g")
    plt.legend()

    axes.scatter(zd1.real, zd1.imag, label="Zd1", color="y")
    plt.legend()

    axes.scatter(zd2.real, zd2.imag, label="Zd2", color="r")
    plt.legend()


'''real_circules()
Imag_circules()
circulo_taul(0.644)
pontos((0.512+0.39j),(0.4146+0.4926j),(0.4146-0.4926j))
'''
