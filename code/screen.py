import pygame


class Screen:

    def __init__(self):
        self.display = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("PokéMoche")
        self.clock = pygame.time.Clock()
        self.framerate: int = 60
        self.deltatime: float = 0.0
        logo = pygame.image.load("../assets/sprite/pokeball.png")
        pygame.display.set_icon(logo)

    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(self.framerate)
        self.display.fill((0, 0, 0))
        self.deltatime = self.clock.get_time()

    def get_delta_time(self) -> float:
        return self.deltatime

    def get_size(self):
        return self.display.get_size()

    def get_display(self):
        return self.display
