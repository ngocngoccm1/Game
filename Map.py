import pygame 
from setting import *


from level import Level
pygame.init()

fps = 60
sr = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
level = Level(level_map,sr)


run = True
while run:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
    sr.fill('grey')
    level.run()
    pygame.display.update()
    clock.tick(fps)

pygame.quit()