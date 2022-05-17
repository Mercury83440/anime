from functools import partial
from typing import List

import tkinter as tk
from tkinter import ttk

from anime.models.anime import Anime, Episode
from anime.views.base import View


class AnimesListView(View):
    """
    View to display all available animes
    """

    def __init__(self, root: tk.Tk, animes: List[Anime], controller):
        self.animes = animes
        super().__init__(root, controller)
        index = 0
        for index, anime in enumerate(animes):
            tk.Label(text=str(anime)).grid(row=index, column=0)
            tk.Button(text="details", command=partial(controller.display_anime, anime_title=anime.name)).grid(row=index,
                                                                                                              column=1)
            tk.Button(text="supprimer", command=partial(controller.delete_anime, anime=anime)).grid(row=index,
                                                                                                    column=2)
        tk.Button(text="Ajouter", command=self.controller.display_add_anime).grid(row=index + 1, column=0)


class AnimeView(View):
    """
    The view to display Anime details
    """

    def __init__(self, root: tk.Tk, anime: Anime, controller):
        self.anime = anime

        super().__init__(root, controller)
        tk.Label(text=f"{self.anime.name} by {self.anime.author}").grid()
        tk.Button(root, text="retour", command=self.controller.display_animes_list).grid(row=0, column=1)
        tk.Button(root, text="edit", command=partial(self.controller.edit_anime, anime=anime)).grid(row=0, column=2)

        tk.Label(text=f"{self.anime.episodes_count} episodes:").grid(row=1, column=0)

        index = 0
        for index, episode in enumerate(self.anime.episodes):
            tk.Label(root, text=f"{episode.number}: {episode.name}").grid(row=2 + index, column=1)
            tk.Button(root, text="view").grid(row=2 + index, column=2)
            tk.Button(root, text="edit",
                      command=partial(self.controller.edit_episode, episode=episode)).grid(
                row=2 + index, column=3)
            tk.Button(root, text="delete",
                      command=partial(self.controller.delete_episode, episode=episode)).grid(
                row=2 + index, column=4)

        tk.Button(root, text="Ajouter épisode", command=partial(self.controller.display_add_episode, anime=anime)).grid(
            row=3 + index, column=0)


        # vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        #
        # canvas = tk.Canvas(root, yscrollcommand=vscrollbar.set)
        #
        # vscrollbar.config(command=canvas.yview)
        #
        # scrollable_frame = tk.Frame(canvas, )
        #
        # scrollable_frame.bind(
        #     "<Configure>",
        #     lambda e: canvas.configure(
        #         scrollregion=canvas.bbox("all")
        #     )
        # )
        #
        # canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        #
        # # canvas.configure(yscrollcommand=scrollbar.set)
        #
        # index = 0
        # for index, episode in enumerate(self.anime.episodes):
        #     tk.Label(scrollable_frame, text=f"{episode.number}: {episode.name}").grid(row=2 + index, column=1)
        #     tk.Button(scrollable_frame, text="view").grid(row=2 + index, column=2)
        #     tk.Button(scrollable_frame, text="edit",
        #               command=partial(self.controller.edit_episode, episode=episode)).grid(
        #         row=2 + index, column=3)
        #     tk.Button(scrollable_frame, text="delete",
        #               command=partial(self.controller.delete_episode, episode=episode)).grid(
        #         row=2 + index, column=4)
        #
        # canvas.grid(row=2, column=0)
        #
        # ttk.Scrollbar(root, orient='vertical', command=canvas.yview).grid(row=2, column=1)

        tk.Button(root, text="Ajouter épisode", command=partial(self.controller.display_add_episode, anime=anime)).grid(
            row=3 + index, column=0)


class EpisodeEditView(View):

    def __init__(self, root: tk.Tk, episode: Episode, controller):
        self.episode = episode

        super().__init__(root, controller)

        tk.Label(root, text="Title: ").grid(row=0, column=0)
        title_entry = tk.Entry(root)
        title_entry.insert(0, episode.name)
        title_entry.grid(row=0, column=1)

        def callback():
            self.controller.update_episode(episode_id=episode.id, new_title=title_entry.get())

        tk.Button(text="retour", command=partial(self.controller.display_anime, anime_title=episode.anime.name)).grid(
            row=2, column=0)
        tk.Button(text="sauvegarder", command=callback).grid(row=2, column=1)


class AnimeEditView(View):

    def __init__(self, root: tk.Tk, anime: Anime, controller):
        self.anime = anime

        super().__init__(root, controller)

        tk.Label(root, text="Title: ").grid(row=0, column=0)
        title_entry = tk.Entry(root)
        title_entry.insert(0, anime.name)
        title_entry.grid(row=0, column=1)

        tk.Label(root, text="Author: ").grid(row=1, column=0)
        author_entry = tk.Entry(root)
        author_entry.insert(0, anime.author)
        author_entry.grid(row=1, column=1)

        def callback():
            self.controller.update_anime(anime=anime, new_title=title_entry.get(), new_author=author_entry.get())

        tk.Button(text="retour", command=partial(self.controller.display_anime, anime_title=anime.name)).grid(row=2,
                                                                                                              column=0)
        tk.Button(text="sauvegarder", command=callback).grid(row=2, column=1)


class AddAnimeView(View):
    """
    View to create a new anime
    """

    def __init__(self, root: tk.Tk, controller):
        super().__init__(root, controller)
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


class AddEpisodeView(View):
    """
    View to create a new anime
    """

    def __init__(self, root: tk.Tk, controller, anime: Anime):
        self.anime = anime
        super().__init__(root, controller)
        tk.Label(text="Episode title: ").grid(row=0, column=0)
        title_entry = tk.Entry()
        title_entry.grid(row=0, column=1)

        tk.Label(text="Number: ").grid(row=1, column=0)
        number_entry = tk.Entry()
        number_entry.grid(row=1, column=1)

        def callback():
            self.controller.add_episode(name=title_entry.get(), number=int(number_entry.get()), anime=anime)
            self.controller.display_anime(anime.name)

        tk.Button(text="Ajouter", command=callback).grid(row=2, column=0)
