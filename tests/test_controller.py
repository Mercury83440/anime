import pytest


from sqlalchemy import create_engine
engine = create_engine("sqlite:///temp.db", echo=True, future=True)


@pytest.fixture
def controller():
    return Controller(engine)

from anime.controllers.controller import Controller



class TestControllerEpisodes:

    # def test_add_episode(self, controller):
    #     controller.add_anime(name="Naruto", author="Kishimoto", episodes_list=["Enter: Naruto Uzumaki!",
    #                                                                            "My Name is Konohamaru!"])

    # def test_fetch_all_animes(self, controller):
    #     animes = controller.fetch_all_animes()
    #     assert animes[0].name == "Naruto"

    def test_display_onepiece(self, controller):
        controller.display_anime("Bleach")

    def test_display_animes_list(self, controller):
        controller.display_animes_list()

    def test_add_anime(self, controller):
        controller.display_add_anime()
