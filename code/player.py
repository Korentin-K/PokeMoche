import random

import pygame

from entity import Entity
from keylistener import KeyListener
from screen import Screen
from switch import Switch
from fightInterface import fightInterface
from pokeMoches import pokeMoches
from attacks import Attack


class Player(Entity):
    def __init__(self, keyListener: KeyListener, screen: Screen, x: int, y: int):
        super().__init__(keyListener, screen, x, y)
        self.in_combat = False
        self.enabled = True
        self.pokeDollars: int = 0
        self.nbMoves = 0
        self.attacks1 = [Attack("Charge", 10), Attack("Ecrasement", 20), Attack("Ecras'Face", 10), Attack("Tranche", 15)]
        self.attacks2 = [Attack("Charge", 10), Attack("Morsure", 15), Attack("Mâchouille", 20), Attack("Coup Bas", 10)]

        self.playerPokeMoche = pokeMoches("Poussifeu", 30, 6, 10, self.attacks1)
        self.randomPokeMoche = pokeMoches("Medhyena", 25, 5, 10, self.attacks2)
        self.spriteSheet_bike: pygame.image = pygame.image.load("../assets/sprite/hero_01_red_m_cycle_roll.png")
        self.fightInterface = fightInterface(self)
        self.switchs: list[Switch] | None = None
        self.collisions: list[pygame.Rect] | None = None
        self.change_map: Switch | None = None
        self.grass: list[pygame.Rect] | None = None
        self.previous_map: Switch | None = None
        self.MAX_MOVES = 25

    def update(self) -> None:
        self.check_input()
        self.check_move()
        super().update()

    def check_move(self) -> None:
        if not self.enabled or self.in_combat:
            return
        if self.playerPokeMoche.current_hp > 0:
            max_rand = int(self.MAX_MOVES - self.nbMoves / 2) if int(self.MAX_MOVES - self.nbMoves / 2) > 1 else 2
            rand = random.randint(1, max_rand)
        else:
            rand = 10000000
        if not self.animation_walk:
            temp_hitbox = self.hitbox.copy()

            key_actions = {
                pygame.K_q: ("left", -16, 0),
                pygame.K_d: ("right", 16, 0),
                pygame.K_z: ("up", 0, -16),
                pygame.K_s: ("down", 0, 16),
            }

            for key, (direction, dx, dy) in key_actions.items():
                if self.keylistener.key_pressed(key):
                    temp_hitbox.x += dx
                    temp_hitbox.y += dy

                    if not self.check_collisions(temp_hitbox):
                        if self.check_grass(temp_hitbox) and (
                                rand == 1 or self.nbMoves == self.MAX_MOVES) and self.playerPokeMoche.current_hp > 0:
                            self.fightInterface.launch_fight()
                            self.fightInterface.endFight()
                            self.nbMoves = 0
                            break
                        else:
                            if self.playerPokeMoche.current_hp <= 0:
                                print("go to a pokeMoche Center to heal your pokeMoche")
                            else:
                                self.nbMoves += 1
                            self.check_collisions_switchs(temp_hitbox)
                            self.move_direction(direction)
                    else:
                        self.direction = direction
                    break

    def move_direction(self, direction: str) -> None:
        if direction == "left":
            self.move_left()
        elif direction == "right":
            self.move_right()
        elif direction == "up":
            self.move_up()
        elif direction == "down":
            self.move_down()

    def add_switchs(self, switchs: list[Switch]):
        self.switchs = switchs

    def check_collisions_switchs(self, temp_hitbox):
        if self.switchs:
            for switch in self.switchs:
                if switch.check_collision(temp_hitbox):
                    self.change_map = switch
                    if self.change_map.name.startswith("centrePokemon"):
                        self.playerPokeMoche.heal()
        return None

    def check_input(self):
        if self.keylistener.key_pressed(pygame.K_b):
            self.switch_bike()

    def switch_bike(self, deactive=False):
        if self.speed == 1 and not deactive:
            self.speed = 2
            self.all_images = self.get_all_images(self.spriteSheet_bike)
        else:
            self.speed = 1
            self.all_images = self.get_all_images(self.spritesheet)
        self.keylistener.remove_key(pygame.K_b)

    def add_collisions(self, collisions):
        self.collisions = collisions

    def add_grass(self, grass):
        self.grass = grass

    def check_grass(self, temp_hitbox: pygame.Rect):
        for grass in self.grass:
            if temp_hitbox.colliderect(grass):
                self.nbMoves += 1
                return True
        return False

    def check_collisions(self, temp_hitbox: pygame.Rect):
        for collision in self.collisions:
            if temp_hitbox.colliderect(collision):
                return True
        return False

    def check_jump_down(self, temp_hitbox: pygame.Rect):
        for jump_rect in self.jump:
            if temp_hitbox.colliderect(jump_rect)and self.player.move_down():
                return True
            return False
    def enable(self):
        self.enabled = True
        self.in_combat = False
        self.keylistener.clear()

    def disable(self):
        self.enabled = False
        self.in_combat = False





