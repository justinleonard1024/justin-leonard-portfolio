"""
Unreal Ping Pong
game_main.py
Created by Justin Leonard
"""

#initialize
import pygame
import random
from game_globals import *
from game_functions import *

def game_mainmenu(core_game, core_entities, core_ui, core_sound):
    """The main menu

    Buttons for the main menu along with the
    display are executed here
    """

    #time
    core_game[ALL_MAIN_ALL][MAIN_MENU_CONTROL] = True
    
    #loop
    while core_game[ALL_MAIN_ALL][MAIN_MENU_CONTROL]:
        
        core_entities[ALL_ENTITY_CLOCK].tick(core_game[ALL_MAIN_GAME][GAME_SECOND])

        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                core_game[ALL_MAIN_ALL][MAIN_MENU_CONTROL] = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mainmenu_event_button_down(core_game,core_entities,core_ui,core_sound)
                        
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mainmenu_event_button_up(core_game,core_entities,core_ui,core_sound)

        #display
        if core_game[ALL_MAIN_ALL][MAIN_MENU_CONTROL]:
            mainmenu_event_display(core_game,core_entities,core_ui,core_sound)

        pygame.display.flip()
