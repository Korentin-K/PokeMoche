import pygame

class AttackButton:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.text = "Attaque"
            self.font = pygame.font.Font(f"../assets/font/PressStart2P-Regular.ttf", 14)
            self.width = 150
            self.height = 50
            self.color = (255, 0, 0)
            self.text_color = (255, 255, 255)
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        def draw(self, screen):
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
            screen.blit(text_surface, text_rect)

        def collidepoint(self, pos):
            return self.rect.collidepoint(pos)

