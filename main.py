
import casamento_serie
from tkinter import *

pagina = Tk()
entrada = Frame(pagina)
saida = Frame(pagina)
pagina.title("Casamento de impedância")
pagina.geometry("500x300")
pagina.maxsize(500, 300)
pagina.configure(background="#DCDCDC")


# função limpar
def limpa_tela():
    caixa1real.delete(0, END)
    caixa1imag.delete(0, END)
    caixaf.delete(0, END)
    caixaz0.delete(0, END)


def executa():
    # pega os dados
    zl_r = int(caixa1real.get().strip())
    zl_img = int(caixa1imag.get())
    zl = complex(zl_r, zl_img)
    z0 = int(caixaz0.get())
    f = int(caixaf.get())*(10**6)

    saida.place(relx=0.51, rely=0.01, relwidth=0.48, relheight=0.95)
    resultos = Label(saida, text="RESULTADOS", font='bold', bg="#d3d3d3", bd=2)
    resultos.place(relx=0, rely=0, relwidth=1)
    print("ok")
    # executa programa
    resp1, resp2 = casamento_serie.cs(zl, z0, f)

    # interface resposta
    fonte = ("Arial", 11)
    Imp1 = Label(saida, text="Zd1:", font=fonte, bg="#d3d3d3")
    d1 = Label(saida, text="d1 (lambda):", font=fonte)
    elemento = Label(saida, text="elemento série:", font=fonte)
    Valor_elemento = Label(saida, text="valor(F ou H):", font=fonte)
    Imp1.place(relx=0.005, rely=0.1)
    d1.place(relx=0.005, rely=0.2)
    elemento.place(relx=0.005, rely=0.3)
    Valor_elemento.place(relx=0.005, rely=0.4)

    out_zd1 = Label(saida, text=str(resp1[0]), font=fonte, bg="#d3d3d3")
    out_d1 = Label(saida, text=str(resp1[1]), font=fonte)
    out_elemento = Label(saida, text=str(resp1[2]), font=fonte)
    out_valor = Label(saida, text=str(resp1[3]), font=fonte)
    out_zd1.place(relx=0.15, rely=0.1)
    out_d1.place(relx=0.37, rely=0.2)
    out_elemento.place(relx=0.45, rely=0.3)
    out_valor.place(relx=0.45, rely=0.4)

    Imp2 = Label(saida, text="Zd2:", font=fonte, bg="#d3d3d3")
    d2 = Label(saida, text="d2 (lambda):", font=fonte)
    elemento2 = Label(saida, text="elemento série:", font=fonte)
    Valor_elemento2 = Label(saida, text="valor(F ou H):", font=fonte)
    Imp2.place(relx=0.005, rely=0.6)
    d2.place(relx=0.005, rely=0.7)
    elemento2.place(relx=0.005, rely=0.8)
    Valor_elemento2.place(relx=0.005, rely=0.9)

    out_zd2 = Label(saida, text=str(resp2[0]), font=fonte, bg="#d3d3d3")
    out_d2 = Label(saida, text=str(resp2[1]), font=fonte)
    out_elemento2 = Label(saida, text=str(resp2[2]), font=fonte)
    out_valor2 = Label(saida, text=str(resp2[3]), font=fonte)
    out_zd2.place(relx=0.15, rely=0.6)
    out_d2.place(relx=0.37, rely=0.7)
    out_elemento2.place(relx=0.45, rely=0.8)
    out_valor2.place(relx=0.45, rely=0.9)


# interface


entrada.place(relx=0.01, rely=0.01, relwidth=0.48, relheight=0.95)

texto1 = Label(entrada, text="Impêdancia da Carga (ZL):")
texto1.place(relx=0.25, rely=0.02)
texto2 = Label(entrada, text="Parte resistiva:")
texto2.place(relx=0.15, rely=0.1)
texto3 = Label(entrada, text="Parte reativa:")
texto3.place(relx=0.55, rely=0.1)
caixa1real = Entry(entrada)
caixa1real.place(relx=0.15, rely=0.2, relwidth=0.3, relheight=0.1)
caixa1imag = Entry(entrada)
caixa1imag.place(relx=0.55, rely=0.2, relwidth=0.3, relheight=0.1)

texto4 = Label(entrada, text="Impêdancia da Linha (Z0):")
texto4.place(relx=0.01, rely=0.37)
caixaz0 = Entry(entrada)
caixaz0.place(relx=0.6, rely=0.36, relwidth=0.25, relheight=0.08)

texto5 = Label(entrada, text="Frequência (f):")
texto5.place(relx=0.01, rely=0.49)
caixaf = Entry(entrada)
caixaf.place(relx=0.6, rely=0.49, relwidth=0.25, relheight=0.08)
texto6 = Label(entrada, text="MHz")
texto6.place(relx=0.85, rely=0.49)

texto1 = Label(entrada, text="Tipo de cansamento:")
texto1.place(relx=0.25, rely=0.6)


serie = Button(entrada, text="Em série",
               command=lambda: executa())
serie.place(relx=0, rely=0.7, relwidth=0.5, relheight=0.1)
paralelo1 = Button(entrada, text="Paralelo em curto")
paralelo1.place(relx=0.5, rely=0.7, relwidth=0.5, relheight=0.1)
paralelo2 = Button(entrada, text="Paralelo aberto")
paralelo2.place(relx=0, rely=0.8, relwidth=0.5, relheight=0.1)
duplo = Button(entrada, text="Toco duplo")
duplo.place(relx=0.5, rely=0.8, relwidth=0.5, relheight=0.1)
limpar = Button(entrada, text="limpar",
                command=lambda: limpa_tela())
limpar.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)


pagina.mainloop()
