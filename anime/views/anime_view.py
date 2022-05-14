#
# from tkinter import *
# from tkinter import ttk
#
# fenetre = Tk()
# fenetre.geometry("500x200")
# fenetre.title("Page user")
#
# liste_anime = ttk.Combobox(values=["Choisissez votre anime","anime1", "anime2", "anime3"])
# liste_anime.grid()
# liste_anime.current(0)
# Label(text="Nom de l'anime :").grid(row=0, column=1)
# Entry().grid(row=0, column=2)
# Label(text="Nombre d'épisode :").grid(row=1, column=1)
# Entry().grid(row=1, column=2)
# Label(text="listes des épisodes :").grid(row=2, column=1)
# liste_anime = ttk.Combobox(values=["Choisissez votre épisode","001", "002", "003","..."])
# liste_anime.grid(row=2, column=2)
# liste_anime.current(0)
# Button(text="visionner").grid(row=3, column=2)
# Button(text="Se déconnecter").grid(row=4, column=2)
#
# fenetre.mainloop()
from functools import partial

import tkinter as tk


class AnimesListView(tk.Frame):
    """
    View to display all available animes
    """

    def __init__(self, root, animes, controller):
        self.controller = controller
        self.animes = animes
        super().__init__(root)
        index = 0
        for index, anime in enumerate(animes):
            tk.Label(text=str(anime)).grid(row=index, column=0)
            tk.Button(text="details", command=partial(controller.display_anime, anime_title=anime.name)).grid(row=index,
                                                                                                              column=1)
        tk.Button(text="Ajouter", command=self.controller.display_add_anime).grid(row=index + 1, column=0)


class AnimeView(tk.Frame):
    """
    The view to display Anime details
    """

    def __init__(self, root, anime, controller):
        self.anime = anime
        self.controller = controller
        super().__init__(root)
        tk.Label(text=f"{self.anime.name} by {self.anime.author}").grid()
        tk.Button(root, text="retour", command=self.controller.display_animes_list).grid(row=0, column=1)
        tk.Label(text=f"{self.anime.episodes_count} episodes:").grid(row=1, column=0)
        for index, episode in enumerate(self.anime.episodes):
            tk.Label(text=f"{episode.number}: {episode.name}").grid(row=2 + index, column=1)
            tk.Button(root, text="view").grid(row=2 + index, column=2)


class AddAnimeView(tk.Frame):
    """
    View to create a new anime
    """

    def __init__(self, root, controller):
        self.controller = controller
        super().__init__(root)
        tk.Label(text="Anime title: ").grid(row=0, column=0)
        title_entry = tk.Entry()
        title_entry.grid(row=0, column=1)

        tk.Label(text="Author: ").grid(row=1, column=0)
        author_entry = tk.Entry()
        author_entry.grid(row=1, column=1)

        def callback():
            self.controller.add_anime(name=title_entry.get(), author=author_entry.get(), episodes_list=[])
            self.controller.display_animes_list()

        tk.Button(text="Ajouter", command=callback).grid(row=2, column=0)
