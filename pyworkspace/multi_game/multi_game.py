import pygame
import sys
import os

from pygame import display

sys.path.insert(0, 'D:\\pyworkspace\\pingpong_game')
sys.path.insert(1, 'D:\\pyworkspace\\rock_fall')
sys.path.insert(2, 'D:\\pyworkspace\\mole_game')

print('1')
import rock as rf
print('2')
import mole_game as ml
print('3')
# import pingpong_game as pg
print('4')

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__) 
image_path = os.path.join(current_path, "images") 

pingpong_image = pygame.image.load(os.path.join(image_path, 'pingpong.png'))
pingpong = pingpong_image.get_rect(centerx=SCREEN_WIDTH //3, centery=SCREEN_HEIGHT//2)

rockfall_image = pygame.image.load(os.path.join(image_path, 'rocket.png'))
rockfall = rockfall_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT//2)

mole_image = pygame.image.load(os.path.join(image_path, 'mole.png'))
mole = mole_image.get_rect(centerx=SCREEN_WIDTH // 3 * 2, centery=SCREEN_HEIGHT//2)

BLACK = (0,0,0)

running = True

print('22222')
print('한글테스트')

while running:

    screen.fill(BLACK)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
        pygame.quit()
        sys.exit()
        break
    if event.type == pygame.MOUSEBUTTONDOWN:
        print(event.pos[0], event.pos[1])
        if rockfall.collidepoint(event.pos):
            print('rockfall')
            rf.rock()
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        elif pingpong.collidepoint(event.pos):
            print('pingpong')
            pg.pinpong_game()
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        elif mole.collidepoint(event.pos):
            print('mole')
            ml.mole()
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    screen.blit(pingpong_image, pingpong)
    screen.blit(rockfall_image, rockfall)
    screen.blit(mole_image, mole)
    pygame.display.update()
    clock.tick(50)

# pygame.quit()
# sys.exit()