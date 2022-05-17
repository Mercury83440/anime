from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

"""déclaration de la classe animé et de ses méthodes"""
class Anime(Base):
    __tablename__ = "anime"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    author = Column(String(30))

    episodes = relationship("Episode", cascade="all, delete-orphan", back_populates="anime")
"""c'est quoi 
relationship ? intéraction entre 2 bases de données ? 
cascade ?   conséquense si le parent est supprimer ?
back_populates ?
property ?
"""

    @property
    """compte le nombre d'épisode lié à cette anime"""
    def episodes_count(self):
        return len(self.episodes)

    def __repr__(self):
        """teste unitaire"""
        title = f"{self.name}, by {self.author}"
        episodes_info = f"{self.episodes_count} episode(s)"
        episodes_list = "\n".join([f"\t{ep}" for ep in self.episodes])

        return "\n".join([title, episodes_info])

"""déclaration de la Episode et de ses méthodes"""
class Episode(Base):
    __tablename__ = "episode"
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    name = Column(String(30))

"""à quoi sert ces 2 lignes"""
    anime_id = Column(Integer, ForeignKey("anime.id"), nullable=False)

    anime = relationship("Anime", back_populates="episodes")

"""renvoie le numéro de lépisode ainsi que son nom"""
    def __repr__(self):
        return f"{self.number}: {self.name}"
