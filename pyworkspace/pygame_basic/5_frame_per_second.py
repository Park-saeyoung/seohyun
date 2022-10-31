import pygame
import os

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("New Game")

#초당 프레임수 설정을 위한 변수
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)

background = pygame.image.load(os.path.join(current_path, "background.png"))
character = pygame.image.load(os.path.join(current_path, "character.png"))


character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width/2
character_y_pos = screen_height - character_height

running = True
to_x = 0
to_y = 0

FPS=120

#이동 속도 조절용 변수
# character_speed = 0.5
character_speed = 10

while running:
    #FPS 초당 프레임 수 설정
    #  tick() 함수는 주어진 FPS 값을 넘지 않기 위해 딜레이를 주는 함수/ 프레임 수가 많을수록 
    dt = clock.tick(FPS)

    #프레임 수 확인
    print("Fps :" + str(clock.get_fps()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x+=character_speed
            elif event.key == pygame.K_LEFT:
                to_x-=character_speed
            elif event.key == pygame.K_UP:
                to_y-=character_speed
            elif event.key == pygame.K_DOWN:
                to_y+=character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key ==pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0 

    character_x_pos += to_x
    character_y_pos += to_y

    # dt를 곱해서 프레임 수에 따른 이동 속도를 동일하게 맞춤 
    # 프레임 수가 많을수록(속도 증가) dt값이 낮아져 속도를 균일하게 유지함
    # character_x_pos += to_x * dt
    # character_y_pos += to_y * dt


    if character_x_pos <= 0:
        character_x_pos = 0
    elif character_x_pos >= screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background,(0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()

    print("dt :" + str(dt))

pygame.quit()