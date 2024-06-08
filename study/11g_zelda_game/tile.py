import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups) # initiate the inherited class from sprite.Sprite (pygame)
        self.image = pygame.image.load('./graphics/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)