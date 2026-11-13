
import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path

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

caminho = Path(__file__).parent / "perfil.png"

imagem_perfil = Image.open(caminho)

imagem_perfil.thumbnail((90, 90))

foto_perfil = ImageTk.PhotoImage(imagem_perfil)

label_perfil = tk.Label(
    pagina,
    image=foto_perfil,
    bg="white"
)

label_perfil.place(
    x=50,
    y=35
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




caminho_sino = Path(__file__).parent / "sino.png"

imagem_sino = Image.open(caminho_sino)

imagem_sino.thumbnail((50, 60))

foto_sino = ImageTk.PhotoImage(imagem_sino)

label_sino = tk.Label(
    pagina,
    image=foto_sino,
    bg="white"
)

label_sino.place(
    x=365,
    y=45
)



caminho_logo = Path(__file__).parent / "logo.png"

imagem_logo = Image.open(caminho_logo)

imagem_logo.thumbnail((100, 100))

foto_logo = ImageTk.PhotoImage(imagem_logo)

label_logo = tk.Label(
    pagina,
    image=foto_logo,
    bg="white"
)

label_logo.place(
    relx=0.94,
    y=40,
    anchor="ne"
)



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



pasta = Path(__file__).parent

# IMAGEM DO SÍMBOLO DE PACIENTE
imagem_paciente = Image.open(pasta / "paciente.png")
imagem_paciente.thumbnail((110, 105))
foto_paciente = ImageTk.PhotoImage(imagem_paciente)

imagem_calendario = Image.open(pasta / "calendario.png")
imagem_calendario.thumbnail((110, 105))
foto_calendario = ImageTk.PhotoImage(imagem_calendario)



def criar_cartao(pai, nome, tipo):
    cartao = tk.Frame(
        pai,
        bg=AZUL_CLARO,
        width=190,
        height=190
    )

    cartao.pack(side="left", padx=18)
    cartao.pack_propagate(False)

    if tipo == "medico":
        simbolo = tk.Label(
            cartao,
            image=foto_paciente,
            bg=AZUL_CLARO
        )
        simbolo.pack(pady=(20, 5))

    elif tipo == "calendario":
        simbolo = tk.Label(
            cartao,
            image=foto_calendario,
            bg=AZUL_CLARO
        )
        simbolo.pack(pady=(20, 5))

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

