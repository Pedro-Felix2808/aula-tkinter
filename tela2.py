import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path


janela = tk.Tk()
janela.title("Minha Interface")
janela.geometry("900x550")
janela.configure(bg="white")

pasta = Path(__file__).parent


imagem1 = Image.open(pasta / "top.png")
imagem1.thumbnail((200, 150))
foto1 = ImageTk.PhotoImage(imagem1)

label1 = tk.Label(
    janela,
    image=foto1,
    bg="white"
)
label1.pack(pady=10)


imagem2 = Image.open(pasta / "meio.png")
imagem2.thumbnail((150, 150))
foto2 = ImageTk.PhotoImage(imagem2)

label2 = tk.Label(
    janela,
    image=foto2,
    bg="white"
)
label2.pack(pady=10)


imagem3 = Image.open(pasta / "logo.png")
imagem3.thumbnail((100, 100))
foto3 = ImageTk.PhotoImage(imagem3)

label3 = tk.Label(
    janela,
    image=foto3,
    bg="white"
)
label3.pack(pady=10)

janela.mainloop()
