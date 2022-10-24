import pygame
import sys
import os


from pygame import display

sys.path.insert(0, 'D:\\workspace\\pythonproject\\pingpong_game')
sys.path.insert(1, 'D:\\workspace\\pythonproject\\rockfall')
sys.path.insert(2, 'D:\\workspace\\pythonproject\\mole_game')

import pingpong_game as pg
import rock as rf
import mole_game as ml

pygame.font.init()

pygame.init()

#화면 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

score_pg = 0
score_rf = 0
score_ml = 0

#화면 크기 설정
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#시간(프레임,딜레이)
clock = pygame.time.Clock()

title_font = pygame.font.Font('D:\\workspace\\pythonproject\\multi_game\\images\\font1.ttf', 43)
title2_font = pygame.font.Font('D:\\workspace\\pythonproject\\multi_game\\images\\font1.ttf', 25)
score_font = pygame.font.Font('D:\\workspace\\pythonproject\\multi_game\\images\\font1.ttf', 18)

scorepg_image = score_font.render('최고점수 : {0}'.format(score_pg),True, (0,0,255))
spimg = scorepg_image.get_rect(centerx=SCREEN_WIDTH //3, centery=SCREEN_HEIGHT//2 + 100)

scorerf_image = score_font.render('최고점수 : {0}'.format(score_rf),True, (0,0,255))
srimg = scorerf_image.get_rect(centerx=SCREEN_WIDTH //2, centery=SCREEN_HEIGHT//2 + 100)

scoreml_image = score_font.render('최고점수 : {0}'.format(score_ml),True, (0,0,255))
smimg = scoreml_image.get_rect(centerx=SCREEN_WIDTH //3*2, centery=SCREEN_HEIGHT//2 + 100)


current_path = os.path.dirname(__file__)  # 현재 파일 위치 반환
image_path = os.path.join(current_path, "images")  # current_path 밑의 image 디렉토리

title_image = title_font.render('메인 화면',True, (255,255,255))
title = title_image.get_rect(centerx=SCREEN_WIDTH // 2, centery= 40)

title2_image1 = title2_font.render('핑퐁 게임', True, (0,0,0))
titleimg1 = title2_image1.get_rect(centerx=SCREEN_WIDTH //3, centery=SCREEN_HEIGHT//2 - 100)

title2_image2 = title2_font.render('슈팅 게임', True, (0,0,0))
titleimg2 = title2_image2.get_rect(centerx=SCREEN_WIDTH //2, centery=SCREEN_HEIGHT//2 - 100)

title2_image3 = title2_font.render('두더지 게임', True, (0,0,0))
titleimg3 = title2_image3.get_rect(centerx=SCREEN_WIDTH //3*2, centery=SCREEN_HEIGHT//2 - 100)


background_image2 = pygame.image.load(os.path.join(image_path, 'background.png'))

pingpong_image = pygame.image.load(os.path.join(image_path, 'pingpong.png'))
pingpong = pingpong_image.get_rect(centerx=SCREEN_WIDTH //3, centery=SCREEN_HEIGHT//2)

rockfall_image = pygame.image.load(os.path.join(image_path, 'rocket.png'))
rockfall = rockfall_image.get_rect(centerx=SCREEN_WIDTH // 2, centery =SCREEN_HEIGHT//2)

mole_image = pygame.image.load(os.path.join(image_path, 'mole.png'))
mole = mole_image.get_rect(centerx=SCREEN_WIDTH // 3 * 2, centery=SCREEN_HEIGHT//2)

exit_image = title_font.render('닫기',True, (255,0,0))
exitt = exit_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT - 70)

running = True



while running:
    
    
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    pygame.font.init()

    score_font = pygame.font.Font(None, 18)
    
    #화면 크기 설정

    screen.blit(background_image2,(0,0))
    screen.blit(pingpong_image, pingpong)
    screen.blit(rockfall_image, rockfall)
    screen.blit(exit_image, exitt)
    screen.blit(mole_image, mole)
    screen.blit(title_image, title)
    screen.blit(title2_image1, titleimg1)
    screen.blit(title2_image2, titleimg2)
    screen.blit(title2_image3, titleimg3)


    # screen.blit(scorepg_image, spimg)
    # screen.blit(scorerf_image, srimg)
    # screen.blit(scoreml_image, smimg)

    # pygame.display.update()
     

    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        print(event.pos[0], event.pos[1])
        if rockfall.collidepoint(event.pos):
            print('rockfall')
            score_rf = score = rf.rockfall()
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        elif pingpong.collidepoint(event.pos):
            print('pingpong')
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            spimg = scorepg_image.get_rect(centerx=SCREEN_WIDTH //3, centery=SCREEN_HEIGHT//2 + 100)
            score_pg = score = pg.pingpong_game()
            print(score_pg)
            pygame.font.init()
            # score_font = pygame.font.Font('D:\\workspace\\pythonproject\\multi_game\\images\\font1.ttf', 18)
            score_font = pygame.font.Font(None, 18)
            scorepg_image = score_font.render('최고점수 : {0}'.format(score_pg),True, (0,0,255))
            print('--- after score_img---')
        elif mole.collidepoint(event.pos):
            print('mole')
            score_ml = score = ml.mole_game()
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        elif exitt.collidepoint(event.pos):
            print('종료되었습니다.')
            running = False
            # pygame.quit()

    print('---end---')
    
    screen.blit(scorepg_image, spimg)
    screen.blit(scorerf_image, srimg)
    screen.blit(scoreml_image, smimg)

    pygame.display.update()

# pygame.quit()
    
   
    # clock.tick(50)