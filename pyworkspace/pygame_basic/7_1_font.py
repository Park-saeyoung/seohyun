from multiprocessing.connection import wait
import time
import pygame
import os

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Font")

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)

background = pygame.image.load(os.path.join(current_path, "background.png"))


pygame.font.init()        

# 파이썬 시스템 글꼴 출력
# print(pygame.font.get_fonts())

#폰트 설정, 사용자 폰트, 폰트 파일이 폴더에 있어야 함.
# font = pygame.font.Font('LexiGulim.ttf',30)

# 시스템에 등록되어 있는 글꼴 이름을 사용
# ("글꼴", 크기, 굵기여부, 기울기)
font = pygame.font.SysFont("arial",30, True, True)

# 출력할 텍스트,  안티앨리어싱의 사용여부, 글자색 
#텍스트가 표시된 Surface 를 만듬 
#출력할 글자, True, 글자색 (텍스트, antialias, 색(튜플), 텍스트 배경색(튜플))
#antialias : 높은 해상도의 신호를 낮은 해상도에서 나타낼 때 생기는 계단 현상을 최소화
text = font.render("Hello Arial",True,(0,255,0))  

# text 라는 surface 를 blit 로 일반 이미지처럼 출력
# background.blit(text,(150,50))        


screen.blit(text, (150,150))
clock.tick(30)
pygame.display.update()
time.sleep(3)
            


