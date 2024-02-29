import pygame


class lifeBar:
    def __init__(self, pokeMoche):
        self.pokeMoche = pokeMoche

    def drawPlayerPokeMoche(self, screen, x, y):
        lines = [f'{self.pokeMoche.name}', f'{self.pokeMoche.current_hp}/{self.pokeMoche.max_hp}']
        font = pygame.font.Font(f"../assets/font/PressStart2P-Regular.ttf", 14)
        for i, line in enumerate(lines):
            text_render = font.render(line, True, (0, 0, 0))
            screen.blit(text_render, (x + 405, y + 340 + i * 20))

    def drawRandomPokeMoche(self, screen, x, y):
        lines = [f'{self.pokeMoche.name}', f'{self.pokeMoche.current_hp}/{self.pokeMoche.max_hp}']
        font = pygame.font.Font(f"../assets/font/PressStart2P-Regular.ttf", 14)
        for i, line in enumerate(lines):
            text_render = font.render(line, True, (0, 0, 0))
            screen.blit(text_render, (x + 40, y + 70 + i * 20))

