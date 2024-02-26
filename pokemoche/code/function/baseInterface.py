import pygame
class BaseInterface:
    def drawAll(self,screen,squareX,squareY,pokemonName):

        lines = ['Que doit faire', f'{pokemonName} ?']
        font = pygame.font.Font(f"../assets/font/PressStart2P-Regular.ttf", 12)
        baseImage = pygame.image.load(f"../assets/sprite/fight/backFight.png").convert_alpha()
        pokeFloor = pygame.image.load(f"../assets/sprite/fight/ourPoke.png").convert_alpha()
        wildFloor = pygame.image.load(f"../assets/sprite/fight/wildPoke.png").convert_alpha()
        wildFloorSized = pygame.transform.scale(wildFloor, (250, 70))
        pokeFloorSized = pygame.transform.scale(pokeFloor, (300, 60))
        sizedImage = pygame.transform.scale(baseImage, (650, 650))
        # ligne du dessous sert pour le fond
        screen.blit(sizedImage, (squareX, squareY))

        # sert pour les lifebars
        pygame.draw.rect(screen, (254, 254, 226), (squareX + 20, squareY + 50, 250, 70))
        pygame.draw.rect(screen, (0, 0, 0), (squareX + 20, squareY + 50, 250, 70), 2)
        screen.blit(wildFloorSized, (squareX + 370, squareY + 200))
        pygame.draw.rect(screen, (254, 254, 226), (squareX + 380, squareY + 320, 250, 70))
        pygame.draw.rect(screen, (0, 0, 0), (squareX + 380, squareY + 320, 250, 70), 2)
        screen.blit(pokeFloorSized, (squareX + 50, squareY + 440))

        #englobe les buttons
        pygame.draw.rect(screen, (254, 254, 226), (squareX,squareY+502,650,147))
        pygame.draw.rect(screen, (0, 0, 0), (squareX+1, squareY + 503, 648, 146),2)
        for i, line in enumerate(lines):
            text_render = font.render(line, True, (0, 0, 0))
            screen.blit(text_render, (squareX + 40, squareY + 570 + i * 20))

