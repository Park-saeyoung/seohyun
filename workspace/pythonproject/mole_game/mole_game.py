import pygame
import os
import random
import time

from pygame.constants import QUIT

def mole_game():

    pygame.init()

    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    #시간 설정(시작시간, 게임시간, 종료시간) 타이머
    start_time = int(time.time())
    total_time = 30

    print('time {0}'.format(start_time))

    dontmolehit = pygame.time.get_ticks() + 3000


    #현재 경로 설정
    current_path = os.path.dirname(__file__) #현재 경로 반환
    image_path = os.path.join(current_path, 'images')
    sound_path = os.path.join(current_path, "sounds")
    #두더지 이미지 로딩
    mole_image = pygame.image.load(os.path.join(image_path,'mole.png'))
    moledie_image = pygame.image.load(os.path.join(image_path,'moledie.png'))
    #배경 이미지 로딩
    background_image = pygame.image.load(os.path.join(image_path,'background.png'))

    shot_sound = pygame.mixer.Sound(os.path.join(sound_path, "moledie.mp3"))
    bgm_sound = pygame.mixer.Sound(os.path.join(sound_path, "bgm.mp3"))
    bgm_sound.play(-1)

    #폰트 설정
    score_font = pygame.font.SysFont('calisto',30, False, False)

    #점수
    score = 0

    gmover = False

    game_over = False

    moles = []

    for i in range(4):
        # mole = mole_image.get_rect()
        # mole.left = (i+1) * 100
        # mole.top = (i+1) * 100

        mole = mole_image.get_rect(left=random.randint(0, SCREEN_WIDTH-mole_image.get_width()),
                                    top=random.randint(0, SCREEN_HEIGHT-mole_image.get_height()))

        after_second = random.randint(0,3)
        during_second = random.randint(1,3)
        appear_time = int(time.time()) + after_second
        dissapear_time = int(time.time()) + after_second + during_second


        moles.append((mole, appear_time, dissapear_time))

    while not game_over:

        pygame.mouse.set_cursor(*pygame.cursors.broken_x)

        screen.blit(background_image,(0,0))
        # screen.fill((120,120,120))
        if game_over == True:
            break

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        #마우스 클릭 이벤트 처리
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                        game_over = True
                        break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos[0], event.pos[1])
            for mole, appear_time, dissapear_time in moles:
                current_time = int(time.time())
                if mole.collidepoint(event.pos):
                    print('Hit')
                    moles.remove((mole, appear_time, dissapear_time))
                    screen.blit(moledie_image,mole)
                    shot_sound.play()
                    mole = mole_image.get_rect(left=random.randint(0, SCREEN_WIDTH-mole_image.get_width()),
                                    top=random.randint(0, SCREEN_HEIGHT-mole_image.get_height()))

                    after_second = random.randint(0,3)
                    during_second = random.randint(1,3)
                    appear_time = int(time.time()) + after_second
                    dissapear_time = int(time.time()) + after_second + during_second 
                    moles.append((mole, appear_time, dissapear_time))
                    score+=2

        for mole, appear_time, dissapear_time in moles:
            current_time = int(time.time())
            if current_time > dissapear_time:
                print('Hit')
                moles.remove((mole, appear_time, dissapear_time))
                mole = mole_image.get_rect(left=random.randint(0, SCREEN_WIDTH-mole_image.get_width()),
                                top=random.randint(0, SCREEN_HEIGHT-mole_image.get_height()))

                after_second = random.randint(0,2)
                during_second = random.randint(1,2)
                appear_time = int(time.time()) + after_second
                dissapear_time = int(time.time()) + after_second + during_second 
                moles.append((mole, appear_time, dissapear_time))

        for mole, appear_time, dissapear_time in moles:
            
            if current_time >= appear_time:
                screen.blit(mole_image, mole)
            if appear_time == 3:
                moles.remove((mole, appear_time, dissapear_time))

        current_time = int(time.time())
        passed_time = current_time - start_time

        if passed_time >= total_time:
            game_over = True
            print('SCORE : {}'.format(score))

        if game_over:
            game_over_image = score_font.render('GAME OVER!!!', True, (0,0,0))
            screen.blit(game_over_image, game_over_image.get_rect(centerx=SCREEN_WIDTH/2,centery=SCREEN_HEIGHT/2))

        score_image = score_font.render('SCORE : {}'.format(score), True, (0,255,0))
        time_image = score_font.render('TIME : {}'.format(passed_time), True, (0,0,0))
        screen.blit(score_image, (10, 10))
        screen.blit(time_image, (10, 50))
        pygame.display.update()

        clock.tick(30)
    pygame.quit()
    return