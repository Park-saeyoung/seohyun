import pygame #파이 게임 모듈 임포트
import os
import random
import time

pygame.init() #파이 게임 초기화
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #화면 크기 설정
clock = pygame.time.Clock() 

#변수

BLACK = (0, 0, 0)

current_path = os.path.dirname(__file__)  # 현재 파일 위치 반환
image_path = os.path.join(current_path, "images")  # current_path 밑의 image 디렉토리
mole_image = pygame.image.load(os.path.join(image_path, 'mole.png'))
background_image = pygame.image.load(os.path.join(image_path, 'background.png'))

moles = []
for i in range(4):
    # mole = mole_image.get_rect()
    # mole.left = (i + 1) * 100
    # mole.top = (i + 1) * 100

    #랜덤으로 두더지 위치 설정
    mole = mole_image.get_rect(left=random.randint(0, SCREEN_WIDTH - mole_image.get_width()), 
        top=random.randint(0, SCREEN_HEIGHT - mole_image.get_height()))
    after_second = random.randint(0, 3)
    during_second = random.randint(1, 3)
    appear_time = int(time.time()) + after_second
    disappear_time = int(time.time()) + after_second + during_second
    moles.append((mole, appear_time, disappear_time))

game_over = False

while True: #게임 루프
    
    #단색으로 채워 화면 지우기
    # screen.fill(BLACK) 

    #배경 이미지
    screen.blit(background_image, (0, 0))


    start_time = int(time.time()) #1970년 1월 1일 0시 0분 0초 부터 현제까지 초 

    #변수 업데이트

    event = pygame.event.poll() #이벤트 처리
    if event.type == pygame.QUIT:
        break
    #마우스 클리 이벤트 처리
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print(event.pos[0], event.pos[1])
        for mole, appear_time, disappear_time in moles:
            if mole.collidepoint(event.pos):
                print(mole)
                print('Hit')
                moles.remove((mole, appear_time, disappear_time))
                mole= mole_image.get_rect(left=random.randint(0, SCREEN_WIDTH - mole_image.get_width()), 
                    top=random.randint(0, SCREEN_HEIGHT - mole_image.get_height()))
                after_second = random.randint(0, 2)
                during_second = random.randint(0, 1)
                appear_time = int(time.time()) + after_second
                disappear_time = int(time.time()) + after_second + during_second
                moles.append((mole, appear_time, disappear_time))

    if not game_over:
        current_time = int(time.time())
        for mole, appear_time, disappear_time in moles:
            if current_time > disappear_time:
                moles.remove((mole, appear_time, disappear_time))
                mole= mole_image.get_rect(left=random.randint(0, SCREEN_WIDTH - mole_image.get_width()), 
                    top=random.randint(0, SCREEN_HEIGHT - mole_image.get_height()))
                after_second = random.randint(0, 2)
                during_second = random.randint(0, 1)
                appear_time = int(time.time()) + after_second
                disappear_time = int(time.time()) + after_second + during_second
                moles.append((mole, appear_time, disappear_time))
    
    
    #화면 그리기
    for mole, appear_time, disappear_time in moles:
        current_time = int(time.time())
        if  current_time >= appear_time:  
            screen.blit(mole_image, mole)

    pygame.display.update() #모든 화면 그리기 업데이트
    clock.tick(30) #30 FPS (초당 프레임 수) 를 위한 딜레이 추가, 딜레이 시간이 아닌 목표로 하는 FPS 값

pygame.quit() 