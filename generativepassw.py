import string
import random
from tkinter import Tk, Label, Button, Entry, StringVar
import pyperclip

def copy_to_clipboard(text):
    pyperclip.copy(text)

def generate_password(length):
    charset = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(charset) for _ in range(length))
    return password

def update_password():
    password_length = int(entry.get())
    new_password = generate_password(password_length)
    password.set('*' * len(new_password))  # Remplace le mot de passe par des astérisques
    copy_to_clipboard(new_password)

root = Tk()
root.geometry("380x100")
root.title("Générateur de mots de passe")

password = StringVar(root)
password.set('*' * 20)  # Initialise avec des astérisques

Label(root, text="Longueur du mot de passe :").pack()
entry = Entry(root, show='')
entry.pack()
entry.insert(0, "15")

Button(root, text="Générer un nouveau mot de passe", command=update_password).pack()

Label(root, textvariable=password).pack()

root.mainloop()
