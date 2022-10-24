import pygame
import os

#초기화
pygame.init()
#위젯설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("퐁 게임")
#불러오기
clock = pygame.time.Clock()
current_path = os.path.dirname(__file__)  # 현재 파일 위치 반환
image_path = os.path.join(current_path, "images")  # current_path 밑의 image 디렉토리
#이미지 로드 및 정의
background = pygame.image.load(os.path.join(current_path, "background.png"))
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]
player = pygame.image.load(os.path.join(image_path, "character.png"))
player_size = player.get_rect().size
player_width = player_size[0]
player_height = player_size[1]
player_x_pos = screen_width/2 - player_width/2
player_y_pos = screen_height - stage_height - player_height
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
ball_images = [
    pygame.image.load(os.path.join(image_path, "ball1.png")),
    pygame.image.load(os.path.join(image_path, "ball2.png")),
    pygame.image.load(os.path.join(image_path, "ball3.png")),
    pygame.image.load(os.path.join(image_path, "ball4.png"))]
#세부 설정값
player_to_x = 0
player_speed = 5
weapons = []
weapon_speed = 10
ball_speed_y = [-18, -15, -12. - 9]
balls = []
balls.append(  # dictionary #첫번째 공 설정
    {"pos_x": 50,
     "pos_y": 50,
     "img_idx": 0,
     "to_x": 3,
     "to_y": -6,
     "init_speed_y": ball_speed_y[0]}
)
weapon_to_remove = -1
ball_to_remove = -1
#폰트 정의
game_font = pygame.font.Font(None, 40)
total_time = 100
start_ticks = pygame.time.get_ticks()
#게임 결과 메시지
game_result = ""  # Game Over #Mision Complete # Time Over
#실행
running = True
while running:
    #fps
    dt = clock.tick(30)
#게임 명령키 입력
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
if event.key == pygame.K_LEFT:
player_to_x -= player_speed
elif event.key == pygame.K_RIGHT:
player_to_x += player_speed
elif event.key == pygame.K_SPACE:  # 무기발사
weapon_x_pos = player_x_pos + (player_width - weapon_width)/2
weapon_y_pos = player_y_pos
weapons.append([weapon_x_pos, weapon_y_pos])
if event.type == pygame.KEYUP:
if event.key == pygame.K_LEFT or pygame.K_RIGHT:
player_to_x = 0
if event.type == pygame.QUIT:
running = False
#캐릭터, 무기 이동시키기
player_x_pos += player_to_x
if player_x_pos <= 0:
player_x_pos = 0
elif player_x_pos >= screen_width - player_width:
player_x_pos = screen_width - player_width
weapons = [[w[0], w[1]-weapon_speed] for w in weapons]  # 무기 위치를 위로
weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]  # 천장에 닿으면 없애기
#공 만들기
for ball_idx, ball_val in enumerate(balls):
ball_pos_x = ball_val["pos_x"]
ball_pos_y = ball_val["pos_y"]
ball_img_idx = ball_val["img_idx"]
ball_size = ball_images[ball_img_idx].get_rect().size
ball_width = ball_size[0]
ball_height = ball_size[1]
#공 튕기기
if ball_pos_x < 0 or ball_pos_x >= screen_width - ball_width:
ball_val["to_x"] = ball_val["to_x"] * -1  # 벽 닿으면 튕기기
if ball_pos_y >= screen_height - stage_height - ball_height:
ball_val["to_y"] = ball_val["init_speed_y"]  # 바닥에 닿으면 가속도 초기화
else:
ball_val["to_y"] += 0.6  # 중력값 #올라가면서 느려지고 떨어지면서 빨라지기
ball_val["pos_x"] += ball_val["to_x"]
ball_val["pos_y"] += ball_val["to_y"]
#공 쪼개기
player_rect = player.get_rect()
player_rect.top = player_y_pos
player_rect.left = player_x_pos
#이중 for문 #버그 원인!
for ball_idx, ball_val in enumerate(balls):
ball_pos_x = ball_val["pos_x"]
ball_pos_y = ball_val["pos_y"]
ball_img_idx = ball_val["img_idx"]
ball_rect = ball_images[ball_img_idx].get_rect()
ball_rect.left = ball_pos_x
ball_rect.top = ball_pos_y
#player와 충돌하면 패배
if player_rect.colliderect(ball_rect):
game_result = "Game Over"
running = False
break
#무기와 충돌하면 쪼개짐
for weapon_idx, weapon_val in enumerate(weapons):
weapon_pos_x = weapon_val[0]
weapon_pos_y = weapon_val[1]
weapon_rect = weapon.get_rect()
weapon_rect.left = weapon_pos_x
weapon_rect.top = weapon_pos_y
if weapon_rect.colliderect(ball_rect):
weapon_to_remove = weapon_idx
ball_to_remove = ball_idx
if ball_img_idx < 3:
ball_width = ball_rect.size[0]
ball_height = ball_rect.size[1]
small_ball_rect = ball_images[ball_img_idx+1].get_rect()
small_ball_width = small_ball_rect.size[0]
small_ball_height = small_ball_rect.size[1]
balls.append(  # dictionary #두번째 공 설정
    {"pos_x": ball_pos_x + (ball_width/2-small_ball_width/2),
     "pos_y": ball_pos_y + (ball_height/2-small_ball_height/2),
     "img_idx": ball_img_idx + 1,
     "to_x": -3,
     "to_y": -6,
     "init_speed_y": ball_speed_y[ball_img_idx + 1]}
)  # 왼쪽으로
balls.append(  # dictionary #두번째 공 설정
    {"pos_x": ball_pos_x + ball_width/2,
     "pos_y": ball_pos_y+ball_height/2,
     "img_idx": ball_img_idx + 1,
     "to_x": 3,
     "to_y": -6,
     "init_speed_y": ball_speed_y[ball_img_idx + 1]}
)  # 오른쪽으로
break
else:
continue  # 안쪽 for문 조건이 맞지 않으면 continue #바깥 for문 계속 수행
break  # 안쪽 for문에서 break만나면 여기로 진입가능 #2중 for문 한번에 탈출 가능
'''
for 바깥 조건:
바깥 동작
for 안쪽 조건:
안쪽 동작
if 충돌하면:
break
else:
continue
break
'''
#공 list에서 제거
if ball_to_remove > -1:
del balls[ball_to_remove]
ball_to_remove = -1
if weapon_to_remove > -1:
del weapons[weapon_to_remove]
weapon_to_remove = -1
#모든 공을 없앤 경우
if len(balls) == 0:
game_result = "Mission Complete"
running = False
#이미지 출력
screen.blit(background, (0, 0))
for weapon_x_pos, weapon_y_pos in weapons:
screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
for idx, val in enumerate(balls):
ball_pos_x = val["pos_x"]
ball_pos_y = val["pos_y"]
ball_img_idx = val["img_idx"]
screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
screen.blit(stage, (0, screen_height-stage_height))
screen.blit(player, (player_x_pos, player_y_pos))
#타이머 출력
elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
timer = game_font.render("Time : {}".format(
    int(total_time - elapsed_time)), True, (255, 0, 0))
screen.blit(timer, (10, 10))
if total_time - elapsed_time <= 0:
game_result = "Time Over"
running = False
#업데이트
pygame.display.update()

#게임오버 메시지
msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center=(int(screen_width/2), int(screen_height/2)))
screen.blit(msg, msg_rect)
pygame.display.update()
#끝내기
pygame.time.delay(2000)


# 메시지박스를 띄워서 재시작/종료를 묻게 해보자!!!!

pygame.quit
