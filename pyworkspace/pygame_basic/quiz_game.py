import pygame
import random
import os

#기본 초기화
pygame.init()

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("New Game")

clock = pygame.time.Clock()
##############################################################################

#1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등등)
#배경 만들기
#캐릭터 만들기
current_path = os.path.dirname(__file__)

background = pygame.image.load(os.path.join(current_path, "background.png"))
character = pygame.image.load(os.path.join(current_path, "character.png"))
enemy = pygame.image.load(os.path.join(current_path, "enemy.png"))
enemy2 = pygame.image.load(os.path.join(current_path, "enemy.png"))

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height

enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0

enemy2_size = enemy.get_rect().size
enemy2_width = enemy_size[0]
enemy2_height = enemy_size[1]
enemy2_x_pos = random.randint(0, screen_width - enemy_width)
enemy2_y_pos = 0


#적의 속도
enemy_speed = 10
enemy2_speed = 10
 
#이동 위치
to_x = 0
to_y = 0
character_speed = 0.5

running = True

while running:
    dt = clock.tick(30)

    #2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_LEFT:
                to_x -= character_speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                to_x = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #3. 가로 경계값 처리
    if character_x_pos <=0:
        character_x_pos = 0
    elif character_x_pos >= screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    #4. 세로 경계값 처리

    #5. 게임 캐릭터 위치 정의
    character_x_pos += to_x

    enemy_y_pos += enemy_speed
    if enemy_y_pos == screen_height:
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        enemy_y_pos = 0

    enemy2_y_pos += enemy2_speed
    if enemy2_y_pos == screen_height:
        enemy2_x_pos = random.randint(0, screen_width - enemy2_width)
        enemy2_y_pos = 0

    #6. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    enemy2_rect = enemy.get_rect()
    enemy2_rect.left = enemy_x_pos
    enemy2_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("***충돌***")
        # enemy_y_pos = screen_height - enemy_height*2
        # enemy_y_pos = screen_height

    #7. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(enemy2, (enemy2_x_pos, enemy2_y_pos))

    pygame.display.update()

pygame.quit()