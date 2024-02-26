import pygame

class ShowPokemon:
    def draw(self, screen,pokemonName,x,y):
        basePokeImage = pygame.image.load(f"../assets/sprite/pokemon/"+pokemonName+".png").convert_alpha()
        sizePokeImage =  pygame.transform.scale(basePokeImage, (180, 140))
        screen.blit(sizePokeImage, (x +100, y +370))