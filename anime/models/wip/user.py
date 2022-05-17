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
        if (User.droit == 0):
            print("vous n'avez pas les droits")
        else:
            print("tu as crée un compte")

    def edit_account():
        if (User.droit == 0):
            print("vous n'avez pas les droits")
        else:
            print("tu modifie un compte")

    def delete_account(self):
        print("tu as supprimé un compte")

    def new_anime():
        if (User.droit == 0):
            print("vous n'avez pas les droits")
        else:
            print("tu as crée un nouveaux anime")

    def edit_anime():
        if (User.droit == 0):
            print("vous n'avez pas les droits")
        else:
            print("tu modifie un anime")

    def delet_anime():
        if (User.droit == 0):
            print("vous n'avez pas les droits")
        else:
            print("tu as supprimée un anime")

    def add_episode():
        if (User.droit == 0):
            print("vous n'avez pas les droits")
        else:
            print("""ouvre le dossier "base de donnée" pour y insérer une vidéo et qui 
        va lui donner un nom équivalent au paramétre indiqué
        exemple : "001 : Je suis Luffy ! Celui qui deviendra Roi des pirates""")

