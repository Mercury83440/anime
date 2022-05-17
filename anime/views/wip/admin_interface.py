# -*- coding: utf-8 -*-
"""
Created on Sat May  7 19:05:29 2022

@author: mathi
"""

from tkinter import *
from tkinter import ttk

fenetre = Tk()
fenetre.geometry("150x150")
fenetre.title("Page admin")

Button(text="Ajouter un compte").grid()
Button(text="consulter un compte").grid(row = 1)
Label(text=" ").grid(row = 2)
Button(text="ajouter un anime").grid(row = 3)
Button(text="consulter un anime").grid(row = 4)

fenetre.mainloop()