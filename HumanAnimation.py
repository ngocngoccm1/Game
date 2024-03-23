from typing import Any
import pygame as py

class Human(py.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.sprites = []
        self.gravity = 10
        self.is_animate = False
        self.is_jump = False
        self.is_flip = False
        self.sprites.append(py.image.load('pngegg\sprite_119.png'))
        self.sprites.append(py.image.load('pngegg\sprite_100.png'))
        self.sprites.append(py.image.load('pngegg\sprite_101.png'))
        self.sprites.append(py.image.load('pngegg\sprite_102.png'))
        self.sprites.append(py.image.load('pngegg\sprite_103.png'))
        self.sprites.append(py.image.load('pngegg\sprite_104.png'))
        self.sprites.append(py.image.load('pngegg\sprite_105.png'))
        self.sprites.append(py.image.load('pngegg\sprite_106.png'))
        self.sprites.append(py.image.load('pngegg\sprite_107.png'))
        self.sprites.append(py.image.load('pngegg\sprite_120.png'))
        self.sprites.append(py.image.load('pngegg\sprite_121.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect(bottomleft= (pos_x,pos_y)) 

    def animate(self):
        self.is_animate = True
    
    def animate_stop(self):
        self.is_animate = False
        self.is_flip = False
        self.image = self.sprites[0]
    def flip(self):
        self.is_flip = True
    def turnR(self):
        if self.is_flip == True : self.is_flip = False
        self.rect.x += 20
        self.animate()
        if self.rect.x > 700 : self.rect.x = 700
    def turnL(self):
        self.rect.x -= 20
        self.flip()
        self.animate()
        if self.rect.x <= 100 : self.rect.x = 100
    def update(self,speed):
        if self.is_animate == True:            
            self.current_sprite += speed
            if self.current_sprite >= len(self.sprites)-2:
                self.current_sprite = 1
            self.image = self.sprites[int(self.current_sprite)]
        if self.is_jump == True:
            self.rect.y -= self.gravity*4
            self.gravity -= 1            
            if  self.gravity < -10:
                self.is_jump = False                
                self.gravity = 10
                self.image = self.sprites[0]
        
        if self.is_flip == True:
            self.image = py.transform.flip(self.image, True, False)
        # if self.rect.bottom >= 500:d
        #     self.rect.bottom = 500 
    def jump(self):
        self.is_jump = True
        self.is_animate = False
        self.image = self.sprites[len(self.sprites)-2]
#Game setup
py.init()
size = (800,600)
sr = py.display.set_mode(size)
clock = py.time.Clock()
py.display.set_caption('Human Run')
#Creating the sprite and groups
moving_sprite = py.sprite.Group()
human = Human(100,500)
moving_sprite.add(human)
run = True
while run:
    for ev in py.event.get():
        if ev.type == py.QUIT:
            run = False
    if py.key.get_pressed():
        if py.key.get_pressed()[py.K_d]:
            human.turnR()
        if py.key.get_pressed()[py.K_a]:
            human.turnL()
        if py.key.get_pressed()[py.K_SPACE]:
            human.jump()

    sr.fill((50,50,50))
    moving_sprite.draw(sr)
    moving_sprite.update(0.3)
    py.display.flip()
    clock.tick(60)
py.quit