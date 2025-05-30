import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

import time

def play_song(filepath):
    pygame.mixer.init()
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()
    print(f"Playing: {filepath}")
    while pygame.mixer.music.get_busy():
        time.sleep(1)
