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
    def __init__(self, ourPokeName, wildPokeName, player):
        self.player = player
        self.ourPokeName = ourPokeName
        self.wildPokeName = wildPokeName
        self.running = True
        self.screen = Screen()
        self.screenSize = pygame.display.get_surface().get_size()
        self.squareSize = 650
        self.squareX = (self.screenSize[0] - self.squareSize) // 2
        self.squareY = (self.screenSize[1] - self.squareSize) // 2
        self.firstButtonX = self.squareX * 3 - 300
        self.firstButtonY = self.squareY + 520
        self.button1 = AttackButton(self.firstButtonX, self.firstButtonY)
        self.button2 = Button(self.firstButtonX + 160, self.firstButtonY, "Sac")
        self.button3 = Button(self.firstButtonX, self.firstButtonY + 60, "PokeMoches")
        self.button4 = RunButton(self.firstButtonX + 160, self.firstButtonY + 60)

    def startFight(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button1.rect.collidepoint(event.pos):
                        # si le bouton d'attaque est appuyé remplace tout les bouton par les attaques
                        self.button1 = AttackTypeButton(self.firstButtonX, self.firstButtonY, 12, "Draco-Griffe")
                        self.button2 = AttackTypeButton(self.firstButtonX + 160, self.firstButtonY, 13, "Draco-Souffle")
                        self.button3 = AttackTypeButton(self.firstButtonX, self.firstButtonY + 60, 25,
                                                           "Lance-Flammes")
                        self.button4 = AttackTypeButton(self.firstButtonX + 160, self.firstButtonY + 60, 10,
                                                        "Danse Flammes")
                    if self.button4.rect.collidepoint(event.pos):
                        self.player.change_map = self.player.previous_map
                        self.running = False


            # Interface de base
            baseInterface = BaseInterface()
            baseInterface.drawAll(self.screen.get_display(), self.squareX, self.squareY, self.ourPokeName)
            showPokemon = ShowPokemon()
            showPokemon.draw(self.screen.get_display(), self.ourPokeName, self.squareX, self.squareY)
            showWildPokemon = ShowWildPokemon()
            showWildPokemon.draw(self.screen.get_display(), self.wildPokeName, self.squareX, self.squareY)

            # Sert à l'agencement des boutons
            self.button1.draw(self.screen.get_display())
            self.button2.draw(self.screen.get_display())
            self.button3.draw(self.screen.get_display())
            self.button4.draw(self.screen.get_display())
            wildLife = lifeBar(self.wildPokeName, 200, 200)
            ourPokeLife = lifeBar(self.ourPokeName, 220, 220)
            wildLife.drawWildPoke(self.screen.get_display(), self.squareX, self.squareY)
            ourPokeLife.drawOurPoke(self.screen.get_display(), self.squareX, self.squareY)
            self.screen.update()
