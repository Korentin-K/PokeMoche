import json
import datetime
import pathlib

from map import Map
from Player import Player
from sql import SQL

class Save:
    def __init__(self,path: str, map: Map):
        self.path = path
        self.map = map
        self.sql = SQL()

    def save(self):
        self.map.save_in_file(self.path)
        #position = self.map.player.
        player_info={
            "name": self.map.player.name,
            "type": self.map.player.type,
            "inventory": self.map.player.inventory,
            "coins": self.map.player.coins,
            "badges": self.map.player.badges,
            "nbPokemoche": self.map.player.nbPokemoches,
            "mocheDex": self.map.player.mocheDex,
        }