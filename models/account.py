# -*- coding: utf-8 -*-
"""
Created on Tue May 10 19:59:50 2022

@author: mathi
"""

class Compte:    
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