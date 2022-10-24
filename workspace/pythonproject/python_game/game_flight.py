import pygame
import random

pygame.init()

screen_width = 400
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load("D:\\workspace\\python\\workspace\\pythonproject\\python_game\\image\\background.png")

character = pygame.image.load("D:\\workspace\\python\\workspace\\pythonproject\\python_game\\image\\character.png")

enemy = pygame.image.load("D:\\workspace\\python\\workspace\\pythonproject\\python_game\\image\\enemy.png")

enemy2 = pygame.image.load("D:\\workspace\\python\\workspace\\pythonproject\\python_game\\image\\enemy2.png")

item1 = pygame.image.load("D:\\workspace\\python\\workspace\\pythonproject\\python_game\\image\\item1.png")

item2 = pygame.image.load("D:\\workspace\\python\\workspace\\pythonproject\\python_game\\image\\item2.png")

character_size = character.get_rect().size
enemy_size = enemy.get_rect().size
enemy2_size = enemy2.get_rect().size
item1_size = item1.get_rect().size
item2_size = item2.get_rect().size

character_width = character_size[0]
character_height = character_size[1]

enemy_width = enemy_size[0]
enemy_height = enemy_size[1]

enemy2_width = enemy2_size[0]
enemy2_height = enemy2_size[1]

item1_width = item1_size[0]
item1_height = item1_size[1]

item2_width = item2_size[0]
item2_height = item2_size[1]

character_x_pos = 0
character_y_pos = 0

character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height  - character_height

enemy_x_pos = screen_width / 2 - enemy_width / 2
enemy_y_pos = screen_height / 2 - enemy_height / 2

enemy2_x_pos = 100
enemy2_y_pos = 100

item1_x_pos = 300
item1_y_pos = 70

item2_x_pos = 300
item2_y_pos = 370

pygame.display.set_caption("GAME_FLIGHT")

#clock = pygame.time.Clock()

char_speed = 2

running = True
to_x = 0
to_y =0

start_ticks = pygame.time.get_ticks()

game_font = pygame.font.Font(None, 40)

sco = 50

character_sz = 0

iscore = 1

col = False

while running:
    #dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x += char_speed
            elif event.key == pygame.K_LEFT:
                to_x -= char_speed
            elif event.key == pygame.K_UP:
                to_y -= char_speed
            elif event.key == pygame.K_DOWN:
                to_y += char_speed
            elif event.key == pygame.K_SPACE:
                character_sz = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    if col == True and a == 1:
        if character_x_pos > enemy_x_pos:
            character_x_pos += 2
        else:
            character_x_pos -= 2
        if character_y_pos > enemy_y_pos:
            character_y_pos += 2
        else:
            character_y_pos -= 2
    else:
        character_x_pos += to_x
        character_y_pos += to_y
    
    if col == True and a == 2:
        if character_x_pos > enemy2_x_pos:
            character_x_pos += 2
        else:
            character_x_pos -= 2
        if character_y_pos > enemy2_y_pos:
            character_y_pos += 2
        else:
            character_y_pos -= 2
    else:
        character_x_pos += to_x
        character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height-character_height:
        character_y_pos = screen_height-character_height

    if character_sz == 1:
        character = pygame.image.load("D:\\workspace\\python\\workspace\\pythonproject\\python_game\\image\\spacecha.png")

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect1 = enemy.get_rect()
    enemy_rect1.top = enemy_y_pos
    enemy_rect1.left = enemy_x_pos

    enemy2_rect1 = enemy2.get_rect()
    enemy2_rect1.top = 100
    enemy2_rect1.left = 100

    enemy_rect2 = enemy.get_rect()
    enemy_rect2.top = 0
    enemy_rect2.left = 0

    enemy_rect3 = enemy.get_rect()
    enemy_rect3.top = 100
    enemy_rect3.left = 100

    enemy_rect4 = enemy.get_rect()
    enemy_rect4.top = 300
    enemy_rect4.left = 350

    enemy_rect5 = enemy.get_rect()
    enemy_rect5.top = 300
    enemy_rect5.left = 550

    item1_rect = item1.get_rect()
    item1_rect.top = item1_y_pos
    item1_rect.left = item1_x_pos

    item2_rect = item2.get_rect()
    item2_rect.top = item2_y_pos
    item2_rect.left = item2_x_pos



    if(character_rect.colliderect(enemy_rect1)):
        col = True
        a = 1
        print("충돌하였음!!!!")
    elif(character_rect.colliderect(enemy2_rect1)):
        col = True
        a = 2
        print("충돌하였음!!!")      
    else:
        col = False
        print("순항중")

    if col == True:
        sco -= 1

    if sco < 0:
        pygame.quit()

    if iscore == 1:
        if(character_rect.colliderect(item1_rect)):
            iscore += 1
            sco +=10
            print("아이템획득")
            item1 = pygame.image.load("D:\\workspace\\python\\workspace\\pythonproject\\python_game\\image\\item1false.png")

    if(character_rect.colliderect(item2_rect)):
        sco += 3
        print("아이템획득")
        item2_x_pos = random.randrange(0, 350)
        item2_y_pos = random.randrange(0, 600)
        item2_rect.top = item2_y_pos
        item2_rect.left = item2_x_pos
        while (item2_rect.colliderect(enemy_rect1) or item2_rect.colliderect(enemy2_rect1)):
            item2_x_pos = random.randrange(0, 350)
            item2_y_pos = random.randrange(0, 600)
            item2_rect.top = item2_y_pos
            item2_rect.left = item2_x_pos



    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = game_font.render(str(int(elapsed_time)),True,(255,255,255))

    score = game_font.render(str(int(sco)),True,(255,255,255))

    if elapsed_time >= 30:
        pygame.quit()

    screen.blit(background,(0,0))
    screen.blit(enemy,(enemy_x_pos, enemy_y_pos))
    screen.blit(enemy2,(enemy2_x_pos, enemy2_y_pos))
    screen.blit(timer,(10, 10))
    screen.blit(score,(360, 10))
    screen.blit(item1,(300, 70))
    screen.blit(item2,(item2_x_pos, item2_y_pos))
    # screen.blit(enemy,(300, 550))
    # screen.blit(enemy,(enemy_x_pos+50, enemy_y_pos +100))
    screen.blit(character,(character_x_pos, character_y_pos))
    pygame.display.update()

pygame.quit()