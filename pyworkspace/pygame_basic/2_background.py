import pygame
import os

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("New Game")

current_path = os.path.dirname(__file__)

background = pygame.image.load(os.path.join(current_path, "background.png"))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 배경채우기
    # screen.fill((0,0,255))
    # blit 함수는 한 표면에서 다른 표면으로 픽셀 복사(이미지 복사) (이미지, 복사위치)
    screen.blit(background, (0, 0))
    # 화면업데이트
    pygame.display.update()

pygame.quit()
