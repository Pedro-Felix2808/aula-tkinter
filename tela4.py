import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path


FUNDO = "white"
AZUL = "#2D8FC7"
AZUL_CLARO = "#DFF1FB"
BORDA = "#B7DDF5"
TEXTO_CAMPO = "#4A7FA6"


janela = tk.Tk()
janela.title("Editar Consulta")
janela.geometry("1200x700")
janela.configure(bg=FUNDO)


pasta = Path(__file__).parent


imagem_perfil = Image.open(pasta / "perfil.png")
imagem_perfil.thumbnail((70, 70))
foto_perfil = ImageTk.PhotoImage(imagem_perfil)


imagem_sino = Image.open(pasta / "sino.png")
imagem_sino.thumbnail((35, 35))
foto_sino = ImageTk.PhotoImage(imagem_sino)


imagem_logo = Image.open(pasta / "logo.png")
imagem_logo.thumbnail((80, 80))
foto_logo = ImageTk.PhotoImage(imagem_logo)


frame_topo = tk.Frame(janela, bg=FUNDO)
frame_topo.pack(fill="x", padx=40, pady=(25, 10))

label_perfil = tk.Label(frame_topo, image=foto_perfil, bg=FUNDO)
label_perfil.pack(side="left")

boas_vindas = tk.Label(
    frame_topo,
    text="BEM VINDO JUAN",
    font=("Arial", 10, "bold"),
    bg=AZUL_CLARO,
    fg=AZUL,
    padx=20,
    pady=10
)
boas_vindas.pack(side="left", padx=15)

label_sino = tk.Label(frame_topo, image=foto_sino, bg=FUNDO)
label_sino.pack(side="left", padx=8)

label_logo = tk.Label(frame_topo, image=foto_logo, bg=FUNDO)
label_logo.pack(side="right")


frame_principal = tk.Frame(janela, bg=FUNDO)
frame_principal.pack(fill="both", expand=True)


label_voltar = tk.Label(
    frame_principal,
    text="←   Voltar",
    font=("Arial", 15),
    fg=AZUL,
    bg=FUNDO
)
label_voltar.place(x=85, y=25)


frame_form = tk.Frame(frame_principal, bg=FUNDO)
frame_form.place(relx=0.5, rely=0.42, anchor="center")

titulo = tk.Label(
    frame_form,
    text="EDITAR CONSULTA",
    font=("Arial", 22, "bold"),
    fg=AZUL,
    bg=FUNDO
)
titulo.pack(pady=(0, 20))

def criar_campo(pai, texto_inicial="", largura=38, cadeado=False):
    """
    Cria um campo visual com Entry.
    Se cadeado=True, mostra um pequeno cadeado na direita.
    """
    frame_campo = tk.Frame(
        pai,
        bg=FUNDO,
        highlightbackground=BORDA,
        highlightthickness=1,
        bd=0
    )

    entry = tk.Entry(
        frame_campo,
        font=("Arial", 11),
        fg=TEXTO_CAMPO,
        bg=FUNDO,
        relief="flat",
        bd=0,
        width=largura
    )
    entry.insert(0, texto_inicial)
    entry.pack(side="left", padx=(10, 5), pady=8)

    if cadeado:
        label_cadeado = tk.Label(
            frame_campo,
            text="🔒",
            font=("Arial", 10),
            fg=AZUL,
            bg=FUNDO
        )
        label_cadeado.pack(side="right", padx=(5, 10))

    return frame_campo, entry


def criar_botao_visual(pai, texto, largura=35):
    """
    Cria um botão apenas visual usando Label.
    """
    botao = tk.Label(
        pai,
        text=texto,
        font=("Arial", 13, "bold"),
        bg=AZUL_CLARO,
        fg=AZUL,
        width=largura,
        pady=10
    )
    return botao



frame_linha1 = tk.Frame(frame_form, bg=FUNDO)
frame_linha1.pack(pady=6)

campo_nome, entry_nome = criar_campo(
    frame_linha1,
    texto_inicial="João Silva",
    largura=28,
    cadeado=True
)
campo_nome.pack(side="left", padx=(0, 10))

campo_data, entry_data = criar_campo(
    frame_linha1,
    texto_inicial="12/09",
    largura=8,
    cadeado=False
)
campo_data.pack(side="left")


campo_endereco, entry_endereco = criar_campo(
    frame_form,
    texto_inicial="83145 Maggie Plaza Suite 204 - Lawton, IA / 71846",
    largura=45,
    cadeado=True
)
campo_endereco.pack(pady=6)


campo_obs, entry_obs = criar_campo(
    frame_form,
    texto_inicial="Jejum de 12 horas",
    largura=49,
    cadeado=False
)
campo_obs.pack(pady=6)


campo_medico, entry_medico = criar_campo(
    frame_form,
    texto_inicial="Dr. Carlos Santos",
    largura=45,
    cadeado=True
)
campo_medico.pack(pady=6)


frame_anexo = tk.Frame(
    frame_form,
    bg=FUNDO,
    highlightbackground=AZUL,
    highlightthickness=1,
    bd=0
)
frame_anexo.pack(pady=12)

label_anexo = tk.Label(
    frame_anexo,
    text="Anexo",
    font=("Arial", 11),
    fg=AZUL,
    bg=FUNDO,
    width=45,
    pady=8
)
label_anexo.pack(side="left", padx=(10, 5))

icone_upload = tk.Label(
    frame_anexo,
    text="☁",
    font=("Arial", 12),
    fg=AZUL,
    bg=FUNDO
)
icone_upload.pack(side="right", padx=(5, 10))


botao_editar = criar_botao_visual(frame_form, "EDITAR", largura=30)
botao_editar.pack(pady=(8, 0))


janela.mainloop()