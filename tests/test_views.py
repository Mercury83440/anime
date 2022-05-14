import pytest
import tkinter as tk

from anime.models.anime import Anime, Episode
from anime.views.anime_view import AnimeView, AddAnimeView
from anime.controllers.controller import Controller


from sqlalchemy import create_engine
engine = create_engine("sqlite:///temp.db", echo=True, future=True)


@pytest.fixture
def controller():
    return Controller(engine)

@pytest.fixture
def deathnote():
    return Anime(name="Deathnote", author="Tsugumi Ohba", episodes=[Episode(name="Rebirth" , number=1)])


class TestAnimeView:

    def test_view_deathnote(self, deathnote):
        root = tk.Tk()
        root.geometry("500x500")
        view = AnimeView(root, deathnote)
        root.mainloop()

    def test_add_anime(self, controller):
        root = tk.Tk()
        view = AddAnimeView(root, controller=controller)
        root.mainloop()

    # def test_view_from_database(self, engine):
