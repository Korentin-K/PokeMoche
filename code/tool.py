import pygame


class Tool:
    @staticmethod
    def split_image(spritesheet:pygame.Surface, x:int, y:int, width:int, height:int):
        return spritesheet.subsurface(pygame.Rect(x,y,width,height))
