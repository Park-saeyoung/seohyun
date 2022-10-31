import pygame
import os

# 임포트된 모든 파이게임 모듈들을 초기화
pygame.init() 

screen_width = 480
screen_height = 640
# 스크린 표면을 생성
# 매개변수 사이드를 통해 높이와 너비 지정
# 보통 매개변수 depth 는 전달하지 않는 것이 최적
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("New Game")

current_path = os.path.dirname(__file__)

background = pygame.image.load(os.path.join(current_path, "background.png"))
character = pygame.image.load(os.path.join(current_path, "character.png"))

# 알파값을 사용하여 이미지를 투명하게
character.set_alpha(128)

# character = pygame.image.load("D:\\pyworkspace\\pygame_basic\\character.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

running = True
while running:
    # 큐에서 이벤트를 얻기
    for event in pygame.event.get():   
    # 타입               리턴

    # QUIT              none
    # ACTIVEEVENT       gain, state
    # KEYDOWN           key, mod, unicode, scancode
    # KEYUP             key, mod
    # MOUSEMOTION       pos, rel, buttons
    # MOUSEBUTTONUP     pos, button
    # MOUSEBUTTONDOWN   pos, button
    
        if event.type == pygame.QUIT:
            running = False

    print(event)
    # blit 함수는 한 표면에서 다른 표면으로 픽셀 복사(이미지 복사) (이미지, 복사위치)
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()

pygame.quit()
