import json
import datetime
import pathlib
from tkinter import *

class fightInterface:
    def __init__(self):
        self.running = True
    def test(self):
        while self.running:
            fenetre = Tk()

            label = Label(fenetre, text="Hello World")
            label.pack()

            fenetre.mainloop()

