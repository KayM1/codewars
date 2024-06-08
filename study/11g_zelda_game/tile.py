import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups) # initiate the inherited class from sprite.Sprite (pygame)
        image = pygame.image.load('./graphics/rock.png').convert_alpha()
        self.image = pygame.transform.scale(image, (64, 64))
        self.rect = self.image.get_rect(topleft = pos)