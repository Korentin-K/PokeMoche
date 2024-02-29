import random

import pygame

from button import Button
from attackButton import AttackButton
from runButton import RunButton
from screen import Screen
from lifeBar import lifeBar
from showPokemon import ShowPokemon
from showWildPokemon import ShowWildPokemon
from baseInterface import BaseInterface
from attackTypeButton import AttackTypeButton


class fightInterface:
    def __init__(self, player):
        self.player = player
        self.playerPokeMoche = self.player.playerPokeMoche
        self.randomPokeMoche = self.player.randomPokeMoche
        self.running = True
        self.screen = Screen()
        self.screenSize = pygame.display.get_surface().get_size()
        self.squareSize = 650
        self.squareX = (self.screenSize[0] - self.squareSize) // 2
        self.squareY = (self.screenSize[1] - self.squareSize) // 2
        self.firstButtonX = self.squareX * 3 - 300
        self.firstButtonY = self.squareY + 520
        self.attackButton = AttackButton(self.firstButtonX, self.firstButtonY)
        self.bag = Button(self.firstButtonX + 160, self.firstButtonY, "Sac")
        self.pokeMochesButton = Button(self.firstButtonX, self.firstButtonY + 60, "PokeMoches")
        self.runAwayButton = RunButton(self.firstButtonX + 160, self.firstButtonY + 60)
        self.firstButtonsUsed = False

    def launch_fight(self):
        randomPokeLife = lifeBar(self.randomPokeMoche)
        playerPokeLife = lifeBar(self.playerPokeMoche)
        showRandomPokemon = ShowWildPokemon()
        showPlayerPokemon = ShowPokemon()
        buttonAttack1, buttonAttack2, buttonAttack3, buttonAttack4 = None, None, None, None
        self.player.disable()
        while self.running and (self.playerPokeMoche.current_hp > 0 and self.randomPokeMoche.current_hp > 0):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not buttonAttack1 is None and buttonAttack1.rect.collidepoint(event.pos):
                        self.start_fight(0)
                        print("click1")
                        self.playerPokeMoche.print_hp()
                        self.randomPokeMoche.print_hp()

                    elif not buttonAttack2 is None and buttonAttack2.rect.collidepoint(event.pos):
                        self.start_fight(1)
                        print("click2")
                        self.playerPokeMoche.print_hp()
                        self.randomPokeMoche.print_hp()

                    elif not buttonAttack3 is None and buttonAttack3.rect.collidepoint(event.pos):
                        self.start_fight(2)
                        print("click3")
                        self.playerPokeMoche.print_hp()
                        self.randomPokeMoche.print_hp()

                    elif not buttonAttack4 is None and buttonAttack4.rect.collidepoint(event.pos):
                        self.start_fight(3)
                        print("click4")
                        self.playerPokeMoche.print_hp()
                        self.randomPokeMoche.print_hp()

                    elif not self.firstButtonsUsed and self.attackButton.rect.collidepoint(event.pos):
                        print("start")
                        self.firstButtonsUsed = True
                        # si le bouton d'attaque est appuyé remplace tout les bouton par les attaques
                        buttonAttack1 = AttackTypeButton(self.firstButtonX, self.firstButtonY,
                                                         self.playerPokeMoche.attacks[0])
                        buttonAttack2 = AttackTypeButton(self.firstButtonX + 160, self.firstButtonY,
                                                         self.playerPokeMoche.attacks[1])
                        buttonAttack3 = AttackTypeButton(self.firstButtonX, self.firstButtonY + 60,
                                                         self.playerPokeMoche.attacks[2])
                        buttonAttack4 = AttackTypeButton(self.firstButtonX + 160, self.firstButtonY + 60,
                                                         self.playerPokeMoche.attacks[3])
                        buttonAttack1.draw(self.screen.get_display())
                        buttonAttack2.draw(self.screen.get_display())
                        buttonAttack3.draw(self.screen.get_display())
                        buttonAttack4.draw(self.screen.get_display())
                        self.screen.update()

                    elif not self.firstButtonsUsed and self.runAwayButton.rect.collidepoint(event.pos):
                        print("fuite")
                        self.player.enable()
                        self.firstButtonsUsed = False
                        self.running = False
                        self.randomPokeMoche.heal()

            # Interface de base
            baseInterface = BaseInterface()
            baseInterface.drawAll(self.screen.get_display(), self.squareX, self.squareY, self.playerPokeMoche.name)
            showPlayerPokemon.draw(self.screen.get_display(), self.playerPokeMoche.name, self.squareX, self.squareY)
            showRandomPokemon.draw(self.screen.get_display(), self.randomPokeMoche.name, self.squareX, self.squareY)

            # Sert à l'agencement des boutons
            self.attackButton.draw(self.screen.get_display())
            self.bag.draw(self.screen.get_display())
            self.pokeMochesButton.draw(self.screen.get_display())
            self.runAwayButton.draw(self.screen.get_display())
            randomPokeLife.drawRandomPokeMoche(self.screen.get_display(), self.squareX, self.squareY)
            playerPokeLife.drawPlayerPokeMoche(self.screen.get_display(), self.squareX, self.squareY)

            if self.firstButtonsUsed:
                buttonAttack1.draw(self.screen.get_display())
                buttonAttack2.draw(self.screen.get_display())
                buttonAttack3.draw(self.screen.get_display())
                buttonAttack4.draw(self.screen.get_display())

            self.screen.update()
        print("end battle")
        self.player.enable()
        self.running = False
        self.randomPokeMoche.heal()
        self.firstButtonsUsed = False

    # si le bouton d'attaque est appuyé remplace tout les bouton par les attaques
    def start_fight(self, button_number):
        self.handle_damage(button_number)
        print("damages done")

    import random

    def handle_damage(self, button_number):
        print("handle damage")

        def calculate_damage(attacker, defender, attack_number):
            damage = attacker.attacks[attack_number].damage - defender.defence
            return 0 if damage < 0 else damage

        def apply_damage(attacker, defender, attack_number):
            damage = calculate_damage(attacker, defender, attack_number)
            defender.decrease_hp(damage)
            print(f"Defender's Defence: {defender.defence}")
            print(f"Attacker's Attack Damage: {attacker.attacks[attack_number].damage}")
            print(f"Calculated Damage: {damage}")

            return self.check_lost()

        player_speed = self.playerPokeMoche.speed
        random_speed = self.randomPokeMoche.speed

        if player_speed > random_speed:
            apply_damage(self.randomPokeMoche, self.playerPokeMoche, button_number)
            if not self.check_lost():
                rand = random.randint(0, 3)
                apply_damage(self.playerPokeMoche, self.randomPokeMoche, rand)

        elif player_speed == random_speed:
            rand = random.randint(0, 3)
            apply_damage(self.playerPokeMoche, self.randomPokeMoche, rand)
            if not self.check_lost():
                apply_damage(self.randomPokeMoche, self.playerPokeMoche, button_number)

        else:
            rand = random.randint(0, 1)
            if rand == 1:
                apply_damage(self.playerPokeMoche, self.randomPokeMoche, button_number)
                if not self.check_lost():
                    rand = random.randint(0, 3)
                    apply_damage(self.randomPokeMoche, self.playerPokeMoche, rand)
            else:
                rand = random.randint(0, 3)
                apply_damage(self.randomPokeMoche, self.playerPokeMoche, rand)
                if not self.check_lost():
                    apply_damage(self.playerPokeMoche, self.randomPokeMoche, button_number)

    def endFight(self):
        self.running = True

    def check_lost(self):
        pass
