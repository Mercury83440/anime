from sqlalchemy import create_engine

from anime.controllers.controller import Controller

if __name__ == '__main__':
    engine = create_engine("sqlite:///anime.db", future=True)
    controller = Controller(engine)
    controller.display_animes_list()
