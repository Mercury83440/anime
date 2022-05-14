# -*- coding: utf-8 -*-
"""
Created on Tue May 10 16:47:34 2022

@author: mathi
"""

class Anime:
    def __init__(self, name, episodes_count, autor, genre):
        self.name = name 
        self.episodes_count = episodes_count
        self.autor = autor
        self.genre = genre
        
    def __repr__(self):
        return f"{self.name} by {self.autor}"
    
    def delete(self):
        print("tu as supprimé un anime")
        
    def edit(self):
        print("l'anime est modifié")
        
    def watch(self):
        print("l'anime est lu")
