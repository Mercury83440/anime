import tkinter as tk
from sqlalchemy.orm import Session
from sqlalchemy import select

from anime.models.anime import Anime, Episode, Base
from anime.views.anime_view import AnimeView, AnimesListView, AddAnimeView, AnimeEditView, EpisodeEditView, \
    AddEpisodeView


class Controller:
    # permet d'initialiser la base de donnée
    def __init__(self, engine):
        self.engine = engine
        Base.metadata.create_all(engine)
        self.root = tk.Tk()

    def reset(self):
        """
        Détruit la fenêtre pour s'assurer d'en avoir toujours une seule à la fois.
        """
        self.root.destroy()
        self.root = tk.Tk()

    def add_anime(self, name, author, episodes_list):
        """
        Ajoute un anime dans la base de données.
        """
        episodes = []
        for k, episode_name in enumerate(episodes_list):
            episodes.append(Episode(
                number=k + 1,  # pour commencer à 1, pas à 0
                name=episode_name
            ))

        anime = Anime(
            name=name,
            author=author,
            episodes=episodes
        )
        with Session(self.engine) as session:
            session.add(anime)
            session.commit()

    def add_episode(self, name, number, anime):
        episode = Episode(
            name=name,
            number=number,
            anime_id=anime.id
        )
        with Session(self.engine) as session:
            session.add(episode)
            session.commit()

    def edit_anime(self, anime):
        self.reset()
        _ = AnimeEditView(self.root, anime, controller=self)
        self.root.mainloop()

    def edit_episode(self, episode):
        self.reset()
        _ = EpisodeEditView(self.root, episode, controller=self)
        self.root.mainloop()

    def delete_anime(self, anime):
        anime_id = anime.id
        with Session(self.engine) as session:
            anime = session.scalar(select(Anime).where(Anime.id == anime_id))
            session.delete(anime)
            session.commit()
        self.display_animes_list()

    def delete_episode(self, episode):
        anime_name = episode.anime.name
        with Session(self.engine) as session:
            episode = session.scalar(select(Episode).where(Episode.id == episode.id))
            session.delete(episode)
            session.commit()
            self.display_anime(anime_name)

    def update_anime(self, anime, new_title, new_author):
        anime_id = anime.id
        with Session(self.engine) as session:
            anime = session.scalar(select(Anime).where(Anime.id == anime_id))
            anime.author = new_author
            anime.name = new_title
            session.add(anime)
            session.commit()
            self.display_anime(anime.name)

    def update_episode(self, episode_id, new_title):
        with Session(self.engine) as session:
            episode = session.scalar(select(Episode).where(Episode.id == episode_id))
            episode.name = new_title
            session.add(episode)
            session.commit()
            self.display_anime(episode.anime.name)

    def display_add_anime(self):
        self.reset()
        _ = AddAnimeView(self.root, self)
        self.root.mainloop()

    def display_add_episode(self, anime):
        self.reset()
        _ = AddEpisodeView(self.root, controller=self, anime=anime)
        self.root.mainloop()

    def display_animes_list(self):
        self.reset()
        with Session(self.engine) as session:
            animes = session.scalars(select(Anime))
            _ = AnimesListView(self.root, animes, controller=self)
            self.root.mainloop()

    def display_anime(self, anime_title):
        # root.geometry("500x500")
        self.reset()
        with Session(self.engine) as session:
            anime = session.scalar(select(Anime).where(Anime.name == anime_title))
            assert anime is not None
            view = AnimeView(self.root, anime, controller=self)
            self.root.mainloop()
