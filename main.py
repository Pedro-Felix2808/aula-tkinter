
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

janela.mainloop()

