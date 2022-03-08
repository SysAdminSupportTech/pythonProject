from pygame import mixer
import os
import pygame
pygame.init()
mixer.init()
mixer.music.load(r'C:\Users\DeptAdmin\Music\EAPlayer\pkon_E_018.mp3')
mixer.music.play()
while mixer.music.get_busy():
    pygame.time.Clock().tick(10)

