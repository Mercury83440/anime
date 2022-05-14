from anime.models.anime import Anime, Episode, Base
from sqlalchemy.orm import Session
from sqlalchemy import select


class Controller:

    def __init__(self, engine):
        self.engine = engine
        Base.metadata.create_all(engine)

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

    def print_all_animes(self):
        session = Session(self.engine)
        for anime in session.scalars(select(Anime)):
            print(anime)
