import pygame
import time
pygame.mixer.init()
pygame.mixer.music.load('Avivamento - Adoração Central.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue