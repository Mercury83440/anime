# -*- coding: utf-8 -*-
"""
Created on Sat May  7 18:18:21 2022

@author: mathi
"""

from tkinter import *
from tkinter import ttk

# Création de la fenêtre
fenetre = Tk()
fenetre.geometry("250x100")
fenetre.title("Page d'accueil")

Label(text="Nom d'utilisateur :").grid()
Entry().grid(row=0, column=1)

Label(text="mots de passe :").grid(row=1)
Entry().grid(row=1, column=1)

radioValue = IntVar()
Radiobutton(text="User",  variable=radioValue, value=0).grid(row=2)
Radiobutton(text="Admin", variable=radioValue, value=1).grid(row=2, column=1)

Button(text="Valider").grid(row=3, column=0)
Button(text="s'inscrire").grid(row=3, column=1)

fenetre.mainloop()