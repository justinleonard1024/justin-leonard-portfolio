"""
Unreal Ping Pong
game_execute.py
Created by Justin Leonard

All game functions are stored here as well as the main game execution
There are individual game functions based on the current screen size setting
"""

#initialize
import pygame
import random
from game_globals import *

#functions
def game_reset(lst_game, lst_entities, lst_ui, lst_sound):
    """Sets the entity properties on round end

    All entity positions are defaulted based
    on the current screen size setting
    """

    #player controls
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_UP] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_DOWN] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_TOP] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_BOTTOM] = False

    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_UP] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_DOWN] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_TOP] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_BOTTOM] = False

    #small screen
    if lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        lst_game[ALL_MAIN_LOC][LOC_PLAYER1_X] = 25
        lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] = SCREEN_MID_SMALL_Y - 50
        lst_game[ALL_MAIN_LOC][LOC_PLAYER2_X] = SCREEN_SIZE_SMALL_X - 50
        lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] = SCREEN_MID_SMALL_Y - 50

        #small ball
        if lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 0:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_SMALL_X - 12
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_SMALL_Y - 12
        
        #medium ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 1:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_SMALL_X - 17
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_SMALL_Y - 17
        
        #large ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 2:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_SMALL_X - 25
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_SMALL_Y - 25

    #medium screen    
    elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        lst_game[ALL_MAIN_LOC][LOC_PLAYER1_X] = 25
        lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] = SCREEN_MID_MEDIUM_Y - 50
        lst_game[ALL_MAIN_LOC][LOC_PLAYER2_X] = SCREEN_SIZE_MEDIUM_X - 50
        lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] = SCREEN_MID_MEDIUM_Y - 50

        #small ball
        if lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 0:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_MEDIUM_X - 12
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_MEDIUM_Y - 12
        
        #medium ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 1:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_MEDIUM_X - 17
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_MEDIUM_Y - 17
        
        #large ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 2:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_MEDIUM_X - 25
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_MEDIUM_Y - 25

    #large screen
    elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        lst_game[ALL_MAIN_LOC][LOC_PLAYER1_X] = 25
        lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] = SCREEN_MID_LARGE_Y - 50
        lst_game[ALL_MAIN_LOC][LOC_PLAYER2_X] = SCREEN_SIZE_LARGE_X - 50
        lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] = SCREEN_MID_LARGE_Y - 50

        #small ball
        if lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 0:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_LARGE_X - 12
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_LARGE_Y - 12
        
        #medium ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 1:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_LARGE_X - 17
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_LARGE_Y - 17
        
        #large ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 2:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_LARGE_X - 25
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_LARGE_Y - 25

def game_pause(lst_game, lst_entities, lst_ui, lst_sound):
    """This will execute every time the game is paused

    The pause title as well as the buttons will be drawn to the screen
    The game is paused and unpaused with the "`" key
    """

    #small screen
    if lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
            
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_SMALL], (0,0))
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_PAUSE][PAUSE_TITLE], (SCREEN_MID_SMALL_X - 100,100))
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_PAUSE][PAUSE_CONTINUE], (SCREEN_MID_SMALL_X - 100,200))
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_PAUSE][PAUSE_QUIT], (SCREEN_MID_SMALL_X - 50,300))

    #medium screen
    elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_MEDIUM], (0,0))
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_PAUSE][PAUSE_TITLE], (SCREEN_MID_MEDIUM_X - 100,150))
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_PAUSE][PAUSE_CONTINUE], (SCREEN_MID_MEDIUM_X - 100,250))
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_PAUSE][PAUSE_QUIT], (SCREEN_MID_MEDIUM_X - 50,350))

    #large screen
    elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_LARGE], (0,0))
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_PAUSE][PAUSE_TITLE], (SCREEN_MID_LARGE_X - 100,200))
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_PAUSE][PAUSE_CONTINUE], (SCREEN_MID_LARGE_X - 100,300))
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_PAUSE][PAUSE_QUIT], (SCREEN_MID_LARGE_X - 50,400))

    pygame.display.flip()

def game_setup(lst_game, lst_entities, lst_ui, lst_sound):
    """Initial game setup

    All variables, displays and entities are defaulted
    to their original state for a new game execution
    """

    #screen
    lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_SMALL].fill((255,255,255))
    lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_MEDIUM].fill((255,255,255))
    lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_LARGE].fill((255,255,255))

    #variables
    lst_game[ALL_MAIN_GAME][GAME_TIME] = 0
    lst_game[ALL_MAIN_GAME][GAME_TIME_FINAL] = 0
    lst_game[ALL_MAIN_GAME][GAME_ROUND] = 1
    lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL] = False
    lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL_RESET] = True

    lst_game[ALL_MAIN_CONTROL][CONTROL_LOOP] = True
    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_SCORE] = True
    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WIN] = True
    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WINNER] = True
    lst_game[ALL_MAIN_CONTROL][CONTROL_INITIAL] = True
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_UP] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_DOWN] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_TOP] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_BOTTOM] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_UP] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_DOWN] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_TOP] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_BOTTOM] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] = 0
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] = 0
    lst_game[ALL_MAIN_CONTROL][CONTROL_X] = random.choice(lst_game[ALL_MAIN_GAME][GAME_LST])
    lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = random.choice(lst_game[ALL_MAIN_GAME][GAME_LST])
    lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = True
    lst_game[ALL_MAIN_CONTROL][CONTROL_DIRECTION] = random.choice(lst_game[ALL_MAIN_GAME][GAME_LST])

    #slow speed
    if lst_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] == 0:
        lst_game[ALL_MAIN_GAME][GAME_SPEED] = 5
        lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER] = 5

    #medium speed
    elif lst_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] == 1:
        lst_game[ALL_MAIN_GAME][GAME_SPEED] = 6
        lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER] = 5

    #fast speed
    elif lst_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] == 2:
        lst_game[ALL_MAIN_GAME][GAME_SPEED] = 7
        lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER] = 5

    #sounds
    lst_sound[ALL_SOUND_MAINMENU].stop()
    lst_sound[ALL_SOUND_MAINMENU_OTHER].stop()

    #small screen
    if lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        lst_game[ALL_MAIN_LOC][LOC_PLAYER1_X] = 25
        lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] = SCREEN_MID_SMALL_Y - 50
        lst_game[ALL_MAIN_LOC][LOC_PLAYER2_X] = SCREEN_SIZE_SMALL_X - 50
        lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] = SCREEN_MID_SMALL_Y - 50

        #small ball
        if lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 0:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_SMALL_X - 12
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_SMALL_Y - 12
        
        #medium ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 1:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_SMALL_X - 17
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_SMALL_Y - 17
        
        #large ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 2:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_SMALL_X - 25
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_SMALL_Y - 25

    #medium screen    
    elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        lst_game[ALL_MAIN_LOC][LOC_PLAYER1_X] = 25
        lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] = SCREEN_MID_MEDIUM_Y - 50
        lst_game[ALL_MAIN_LOC][LOC_PLAYER2_X] = SCREEN_SIZE_MEDIUM_X - 50
        lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] = SCREEN_MID_MEDIUM_Y - 50

        #small ball
        if lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 0:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_MEDIUM_X - 12
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_MEDIUM_Y - 12
        
        #medium ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 1:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_MEDIUM_X - 17
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_MEDIUM_Y - 17
        
        #large ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 2:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_MEDIUM_X - 25
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_MEDIUM_Y - 25

    #large screen
    elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        lst_game[ALL_MAIN_LOC][LOC_PLAYER1_X] = 25
        lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] = SCREEN_MID_LARGE_Y - 50
        lst_game[ALL_MAIN_LOC][LOC_PLAYER2_X] = SCREEN_SIZE_LARGE_X - 50
        lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] = SCREEN_MID_LARGE_Y - 50

        #small ball
        if lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 0:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_LARGE_X - 12
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_LARGE_Y - 12
        
        #medium ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 1:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_LARGE_X - 17
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_LARGE_Y - 17
        
        #large ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 2:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_LARGE_X - 25
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_LARGE_Y - 25

def game_setup_final(lst_game, lst_entities, lst_ui, lst_sound):
    """Final game setup

    All variables, displays and entities are defaulted
    to their original state to clean up after the
    game execution

    The main menu is opened after this execution along with
    playing the main menu music if sound music is set to on
    """

    #screen
    lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_SMALL].fill((255,255,255))
    lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_MEDIUM].fill((255,255,255))
    lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_LARGE].fill((255,255,255))

    #variables
    lst_game[ALL_MAIN_GAME][GAME_TIME] = 0
    lst_game[ALL_MAIN_GAME][GAME_TIME_FINAL] = 0
    lst_game[ALL_MAIN_GAME][GAME_ROUND] = 1
    lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL] = False
    lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL_RESET] = True

    lst_game[ALL_MAIN_CONTROL][CONTROL_LOOP] = True
    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_SCORE] = True
    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WIN] = True
    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WINNER] = True
    lst_game[ALL_MAIN_CONTROL][CONTROL_INITIAL] = True
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_UP] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_DOWN] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_TOP] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_BOTTOM] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_UP] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_DOWN] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_TOP] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_BOTTOM] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] = 0
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] = 0
    lst_game[ALL_MAIN_CONTROL][CONTROL_X] = random.choice(lst_game[ALL_MAIN_GAME][GAME_LST])
    lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = random.choice(lst_game[ALL_MAIN_GAME][GAME_LST])
    lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = True
    lst_game[ALL_MAIN_CONTROL][CONTROL_DIRECTION] = random.choice(lst_game[ALL_MAIN_GAME][GAME_LST])

    #slow speed
    if lst_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] == 0:
        lst_game[ALL_MAIN_GAME][GAME_SPEED] = 5
        lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER] = 5

    #medium speed
    elif lst_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] == 1:
        lst_game[ALL_MAIN_GAME][GAME_SPEED] = 6
        lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER] = 5

    #fast speed
    elif lst_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] == 2:
        lst_game[ALL_MAIN_GAME][GAME_SPEED] = 7
        lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER] = 5

    #sounds
    if lst_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
        lst_sound[ALL_SOUND_MAINMENU].play()

    #small screen
    if lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        lst_game[ALL_MAIN_LOC][LOC_PLAYER1_X] = 25
        lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] = SCREEN_MID_SMALL_Y - 50
        lst_game[ALL_MAIN_LOC][LOC_PLAYER2_X] = SCREEN_SIZE_SMALL_X - 50
        lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] = SCREEN_MID_SMALL_Y - 50

        #small ball
        if lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 0:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_SMALL_X - 12
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_SMALL_Y - 12
        
        #medium ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 1:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_SMALL_X - 17
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_SMALL_Y - 17
        
        #large ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 2:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_SMALL_X - 25
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_SMALL_Y - 25

    #medium screen    
    elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        lst_game[ALL_MAIN_LOC][LOC_PLAYER1_X] = 25
        lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] = SCREEN_MID_MEDIUM_Y - 50
        lst_game[ALL_MAIN_LOC][LOC_PLAYER2_X] = SCREEN_SIZE_MEDIUM_X - 50
        lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] = SCREEN_MID_MEDIUM_Y - 50

        #small ball
        if lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 0:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_MEDIUM_X - 12
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_MEDIUM_Y - 12
        
        #medium ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 1:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_MEDIUM_X - 17
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_MEDIUM_Y - 17
        
        #large ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 2:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_MEDIUM_X - 25
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_MEDIUM_Y - 25

    #large screen
    elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        lst_game[ALL_MAIN_LOC][LOC_PLAYER1_X] = 25
        lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] = SCREEN_MID_LARGE_Y - 50
        lst_game[ALL_MAIN_LOC][LOC_PLAYER2_X] = SCREEN_SIZE_LARGE_X - 50
        lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] = SCREEN_MID_LARGE_Y - 50

        #small ball
        if lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 0:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_LARGE_X - 12
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_LARGE_Y - 12
        
        #medium ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 1:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_LARGE_X - 17
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_LARGE_Y - 17
        
        #large ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 2:
            lst_game[ALL_MAIN_LOC][LOC_BALL_X] = SCREEN_MID_LARGE_X - 25
            lst_game[ALL_MAIN_LOC][LOC_BALL_Y] = SCREEN_MID_LARGE_Y - 25

def player1_goal(lst_game, lst_entities, lst_ui, lst_sound):
    """Player 1 makes a goal

    Happens if the ball hits the right most boundary of the screen
    This will default all entity positions and make the ball
    move towards the player which scored the goal
    """

    #random direction
    temp = random.choice(lst_game[ALL_MAIN_GAME][GAME_LST])

    #add to score and round
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] += 1
    lst_game[ALL_MAIN_GAME][GAME_ROUND] += 1

    #last round
    if(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] < lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS]):
        if lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] == (lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] - 1) or lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] == (lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] - 1):
            lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL_RESET] = True

    #set directions        
    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_SCORE] = True

    #last round
    if lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL]:
        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = False
        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = temp
        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = True
        lst_game[ALL_MAIN_CONTROL][CONTROL_DIRECTION] = False

    #normal round    
    else:
        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = False
        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = False
        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = True
        lst_game[ALL_MAIN_CONTROL][CONTROL_DIRECTION] = False

def player2_goal(lst_game, lst_entities, lst_ui, lst_sound):
    """Player 2 makes a goal

    Happens if the ball hits the left most boundary of the screen
    This will default all entity positions and make the ball
    move towards the player which scored the goal
    """

    #random direction
    temp = random.choice(lst_game[ALL_MAIN_GAME][GAME_LST])
 
    #add to score and round   
    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] += 1
    lst_game[ALL_MAIN_GAME][GAME_ROUND] += 1

    #last round
    if(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] < lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS]):
        if lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] == (lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] - 1) or lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] == (lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] - 1):
            lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL_RESET] = True

    #set directions               
    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN] = False
    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_SCORE] = False

    #last round
    if lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL]:
        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = True
        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = temp
        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = True
        lst_game[ALL_MAIN_CONTROL][CONTROL_DIRECTION] = True

    #normal round          
    else:
        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = True
        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = False
        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = True
        lst_game[ALL_MAIN_CONTROL][CONTROL_DIRECTION] = True

def player1_win(lst_game, lst_entities, lst_ui, lst_sound):
    """Player 1 wins the game

    Happens if the score of player 1 is equal to the max score amount
    This will show the final winner display and play the winner music
    """

    #small screen
    if lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:

        #player is winner
        if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WINNER]:
            
            lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WINNER] = False
            lst_sound[ALL_SOUND_FINAL].stop()
            if lst_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                lst_sound[ALL_SOUND_END].play()

        #display        
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_SMALL], (0,0))
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_SCORE][UI_PLAYER1_WIN], (SCREEN_MID_SMALL_X - 150, SCREEN_MID_SMALL_Y - 75))

    #medium screen
    elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        
        #player is winner
        if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WINNER]:
            
            lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WINNER] = False
            lst_sound[ALL_SOUND_FINAL].stop()
            if lst_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                lst_sound[ALL_SOUND_END].play()
          
        #display          
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_MEDIUM], (0,0))
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_SCORE][UI_PLAYER1_WIN], (SCREEN_MID_MEDIUM_X - 150, SCREEN_MID_MEDIUM_Y - 75))

    #large screen
    elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        
        #player is winner
        if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WINNER]:
            
            lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WINNER] = False
            lst_sound[ALL_SOUND_FINAL].stop()
            if lst_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                lst_sound[ALL_SOUND_END].play()
             
        #display       
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_LARGE], (0,0))
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_SCORE][UI_PLAYER1_WIN], (SCREEN_MID_LARGE_X - 150, SCREEN_MID_LARGE_Y - 75))

def player2_win(lst_game, lst_entities, lst_ui, lst_sound):
    """Player 2 wins the game

    Happens if the score of player 2 is equal to the max score amount
    This will show the final winner display and play the winner music
    """

    #small screen
    if lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        
        #player is winner
        if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WINNER]:
            
            lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WINNER] = False
            lst_sound[ALL_SOUND_FINAL].stop()
            if lst_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                lst_sound[ALL_SOUND_END].play()
            
        #display        
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_SMALL], (0,0))
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_SCORE][UI_PLAYER2_WIN], (SCREEN_MID_SMALL_X - 150, SCREEN_MID_SMALL_Y - 75))

    #medium screen
    elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        
        #player is winner
        if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WINNER]:
            
            lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WINNER] = False
            lst_sound[ALL_SOUND_FINAL].stop()
            if lst_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                lst_sound[ALL_SOUND_END].play()
               
        #display    
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_MEDIUM], (0,0))
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_SCORE][UI_PLAYER2_WIN], (SCREEN_MID_MEDIUM_X - 150, SCREEN_MID_MEDIUM_Y - 75))

    #large screen
    elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        
        #player is winner
        if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WINNER]:
            
            lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WINNER] = False
            lst_sound[ALL_SOUND_FINAL].stop()
            if lst_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                lst_sound[ALL_SOUND_END].play()
               
        #display     
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_LARGE], (0,0))
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_SCORE][UI_PLAYER2_WIN], (SCREEN_MID_LARGE_X - 150, SCREEN_MID_LARGE_Y - 75))

def check_score(lst_game, lst_entities, lst_ui, lst_sound):
    """Checks the current score value

    The score title image is displayed to the
    screen along with the scores of each player
    """
    
    #main score ui
    if lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_SMALL].blit(lst_ui[ALL_UI_SCORE][UI_SCORE_DISPLAY], ((SCREEN_MID_SMALL_X) - 50, 25))
        
        #player1
        for i in range(11):
            if lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] == i:
                lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_NUM][i], ((SCREEN_MID_SMALL_X) - 100, 50))

        #player2        
        for i in range(11):
            if lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] == i:
                lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_NUM][i], ((SCREEN_MID_SMALL_X) + 75, 50))   
                
    elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_MEDIUM].blit(lst_ui[ALL_UI_SCORE][UI_SCORE_DISPLAY], ((SCREEN_MID_MEDIUM_X) - 50, 25))
        
        #player1
        for i in range(11):
            if lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] == i:
                lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_NUM][i], ((SCREEN_MID_MEDIUM_X) - 100, 50))

        #player2        
        for i in range(11):
            if lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] == i:
                lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_NUM][i], ((SCREEN_MID_MEDIUM_X) + 75, 50))  
        
    elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_LARGE].blit(lst_ui[ALL_UI_SCORE][UI_SCORE_DISPLAY], ((SCREEN_MID_LARGE_X) - 50, 25))
        
        #player1
        for i in range(11):
            if lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] == i:
                lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_NUM][i], ((SCREEN_MID_LARGE_X) - 100, 50))

        #player2        
        for i in range(11):
            if lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] == i:
                lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_NUM][i], ((SCREEN_MID_LARGE_X) + 75, 50))

def check_round(lst_game, lst_entities, lst_ui, lst_sound):
    """Checks the current round value

    Every two rounds, the speed of the ball is increased by one
    Every four rounds, starting from the sixth round, the speed
    of the players is increased by one

    If any player has one point less than the max score,
    this function is not used so it does not change the speed
    of the ball or players which are disabled at this time
    """

    #normal round
    if lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL] == False:
        
        if lst_game[ALL_MAIN_GAME][GAME_ROUND] == 2 and lst_game[ALL_MAIN_GAME][GAME_LST_ROUND][ROUND_NUM_2]:
            lst_game[ALL_MAIN_GAME][GAME_LST_ROUND][ROUND_NUM_2] = False
            lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1
        
        elif lst_game[ALL_MAIN_GAME][GAME_ROUND] == 4 and lst_game[ALL_MAIN_GAME][GAME_LST_ROUND][ROUND_NUM_4]:
            lst_game[ALL_MAIN_GAME][GAME_LST_ROUND][ROUND_NUM_4] = False
            lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1
            
        elif lst_game[ALL_MAIN_GAME][GAME_ROUND] == 6 and lst_game[ALL_MAIN_GAME][GAME_LST_ROUND][ROUND_NUM_6]:
            lst_game[ALL_MAIN_GAME][GAME_LST_ROUND][ROUND_NUM_6] = False
            lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1
            lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER] += 1
            
        elif lst_game[ALL_MAIN_GAME][GAME_ROUND] == 8 and lst_game[ALL_MAIN_GAME][GAME_LST_ROUND][ROUND_NUM_8]:
            lst_game[ALL_MAIN_GAME][GAME_LST_ROUND][ROUND_NUM_8] = False
            lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1
            
        elif lst_game[ALL_MAIN_GAME][GAME_ROUND] == 10 and lst_game[ALL_MAIN_GAME][GAME_LST_ROUND][ROUND_NUM_10]:
            lst_game[ALL_MAIN_GAME][GAME_LST_ROUND][ROUND_NUM_10] = False
            lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1
            lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER] += 1
            
        elif lst_game[ALL_MAIN_GAME][GAME_ROUND] == 12 and lst_game[ALL_MAIN_GAME][GAME_LST_ROUND][ROUND_NUM_12]:
            lst_game[ALL_MAIN_GAME][GAME_LST_ROUND][ROUND_NUM_12] = False
            lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1
            
        elif lst_game[ALL_MAIN_GAME][GAME_ROUND] == 14 and lst_game[ALL_MAIN_GAME][GAME_LST_ROUND][ROUND_NUM_14]:
            lst_game[ALL_MAIN_GAME][GAME_LST_ROUND][ROUND_NUM_14] = False
            lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1
            lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER] += 1
            
        elif lst_game[ALL_MAIN_GAME][GAME_ROUND] == 16 and lst_game[ALL_MAIN_GAME][GAME_LST_ROUND][ROUND_NUM_16]:
            lst_game[ALL_MAIN_GAME][GAME_LST_ROUND][ROUND_NUM_16] = False
            lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1
            
        elif lst_game[ALL_MAIN_GAME][GAME_ROUND] == 18 and lst_game[ALL_MAIN_GAME][GAME_LST_ROUND][ROUND_NUM_18]:
            lst_game[ALL_MAIN_GAME][GAME_LST_ROUND][ROUND_NUM_18] = False
            lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1
            lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER] += 1

def check_round_last(lst_game, lst_entities, lst_ui, lst_sound):
    """Checks if the current round is the last round

    The last round is either defined as when one player reaches
    one point less than the max score or when both players
    reach one point less than the max score

    The only difference between if one player needs one more point
    or if both players need one point is the background and music

    The properties of the last round are:

    The background and music change based on how many players
    reach one point less than the max score
    
    The ball speed starts at one and is increased by one
    everytime either player hits the ball

    The player move speed is constant
    """

    #small screen
    if lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        
        #final round
        if(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] == (lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] - 1) or lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] == (lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] - 1)):

            lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_SMALL].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_FINAL_SMALL], (0, 0))
            lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL] = True

            #reset entity speed
            if lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL_RESET]:
                    lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL_RESET] = False
                    lst_game[ALL_MAIN_GAME][GAME_SPEED] = 2 #speedtest
                    lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER] = 5
   
    #medium screen     
    elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        
        #final round
        if(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] == (lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] - 1) or lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] == (lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] - 1)):

            lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_MEDIUM].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_FINAL_MEDIUM], (0, 0))
            lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL] = True
            
            #reset entity speed
            if lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL_RESET]:
                    lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL_RESET] = False
                    lst_game[ALL_MAIN_GAME][GAME_SPEED] = 2 #speedtest
                    lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER] = 5
       
    #large screen 
    elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        
        #final round
        if(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] == (lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] - 1) or lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] == (lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] - 1)):

            lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_LARGE].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_FINAL_LARGE], (0, 0))
            lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL] = True
            
            #reset entity speed
            if lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL_RESET]:
                    lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL_RESET] = False
                    lst_game[ALL_MAIN_GAME][GAME_SPEED] = 2 #speedtest
                    lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER] = 5

def check_round_win(lst_game, lst_entities, lst_ui, lst_sound):
    """Checks if a player wins the game

    When either of the player's scores are equal to the max score
    the game will end and the player is the winner

    When lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WIN] is set to false,
    the main game execution stops and the winner execution will start
    """
    
    #player is winner
    if(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] == lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] or lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] == lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS]):
        lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WIN] = False

def game_exec_small(lst_game, lst_entities, lst_ui, lst_sound):
    """Executes the main game loop

    This will only execute if the current screen setting is small
    All display settings, entity locations and boundaries
    are based on the current screen size

    This will get and set entity location, check boundaries,
    display ui, execute the initial game countdown and stop
    the game execution if there is a winner

    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN] controls whether
    or not the game is running or it will be reset for a new round
    which starts the initial countdown

    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WIN] controls whether
    or not there is a winner 
    """

    #no winner
    if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WIN]:

        #game is running
        if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN]:

            #entity speed
            
            #player 1
            if lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_UP]:
                if(not(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_TOP])):
                    lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] -= lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER]
                        
            if lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_DOWN]:
                if(not(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_BOTTOM])):
                    lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] += lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER]

            #player 2
            if lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_UP]:
                if(not(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_TOP])):
                    lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] -= lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER]
                        
            if lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_DOWN]:
                if(not(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_BOTTOM])):
                    lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] += lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER]

            if lst_game[ALL_MAIN_CONTROL][CONTROL_BALL]:
                
                #ball                
                if lst_game[ALL_MAIN_CONTROL][CONTROL_DIRECTION]:
                    lst_game[ALL_MAIN_LOC][LOC_BALL_X] += lst_game[ALL_MAIN_GAME][GAME_SPEED]
                else:
                    lst_game[ALL_MAIN_LOC][LOC_BALL_X] -= lst_game[ALL_MAIN_GAME][GAME_SPEED]

            else:
                     
                #ball                
                if lst_game[ALL_MAIN_CONTROL][CONTROL_X]:
                    lst_game[ALL_MAIN_LOC][LOC_BALL_X] += lst_game[ALL_MAIN_GAME][GAME_SPEED]
                else:
                    lst_game[ALL_MAIN_LOC][LOC_BALL_X] -= lst_game[ALL_MAIN_GAME][GAME_SPEED]

                if lst_game[ALL_MAIN_CONTROL][CONTROL_Y]:
                    lst_game[ALL_MAIN_LOC][LOC_BALL_Y] += lst_game[ALL_MAIN_GAME][GAME_SPEED]
                else:
                    lst_game[ALL_MAIN_LOC][LOC_BALL_Y] -= lst_game[ALL_MAIN_GAME][GAME_SPEED]

            #boundaries
                    
            #player 1
            if lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100 >= SCREEN_SIZE_SMALL_Y:
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_TOP] = False
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_BOTTOM] = True
                        
            elif lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] <= 0:
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_TOP] = True
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_BOTTOM] = False
                    
            else:
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_TOP] = False
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_BOTTOM] = False

            #player 2
            if lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100 >= SCREEN_SIZE_SMALL_Y:
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_TOP] = False
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_BOTTOM] = True
                        
            elif lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] <= 0:
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_TOP] = True
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_BOTTOM] = False
                    
            else:
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_TOP] = False
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_BOTTOM] = False

            #small ball
            if lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 0:
                
                if lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL]:
                    
                    if lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 0:
                        player2_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_SMALL_X - 25:
                        player1_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= 25 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                        lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_SMALL_X - 75 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= SCREEN_SIZE_SMALL_X - 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                        lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1

                    if lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= 0:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= SCREEN_SIZE_SMALL_Y - 25:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                else:
                    
                    if lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 0:
                        player2_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_SMALL_X - 25:
                        player1_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= 25 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_SMALL_X - 75 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= SCREEN_SIZE_SMALL_X - 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False

                    if lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= 0:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= SCREEN_SIZE_SMALL_Y - 25:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False

            #medium ball
            elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 1:
                
                if lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL]:
                    
                    if lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 0:
                        
                        player2_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_SMALL_X - 35:
                        player1_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= 25 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                        lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_SMALL_X - 85 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= SCREEN_SIZE_SMALL_X - 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                        lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1

                    if lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= 0:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= SCREEN_SIZE_SMALL_Y - 35:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                else:
                    
                    if lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 0:
                        player2_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_SMALL_X - 35:
                        player1_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= 25 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_SMALL_X - 85 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= SCREEN_SIZE_SMALL_X - 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False

                    if lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= 0:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= SCREEN_SIZE_SMALL_Y - 35:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False

            #large ball
            elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 2:
                
                if lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL]:
                    
                    if lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 0:
                        
                        player2_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_SMALL_X - 50:
                        player1_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= 25 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                        lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_SMALL_X - 100 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= SCREEN_SIZE_SMALL_X - 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                        lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1

                    if lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= 0:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= SCREEN_SIZE_SMALL_Y - 50:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                else:
                    
                    if lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 0:
                        player2_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_SMALL_X - 50:
                        player1_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= 25 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_SMALL_X - 100 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= SCREEN_SIZE_SMALL_X - 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False

                    if lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= 0:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= SCREEN_SIZE_SMALL_Y - 50:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False

        #end of round               
        elif lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN] == False:

            #first round
            if (lst_game[ALL_MAIN_CONTROL][CONTROL_INITIAL] and (lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] < lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] or lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] < lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS])):
                
                lst_game[ALL_MAIN_GAME][GAME_TIME] += 1

                #count down
                if(lst_game[ALL_MAIN_GAME][GAME_TIME] == 1):
                    
                    if lst_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                        lst_sound[ALL_SOUND_START].play()
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_SMALL], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_3], (SCREEN_MID_SMALL_X - 16, SCREEN_MID_SMALL_Y - 32))
                        
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]):
                    
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_SMALL], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_2], (SCREEN_MID_SMALL_X - 16, SCREEN_MID_SMALL_Y - 32))
                          
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*2):
                    
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_SMALL], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_1], (SCREEN_MID_SMALL_X - 16, SCREEN_MID_SMALL_Y - 32))
                          
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*3):
                    
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_SMALL], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_GO], (SCREEN_MID_SMALL_X - 50, SCREEN_MID_SMALL_Y - 50))
                    game_reset(lst_game,lst_entities,lst_ui,lst_sound)
                          
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*4):
                    
                    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN] = True
                    lst_game[ALL_MAIN_CONTROL][CONTROL_INITIAL] = False
                    check_score(lst_game,lst_entities,lst_ui,lst_sound)
                    lst_game[ALL_MAIN_GAME][GAME_TIME] = 0
                    lst_sound[ALL_SOUND_START].stop()
                    if lst_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                        lst_sound[ALL_SOUND_MUSIC].play()
                        
            #normal round            
            elif (lst_game[ALL_MAIN_CONTROL][CONTROL_INITIAL] == False and (lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] < lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] or lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] < lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS])):
                
                lst_game[ALL_MAIN_GAME][GAME_TIME] += 1
                lst_sound[ALL_SOUND_MUSIC].stop()
                lst_sound[ALL_SOUND_FINAL].stop()

                #count down
                if(lst_game[ALL_MAIN_GAME][GAME_TIME] == 1):
                    
                    if lst_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                        lst_sound[ALL_SOUND_WIN].play()
                        
                    if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_SCORE]:
                        
                        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_SMALL], (0,0))
                        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_SCORE][UI_PLAYER1_SCORE], (SCREEN_MID_SMALL_X - 150, SCREEN_MID_SMALL_Y - 75))

                    else:
                        
                        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_SMALL], (0,0))
                        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_SCORE][UI_PLAYER2_SCORE], (SCREEN_MID_SMALL_X - 150, SCREEN_MID_SMALL_Y - 75))

                if(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*5):
                    
                    if lst_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                        lst_sound[ALL_SOUND_START].play()
                    lst_sound[ALL_SOUND_WIN].stop()
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_SMALL], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_3], (SCREEN_MID_SMALL_X - 16, SCREEN_MID_SMALL_Y - 32))
                        
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*6):

                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_SMALL], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_2], (SCREEN_MID_SMALL_X - 16, SCREEN_MID_SMALL_Y - 32))
                          
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*7):

                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_SMALL], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_1], (SCREEN_MID_SMALL_X - 16, SCREEN_MID_SMALL_Y - 32))
                          
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*8):

                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_SMALL], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_GO], (SCREEN_MID_SMALL_X - 50, SCREEN_MID_SMALL_Y - 50))
                    game_reset(lst_game,lst_entities,lst_ui,lst_sound)
                          
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*9):

                    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN] = True
                    check_score(lst_game,lst_entities,lst_ui,lst_sound)
                    lst_game[ALL_MAIN_GAME][GAME_TIME] = 0
                    lst_sound[ALL_SOUND_START].stop()

                    if(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] == (lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] - 1)) or lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] == (lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] - 1):
                        if lst_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                            lst_sound[ALL_SOUND_FINAL].play()
                            lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
        
                    else:
                        if lst_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                            lst_sound[ALL_SOUND_MUSIC].play()

    #end of game
    else:
        
        #time
        if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WINNER]:
            lst_game[ALL_MAIN_GAME][GAME_TIME] = 0
            lst_game[ALL_MAIN_GAME][GAME_TIME_FINAL] = 0
        else:
            lst_game[ALL_MAIN_GAME][GAME_TIME] += 1

        if lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]:
            lst_game[ALL_MAIN_GAME][GAME_TIME] = 0
            lst_game[ALL_MAIN_GAME][GAME_TIME_FINAL] += 1
        
        #display
        if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_SCORE]:
            player1_win(lst_game,lst_entities,lst_ui,lst_sound)
        else:
            player2_win(lst_game,lst_entities,lst_ui,lst_sound)

    #refresh screen

    #entities
    if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN]:
        
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_SMALL], (0, 0))

        check_round_last(lst_game,lst_entities,lst_ui,lst_sound)
                
        lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_SMALL].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_BORDER_BLUE_SMALL], (0, 0))
        lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_SMALL].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_BORDER_RED_SMALL], (SCREEN_SIZE_SMALL_X - 25, 0))
        
        check_score(lst_game,lst_entities,lst_ui,lst_sound)
        
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_entities[ALL_ENTITY_PLAYER1], (lst_game[ALL_MAIN_LOC][LOC_PLAYER1_X], lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y]))
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_entities[ALL_ENTITY_PLAYER2], (lst_game[ALL_MAIN_LOC][LOC_PLAYER2_X], lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y]))
        
        #small ball
        if lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 0:
            lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_entities[ALL_ENTITY_BALL_SMALL], (lst_game[ALL_MAIN_LOC][LOC_BALL_X], lst_game[ALL_MAIN_LOC][LOC_BALL_Y]))

        #medium ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 1:
            lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_entities[ALL_ENTITY_BALL_MEDIUM], (lst_game[ALL_MAIN_LOC][LOC_BALL_X], lst_game[ALL_MAIN_LOC][LOC_BALL_Y]))

        #large ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 2:
            lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_entities[ALL_ENTITY_BALL_LARGE], (lst_game[ALL_MAIN_LOC][LOC_BALL_X], lst_game[ALL_MAIN_LOC][LOC_BALL_Y]))
    
    pygame.display.flip()

    #final checks
    check_round(lst_game,lst_entities,lst_ui,lst_sound)
    check_round_win(lst_game,lst_entities,lst_ui,lst_sound)

def game_exec_medium(lst_game, lst_entities, lst_ui, lst_sound):
    """Executes the main game loop

    This will only execute if the current screen setting is medium
    All display settings, entity locations and boundaries
    are based on the current screen size

    This will get and set entity location, check boundaries,
    display ui, execute the initial game countdown and stop
    the game execution if there is a winner

    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN] controls whether
    or not the game is running or it will be reset for a new round
    which starts the initial countdown

    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WIN] controls whether
    or not there is a winner 
    """
    
    #no winner
    if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WIN]:

        #game is running
        if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN]:

            #entity speed
            
            #player 1
            if lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_UP]:
                if(not(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_TOP])):
                    lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] -= lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER]
                        
            if lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_DOWN]:
                if(not(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_BOTTOM])):
                    lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] += lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER]

            #player 2
            if lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_UP]:
                if(not(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_TOP])):
                    lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] -= lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER]
                        
            if lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_DOWN]:
                if(not(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_BOTTOM])):
                    lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] += lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER]

            if lst_game[ALL_MAIN_CONTROL][CONTROL_BALL]:
                
                #ball                
                if lst_game[ALL_MAIN_CONTROL][CONTROL_DIRECTION]:
                    lst_game[ALL_MAIN_LOC][LOC_BALL_X] += lst_game[ALL_MAIN_GAME][GAME_SPEED]
                else:
                    lst_game[ALL_MAIN_LOC][LOC_BALL_X] -= lst_game[ALL_MAIN_GAME][GAME_SPEED]

            else:
                     
                #ball                
                if lst_game[ALL_MAIN_CONTROL][CONTROL_X]:
                    lst_game[ALL_MAIN_LOC][LOC_BALL_X] += lst_game[ALL_MAIN_GAME][GAME_SPEED]
                else:
                    lst_game[ALL_MAIN_LOC][LOC_BALL_X] -= lst_game[ALL_MAIN_GAME][GAME_SPEED]

                if lst_game[ALL_MAIN_CONTROL][CONTROL_Y]:
                    lst_game[ALL_MAIN_LOC][LOC_BALL_Y] += lst_game[ALL_MAIN_GAME][GAME_SPEED]
                else:
                    lst_game[ALL_MAIN_LOC][LOC_BALL_Y] -= lst_game[ALL_MAIN_GAME][GAME_SPEED]

            #boundaries
                    
            #player 1
            if lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100 >= SCREEN_SIZE_MEDIUM_Y:
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_TOP] = False
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_BOTTOM] = True
                        
            elif lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] <= 0:
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_TOP] = True
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_BOTTOM] = False
                    
            else:
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_TOP] = False
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_BOTTOM] = False

            #player 2
            if lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100 >= SCREEN_SIZE_MEDIUM_Y:
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_TOP] = False
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_BOTTOM] = True
                        
            elif lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] <= 0:
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_TOP] = True
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_BOTTOM] = False
                    
            else:
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_TOP] = False
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_BOTTOM] = False

            #small ball
            if lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 0:
                
                if lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL]:
                    
                    if lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 0:
                        player2_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_MEDIUM_X - 25:
                        player1_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= 25 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                        lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_MEDIUM_X - 75 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= SCREEN_SIZE_MEDIUM_X - 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                        lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1

                    if lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= 0:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= SCREEN_SIZE_MEDIUM_Y - 25:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                else:
                    
                    if lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 0:
                        player2_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_MEDIUM_X - 25:
                        player1_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= 25 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_MEDIUM_X - 75 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= SCREEN_SIZE_MEDIUM_X - 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False

                    if lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= 0:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= SCREEN_SIZE_MEDIUM_Y - 25:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False

            #medium ball
            elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 1:
                
                if lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL]:
                    
                    if lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 0:
                        
                        player2_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_MEDIUM_X - 35:
                        player1_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= 25 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                        lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_MEDIUM_X - 85 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= SCREEN_SIZE_MEDIUM_X - 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                        lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1

                    if lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= 0:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= SCREEN_SIZE_MEDIUM_Y - 35:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                else:
                    
                    if lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 0:
                        player2_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_MEDIUM_X - 35:
                        player1_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= 25 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_MEDIUM_X - 85 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= SCREEN_SIZE_MEDIUM_X - 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False

                    if lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= 0:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= SCREEN_SIZE_MEDIUM_Y - 35:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False

            #large ball
            elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 2:
                
                if lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL]:
                    
                    if lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 0:
                        
                        player2_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_MEDIUM_X - 50:
                        player1_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= 25 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                        lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_MEDIUM_X - 100 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= SCREEN_SIZE_MEDIUM_X - 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                        lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1

                    if lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= 0:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= SCREEN_SIZE_MEDIUM_Y - 50:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                else:
                    
                    if lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 0:
                        player2_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_MEDIUM_X - 50:
                        player1_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= 25 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_MEDIUM_X - 100 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= SCREEN_SIZE_MEDIUM_X - 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False

                    if lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= 0:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= SCREEN_SIZE_MEDIUM_Y - 50:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False

        #end of round               
        elif lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN] == False:

            #first round
            if (lst_game[ALL_MAIN_CONTROL][CONTROL_INITIAL] and (lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] < lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] or lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] < lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS])):
                
                lst_game[ALL_MAIN_GAME][GAME_TIME] += 1

                #count down
                if(lst_game[ALL_MAIN_GAME][GAME_TIME] == 1):
                    
                    if lst_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                        lst_sound[ALL_SOUND_START].play()
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_MEDIUM], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_3], (SCREEN_MID_MEDIUM_X - 16, SCREEN_MID_MEDIUM_Y - 32))
                        
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]):
                    
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_MEDIUM], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_2], (SCREEN_MID_MEDIUM_X - 16, SCREEN_MID_MEDIUM_Y - 32))
                          
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*2):
                    
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_MEDIUM], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_1], (SCREEN_MID_MEDIUM_X - 16, SCREEN_MID_MEDIUM_Y - 32))
                          
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*3):
                    
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_MEDIUM], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_GO], (SCREEN_MID_MEDIUM_X - 50, SCREEN_MID_MEDIUM_Y - 50))
                    game_reset(lst_game,lst_entities,lst_ui,lst_sound)
                          
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*4):
                    
                    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN] = True
                    lst_game[ALL_MAIN_CONTROL][CONTROL_INITIAL] = False
                    check_score(lst_game,lst_entities,lst_ui,lst_sound)
                    lst_game[ALL_MAIN_GAME][GAME_TIME] = 0
                    lst_sound[ALL_SOUND_START].stop()
                    if lst_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                        lst_sound[ALL_SOUND_MUSIC].play()
                        
            #normal round            
            elif (lst_game[ALL_MAIN_CONTROL][CONTROL_INITIAL] == False and (lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] < lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] or lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] < lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS])):
                
                lst_game[ALL_MAIN_GAME][GAME_TIME] += 1
                lst_sound[ALL_SOUND_MUSIC].stop()
                lst_sound[ALL_SOUND_FINAL].stop()

                #count down
                if(lst_game[ALL_MAIN_GAME][GAME_TIME] == 1):
                    
                    if lst_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                        lst_sound[ALL_SOUND_WIN].play()
                        
                    if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_SCORE]:
                        
                        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_MEDIUM], (0,0))
                        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_SCORE][UI_PLAYER1_SCORE], (SCREEN_MID_MEDIUM_X - 150, SCREEN_MID_MEDIUM_Y - 75))

                    else:
                        
                        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_MEDIUM], (0,0))
                        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_SCORE][UI_PLAYER2_SCORE], (SCREEN_MID_MEDIUM_X - 150, SCREEN_MID_MEDIUM_Y - 75))

                if(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*5):
                    
                    if lst_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                        lst_sound[ALL_SOUND_START].play()
                    lst_sound[ALL_SOUND_WIN].stop()
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_MEDIUM], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_3], (SCREEN_MID_MEDIUM_X - 16, SCREEN_MID_MEDIUM_Y - 32))
                        
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*6):

                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_MEDIUM], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_2], (SCREEN_MID_MEDIUM_X - 16, SCREEN_MID_MEDIUM_Y - 32))
                          
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*7):

                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_MEDIUM], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_1], (SCREEN_MID_MEDIUM_X - 16, SCREEN_MID_MEDIUM_Y - 32))
                          
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*8):

                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_MEDIUM], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_GO], (SCREEN_MID_MEDIUM_X - 50, SCREEN_MID_MEDIUM_Y - 50))
                    game_reset(lst_game,lst_entities,lst_ui,lst_sound)
                          
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*9):

                    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN] = True
                    check_score(lst_game,lst_entities,lst_ui,lst_sound)
                    lst_game[ALL_MAIN_GAME][GAME_TIME] = 0
                    lst_sound[ALL_SOUND_START].stop()

                    if(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] == (lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] - 1)) or lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] == (lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] - 1):
                        if lst_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                            lst_sound[ALL_SOUND_FINAL].play()
                            lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
        
                    else:
                        if lst_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                            lst_sound[ALL_SOUND_MUSIC].play()

    #end of game
    else:
        
        #time
        if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WINNER]:
            lst_game[ALL_MAIN_GAME][GAME_TIME] = 0
            lst_game[ALL_MAIN_GAME][GAME_TIME_FINAL] = 0
        else:
            lst_game[ALL_MAIN_GAME][GAME_TIME] += 1

        if lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]:
            lst_game[ALL_MAIN_GAME][GAME_TIME] = 0
            lst_game[ALL_MAIN_GAME][GAME_TIME_FINAL] += 1
        
        #display
        if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_SCORE]:
            player1_win(lst_game,lst_entities,lst_ui,lst_sound)
        else:
            player2_win(lst_game,lst_entities,lst_ui,lst_sound)

    #refresh screen

    #entities
    if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN]:
        
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_MEDIUM], (0, 0))

        check_round_last(lst_game,lst_entities,lst_ui,lst_sound)
                
        lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_MEDIUM].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_BORDER_BLUE_MEDIUM], (0, 0))
        lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_MEDIUM].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_BORDER_RED_MEDIUM], (SCREEN_SIZE_MEDIUM_X - 25, 0))
        
        check_score(lst_game,lst_entities,lst_ui,lst_sound)
        
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_entities[ALL_ENTITY_PLAYER1], (lst_game[ALL_MAIN_LOC][LOC_PLAYER1_X], lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y]))
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_entities[ALL_ENTITY_PLAYER2], (lst_game[ALL_MAIN_LOC][LOC_PLAYER2_X], lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y]))
        
        #small ball
        if lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 0:
            lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_entities[ALL_ENTITY_BALL_SMALL], (lst_game[ALL_MAIN_LOC][LOC_BALL_X], lst_game[ALL_MAIN_LOC][LOC_BALL_Y]))

        #medium ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 1:
            lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_entities[ALL_ENTITY_BALL_MEDIUM], (lst_game[ALL_MAIN_LOC][LOC_BALL_X], lst_game[ALL_MAIN_LOC][LOC_BALL_Y]))

        #large ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 2:
            lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_entities[ALL_ENTITY_BALL_LARGE], (lst_game[ALL_MAIN_LOC][LOC_BALL_X], lst_game[ALL_MAIN_LOC][LOC_BALL_Y]))
    
    pygame.display.flip()

    #final checks
    check_round(lst_game,lst_entities,lst_ui,lst_sound)
    check_round_win(lst_game,lst_entities,lst_ui,lst_sound)

def game_exec_large(lst_game, lst_entities, lst_ui, lst_sound):
    """Executes the main game loop

    This will only execute if the current screen setting is large
    All display settings, entity locations and boundaries
    are based on the current screen size

    This will get and set entity location, check boundaries,
    display ui, execute the initial game countdown and stop
    the game execution if there is a winner

    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN] controls whether
    or not the game is running or it will be reset for a new round
    which starts the initial countdown

    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WIN] controls whether
    or not there is a winner 
    """
    
    #no winner
    if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WIN]:

        #game is running
        if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN]:

            #entity speed
            
            #player 1
            if lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_UP]:
                if(not(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_TOP])):
                    lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] -= lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER]
                        
            if lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_DOWN]:
                if(not(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_BOTTOM])):
                    lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] += lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER]

            #player 2
            if lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_UP]:
                if(not(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_TOP])):
                    lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] -= lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER]
                        
            if lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_DOWN]:
                if(not(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_BOTTOM])):
                    lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] += lst_game[ALL_MAIN_GAME][GAME_SPEED_PLAYER]

            if lst_game[ALL_MAIN_CONTROL][CONTROL_BALL]:
                
                #ball                
                if lst_game[ALL_MAIN_CONTROL][CONTROL_DIRECTION]:
                    lst_game[ALL_MAIN_LOC][LOC_BALL_X] += lst_game[ALL_MAIN_GAME][GAME_SPEED]
                else:
                    lst_game[ALL_MAIN_LOC][LOC_BALL_X] -= lst_game[ALL_MAIN_GAME][GAME_SPEED]

            else:
                     
                #ball                
                if lst_game[ALL_MAIN_CONTROL][CONTROL_X]:
                    lst_game[ALL_MAIN_LOC][LOC_BALL_X] += lst_game[ALL_MAIN_GAME][GAME_SPEED]
                else:
                    lst_game[ALL_MAIN_LOC][LOC_BALL_X] -= lst_game[ALL_MAIN_GAME][GAME_SPEED]

                if lst_game[ALL_MAIN_CONTROL][CONTROL_Y]:
                    lst_game[ALL_MAIN_LOC][LOC_BALL_Y] += lst_game[ALL_MAIN_GAME][GAME_SPEED]
                else:
                    lst_game[ALL_MAIN_LOC][LOC_BALL_Y] -= lst_game[ALL_MAIN_GAME][GAME_SPEED]

            #boundaries
                    
            #player 1
            if lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100 >= SCREEN_SIZE_LARGE_Y:
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_TOP] = False
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_BOTTOM] = True
                        
            elif lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] <= 0:
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_TOP] = True
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_BOTTOM] = False
                    
            else:
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_TOP] = False
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_BOTTOM] = False

            #player 2
            if lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100 >= SCREEN_SIZE_LARGE_Y:
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_TOP] = False
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_BOTTOM] = True
                        
            elif lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] <= 0:
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_TOP] = True
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_BOTTOM] = False
                    
            else:
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_TOP] = False
                lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_BOTTOM] = False

            #small ball
            if lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 0:
                
                if lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL]:
                    
                    if lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 0:
                        player2_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_LARGE_X - 25:
                        player1_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= 25 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                        lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_LARGE_X - 75 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= SCREEN_SIZE_LARGE_X - 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                        lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1

                    if lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= 0:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= SCREEN_SIZE_LARGE_Y - 25:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                else:
                    
                    if lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 0:
                        player2_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_LARGE_X - 25:
                        player1_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= 25 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_LARGE_X - 75 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= SCREEN_SIZE_LARGE_X - 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False

                    if lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= 0:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= SCREEN_SIZE_LARGE_Y - 25:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False

            #medium ball
            elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 1:
                
                if lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL]:
                    
                    if lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 0:
                        
                        player2_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_LARGE_X - 35:
                        player1_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= 25 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                        lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_LARGE_X - 85 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= SCREEN_SIZE_LARGE_X - 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                        lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1

                    if lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= 0:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= SCREEN_SIZE_LARGE_Y - 35:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                else:
                    
                    if lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 0:
                        player2_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_LARGE_X - 35:
                        player1_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= 25 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_LARGE_X - 85 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= SCREEN_SIZE_LARGE_X - 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False

                    if lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= 0:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= SCREEN_SIZE_LARGE_Y - 35:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False

            #large ball
            elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 2:
                
                if lst_game[ALL_MAIN_GAME][GAME_SPEED_FINAL]:
                    
                    if lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 0:
                        
                        player2_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_LARGE_X - 50:
                        player1_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= 25 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                        lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_LARGE_X - 100 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= SCREEN_SIZE_LARGE_X - 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                        lst_game[ALL_MAIN_GAME][GAME_SPEED] += 1

                    if lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= 0:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= SCREEN_SIZE_LARGE_Y - 50:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                else:
                    
                    if lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 0:
                        player2_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_LARGE_X - 50:
                        player1_goal(lst_game,lst_entities,lst_ui,lst_sound)
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= 25 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif ((lst_game[ALL_MAIN_LOC][LOC_BALL_X] >= SCREEN_SIZE_LARGE_X - 100 and lst_game[ALL_MAIN_LOC][LOC_BALL_X] <= SCREEN_SIZE_LARGE_X - 50) and (lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] and lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y] + 100)):
                        lst_game[ALL_MAIN_CONTROL][CONTROL_X] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False

                    if lst_game[ALL_MAIN_LOC][LOC_BALL_Y] <= 0:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = True
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
                            
                    elif lst_game[ALL_MAIN_LOC][LOC_BALL_Y] >= SCREEN_SIZE_LARGE_Y - 50:
                        lst_game[ALL_MAIN_CONTROL][CONTROL_Y] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False

        #end of round               
        elif lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN] == False:

            #first round
            if (lst_game[ALL_MAIN_CONTROL][CONTROL_INITIAL] and (lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] < lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] or lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] < lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS])):
                
                lst_game[ALL_MAIN_GAME][GAME_TIME] += 1

                #count down
                if(lst_game[ALL_MAIN_GAME][GAME_TIME] == 1):
                    
                    if lst_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                        lst_sound[ALL_SOUND_START].play()
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_LARGE], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_3], (SCREEN_MID_LARGE_X - 16, SCREEN_MID_LARGE_Y - 32))
                        
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]):
                    
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_LARGE], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_2], (SCREEN_MID_LARGE_X - 16, SCREEN_MID_LARGE_Y - 32))
                          
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*2):
                    
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_LARGE], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_1], (SCREEN_MID_LARGE_X - 16, SCREEN_MID_LARGE_Y - 32))
                          
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*3):
                    
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_LARGE], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_GO], (SCREEN_MID_LARGE_X - 50, SCREEN_MID_LARGE_Y - 50))
                    game_reset(lst_game,lst_entities,lst_ui,lst_sound)
                          
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*4):
                    
                    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN] = True
                    lst_game[ALL_MAIN_CONTROL][CONTROL_INITIAL] = False
                    check_score(lst_game,lst_entities,lst_ui,lst_sound)
                    lst_game[ALL_MAIN_GAME][GAME_TIME] = 0
                    lst_sound[ALL_SOUND_START].stop()
                    if lst_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                        lst_sound[ALL_SOUND_MUSIC].play()
                        
            #normal round            
            elif (lst_game[ALL_MAIN_CONTROL][CONTROL_INITIAL] == False and (lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] < lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] or lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] < lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS])):
                
                lst_game[ALL_MAIN_GAME][GAME_TIME] += 1
                lst_sound[ALL_SOUND_MUSIC].stop()
                lst_sound[ALL_SOUND_FINAL].stop()

                #count down
                if(lst_game[ALL_MAIN_GAME][GAME_TIME] == 1):
                    
                    if lst_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                        lst_sound[ALL_SOUND_WIN].play()
                        
                    if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_SCORE]:
                        
                        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_LARGE], (0,0))
                        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_SCORE][UI_PLAYER1_SCORE], (SCREEN_MID_LARGE_X - 150, SCREEN_MID_LARGE_Y - 75))

                    else:
                        
                        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_LARGE], (0,0))
                        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_SCORE][UI_PLAYER2_SCORE], (SCREEN_MID_LARGE_X - 150, SCREEN_MID_LARGE_Y - 75))

                if(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*5):
                    
                    if lst_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                        lst_sound[ALL_SOUND_START].play()
                    lst_sound[ALL_SOUND_WIN].stop()
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_LARGE], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_3], (SCREEN_MID_LARGE_X - 16, SCREEN_MID_LARGE_Y - 32))
                        
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*6):

                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_LARGE], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_2], (SCREEN_MID_LARGE_X - 16, SCREEN_MID_LARGE_Y - 32))
                          
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*7):

                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_LARGE], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_1], (SCREEN_MID_LARGE_X - 16, SCREEN_MID_LARGE_Y - 32))
                          
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*8):

                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_LARGE], (0,0))
                    lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_UI_INTRO][UI_INTRO_GO], (SCREEN_MID_LARGE_X - 50, SCREEN_MID_LARGE_Y - 50))
                    game_reset(lst_game,lst_entities,lst_ui,lst_sound)
                          
                elif(lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]*9):

                    lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN] = True
                    check_score(lst_game,lst_entities,lst_ui,lst_sound)
                    lst_game[ALL_MAIN_GAME][GAME_TIME] = 0
                    lst_sound[ALL_SOUND_START].stop()

                    if(lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_SCORE] == (lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] - 1)) or lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_SCORE] == (lst_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] - 1):
                        if lst_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                            lst_sound[ALL_SOUND_FINAL].play()
                            lst_game[ALL_MAIN_CONTROL][CONTROL_BALL] = False
        
                    else:
                        if lst_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                            lst_sound[ALL_SOUND_MUSIC].play()

    #end of game
    else:
        
        #time
        if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WINNER]:
            lst_game[ALL_MAIN_GAME][GAME_TIME] = 0
            lst_game[ALL_MAIN_GAME][GAME_TIME_FINAL] = 0
        else:
            lst_game[ALL_MAIN_GAME][GAME_TIME] += 1

        if lst_game[ALL_MAIN_GAME][GAME_TIME] == lst_game[ALL_MAIN_GAME][GAME_SECOND]:
            lst_game[ALL_MAIN_GAME][GAME_TIME] = 0
            lst_game[ALL_MAIN_GAME][GAME_TIME_FINAL] += 1
        
        #display
        if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_SCORE]:
            player1_win(lst_game,lst_entities,lst_ui,lst_sound)
        else:
            player2_win(lst_game,lst_entities,lst_ui,lst_sound)

    #refresh screen

    #entities
    if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN]:
        
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_LARGE], (0, 0))

        check_round_last(lst_game,lst_entities,lst_ui,lst_sound)
                
        lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_LARGE].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_BORDER_BLUE_LARGE], (0, 0))
        lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_LARGE].blit(lst_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_BORDER_RED_LARGE], (SCREEN_SIZE_LARGE_X - 25, 0))
        
        check_score(lst_game,lst_entities,lst_ui,lst_sound)
        
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_entities[ALL_ENTITY_PLAYER1], (lst_game[ALL_MAIN_LOC][LOC_PLAYER1_X], lst_game[ALL_MAIN_LOC][LOC_PLAYER1_Y]))
        lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_entities[ALL_ENTITY_PLAYER2], (lst_game[ALL_MAIN_LOC][LOC_PLAYER2_X], lst_game[ALL_MAIN_LOC][LOC_PLAYER2_Y]))
        
        #small ball
        if lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 0:
            lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_entities[ALL_ENTITY_BALL_SMALL], (lst_game[ALL_MAIN_LOC][LOC_BALL_X], lst_game[ALL_MAIN_LOC][LOC_BALL_Y]))

        #medium ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 1:
            lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_entities[ALL_ENTITY_BALL_MEDIUM], (lst_game[ALL_MAIN_LOC][LOC_BALL_X], lst_game[ALL_MAIN_LOC][LOC_BALL_Y]))

        #large ball
        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == 2:
            lst_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(lst_entities[ALL_ENTITY_BALL_LARGE], (lst_game[ALL_MAIN_LOC][LOC_BALL_X], lst_game[ALL_MAIN_LOC][LOC_BALL_Y]))
    
    pygame.display.flip()

    #final checks
    check_round(lst_game,lst_entities,lst_ui,lst_sound)
    check_round_win(lst_game,lst_entities,lst_ui,lst_sound)

def game_exec(lst_game, lst_entities, lst_ui, lst_sound):
    """Main game execution

    This will set up the game to the default configuration

    The main game loop controls mouse and key presses
    It executes the proper game function based on screen size
    """

    #setup
    game_setup(lst_game,lst_entities,lst_ui,lst_sound)

    #loop
    while lst_game[ALL_MAIN_CONTROL][CONTROL_LOOP]:

        #time
        lst_entities[ALL_ENTITY_CLOCK].tick(lst_game[ALL_MAIN_GAME][GAME_SECOND])

        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lst_game[ALL_MAIN_ALL][MAIN_MENU_CONTROL] = False
                lst_game[ALL_MAIN_ALL][MAIN_MENU_PLAY] = False
                lst_game[ALL_MAIN_CONTROL][CONTROL_LOOP] = False

            #left mouse click up
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:

                #game is running
                if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN]:

                    #game is paused
                    if lst_game[ALL_MAIN_ALL][MAIN_MENU_PAUSE]:
                        
                        pos = pygame.mouse.get_pos()

                        #small screen
                        if lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
                            
                            #continue button
                            if (pos[0] >= 220 and pos[0] <= 420) and (pos[1] >= 200 and pos[1] <= 250):
                                lst_game[ALL_MAIN_ALL][MAIN_MENU_PAUSE] = False
                                pygame.mixer.unpause()
                            
                            #quit button
                            elif (pos[0] >= 270 and pos[0] <= 370) and (pos[1] >= 300 and pos[1] <= 350):

                                #control
                                lst_game[ALL_MAIN_ALL][MAIN_MENU_PLAY] = False
                                lst_game[ALL_MAIN_ALL][MAIN_MENU_PAUSE] = False
                                lst_game[ALL_MAIN_CONTROL][CONTROL_LOOP] = False

                                #sound
                                pygame.mixer.unpause()
                                
                                lst_sound[ALL_SOUND_START].stop()
                                lst_sound[ALL_SOUND_END].stop()
                                lst_sound[ALL_SOUND_FINAL].stop()
                                lst_sound[ALL_SOUND_MUSIC].stop()
                                lst_sound[ALL_SOUND_WIN].stop()

                                #setup                                 
                                game_setup_final(lst_game,lst_entities,lst_ui,lst_sound)
                                return

                        #medium screen
                        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
                            
                            #continue button
                            if (pos[0] >= 300 and pos[0] <= 500) and (pos[1] >= 250 and pos[1] <= 300):
                                
                                lst_game[ALL_MAIN_ALL][MAIN_MENU_PAUSE] = False
                                pygame.mixer.unpause()
                            
                            #quit button
                            elif (pos[0] >= 350 and pos[0] <= 450) and (pos[1] >= 350 and pos[1] <= 400):

                                #control
                                lst_game[ALL_MAIN_ALL][MAIN_MENU_PLAY] = False
                                lst_game[ALL_MAIN_ALL][MAIN_MENU_PAUSE] = False
                                lst_game[ALL_MAIN_CONTROL][CONTROL_LOOP] = False

                                #sound
                                pygame.mixer.unpause()
                                
                                lst_sound[ALL_SOUND_START].stop()
                                lst_sound[ALL_SOUND_END].stop()
                                lst_sound[ALL_SOUND_FINAL].stop()
                                lst_sound[ALL_SOUND_MUSIC].stop()
                                lst_sound[ALL_SOUND_WIN].stop()

                                #setup                                 
                                game_setup_final(lst_game,lst_entities,lst_ui,lst_sound)
                                return

                        #large screen
                        elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
                            
                            #continue button
                            if (pos[0] >= 412 and pos[0] <= 612) and (pos[1] >= 300 and pos[1] <= 350):
                                
                                lst_game[ALL_MAIN_ALL][MAIN_MENU_PAUSE] = False
                                pygame.mixer.unpause()
                            
                            #quit button
                            elif (pos[0] >= 462 and pos[0] <= 562) and (pos[1] >= 400 and pos[1] <= 450):

                                #control
                                lst_game[ALL_MAIN_ALL][MAIN_MENU_PLAY] = False
                                lst_game[ALL_MAIN_ALL][MAIN_MENU_PAUSE] = False
                                lst_game[ALL_MAIN_CONTROL][CONTROL_LOOP] = False

                                #sound
                                pygame.mixer.unpause()
                                
                                lst_sound[ALL_SOUND_START].stop()
                                lst_sound[ALL_SOUND_END].stop()
                                lst_sound[ALL_SOUND_FINAL].stop()
                                lst_sound[ALL_SOUND_MUSIC].stop()
                                lst_sound[ALL_SOUND_WIN].stop()

                                #setup                                 
                                game_setup_final(lst_game,lst_entities,lst_ui,lst_sound)
                                return

            #key down       
            elif event.type == pygame.KEYDOWN:

                #game is running
                if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN]:

                    #game is paused
                    if lst_game[ALL_MAIN_ALL][MAIN_MENU_PAUSE]:
                        
                        if event.key == pygame.K_BACKQUOTE:
                            lst_game[ALL_MAIN_ALL][MAIN_MENU_PAUSE] = False
                            pygame.mixer.unpause() 
                    else:
                        
                        if event.key == pygame.K_BACKQUOTE:
                            lst_game[ALL_MAIN_ALL][MAIN_MENU_PAUSE] = True
                            pygame.mixer.pause()

                #game is over
                if lst_game[ALL_MAIN_CONTROL][CONTROL_MAIN_WIN] == False:
                    
                    if event.key == pygame.K_BACKQUOTE:
                        
                        #control
                        lst_game[ALL_MAIN_ALL][MAIN_MENU_PLAY] = False
                        lst_game[ALL_MAIN_ALL][MAIN_MENU_PAUSE] = False
                        lst_game[ALL_MAIN_CONTROL][CONTROL_LOOP] = False

                        #sound
                        pygame.mixer.unpause()
                        
                        lst_sound[ALL_SOUND_START].stop()
                        lst_sound[ALL_SOUND_END].stop()
                        lst_sound[ALL_SOUND_FINAL].stop()
                        lst_sound[ALL_SOUND_MUSIC].stop()
                        lst_sound[ALL_SOUND_WIN].stop()

                        #setup                                 
                        game_setup_final(lst_game,lst_entities,lst_ui,lst_sound)
                        return

                if event.key == pygame.K_w:
                    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_UP] = True
                    
                if event.key == pygame.K_s:
                    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_DOWN] = True
                        
                if event.key == pygame.K_UP:
                    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_UP] = True
                    
                if event.key == pygame.K_DOWN:
                    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_DOWN] = True

            #key up            
            elif event.type == pygame.KEYUP:
                
                if event.key == pygame.K_w:
                    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_UP] = False
                    
                if event.key == pygame.K_s:
                    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER1_DOWN] = False
                        
                if event.key == pygame.K_UP:
                    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_UP] = False
                    
                if event.key == pygame.K_DOWN:
                    lst_game[ALL_MAIN_CONTROL][CONTROL_PLAYER2_DOWN] = False

        #game is paused
        if lst_game[ALL_MAIN_ALL][MAIN_MENU_PAUSE]:
            game_pause(lst_game,lst_entities,lst_ui,lst_sound)

        #game is running
        else:
            #small screen
            if lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
                game_exec_small(lst_game,lst_entities,lst_ui,lst_sound)

            #medium screen
            elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
                game_exec_medium(lst_game,lst_entities,lst_ui,lst_sound)

            #large screen
            elif lst_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
                game_exec_large(lst_game,lst_entities,lst_ui,lst_sound)

        #end game
        if lst_game[ALL_MAIN_GAME][GAME_TIME_FINAL] >= int(lst_sound[ALL_SOUND_END].get_length()):
            
            #control
            lst_game[ALL_MAIN_ALL][MAIN_MENU_PLAY] = False
            lst_game[ALL_MAIN_ALL][MAIN_MENU_PAUSE] = False
            lst_game[ALL_MAIN_CONTROL][CONTROL_LOOP] = False

            #sound
            pygame.mixer.unpause()
            
            lst_sound[ALL_SOUND_START].stop()
            lst_sound[ALL_SOUND_END].stop()
            lst_sound[ALL_SOUND_FINAL].stop()
            lst_sound[ALL_SOUND_MUSIC].stop()
            lst_sound[ALL_SOUND_WIN].stop()

            #setup                                 
            game_setup_final(lst_game,lst_entities,lst_ui,lst_sound)
            return
