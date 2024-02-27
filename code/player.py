import pygame

from entity import Entity
from keylistener import KeyListener
from screen import Screen
from switch import Switch
from fightInterface import fightInterface

class Player(Entity):
    def __init__(self, keylistener: KeyListener, screen: Screen, x: int, y: int):
        super().__init__(keylistener, screen, x, y)
        self.pokedollars: int = 0

        self.spritesheet_bike: pygame.image = pygame.image.load("../assets/sprite/hero_01_red_m_cycle_roll.png")
        self.fightInterface=fightInterface()
        self.switchs: list[Switch] | None = None
        self.collisions: list[pygame.Rect] | None = None
        self.change_map: Switch | None = None
        self.grass:list[pygame.Rect] | None = None

    def update(self) -> None:
        self.check_input()
        self.check_move()
        super().update()

    def check_move(self) -> None:
        if self.animation_walk is False:
            temp_hitbox = self.hitbox.copy()
            if self.keylistener.key_pressed(pygame.K_q):
                temp_hitbox.x -= 16
                if not self.check_collisions(temp_hitbox):
                    if self.check_grass(temp_hitbox):
                        self.fightInterface.startFight()
                    else:
                        self.check_collisions_switchs(temp_hitbox)
                        self.move_left()
            elif self.keylistener.key_pressed(pygame.K_d):
                temp_hitbox.x += 16
                if not self.check_collisions(temp_hitbox):
                    if self.check_grass(temp_hitbox):
                        self.fightInterface.startFight()
                    else:
                        self.check_collisions_switchs(temp_hitbox)
                        self.move_right()
            elif self.keylistener.key_pressed(pygame.K_z):
                temp_hitbox.y -= 16
                if not self.check_collisions(temp_hitbox):
                    if self.check_grass(temp_hitbox):
                        self.fightInterface.startFight()
                    else:
                        self.check_collisions_switchs(temp_hitbox)
                        self.move_up()
            elif self.keylistener.key_pressed(pygame.K_s):
                temp_hitbox.y += 16
                if not self.check_collisions(temp_hitbox):
                    if self.check_grass(temp_hitbox):
                        self.fightInterface.startFight()
                    else:
                        self.check_collisions_switchs(temp_hitbox)
                        self.move_down()

    def add_switchs(self, switchs: list[Switch]):
        self.switchs = switchs

    def check_collisions_switchs(self, temp_hitbox):
        if self.switchs:
            for switch in self.switchs:
                if switch.check_collision(temp_hitbox):

                    self.change_map = switch
        return None

    def check_input(self):
        if self.keylistener.key_pressed(pygame.K_b):
            self.switch_bike()

    def switch_bike(self, deactive=False):
        if self.speed == 1 and not deactive:
            self.speed = 2
            self.all_images = self.get_all_images(self.spritesheet_bike)
        else:
            self.speed = 1
            self.all_images = self.get_all_images(self.spritesheet)
        self.keylistener.remove_key(pygame.K_b)

    def add_collisions(self, collisions):
        self.collisions = collisions

    def add_grass(self,grass):
        self.grass = grass

    def check_grass(self, temp_hitbox: pygame.Rect):
        for grass in self.grass:
            if temp_hitbox.colliderect(grass):
                return True
        return False


    def check_collisions(self, temp_hitbox: pygame.Rect):
        for collision in self.collisions:
            if temp_hitbox.colliderect(collision):
                return True
        return False
