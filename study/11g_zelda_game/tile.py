import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups) # initiate the inherited class from sprite.Sprite (pygame)
        self.sprite_type = sprite_type
        self.image = surface
        if sprite_type == 'object':
            self.image = pygame.transform.scale(self.image, (128, 128))
        else:
            self.image = pygame.transform.scale(self.image, (64, 64))
        # image = pygame.image.load('./graphics/rock.png').convert_alpha()
        # self.image = pygame.transform.scale(image, (64, 64))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10) # change the hitbox / rect -10 = shrink by 5 on each side