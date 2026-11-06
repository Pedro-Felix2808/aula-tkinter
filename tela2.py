
import tkinter as tk

AZUL = "#298FC2"
AZUL_CLARO = "#99D8F7"
AZUL_ESCURO = "#4D8BC8"
FUNDO = "white"

janela = tk.Tk()
janela.title("Doctor - Home")
janela.geometry("1200x700")
janela.configure(bg=FUNDO)

pagina = tk.Frame(janela, bg=FUNDO)
pagina.place(
    relx=0.5,
    rely=0.5,
    relwidth=1,
    relheight=1,
    anchor="center"
)

avatar = tk.Canvas(
    pagina,
    width=80,
    height=80,
    bg=FUNDO,
    highlightthickness=0
)
avatar.place(x=50, y=35)

avatar.create_oval(
    5, 5, 75, 75,
    fill=AZUL_CLARO,
    outline=AZUL,
    width=2
)


avatar.create_oval(
    28, 18, 52, 47,
    fill="white",
    outline=AZUL_ESCURO,
    width=2
)


avatar.create_arc(
    18, 40, 62, 83,
    start=0,
    extent=180,
    style="pieslice",
    fill="#DDF2FF",
    outline=AZUL_ESCURO,
    width=2
)


boas_vindas = tk.Label(
    pagina,
    text="BEM VINDO JUAN",
    font=("Arial", 12, "bold"),
    bg="#DDF2FF",
    fg=AZUL,
    padx=25,
    pady=15
)
boas_vindas.place(x=150, y=48)


sino = tk.Canvas(
    pagina,
    width=50,
    height=60,
    bg=FUNDO,
    highlightthickness=0
)
sino.place(x=365, y=45)

sino.create_arc(
    10, 10, 40, 45,
    start=0,
    extent=180,
    style="pieslice",
    fill="#DDF2FF",
    outline=AZUL_ESCURO,
    width=2
)

sino.create_line(
    10, 25, 10, 43, 40, 43, 40, 25,
    fill=AZUL_ESCURO,
    width=2
)

sino.create_oval(
    22, 43, 28, 49,
    fill=AZUL_ESCURO,
    outline=AZUL_ESCURO
)


logo = tk.Label(
    pagina,
    text="a+",
    font=("Arial", 32, "bold"),
    bg=FUNDO,
    fg=AZUL
)
logo.place(relx=0.94, y=40, anchor="ne")


frame_centro = tk.Frame(
    pagina,
    bg=FUNDO
)

frame_centro.place(
    relx=0.5,
    rely=0.53,
    anchor="center"
)

titulo = tk.Label(
    frame_centro,
    text="PERFIL: MÉDICO",
    font=("Arial", 13),
    fg=AZUL,
    bg=FUNDO
)
titulo.pack(anchor="w", pady=(0, 10))


frame_cartoes = tk.Frame(
    frame_centro,
    bg=FUNDO
)
frame_cartoes.pack()

def criar_cartao(pai, nome, tipo):

    cartao = tk.Frame(
        pai,
        bg=AZUL_CLARO,
        width=190,
        height=190
    )

    cartao.pack(
        side="left",
        padx=18
    )

    cartao.pack_propagate(False)

    desenho = tk.Canvas(
        cartao,
        width=110,
        height=105,
        bg=AZUL_CLARO,
        highlightthickness=0
    )
    desenho.pack(pady=(20, 5))

    if tipo == "medico":

        desenho.create_oval(
            40, 15, 70, 55,
            fill="white",
            outline=AZUL_ESCURO,
            width=3
        )

     
        desenho.create_arc(
            20, 55, 90, 110,
            start=0,
            extent=180,
            style="pieslice",
            fill="#DDF2FF",
            outline=AZUL_ESCURO,
            width=3
        )

    else:

        desenho.create_rectangle(
            25, 12, 85, 85,
            fill="white",
            outline=AZUL_ESCURO,
            width=3
        )

        desenho.create_line(
            25, 25, 85, 25,
            fill=AZUL_ESCURO,
            width=3
        )

        desenho.create_text(
            55, 55,
            text="12",
            font=("Arial", 25),
            fill=AZUL_ESCURO
        )

   
    texto = tk.Label(
        cartao,
        text=nome,
        font=("Arial", 13, "bold"),
        bg=AZUL_CLARO,
        fg="white"
    )
    texto.pack(pady=5)


criar_cartao(frame_cartoes, "PACIENTES", "medico")
criar_cartao(frame_cartoes, "PALESTRAS", "calendario")
criar_cartao(frame_cartoes, "CONSULTAS", "calendario")



ajuda = tk.Label(
    pagina,
    text="PRECISA DE AJUDA?  ☹",
    font=("Arial", 22, "bold"),
    bg=FUNDO,
    fg=AZUL
)

ajuda.place(
    relx=0.5,
    rely=0.85,
    anchor="center"
)


janela.mainloop()

