import pygame
pygame.mixer.init()
pygame.mixer.music.load('exx021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()