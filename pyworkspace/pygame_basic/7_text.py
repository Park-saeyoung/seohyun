import pygame
import os

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("New Game")

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)

background = pygame.image.load(os.path.join(current_path, "background.png"))
character = pygame.image.load(os.path.join(current_path, "character.png"))

enemy = pygame.image.load(os.path.join(current_path, "enemy.png"))

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width/2
character_y_pos = screen_height - character_height

running = True
to_x = 0
to_y = 0

character_speed = 0.2

enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = screen_width/2 - enemy_width/2
enemy_y_pos = screen_height/2 - enemy_height

game_font = pygame.font.Font(None, 40)

# SysFont("글꼴", 크기, 굵기여부, 기울기(여부))  -> 폰트 가져오기
game_font = pygame.font.SysFont('arial',30, True, True)


font1 = pygame.font.SysFont(None,30)
img1 = font1.render('HELLO WOLRD! 안녕하세요!',True,(0,255,0))
screen.blit(img1, (50,50))


total_time = 10
#시작시간
start_titcks = pygame.time.get_ticks()

while running:
    dt = clock.tick(60)

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

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    if character_x_pos <= 0:
        character_x_pos = 0
    elif character_x_pos >= screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌 발생!!!!!")

    screen.blit(background,(0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    #경과 시간
    # get_ticks(): pygame.init()이 호출된 이후 흐른 시간(ms)를 리턴해주므로 계속 증가하는 값
    elapsed_time = (pygame.time.get_ticks() - start_titcks) / 1000

    #출력할 글자, True, 글자색 (텍스트, antialias, 색(튜플), 텍스트 배경색(튜플))
    #antialias : 높은 해상도의 신호를 낮은 해상도에서 나타낼 때 생기는 계단 현상을 최소화
    timer = game_font.render(str(int(total_time-elapsed_time)), True, (255,255,255),(0,0,0))

    screen.blit(timer, (10,10))

    if total_time - elapsed_time <=0:
        print("타임아웃")
        running = False

    pygame.display.update()
    # pygame.time.delay(2000)

    
pygame.quit()