from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Anime(Base):
    __tablename__ = "anime"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    author_id = Column(String(30))

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r})"


class Episode(Base):
    __tablename__ = "episode"
    id = Column(Integer, primary_key=True)
    number = Column(Integer(30))
    name = Column(String(30))
    duration = Column(Integer(30))
