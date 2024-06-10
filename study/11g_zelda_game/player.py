import pygame
from settings import *
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups) # initiate the inherited class from sprite.Sprite (pygame)
        image = pygame.image.load('./graphics/player.png').convert_alpha()
        self.image = pygame.transform.scale(image, (64, 64))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-10, -26)

        # define movement
        self.direction = pygame.math.Vector2()
        self.speed = 5 # define speed (we might replace this with a dictionary of all player attributes later)
        self.min_speed = 5
        # attacking
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

        #import graphics
        self.import_player_assets()

        # apply graphics based on player status
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        # interact with obstacles
        self.obstacle_sprites = obstacle_sprites

        #sprinting
        self.start_speed = 6
        self.slow_speed = 6
        self.high_speed = 12
        self.sprint = False


    # import player graphics
    def import_player_assets(self):
        character_path = './graphics/player/'
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'right_idle' : [], 'left_idle' : [], 'down_idle': [], 'up_idle': [],
                           'right_attack': [], 'left_attack':[], 'down_attack': [], 'up_attack':[]
                           }

        for animation in self.animations:
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
        
        print(self.animations)

    def input(self):
        keys = pygame.key.get_pressed()

        # movement input
        #sprint

        if keys[pygame.K_z]:
            self.speed = self.high_speed
            self.sprint = True
        else:
            self.speed =  self.slow_speed
            self.sprint = False

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0 # also applies when we stop holding a button

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0 # also applies when we stop holding a button
        
        if self.direction.x == 0 and self.direction.y == 0:
            self.speed = self.min_speed

        # attack input
        if keys[pygame.K_e] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            print('attack')

        # magic
        if keys[pygame.K_a] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            print('magic')


    def get_status(self):

        #idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'
        
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    # override idle
                    self.status = self.status.replace('_idle', '_attack')
                else:    
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack', '')

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize() # prevent we are moving too fast diagonally
        
        if not '_idle' in self.status:
            self.start_speed = self.start_speed + self.start_speed * 0.03
        else:
            self.start_speed = 5
        if self.sprint == False:
            self.speed = min(self.start_speed, speed+5)
            if self.start_speed >= self.slow_speed:
                self.start_speed = self.slow_speed
        else:
            self.speed = min(self.start_speed, speed+self.high_speed)
            if self.start_speed >= self.high_speed:
                self.start_speed = self.high_speed

        self.hitbox.x += self.direction.x * self.speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * self.speed
        self.collision('vertical')
        # self.rect.center += self.direction * speed (same as above but merged (simpler / earlier))
        self.rect.center = self.hitbox.center


    def collision (self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

    def animate(self):
        animation = self.animations[self.status]

        # loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        # set the image
        self.image = animation[int(self.frame_index)]
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)