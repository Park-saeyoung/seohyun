import os
import random

import pygame


def rockfall():

    pygame.init()

    pygame.mixer.init()

    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 640
    #화면 크기
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #시간 ( 프레임 ,딜레이 )
    clock = pygame.time.Clock()

    score_font = pygame.font.SysFont('inkfree', 25)
    life_font = pygame.font.SysFont('inkfree', 25)
    fallrock_font = pygame.font.SysFont('inkfree', 25)
    #변수 설정

    score = 0

    fallrockpoint = 0

    misspoint = 0 

    lifesco = 5

    rocksimg = []

    current_path = os.path.dirname(__file__)
    image_path = os.path.join(current_path, "images")
    sound_path = os.path.join(current_path, "sounds")
    #이미지 로드
    background_image = pygame.image.load(os.path.join(image_path, "background.png"))
    character_image = pygame.image.load(os.path.join(image_path, "character.png"))

    rock_image = pygame.image.load(os.path.join(image_path, "rock.png"))
    rock2_image = pygame.image.load(os.path.join(image_path, "rock2.png"))
    rock3_image = pygame.image.load(os.path.join(image_path, "rock3.png"))
    rocksimg.append(rock_image)
    rocksimg.append(rock2_image)
    rocksimg.append(rock3_image)
    bullet_image = pygame.image.load(os.path.join(image_path, "bullet.png"))
    explosion_image = pygame.image.load(os.path.join(image_path, "explosion.png"))
    explosion2_image = pygame.image.load(os.path.join(image_path, "explosion2.png"))

    bullets = []

    rockshot_sound = pygame.mixer.Sound(os.path.join(sound_path, "rockshot.wav"))

    bgm_sound = pygame.mixer.Sound(os.path.join(sound_path, "bgm.mp3"))
    bgm_sound.play(-1)

    bullet_sound = pygame.mixer.Sound(os.path.join(sound_path, "bullet.mp3"))

    #캐릭터 시작 위치
    character = character_image.get_rect(centerx=SCREEN_WIDTH/2, bottom=SCREEN_HEIGHT) 

    rocks = []

    game_over = False
    #돌 안겹치게 여러개 생성
    for i in range(3):
    #    rock = rock_image.get_rect(left=random.randrange(0, 350), top=0)
        rock = rock_image.get_rect(left=(i+1)*100, top=0)
        rocks.append(rock)

    while True:
        screen.blit(background_image,(0,0))
        if game_over == True:
            break

        event = pygame.event.poll()#이벤트 처리
        if event.type == pygame.QUIT:
                break
        #총알 쏠수 있게
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(bullet_image.get_rect(centerx=character.centerx, top=character.top))
                bullets.append(bullet)
                bullet_sound.play()
            elif event.key == pygame.K_ESCAPE:
                game_over = True
                break
        #비행기 방향키로 움직이게
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            character.left -= 9
        elif pressed[pygame.K_RIGHT]:
            character.left += 9
        #캐릭터 맵 이탈 방지
        if character.left < 0:   
            character.left = 0
        if character.right > SCREEN_WIDTH:
            character.right = SCREEN_WIDTH

        for bullet in bullets:
            bullet.top -= 15
            if bullet.top < 0:
                bullets.remove(bullet)
                score -=5
                misspoint += 1

        #돌 떨어지게 
        for rock in rocks:
            rock.top += random.randint(1,10)
            if score >= 100:
                rock.top += 3
            if score >= 200:
                rock.top += 3
            if score >= 300:
                rock.top += 4
            if score >= 400:
                rock.top += 5
            if score >= 500:
                rock.top += 7
            if rock.top > 640:
                rock.top = 0
                rock.left = random.randrange(0, 350)
                fallrockpoint += 1
                score -= 20

        #화면에 이미지 입력
        for bullet in bullets:
            screen.blit(bullet_image, bullet)

        for rock in rocks:
            screen.blit(rock2_image, rock)
            if rock.colliderect(character):
                rocks.remove(rock)
                lifesco -= 1
                rock = rock_image.get_rect(left=random.randrange(0,350), top = 0)
                rocks.append(rock)
                if lifesco == 0:
                    pygame.quit()
            for bullet in bullets:
                if bullet.colliderect(rock):
                    rocks.remove(rock)
                    bullets.remove(bullet)
                    score += 10
                    rockshot_sound.play()
                    screen.blit(explosion_image, rock)
                    screen.blit(explosion2_image, rock)
                    rock = rock_image.get_rect(left=random.randrange(0,350), top = 0)
                    rocks.append(rock)
        
        score_image = score_font.render('Score : {0}'.format(score),True, (255,255,255))
        fallrock_image = fallrock_font.render('miss : {0}'.format(fallrockpoint),True, (255,255,255))
        life_image = life_font.render('Life : {0}'.format(lifesco),True, (255,255,255))

        screen.blit(score_image, (10,10))
        screen.blit(fallrock_image, (10,50))
        screen.blit(life_image, (10,90))
        #screen.blit(life_image, (10,50))
        screen.blit(character_image, character)
        pygame.display.update()
        clock.tick(30)
    
    pygame.quit()
    return score
