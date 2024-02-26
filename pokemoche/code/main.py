import pygame

from game import Game
from fightInterface import fightInterface


pygame.init()


if __name__ == "__main__":
    #game = Game()
    #game.run()
    fightInterface = fightInterface()
    fightInterface.startFight()
