import pygame, time
pygame.init()
pygame.mixer.music.load('Avivamento - Adoração Central.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    time.sleep(0.1)