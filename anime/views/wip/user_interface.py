# -*- coding: utf-8 -*-
"""
Created on Mon May  9 18:00:19 2022

@author: mathi
"""

from tkinter import *
from tkinter import ttk

fenetre = Tk()
fenetre.geometry("500x200")
fenetre.title("Page user")

liste_anime = ttk.Combobox(values=["Choisissez votre anime","anime1", "anime2", "anime3"])
liste_anime.grid()
liste_anime.current(0)
Label(text="Nom de l'anime :").grid(row=0, column=1)
Entry().grid(row=0, column=2)
Label(text="Nombre d'épisode :").grid(row=1, column=1)
Entry().grid(row=1, column=2)
Label(text="listes des épisodes :").grid(row=2, column=1)
liste_anime = ttk.Combobox(values=["Choisissez votre épisode","001", "002", "003","..."])
liste_anime.grid(row=2, column=2)
liste_anime.current(0)
Button(text="visionner").grid(row=3, column=2)
Button(text="Se déconnecter").grid(row=4, column=2)

fenetre.mainloop()