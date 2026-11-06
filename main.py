
import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path

janela = tk.Tk()

janela.title("Sistema Médico - Login")
janela.geometry("900x550")
janela.configure(bg="white")

janela.lift()
janela.attributes("-topmost", True)

caminho = Path(__file__).parent / "logo.png"

imagem = Image.open(caminho)

imagem.thumbnail((250, 150))

logo = ImageTk.PhotoImage(imagem)

label_logo = tk.Label(
    janela,
    image=logo,
    bg="white"
)

label_logo.pack(pady=30)


campo_email = tk.Entry(
    janela,
    font=("Arial", 14),
    width=35,
    bg="#F0ECEC",
    fg="gray"
)

campo_email.insert(0, "Email")

campo_email.pack(pady=10)

def ao_clicar(event):
    if campo_email.get() == "Email":
        campo_email.delete(0, tk.END)
        campo_email.config(fg="black")


def ao_sair(event):
    if campo_email.get() == "":
        campo_email.insert(0, "Email")
        campo_email.config(fg="gray")



campo_email.bind("<FocusIn>", ao_clicar)
campo_email.bind("<FocusOut>", ao_sair)

campo_senha = tk.Entry(
    janela,
    font=("Arial", 14),
    width=35,
    bg="#F0ECEC",
    fg="gray"
)
campo_senha.insert(0, "Senha")
campo_senha.pack(pady=10)

def entrar_senha(event):
    if campo_senha.get() == "Senha":
        campo_senha.delete(0, tk.END)
        campo_senha.config(fg="black", show="*")

def sair_senha(event):
    if campo_senha.get() == "":
        campo_senha.config(show="")
        campo_senha.insert(0, "Senha")
        campo_senha.config(fg="gray")

campo_senha.bind("<FocusIn>", entrar_senha)
campo_senha.bind("<FocusOut>", sair_senha)


janela.mainloop()

