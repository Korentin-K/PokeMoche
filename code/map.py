import pygame
import pytmx
import pyscroll

from screen import Screen
from player import Player
from switch import Switch


class Map:
    def __init__(self, screen: Screen):
        self.screen = screen
        self.tmx_data = None
        self.map_layer = None
        self.group = None

        self.player: Player | None = None
        self.switchs: list[Switch]  # type, nom carte, coords zone, port d'entrée/sortie
        self.current_map: Switch = Switch("switch", "zone1", pygame.Rect(0, 0, 0, 0), 0)

        self.switch_map(self.current_map)

    def switch_map(self, switch: Switch):
        self.tmx_data = pytmx.load_pygame(f"../assets/map/{switch.name}.tmx")
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 2
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=7)

        self.switchs = []

        for obj in self.tmx_data.objects:
            type = obj.name.split(" ")[0]

            if type == "switch":
                self.switchs.append(Switch(
                    type, obj.name.split(" ")[1], pygame.Rect(obj.x, obj.y, obj.width, obj.height),
                    int(obj.name.split(" ")[-1])
                ))  # recup infos de zone declenchement changement de carte
                

        if self.player:
            self.pose_player(switch)
            self.player.align_hitbox()
            self.player.step = 16
            self.player.add_switchs(self.switchs)
            self.group.add(self.player)
            if switch.name.split(" ")[0] != "zone1" and switch.name.split(" ")[0]!="zone2" and switch.name.split(" ")[0]!="zone3" and switch.name.split(" ")[0]!="zone4" and switch.name.split(" ")[0]!="zone5":
                self.player.switch_bike(True)

        self.current_map = switch


    def add_player(self, player):
        self.group.add(player)
        self.player = player
        self.player.align_hitbox()
        self.player.step = 16
        self.player.add_switchs(self.switchs)

    def update(self):
        if self.player:
            if self.player.change_map and self.player.step>=8:
                self.switch_map(self.player.change_map)
                self.player.change_map = None
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen.display)

    def pose_player(self, switch: Switch):
        position = self.tmx_data.get_object_by_name("spawn "+self.current_map.name+" "+str(switch.port))
        self.player.position = pygame.math.Vector2(position.x, position.y)
