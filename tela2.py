import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path

janela = tk.Tk()
janela.title("Doctor - Home")
janela.geometry("1200x700")
janela.configure(bg="white")


pasta = Path(__file__).parent

imagem1 = Image.open(pasta / "top.png")
imagem1.thumbnail((350, 120))
foto1 = ImageTk.PhotoImage(imagem1)

label1 = tk.Label(
    janela,
    image=foto1,
    bg="white"
)

label1.place(
    x=40,
    y=30
)

imagem2 = Image.open(pasta / "meio.png")
imagem2.thumbnail((650, 300))
foto2 = ImageTk.PhotoImage(imagem2)

label2 = tk.Label(
    janela,
    image=foto2,
    bg="white"
)

label2.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)

imagem3 = Image.open(pasta / "logo.png")
imagem3.thumbnail((100, 100))
foto3 = ImageTk.PhotoImage(imagem3)

label3 = tk.Label(
    janela,
    image=foto3,
    bg="white"
)

label3.place(
    relx=0.95,
    y=30,
    anchor="ne"
)


ajuda = tk.Label(
    janela,
    text="PRECISA DE AJUDA? 😟",
    font=("Arial", 20, "bold"),
    bg="white",
    fg="#298FC2"
)

ajuda.place(
    relx=0.5,
    rely=0.85,
    anchor="center"
)

janela.mainloop()
