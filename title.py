import pygame
title2 = pygame.image.load("rensrandomrooms/titlecardfun.png")
title2=pygame.transform.scale(title2,(1280,700))

def load_title_screen(window):
    window.blit(title2,(0,0))
