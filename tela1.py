import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path


janela = tk.Tk()
janela.title("Sistema Médico - Login")
janela.geometry("900x550")
janela.configure(bg="white")

janela.lift()
janela.attributes("-topmost", True)


frame_login = tk.Frame(
    janela,
    bg="white"
)


frame_login.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)


caminho = Path(__file__).parent / "logo.png"

imagem = Image.open(caminho)
imagem.thumbnail((250, 150))

logo = ImageTk.PhotoImage(imagem)

label_logo = tk.Label(
    frame_login,
    image=logo,
    bg="white"
)
label_logo.pack(pady=(0, 30))


campo_email = tk.Entry(
    frame_login,
    font=("Arial", 14),
    width=35,
    bg="#F0ECEC",
    fg="gray"
)

campo_email.insert(0, "Email")
campo_email.pack(pady=10)

def entrar_email(event):
    if campo_email.get() == "Email":
        campo_email.delete(0, tk.END)
        campo_email.config(fg="black")

def sair_email(event):
    if campo_email.get() == "":
        campo_email.insert(0, "Email")
        campo_email.config(fg="gray")

campo_email.bind("<FocusIn>", entrar_email)
campo_email.bind("<FocusOut>", sair_email)


campo_senha = tk.Entry(
    frame_login,
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


botao_acessar = tk.Label(
    frame_login,
    text="ACESSAR",
    font=("Arial", 12, "bold"),
    bg="#298FC2",
    fg="white",
    width=35,
    pady=10
)

botao_acessar.pack(pady=(15, 25))

primeiro_acesso = tk.Label(
    frame_login,
    text="PRIMEIRO ACESSO",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#298FC2"
)

primeiro_acesso.pack(pady=10)


janela.mainloop()

