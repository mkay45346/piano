import pygame
from pygame import Vector2
import sys
pygame.init()
width = 1500
height = 500
key_size = 100
blackkey_size = 40
fps = 60
screen = pygame.display.set_mode((width, height))
name = pygame.display.set_caption("piano")
timer = pygame.time.Clock()
mpos = pygame.mouse.get_pos()
pressed_white = None
class White:
    def __init__(self):
        self.keys = [Vector2(x, 0) for x in range(15)]
    def draw(self):
        for i, key in enumerate(self.keys):
            if i == pressed_white:
                color = 'GRAY'
            else:
                color = 'WHITE'
            segment_rect = (key.x * key_size, 0, key_size - 5, height)
            pygame.draw.rect(screen,color , segment_rect)
    def press(self):
        pass

class Black:
    def __init__(self):
        self.keys = [Vector2(x, 0) for x in range(15) if x not in (0, 3, 7, 10)]
    def draw(self):

        for key in self.keys:
            segment_rect = (key.x * key_size - 20, 0, blackkey_size, height//2)

            pygame.draw.rect(screen,'BLACK', segment_rect)
    def press(self):
        pass

cthree = pygame.mixer.Sound("mp3 Notes/c-3.mp3")
dthree = pygame.mixer.Sound("mp3 Notes/d-3.mp3")
ethree = pygame.mixer.Sound("mp3 Notes/e3.mp3")
fthree = pygame.mixer.Sound("mp3 Notes/f-3.mp3")
gthree = pygame.mixer.Sound("mp3 Notes/g-3.mp3")
afour = pygame.mixer.Sound("mp3 Notes/a-4.mp3")
bfour = pygame.mixer.Sound("mp3 Notes/b4.mp3")
cfour = pygame.mixer.Sound("mp3 Notes/c-4.mp3")
dfour = pygame.mixer.Sound("mp3 Notes/d4.mp3")
efour = pygame.mixer.Sound("mp3 Notes/e4.mp3")
ffour = pygame.mixer.Sound("mp3 Notes/f-4.mp3")
gfour = pygame.mixer.Sound("mp3 Notes/g-4.mp3")

white = White()
black = Black()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                cthree.play()
                pressed_white = 0
            if event.key == pygame.K_s:
                dthree.play()
                pressed_white = 1
            if event.key == pygame.K_d:
                ethree.play()
                pressed_white = 2
            if event.key == pygame.K_f:
                fthree.play()
                pressed_white = 3
            if event.key == pygame.K_g:
                gthree.play()
                pressed_white = 4
            if event.key == pygame.K_h:
                afour.play()
                pressed_white = 5
            if event.key == pygame.K_j:
                bfour.play()
                pressed_white = 6
            if event.key == pygame.K_k:
                cfour.play()
                pressed_white = 7
            if event.key == pygame.K_l:
                dfour.play()
                pressed_white = 8
            if event.key == pygame.K_SEMICOLON:
                efour.play()
                pressed_white = 9
            if event.key == pygame.K_QUOTE:
                ffour.play()
                pressed_white = 10
            if event.key == pygame.K_KP4:
                gfour.play()
                pressed_white = 11
        if event.type == pygame.KEYUP:
                pressed_white = None
    screen.fill("BLACK")
    white.draw()
    black.draw()
    pygame.display.update()
    timer.tick(fps)