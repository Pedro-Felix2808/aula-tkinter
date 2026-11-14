
import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path


AZUL = "#298FC2"
AZUL_CLARO = "#DDF2FF"
FUNDO = "white"
CINZA_CLARO = "#F2F8FC"

 
janela = tk.Tk()
janela.title("Doctor - Palestras")
janela.geometry("1200x700")
janela.configure(bg=FUNDO)


pasta = Path(__file__).parent


imagem_perfil = Image.open(pasta / "perfil.png")
imagem_perfil.thumbnail((80, 80))
foto_perfil = ImageTk.PhotoImage(imagem_perfil)


imagem_sino = Image.open(pasta / "sino.png")
imagem_sino.thumbnail((45, 50))
foto_sino = ImageTk.PhotoImage(imagem_sino)


imagem_logo = Image.open(pasta / "logo.png")
imagem_logo.thumbnail((100, 80))
foto_logo = ImageTk.PhotoImage(imagem_logo)


frame_topo = tk.Frame(janela, bg=FUNDO)
frame_topo.pack(fill="x", padx=50, pady=(30, 10))


label_perfil = tk.Label(
    frame_topo,
    image=foto_perfil,
    bg=FUNDO
)
label_perfil.pack(side="left")


boas_vindas = tk.Label(
    frame_topo,
    text="BEM VINDO JUAN",
    font=("Arial", 12, "bold"),
    bg=AZUL_CLARO,
    fg=AZUL,
    padx=22,
    pady=12
)
boas_vindas.pack(side="left", padx=20)


label_sino = tk.Label(
    frame_topo,
    image=foto_sino,
    bg=FUNDO
)
label_sino.pack(side="left")


label_logo = tk.Label(
    frame_topo,
    image=foto_logo,
    bg=FUNDO
)
label_logo.pack(side="right")



frame_titulo = tk.Frame(janela, bg=FUNDO)
frame_titulo.pack(fill="x", padx=80, pady=(20, 25))

# Texto Voltar apenas visual
voltar = tk.Label(
    frame_titulo,
    text="←  Voltar",
    font=("Arial", 14),
    fg=AZUL,
    bg=FUNDO
)
voltar.place(x=0, rely=0.5, anchor="w")


titulo = tk.Label(
    frame_titulo,
    text="PALESTRAS",
    font=("Arial", 22, "bold"),
    fg=AZUL,
    bg=FUNDO
)
titulo.pack()

# ===================================
# TABELA
# ===================================

# Frame que contém a tabela
frame_tabela = tk.Frame(
    janela,
    bg=FUNDO
)
frame_tabela.pack(
    fill="x",
    padx=80,
    pady=(10, 0)
)

# Configuração das cinco colunas
for coluna in range(5):
    frame_tabela.grid_columnconfigure(
        coluna,
        weight=1,
        uniform="colunas"
    )

# Nomes das colunas
colunas = [
    "Palestra",
    "Data",
    "Local",
    "Valor",
    "Duração"
]

# Criando o cabeçalho da tabela
for indice, nome in enumerate(colunas):

    cabecalho = tk.Label(
        frame_tabela,
        text=nome,
        font=("Arial", 13, "bold"),
        fg=AZUL,
        bg=FUNDO,
        pady=15
    )

    cabecalho.grid(
        row=0,
        column=indice,
        sticky="nsew"
    )

# Dados de exemplo
dados = [
    ["Lorem", "Lorem", "Lorem", "Lorem", "Lorem"],
    ["Lorem", "Lorem", "Lorem", "Lorem", "Lorem"],
    ["Lorem", "Lorem", "Lorem", "Lorem", "Lorem"],
    ["Lorem", "Lorem", "Lorem", "Lorem", "Lorem"],
    ["Lorem", "Lorem", "Lorem", "Lorem", "Lorem"],
    ["Lorem", "Lorem", "Lorem", "Lorem", "Lorem"],
    ["Lorem", "Lorem", "Lorem", "Lorem", "Lorem"],
    ["Lorem", "Lorem", "Lorem", "Lorem", "Lorem"]
]

# Criando as linhas da tabela
for indice_linha, linha in enumerate(dados):

    # Alternando a cor de fundo
    if indice_linha % 2 == 0:
        cor_linha = FUNDO
    else:
        cor_linha = CINZA_CLARO

    # Criando cada célula
    for indice_coluna, valor in enumerate(linha):

        celula = tk.Label(
            frame_tabela,
            text=valor,
            font=("Arial", 13),
            fg=AZUL,
            bg=cor_linha,
            pady=11
        )

        celula.grid(
            row=indice_linha + 1,
            column=indice_coluna,
            sticky="nsew"
        )
