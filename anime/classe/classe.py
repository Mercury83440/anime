# -*- coding: utf-8 -*-
"""
Created on Mon May  9 19:13:24 2022

@author: mathi
"""

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
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)
    
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r})"

"""class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    
    def __repr__(self):
        return self.name"""
    
class User(Base):    
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    pwd = Column(String(30))
    droit = NotImplemented
    def __init__(self, nom_utilisateur, mdp):
        self.nom_utilisateur = nom_utilisateur
        self.mdp = mdp
    
    def delete(self):
        print("plop")

    
    def edit():
        print("tu as supprimé un compte")

        
class User(Compte):
    droit = 0
    def sign_up():
        print("OOOOO")

    
class Admin(Compte):
    droit = 1    
    def new_anime():
        print("tu as crée un nouveaux anime") 
        
    def new_compte():
        print("tu as crée un nouveaux compte")

    