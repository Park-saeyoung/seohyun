# import pygame
# import os
# import random

# pygame.init()

# pygame.mixer.init()

# SCREEN_WIDTH = 400
# SCREEN_HEIGHT = 640

# #화면 크기 설정
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# #시간(프레임,딜레이)
# clock = pygame.time.Clock()

# #폰트 설정
# score_font = pygame.font.SysFont('calisto', 40,False,False)

# #변수설정
# score = 100
# current_path = os.path.dirname(__file__) #현재 경로 반환 C:\Users\user\PycharmProjects\pythonProject\python_game\
# image_path = os.path.join(current_path, "images")
# sound_path = os.path.join(current_path,"sounds")


# pygame.mixer.music.load(os.path.join(sound_path,'bgm3.mp3'))
# pygame.mixer.music.play(0) #옵션 : -1:무한 반복, 0:한번


# background_image = pygame.image.load(os.path.join(image_path, "background.png"))
# rock_image = pygame.image.load(os.path.join(image_path, "rock.png"))
# fighter_image = pygame.image.load(os.path.join(image_path, "fighter.png"))
# missile_image = pygame.image.load(os.path.join(image_path, "missile.png"))
# explosion_image = pygame.image.load(os.path.join(image_path, "explosion.png"))



# missiles = []

# missile_sound = pygame.mixer.Sound(os.path.join(sound_path,'missile.mp3'))

# fighter = fighter_image.get_rect(centerx=SCREEN_WIDTH//2, bottom=SCREEN_HEIGHT)

# rocks = []

# for i in range(3):
#     # rand_k = random.randrange(1, 2)
#     rock = rock_image.get_rect(left=(i+1)*100, top=0)
#     rocks.append(rock)

# while True:
#     screen.blit(background_image,(0,0))

#     event = pygame.event.poll() #이벤트 처리
#     if event.type == pygame.QUIT:
#         break
#     elif event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_SPACE:
#             missile = pygame.Rect(missile_image.get_rect(centerx=fighter.centerx, top=fighter.top))
#             missiles.append(missile)
#             missile_sound.play()
#     pressed = pygame.key.get_pressed()
#     if pressed[pygame.K_LEFT]:
#         fighter.left -= 5
#     elif pressed[pygame.K_RIGHT]:
#         fighter.left +=5

#     if fighter.left < 0:
#         fighter.left = 0
#     if fighter.right > SCREEN_WIDTH:
#         fighter.right = SCREEN_WIDTH

#     for rock in rocks:
#         rock.top += 2
#         if rock.top > 600:
#             rock.top = 0
#             rand_k = random.randrange(30,50)
#             rock.left +=rand_k
#             if rock.right>SCREEN_WIDTH:
#                 rock.left=0

#     for missile in missiles:
#         missile.top -= 5
#         if missile.top < 0:
#             missiles.remove(missile)

#     screen.blit(fighter_image, fighter)

#     for rock in rocks:
#         if rock.colliderect(fighter):
#             pygame.quit()
#         screen.blit(rock_image, rock)
#         for missile in missiles:
#             if missile.colliderect(rock):
#                 rocks.remove(rock)
#                 missiles.remove(missile)
#                 screen.blit(explosion_image, rock)
#                 rock = rock_image.get_rect(left=random.randrange(0,350), top=0)
#                 rocks.append(rock)



#     for missile in missiles:
#         screen.blit(missile_image, missile)

#     score_image = score_font.render('Score : {0}'.format(score),True, (255,0,0), (0,0,0))

#     screen.blit(score_image, (10,10))
#     pygame.display.update()
#     clock.tick(50)

# pygame.quit()


import pygame
import os
import random
import sys


def rock():
    pygame.init()

    pygame.mixer.init()

    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 640

    #화면 크기 설정
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #시간(프레임,딜레이)
    clock = pygame.time.Clock()

    #폰트 설정
    score_font = pygame.font.SysFont('calisto', 40,False,False)

    #변수설정
    score = 100
    current_path = os.path.dirname(__file__) #현재 경로 반환 C:\Users\user\PycharmProjects\pythonProject\python_game\
    image_path = os.path.join(current_path, "images")
    sound_path = os.path.join(current_path,"sounds")


    pygame.mixer.music.load(os.path.join(sound_path,'bgm3.mp3'))
    pygame.mixer.music.play(0) #옵션 : -1:무한 반복, 0:한번


    background_image = pygame.image.load(os.path.join(image_path, "background.png"))
    rock_image = pygame.image.load(os.path.join(image_path, "rock.png"))
    fighter_image = pygame.image.load(os.path.join(image_path, "fighter.png"))
    missile_image = pygame.image.load(os.path.join(image_path, "missile.png"))
    explosion_image = pygame.image.load(os.path.join(image_path, "explosion.png"))



    missiles = []

    missile_sound = pygame.mixer.Sound(os.path.join(sound_path,'missile.mp3'))

    fighter = fighter_image.get_rect(centerx=SCREEN_WIDTH//2, bottom=SCREEN_HEIGHT)

    rocks = []

    for i in range(3):
        rand_k = random.randrange(1, 2)
        rock = rock_image.get_rect(left=(i+1)*100, top=0)
        rocks.append(rock)

    running = True

    while running:
        screen.blit(background_image,(0,0))

        event = pygame.event.poll() #이벤트 처리
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                missile = pygame.Rect(missile_image.get_rect(centerx=fighter.centerx, top=fighter.top))
                missiles.append(missile)
                missile_sound.play()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            fighter.left -= 5
        elif pressed[pygame.K_RIGHT]:
            fighter.left +=5

        if fighter.left < 0:
            fighter.left = 0
        if fighter.right > SCREEN_WIDTH:
            fighter.right = SCREEN_WIDTH

        for rock in rocks:
            rock.top += 2
            if rock.top > 600:
                rock.top = 0
                rand_k = random.randrange(30,50)
                rock.left +=rand_k
                if rock.right>SCREEN_WIDTH:
                    rock.left=0

        for missile in missiles:
            missile.top -= 5
            if missile.top < 0:
                missiles.remove(missile)

        screen.blit(fighter_image, fighter)

        for rock in rocks:
            if rock.colliderect(fighter):
                # pygame.quit()
                running = False
                break
            screen.blit(rock_image, rock)
            for missile in missiles:
                if missile.colliderect(rock):
                    rocks.remove(rock)
                    missiles.remove(missile)
                    screen.blit(explosion_image, rock)
                    rock = rock_image.get_rect(left=random.randrange(0,350), top=0)
                    rocks.append(rock)



        for missile in missiles:
            screen.blit(missile_image, missile)

        score_image = score_font.render('Score : {0}'.format(score),True, (255,0,0), (0,0,0))

        screen.blit(score_image, (10,10))
        pygame.display.update()
        clock.tick(50)

    # pygame.quit()
    # sys.exit()
    return 0

rock()
