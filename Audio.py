import pygame
import random
from AudioFiles import *


def music_loop():
    pygame.mixer_music.load()
    pygame.mixer_music.play(-1)
'''
def pause():
    pygame.mixer_music.pause()
    pause_text = pygame.font.SysFont('Helvetica', 24)
    TextSurf, TextRect =

def unpause():
    global pause()
    pygame.mixer_music.unpause()
    pause = False ?????
'''


def sword_swing():
    pygame.mixer_music.pause()
    pygame.mixer_music.play(AudioDict['sword_swing_sound'])
    pygame.mixer_music.unpause()


def switch_lanes_sound():
    pygame.mixer_music.pause()
    pygame.mixer_music.play(AudioDict['switch_lanes_sound'])
    pygame.mixer_music.unpause()


def open_menu_sound():
    pygame.mixer_music.pause()
    pygame.mixer_music.play(AudioDict['open_menu_sound'])
    pygame.mixer_music.unpause()


def close_menu_sound():
    pygame.mixer_music.pause()
    pygame.mixer_music.play(AudioDict['close_menu_sound'])
    pygame.mixer_music.unpause()


def press_button_sound():
    pygame.mixer_music.pause()
    pygame.mixer_music.play(AudioDict['press_button_sound'])
    pygame.mixer_music.unpause()


def damaging_enemy():
    pygame.mixer_music.pause()
    pygame.mixer_music.play(AudioDict['damaging_enemy_sounds']
                                     [random.randint(0,1)])
    pygame.mixer_music.unpause()


def killing_enemy():
    pygame.mixer_music.pause()
    pygame.mixer_music.play(AudioDict['killing_enemy_sounds']
                                     [random.randint(0, 1)])
    pygame.mixer_music.unpause()


def enemy_idle_sound():
    pygame.mixer_music.pause()
    pygame.mixer_music.play(AudioDict['enemy_idle_sound']
                                     [random.randint(0, 1)])
    pygame.mixer_music.unpause()



