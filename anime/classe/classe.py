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
    
    
class Episode(Base):
    __tablename__ = "episode"
    id = Column(Integer, primary_key=True)
    episode_number = Column(Integer(30))
    name = Column(String(30))
    duration = Column(Integer(30))
    
    

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
    
    def new_account():
        if (User.droit == 0) :
            print("vous n'avez pas les droits")
        else :
            print("tu as crée un compte")
    
    def edit_account():
        if (User.droit == 0) :
            print("vous n'avez pas les droits")
        else :
            print("tu modifie un compte")
    
    def delete_account(self):
        print("tu as supprimé un compte")
        
    def new_anime():
        if (User.droit == 0) :
            print("vous n'avez pas les droits")
        else :
            print("tu as crée un nouveaux anime") 
        
    def edit_anime():
        if (User.droit == 0) :
            print("vous n'avez pas les droits")
        else :
            print("tu modifie un anime")
    
    def delet_anime():
        if (User.droit == 0) :
            print("vous n'avez pas les droits")
        else :
            print("tu as supprimée un anime")  
            
    def add_episode():
        if (User.droit == 0) :
            print("vous n'avez pas les droits")
        else :
            print("""ouvre le dossier "base de donnée" pour y insérer une vidéo et qui 
        va lui donner un nom équivalent au paramétre indiqué
        exemple : "001 : Je suis Luffy ! Celui qui deviendra Roi des pirates""")

    