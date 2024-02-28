import pygame


class ShowWildPokemon:
    def draw(self, screen, pokemonName, x, y):
        basePokeImage = pygame.image.load(f"../assets/sprite/pokemon/" + pokemonName + ".png").convert_alpha()
        sizePokeImage = pygame.transform.scale(basePokeImage, (200, 200))
        screen.blit(sizePokeImage, (x + 400, y + 70))
