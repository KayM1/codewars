import pygame
from settings import *
from tile import Tile
from player import Player
from support import import_csv_layout, import_folder
from random import choice

# from debug import debug

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('./maps/head_map._obstacles.csv'),
            'grass': import_csv_layout('./maps/head_map._grass.csv'),
            'object': import_csv_layout('./maps/head_map._objects.csv')
        }

        graphics = {
            'grass' : import_folder('./graphics/grass'),
            'objects': import_folder('./graphics/objects')
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE

                        if style == 'boundary':
                            Tile((x,y), [self.obstacle_sprites], 'invisible')
                        if style == 'grass':
                            random_grass_choice = choice(['127','128','126','129'])
                            random_grass_choice2 = choice(['127','128','126','129'])
                            if col == random_grass_choice or col == random_grass_choice2:
                                # create a grass tile
                                random_grass_image = choice(graphics['grass'])
                                Tile((x,y), [self.obstacle_sprites, self.visible_sprites], 'grass', random_grass_image)

                        if style == 'object':
                            surf = graphics['objects'][int(col)-1]
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)

        # for row_index, row in enumerate(WORLD_MAP):
        #     for col_index, col in enumerate(row):
        #         x = col_index * TILESIZE
        #         y = row_index * TILESIZE
                
        #         if  col == 'x':
        #             Tile((x,y), [self.visible_sprites, self.obstacle_sprites])

        #         if col == 'p':
        #             self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites) # we pass along the info of obstacles to the player, even if they are not in that group 

        self.player = Player((3700, 2500), [self.visible_sprites], self.obstacle_sprites)

    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        # debug(self.player.direction) see what direction the player is going



class YSortCameraGroup(pygame.sprite.Group): # inheriting from the group class and then customize it
    def __init__(self):

        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating the floormap
        self.floor_surf = pygame.image.load('./graphics/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self, player):
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        # for sprite in self.sprites():
        # reordering the sprites so higher Y sprites get drawn later than lower Y sprites
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)