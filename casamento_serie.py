
#import plotly.graph_objects as go
from cmath import polar, phase
from math import degrees, pi, pow
from numpy import format_float_scientific as format
import carta_de_smith


def posicao(theta):
    if theta == pi:
        return 0.25
    else:
        return round((pi - theta)/(4*pi), 4)


def circulos(R):
    ''' resolvendo o sistema de equações:
     x² +y² = R² (para tau_l)
     -
     (x-0.5)²+y² = 0.25 (para z = 1+0j)
     ---------------------
     x² - (x-0.5)² = R² - 0,25
     x -0.25 = R² -0,25
     x = R² (1)
     Assim, usando (1) para tau_l:
     (R²)² +y² = R²
     y² +(R^4-R²)= 0 (duas raizes opostas)'''
    x = R**2
    a = 1
    b = 0
    c = pow(R, 4)-(R**2)
    D = (b**2 - 4*a*c)
    y1 = (-b + D**(1/2)) / (2*a)
    y2 = -y1
    return x, y1, y2


def valor_d(d_inicial, d_final):
    if d_final > d_inicial:
        return d_final-d_inicial
    elif d_final < d_inicial:
        return 0.5-(d_inicial-d_final)
    else:
        return 0


def elemento_reativo(j, f):
    if j < 0:  # indutor
        L = abs(j/2*pi*f)
        return L, "Indutor"
    elif j > 0:
        C = 1/(2*pi*f*j)
        return C, "Capacitor"
    else:
        return 0


def l_metro(f, d):
    c = 3*(10**8)
    lam = c/f
    return lam*d


def cs(ZL, Z0, f):
    # passo 1
    zl = (ZL)/(Z0)
    # passo 2
    tau_l = ((ZL)-(Z0))/((ZL)+(Z0))
    ptau_l = polar(tau_l)  # armazena modulo e a fase
    print(zl, tau_l, ptau_l)  # apagar
    print(degrees(ptau_l[1]))  # apagar
    # passo3
    p_inicial = posicao(ptau_l[1])

    # passo 4 - 7
    x, y1, y2 = circulos(ptau_l[0])
    y = [y1, y2]
    tau_zd1 = complex(x, y1)
    tau_zd2 = complex(x, y2)
    # print(f"resultados de intersecção {circulos(ptau_l[0])}")  # apagar

    # passo 8
    zd = []

    for yx in y:
        # parte real de zd
        r = (1-pow(x, 2)-pow(yx, 2))/((pow(1-x, 2)+pow(yx, 2)))
        # parte imaginária
        j = (2*yx)/(pow(1-x, 2)+pow(yx, 2))

        zd.append(complex(round(r, 4), round(j, 4)))

    zd1 = zd[0]
    zd2 = zd[1]
    # print(f"valores de zd1 = {zd[0]} e de zd2 = {zd[1]}")  # apagar

    # passo 9 e 10

    theta1 = phase(zd1)
    theta2 = phase(zd2)
    p_d1 = posicao(theta1)
    p_d2 = posicao(theta2)
    print(f"zd1 está em {p_d1} e zd2 está em {p_d2}")  # apagar

    # passo 11
    d1 = round(valor_d(p_inicial, p_d1), 4)
    d2 = round(valor_d(p_inicial, p_d2), 4)
    d1_m = l_metro(f, d1)
    d1_m = l_metro(f, d1)

    #print(f"d1 = {d1} lambda e d2 = {d2} lambda")
    # passo 12
    Z_d1 = Z0*zd1
    Z_d2 = Z0*zd2
    #print(f"Zd1 = {Z_d1} lambda e Zd2 = {Z_d2} lambda")
    # passo 13
    valor1, el1 = elemento_reativo(Z_d1.imag, f)
    valor2, el2 = elemento_reativo(Z_d2.imag, f)
    #print( f" o Elemento de Zd1 é o {el1} = {valor1} e o elemento de Zd2 é o {el2} = {valor2}")

    # passo 14

    carta_de_smith.executar_grafico(ptau_l[0], tau_l, tau_zd1, tau_zd2)

    # passo 15 (retorna informações):

    resp1 = [Z_d1, d1, el1, format(valor1, precision=3)]
    resp2 = [Z_d2, d2, el2, format(valor2, precision=3)]
    return resp1, resp2
