import tkinter as tk



class View(tk.Frame):

    def __init__(self, root: tk.Tk, controller):
        self.controller = controller
        super().__init__(root)
