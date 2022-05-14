import tkinter as tk

from anime.models.anime import Anime, Episode, Base
from anime.views.anime_view import AnimeView, AnimesListView, AddAnimeView

from sqlalchemy.orm import Session
from sqlalchemy import select


class Controller:

    def __init__(self, engine):
        self.engine = engine
        Base.metadata.create_all(engine)
        self.root = tk.Tk()

    def reset(self):
        self.root.destroy()
        self.root = tk.Tk()

    def add_anime(self, name, author, episodes_list):
        anime = Anime(
            name=name,
            author=author,
            episodes=[
                Episode(
                    number=k+1,
                    name=episode_name
                ) for k, episode_name in enumerate(episodes_list)
            ]
        )
        with Session(self.engine) as session:
            session.add(anime)
            session.commit()

    def display_anime(self, anime_title):
        # root.geometry("500x500")
        self.reset()
        with Session(self.engine) as session:
            anime = session.scalar(select(Anime).where(Anime.name == anime_title))
            assert anime is not None
            view = AnimeView(self.root, anime, controller=self)
            self.root.mainloop()

    def display_animes_list(self):
        self.reset()
        with Session(self.engine) as session:
            animes = session.scalars(select(Anime))
            view = AnimesListView(self.root, animes, controller=self)
            self.root.mainloop()


    def print_all_animes(self):
        session = Session(self.engine)
        for anime in session.scalars(select(Anime)):
            print(anime)


    def display_add_anime(self):
        self.reset()
        view = AddAnimeView(self.root, self)
        self.root.mainloop()