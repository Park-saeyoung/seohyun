import sys
import pygame
import random

def pingpong_game():

    clock = pygame.time.Clock()

    #화면 크기
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    #초기화
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    button_image = pygame.image.load("D:\\workspace\\python\\workspace\\pythonproject\\python_game\\image\\playbutton.png")
    #button2_image = pygame.image.load("D:\\workspace\\pythonproject\\pingpong_game\\images\\stop.png")
    stop_image = pygame.image.load("D:\\workspace\\python\\workspace\\pythonproject\\python_game\\image\\stop.png")
    stop1 = stop_image.get_rect(centerx=SCREEN_WIDTH // 2, centery= 70)
    bgm_sound = pygame.mixer.Sound("D:\\workspace\\python\\workspace\\pythonproject\\python_game\\sounds\\bgm.mp3")


    #패들 좌표,사이즈 설정
    right_paddle = pygame.Rect(0, SCREEN_HEIGHT//2 - 80//2, 16, 80)
    left_paddle = pygame.Rect(SCREEN_WIDTH-16, SCREEN_HEIGHT//2 - 80//2, 16, 80)

    #공 만들기
    ball = pygame.Rect(SCREEN_WIDTH//2-16//2,SCREEN_HEIGHT//2-16//2,16,16)

    #공의 이동 변수
    ball_x = 6
    ball_y = -6

    score_font = pygame.font.SysFont('inkfree', 40)
    score1 = 0
    score2 = 0

    ball_speed = 0

    for i in range(1):
        button = button_image.get_rect(top=190,left=330)
        #button2 = button2_image.get_rect(left=random.randint(0, SCREEN_WIDTH-button2_image.get_width()),
                                    #top=random.randint(0, SCREEN_HEIGHT-button2_image.get_height()))

    #색
    BLACK = (0,0,0)
    RED = (255,0,0)
    WHITE = (255,255,255)
    BLUE = (0,0,255)
    PURPLE = (255,0,255)
    DSDF = (100,200,30)


    asdf = False


    #게임 종료
    game_over = False

    pygame.key.set_repeat(1,10)

    def start():
        screen.blit(button_image, button)
        pygame.display.update()
        start = True
        while start:
            event = pygame.event.poll()
            if event.type == pygame. MOUSEBUTTONDOWN:
                print(event.pos[0], event.pos[1])
                if button.collidepoint(event.pos):
                    print('start')
                    start = False

    def stop():
        #screen.blit(button2_image, button2)
        pygame.display.update()
        stop = True
        while stop:
            event = pygame.event.poll()
            if event.type == pygame. MOUSEBUTTONDOWN:
                print(event.pos[0], event.pos[1])
                #if button2.collidepoint(event.pos):
                    #print('end')
                    #asdf = True
                    #break
                    

    # start()

    while True:
        screen.fill(BLACK)
        screen.blit(stop_image, stop1)
        bgm_sound.play(-1)
        if game_over == True:
            break

        #이벤트 처리
        #event = pygame.event.poll() #이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    left_paddle.top -=3
                elif event.key == pygame.K_DOWN:
                    left_paddle.top +=3
                elif event.key == pygame.K_w:
                    right_paddle.top -=3
                elif event.key == pygame.K_s:
                    right_paddle.top +=3
                elif event.key == pygame.K_ESCAPE:
                    game_over = True
                    break
                    #stop()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos[0], event.pos[1])
            if stop1.collidepoint(event.pos):
                print('종료되었습니다')
                break
                

        if right_paddle.top < 0:
            right_paddle.top = 0
        elif right_paddle.bottom > SCREEN_HEIGHT:
            right_paddle.bottom = SCREEN_HEIGHT
            
        if left_paddle.top < 0:
                left_paddle.top = 0
        elif left_paddle.bottom > SCREEN_HEIGHT:
            left_paddle.bottom = SCREEN_HEIGHT

        ball.left +=ball_x
        ball.top  +=ball_y

        if ball.bottom>SCREEN_HEIGHT:
            ball_y *= -1
        elif ball.top <= 0 :
            ball_y *= -1
        
        if ball.right > SCREEN_WIDTH or ball.left<=0:
            ball.centerx = SCREEN_WIDTH//2
            ball.centery = SCREEN_HEIGHT//2


        if right_paddle.colliderect(ball) or left_paddle.colliderect(ball):
            ball_x *= -1

        if ball.right > SCREEN_WIDTH-5:
            score1 += 5
        if ball.left <= 5:
            score2 += 5

        if asdf == True:
            break
            


        pygame.draw.circle(screen, WHITE, (ball.centerx, ball.centery), ball.width//2 )
        pygame.draw.rect(screen,PURPLE ,right_paddle)
        pygame.draw.rect(screen,RED, left_paddle)

        score1_image = score_font.render('score : {0}'.format(score1),True, (255,0,255))
        score2_image = score_font.render('score : {0}'.format(score2),True, (255,0,0))

        screen.blit(score1_image, (120,0))
        screen.blit(score2_image, (550,0))

        pygame.display.update()
        clock.tick(30)

    # pygame.quit()

# pingpong_game()
    pygame.quit()
    # sys.exit()
    return score1