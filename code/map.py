import pygame
import pytmx
import pyscroll

from screen import Screen


class Map:
    def __init__(self, screen: Screen):
        self.screen = screen
        self.tmx_data = None
        self.map_layer = None
        self.group = None

        self.switch_map()
        self.player=None

    def switch_map(self):
        self.tmx_data = pytmx.load_pygame(f"../assets/map/map0.tmx")
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 2
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=7)


    def add_player(self, player):
        self.group.add(player)
        self.player = player

    def update(self):
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen.display)
