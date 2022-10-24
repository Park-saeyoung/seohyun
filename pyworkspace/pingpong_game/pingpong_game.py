# import pygame
# import random

# def pinpong_game():
#     clock = pygame.time.Clock()

#     #화면 크기
#     SCREEN_WIDTH = 800
#     SCREEN_HEIGHT = 600

#     #초기화
#     pygame.init()

#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#     #패들 좌표,사이즈 설정
#     left_paddle = pygame.Rect(0, SCREEN_HEIGHT//2 - 80//2, 16, 80)
#     right_paddle = pygame.Rect(SCREEN_WIDTH-16, SCREEN_HEIGHT//2 - 80//2, 16, 80)

#     #공 만들기
#     ball = pygame.Rect(SCREEN_WIDTH//2-16//2,SCREEN_HEIGHT//2-16//2,16,16)

#     #공의 이동 변수
#     ball_x = 5
#     ball_y = 5

#     #색
#     BLACK = (0,0,0)
#     RED = (255,0,0)
#     WHITE = (255,255,255)

#     #폰트 설정
#     score_font = pygame.font.SysFont('calisto',30, False, False)

#     #
#     rscore = 0
#     lscore = 0

#     #게임 종료
#     game_over = False

#     pygame.key.set_repeat(1,10)

#     while True:
#         screen.fill(BLACK)
        
#         if game_over == True:
#             break

#         #이벤트 처리
#         #event = pygame.event.poll() #이벤트 처리
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#                 break
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_UP:
#                     right_paddle.top -=3
#                 elif event.key == pygame.K_DOWN:
#                     right_paddle.top +=3
#                 elif event.key == pygame.K_w:
#                     left_paddle.top -=3
#                 elif event.key == pygame.K_s:
#                     left_paddle.top +=3

#         if right_paddle.top < 0:
#             right_paddle.top = 0
#         elif right_paddle.bottom > SCREEN_HEIGHT:
#             right_paddle.bottom = SCREEN_HEIGHT
            
#         if left_paddle.top < 0:
#                 left_paddle.top = 0
#         elif left_paddle.bottom > SCREEN_HEIGHT:
#             left_paddle.bottom = SCREEN_HEIGHT

#         if ball.bottom>SCREEN_HEIGHT:
#             ball_y *= -1
#         elif ball.top <= 0 :
#             ball_y *= -1

#         if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
#             ball_x *= -1
#         elif ball.left > SCREEN_WIDTH:
#             ball.centerx = SCREEN_WIDTH//2
#             ball.centery = SCREEN_HEIGHT//2
#             rscore +=1
#         elif ball.left<=0:
#             ball.centerx = SCREEN_WIDTH//2
#             ball.centery = SCREEN_HEIGHT//2
#             lscore +=1
        
#         ball.left +=ball_x
#         ball.top  +=ball_y

#         print('ball_x :{0}, ball_y :{1}, r_score:{2}, l_score{3}'.format(ball_x, ball_y, rscore, lscore))
#         # if left_paddle.colliderect(ball) or left_paddle.colliderect(ball):
#         #     ball_x *= -1

#         r_score_image = score_font.render('SCORE : {}'.format(rscore), True, (0,255,0))
#         l_score_image = score_font.render('SCORE : {}'.format(lscore), True, (0,255,0))
#         ball_speed = score_font.render('ball_speed : {}'.format(abs(ball_x)), True, (0,255,0))

#         screen.blit(r_score_image, (10, 10))
#         screen.blit(l_score_image, (600, 10))
#         screen.blit(ball_speed, (SCREEN_WIDTH//2 - 100, 10))
#         pygame.draw.circle(screen,WHITE, (ball.centerx, ball.centery), ball.width//2 )
#         pygame.draw.rect(screen,RED ,left_paddle)
#         pygame.draw.rect(screen,RED, right_paddle)

#         pygame.display.update()
#         clock.tick(30)

#     pygame.quit()


import pygame
import random
import os
import time
import sys

def pingpong_game():
    #화면 크기
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    #초기화
    pygame.init()

    clock = pygame.time.Clock()

    current_path = os.path.dirname(__file__)  # 현재 파일 위치 반환
    image_path = os.path.join(current_path, "images")  # current_path 밑의 image 디렉토리

    # start_image = pygame.image.load(os.path.join(image_path, 'start.png'))
    # start = start_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT//2)

    end_image = pygame.image.load(os.path.join(image_path, 'end.png'))
    end = end_image.get_rect(centerx=SCREEN_WIDTH // 2, bottom=SCREEN_HEIGHT)

    mpos = pygame.mouse.get_pos()
    mpress = pygame.mouse.get_pressed()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #패들 좌표,사이즈 설정
    left_paddle = pygame.Rect(0, SCREEN_HEIGHT//2 - 80//2, 16, 80)
    right_paddle = pygame.Rect(SCREEN_WIDTH-16, SCREEN_HEIGHT//2 - 80//2, 16, 80)

    #공 만들기
    ball = pygame.Rect(SCREEN_WIDTH//2-16//2,SCREEN_HEIGHT//2-16//2,16,16)

    #공의 이동 변수
    ball_x = 5
    ball_y = 5

    #색
    BLACK = (0,0,0)
    RED = (255,0,0)
    WHITE = (255,255,255)

    #폰트 설정
    score_font = pygame.font.SysFont('calisto',30, False, False)

    #
    rscore = 0
    lscore = 0

    #게임 종료
    game_over = False

    pygame.key.set_repeat(1,10)

    flag = True
    r_flag_num = 0
    l_flag_num = 0

    start_image = pygame.image.load(os.path.join(image_path, 'start.png'))
    start = start_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT//2)

    def start_game():
        screen.blit(start_image, start)
        pygame.display.update()
        #마우스 클리 이벤트 처리
        running = True
        while running:
            event = pygame.event.poll()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos[0], event.pos[1])
                if start.collidepoint(event.pos):
                    print('start')
                    running = False

    start_game()

    while True:
        screen.fill(BLACK)
    
        if game_over == True:
            break

        #이벤트 처리
        #event = pygame.event.poll() #이벤트 처리
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos[0], event.pos[1])
            if end.collidepoint(event.pos):
                print('end')
                break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    right_paddle.top -=3
                elif event.key == pygame.K_DOWN:
                    right_paddle.top +=3
                elif event.key == pygame.K_w:
                    left_paddle.top -=3
                elif event.key == pygame.K_s:
                    left_paddle.top +=3

        if right_paddle.top < 0:
            right_paddle.top = 0
        elif right_paddle.bottom > SCREEN_HEIGHT:
            right_paddle.bottom = SCREEN_HEIGHT
        
        if left_paddle.top < 0:
                left_paddle.top = 0
        elif left_paddle.bottom > SCREEN_HEIGHT:
            left_paddle.bottom = SCREEN_HEIGHT

        if ball.bottom>SCREEN_HEIGHT:
            ball_y *= -1
        elif ball.top <= 0 :
            ball_y *= -1

        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            ball_x *= -1
        elif ball.left > SCREEN_WIDTH:
            ball.centerx = SCREEN_WIDTH//2
            ball.centery = SCREEN_HEIGHT//2
            rscore +=1
        elif ball.left<=0:
            ball.centerx = SCREEN_WIDTH//2
            ball.centery = SCREEN_HEIGHT//2
            lscore +=1

        if rscore > lscore and rscore%5 == 0 and flag == True:
            r_flag_num = rscore
            flag=False
            if ball_x <= 0 and ball_y <= 0:
                ball_x -=2
                ball_y -=2
            elif ball_x <= 0 and ball_y > 0:
                ball_x -=2
                ball_y +=2
            elif ball_x > 0 and ball_y <= 0:
                ball_x +=2
                ball_y -=2
            else:
                ball_x +=2
                ball_y +=2            
        elif lscore > rscore and lscore%5 == 0 and flag == True:
            l_flag_num = lscore
            flag=False
            if ball_x <= 0 and ball_y <= 0:
                ball_x -=2
                ball_y -=2
            elif ball_x <= 0 and ball_y > 0:
                ball_x -=2
                ball_y +=2
            elif ball_x > 0 and ball_y <= 0:
                ball_x +=2
                ball_y -=2
            else:
                ball_x +=2
                ball_y +=2

        if r_flag_num +5 == rscore:
            flag = True
        elif l_flag_num +5 == lscore:
            flag = True


        ball.left +=ball_x
        ball.top  +=ball_y

        print('-'*50)
        print('ball_x :{0}, ball_y :{1}, r_score:{2}, l_score{3}'.format(ball_x, ball_y, rscore, lscore))
        print('r_flag_num :{0}, l_flag_num :{1}, flag:{2}'.format(r_flag_num, l_flag_num, flag))
        # if left_paddle.colliderect(ball) or left_paddle.colliderect(ball):
        #     ball_x *= -1

        r_score_image = score_font.render('SCORE : {}'.format(rscore), True, (0,255,0))
        l_score_image = score_font.render('SCORE : {}'.format(lscore), True, (0,255,0))
        ball_speed = score_font.render('ball_speed : {}'.format(abs(ball_x)), True, (0,255,0))

        screen.blit(end_image, end)
        screen.blit(r_score_image, (10, 10))
        screen.blit(l_score_image, (600, 10))
        screen.blit(ball_speed, (SCREEN_WIDTH//2 - 100, 10))
        pygame.draw.circle(screen,WHITE, (ball.centerx, ball.centery), ball.width//2 )
        pygame.draw.rect(screen,RED ,left_paddle)
        pygame.draw.rect(screen,RED, right_paddle)

        pygame.display.update()
        clock.tick(30)

pygame.quit()
sys.exit()
