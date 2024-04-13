import pygame
from title import *
import asyncio

pygame.init()

width = 1280
height = 720
display = pygame.display.set_mode((width, height))
bg = pygame.transform.scale(pygame.image.load("rensrandomrooms/1bg.png"),(width, height))
bg2 = pygame.transform.scale(pygame.image.load("rensrandomrooms/Screenshot 2024-03-16 115217.png"),(width, height))
poster1 = pygame.transform.scale(pygame.image.load("rensrandomrooms/doodle1-removebg-preview.png"),(500, 520))
user = pygame.transform.scale(pygame.image.load("rensrandomrooms/bruh (2).png"),(500, 500))
caclu = pygame.transform.scale(pygame.image.load("rensrandomrooms/caclu-removebg-preview.png"),(300, 300))
exit = pygame.transform.scale(pygame.image.load("rensrandomrooms/image_2024-03-09_115057502-removebg-preview.png"),(100, 100))
bomb = pygame.transform.scale(pygame.image.load("rensrandomrooms/tnt.png"),(300, 300))
bombhitbox = pygame.Rect(1000,500,300,300)
title3 = False
title_music = pygame.mixer.Sound("rensrandomrooms/rensroomsopeingtheme.ogg")
openCalcu = False
poster_open = False
caclhold = False
windowsdialup = pygame.mixer.Sound("rensrandomrooms/dial-up-modem-01.wav")

def update_display():
    global title3, openCalcu, poster1
    if title3 is True:

        display.blit(bg, (0, 0))
        display.blit(user,(550,200))
        rectposter = pygame.Rect(150,50,500,200)#todo change values here
      
        display.blit(poster1, (150, 50))
        if not openCalcu:
            display.blit(caclu, (60,500))
            display.blit(bomb, (1000, 500))
        calcu_rect = pygame.Rect(60, 500, 300, 300)
        if calcu_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            openCalcu = True
        if openCalcu:
            global caclhold, poster_open
            exitrect = pygame.Rect(300,200, 80,80)
            #pygame.draw.rect(display,(255,0,0),exitrect)
            display.blit(bg2, (0, 0))
            display.blit(exit, (300, 190))

            display.blit(pygame.transform.scale(pygame.image.load("rensrandomrooms/caclu2-removebg-preview.png"),(600,500)), (300, 230))
            cacluno = pygame.Rect(300, 230,600,500)
            if exitrect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                caclhold = False
                openCalcu = False
            if cacluno.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:

                caclhold = True
            if caclhold:
                display.blit(pygame.transform.scale(pygame.image.load("rensrandomrooms/cualcurnoman-removebg-preview.png"),
                                                    (830, 650)), (200, 90))

        if rectposter.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            poster_open = not poster_open

        if bombhitbox.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            display.blit(pygame.transform.scale(pygame.image.load("rensrandomrooms/done.png"),(1280,720)),(0,0))
            pygame.display.update()
            pygame.time.wait(5000)
            pygame.quit()

        if poster_open:
            display.blit(pygame.transform.scale(pygame.image.load("rensrandomrooms/lol.png"), (1280, 720)), (0, 0))
    else:
        load_title_screen(display)
        if pygame.mouse.get_pressed()[0]:
            title3 = True








async def main():
    run = True
    title_music.play()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit
                quit()
        update_display()
        pygame.display.update()


asyncio.run(main())




















