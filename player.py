import pygame
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.import_character()
        self.frame_index = 0
        self.animations_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]

        self.rect = self.image.get_rect(topleft = pos)
        # player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.speed_jump = -16
        # player status
        self.status = 'idle'
        self.racting_right = True
        self.on_ground = False
        self.on_ceilling = False
        self.on_left = False
        self.on_right = False
        
    def import_character(self):
        character_path = 'graphics/character/'
        self.animations = {'idle':[],'run':[],'jump':[],'fall':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.racting_right = True
        elif keys[pygame.K_a]:
            self.direction.x = - 1
            self.racting_right = False
        else: self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_ground: self.jump()

    def get_status(self):
        if self.direction.y < 0:
            self.status ='jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle' 

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.speed_jump

    def animate(self):
        animation = self.animations[self.status]

    #loop over frame index
        self.frame_index += self.animations_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        image = animation[int(self.frame_index)]
        if  self.racting_right:
            self.image = image
        else:
            flip_img = pygame.transform.flip(image,True,False)
            self.image = flip_img

        if self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceilling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceilling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceilling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()