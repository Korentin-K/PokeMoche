import json
import pygame
import datetime

from screen import Screen
from map import Map
from sql import SQL
from controller import Controller
from save import Save
class Option:
    def __init__(self,screen : Screen,controller : Controller,map : Map,langage : str,save : Save):
        self.screen = screen
        self.controller = controller
        self.map = map
        self.langage = langage
        self.save = save