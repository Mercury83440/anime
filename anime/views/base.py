import tkinter as tk
from typing import TYPE_CHECKING

from anime.controllers.controller import Controller


class View(tk.Frame):

    def __init__(self, root: tk.Tk, controller: Controller):
        self.controller = controller
        super().__init__(root)
