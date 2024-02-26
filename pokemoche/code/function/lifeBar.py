import pygame

class lifeBar:
    def __init__(self,pokemonName,health,healthMax):
        self.pokemonName = pokemonName
        self.health = health
        self.healthMax = healthMax

    def draw(self,screen,x,y):
        lines = [ f'{self.pokemonName}',f'{self.health}/{self.healthMax}']
        font = pygame.font.Font(f"../assets/font/PressStart2P-Regular.ttf", 12)
        for i, line in enumerate(lines):
            text_render = font.render(line, True, (0, 0, 0))
            screen.blit(text_render, (x + 40, y + 70 + i * 20))