"""
Unreal Ping Pong
game_functions.py
Created by Justin Leonard

Contains main game functions fo the game menus
This will have the menus along with functions
for logic and button press events
"""

#initialize
import pygame
from game_globals import *
from game_execute import *

#menu functions

#play menu

def game_playmenu(core_game, core_entities, core_ui, core_sound):
    """The play menu

    Buttons for the play menu along with the
    display are executed here
    """

    #control
    core_game[ALL_MAIN_ALL][MAIN_MENU_PLAY] = True

    #loop
    while core_game[ALL_MAIN_ALL][MAIN_MENU_PLAY]:
        
	#time
        core_entities[ALL_ENTITY_CLOCK].tick(core_game[ALL_MAIN_GAME][GAME_SECOND])

        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                core_game[ALL_MAIN_ALL][MAIN_MENU_CONTROL] = False
                core_game[ALL_MAIN_ALL][MAIN_MENU_PLAY] = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                playmenu_event_button_down(core_game,core_entities,core_ui,core_sound)
                        
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                playmenu_event_button_up(core_game,core_entities,core_ui,core_sound)
                
        #display
        if core_game[ALL_MAIN_ALL][MAIN_MENU_PLAY]:
            playmenu_event_display(core_game,core_entities,core_ui,core_sound)
            
        pygame.display.flip()

#options menu

def game_optionsmenu(core_game, core_entities, core_ui, core_sound):
    """The options menu

    Buttons for the options menu along with the
    display are executed here
    """

    #control
    core_game[ALL_MAIN_ALL][MAIN_MENU_OPTIONS] = True

    #loop
    while core_game[ALL_MAIN_ALL][MAIN_MENU_OPTIONS]:

        #time
        core_entities[ALL_ENTITY_CLOCK].tick(core_game[ALL_MAIN_GAME][GAME_SECOND])

        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                core_game[ALL_MAIN_ALL][MAIN_MENU_CONTROL] = False
                core_game[ALL_MAIN_ALL][MAIN_MENU_OPTIONS] = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                optionsmenu_event_button_down(core_game,core_entities,core_ui,core_sound)
                        
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                optionsmenu_event_button_up(core_game,core_entities,core_ui,core_sound)

        #display
        if core_game[ALL_MAIN_ALL][MAIN_MENU_OPTIONS]:
            optionsmenu_event_display(core_game,core_entities,core_ui,core_sound)
            
        pygame.display.flip()

#check functions

#play menu

def playmenu_check_maxrounds(core_game, core_entities, core_ui, core_sound):
    """Check max rounds

    Checks the current value of the max rounds
    and displays it based on screen size
    """

    #small screen
    if core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        for i in range(3,11):
            if core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] == i:
                core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_UI_NUM][i + 11], (300, 120))

    #medium screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        for i in range(3,11):
            if core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] == i:
                core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_UI_NUM][i + 11], (380, 150))

    #large screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        for i in range(3,11):
            if core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] == i:
                core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_UI_NUM][i + 11], (554, 150))

def playmenu_check_ballspeed(core_game, core_entities, core_ui, core_sound):
    """Check ball speed

    Checks the current value of the ball speed
    and displays it based on screen size
    """

    #small screen
    if core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        if core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] == 0:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_SLOW], (300, 190))
            
        elif core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] == 1:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_MEDIUM], (300, 190))
            
        elif core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] == 2:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_FAST], (300, 190))

    #medium screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        if core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] == 0:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_SLOW], (380, 240))
            
        elif core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] == 1:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_MEDIUM], (380, 240))
            
        elif core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] == 2:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_FAST], (380, 240))

    #large screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        if core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] == 0:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_SLOW], (554, 275))
            
        elif core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] == 1:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_MEDIUM], (554, 275))
            
        elif core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] == 2:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_FAST], (554, 275))

def playmenu_check_ballsize(core_game, core_entities, core_ui, core_sound):
    """Check ball size

    Checks the current value of the ball size
    and displays it based on screen size
    """

    #small screen
    if core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        for i in range(0,3):
            if core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == i:
                core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][i + 1], (300, 260))

    #medium screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        for i in range(0,3):
            if core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == i:
                core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][i + 1], (380, 330))

    #large screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        for i in range(0,3):
            if core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] == i:
                core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][i + 1], (554, 400))

#options menu

def optionsmenu_check_effects(core_game, core_entities, core_ui, core_sound):
    """Check sound effects

    Checks the current state of the sound effects
    and displays it based on screen size
    """

    #small screen
    if core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_ON], (310, 200))
        else:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_OFF], (310, 200))

    #medium screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_ON], (385, 265))
        else:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_OFF], (385, 265))

    #large screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_ON], (535, 300))
        else:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_OFF], (535, 300))

def optionsmenu_check_music(core_game, core_entities, core_ui, core_sound):
    """Check sound music

    Checks the current state of the sound music
    and displays it based on screen size
    """

    #small screen
    if core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        if core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_ON], (310, 275))
        else:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_OFF], (310, 275))

    #medium screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        if core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_ON], (385, 385))
        else:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_OFF], (385, 385))

    #large screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        if core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_ON], (535, 450))
        else:
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_OFF], (535, 450))

#event functions

#main menu

def mainmenu_event_button_down(core_game, core_entities, core_ui, core_sound):
    """Main menu mouse down click event

    Executes when the left mouse button is clicked
    and evaluates which button the user clicked

    The mouse down events are used for
    the button click sound effects

    If the sound effect game option is set
    to off, the clicks will not play
    """

    pos = pygame.mouse.get_pos()

    #small screen
    if core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        #play button
        if (pos[0] >= 50 and pos[0] <= 200) and (pos[1] >= 240 and pos[1] <= 290):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()
            
        #options button
        elif (pos[0] >= 50 and pos[0] <= 300) and (pos[1] >= 320 and pos[1] <= 370):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()

    #medium screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        #play button
        if (pos[0] >= 50 and pos[0] <= 200) and (pos[1] >= 340 and pos[1] <= 390):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()
            
        #options button
        elif (pos[0] >= 50 and pos[0] <= 300) and (pos[1] >= 420 and pos[1] <= 470):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()

    #large screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        #play button
        if (pos[0] >= 50 and pos[0] <= 200) and (pos[1] >= 440 and pos[1] <= 490):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()
            
        #options button
        elif (pos[0] >= 50 and pos[0] <= 300) and (pos[1] >= 520 and pos[1] <= 570):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()

def mainmenu_event_button_up(core_game, core_entities, core_ui, core_sound):
    """"Main menu mouse up click event

    Executes when the left mouse button is released
    and evaluates which button the user clicked

    The mouse up events are used for
    the button event execution
    """

    pos = pygame.mouse.get_pos()
    
    #small screen
    if core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        #play button
        if (pos[0] >= 50 and pos[0] <= 200) and (pos[1] >= 240 and pos[1] <= 290):
            game_playmenu(core_game,core_entities,core_ui,core_sound)
            
        #options button
        elif (pos[0] >= 50 and pos[0] <= 300) and (pos[1] >= 320 and pos[1] <= 370):
            game_optionsmenu(core_game,core_entities,core_ui,core_sound)
            
        #quit button
        elif (pos[0] >= 50 and pos[0] <= 200) and (pos[1] >= 400 and pos[1] <= 450):
            core_game[ALL_MAIN_ALL][MAIN_MENU_CONTROL] = False

    #medium screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        #play button
        if (pos[0] >= 50 and pos[0] <= 200) and (pos[1] >= 340 and pos[1] <= 390):
            game_playmenu(core_game,core_entities,core_ui,core_sound)
            
        #options button
        elif (pos[0] >= 50 and pos[0] <= 300) and (pos[1] >= 420 and pos[1] <= 470):
            game_optionsmenu(core_game,core_entities,core_ui,core_sound)
            
        #quit button
        elif (pos[0] >= 50 and pos[0] <= 200) and (pos[1] >= 500 and pos[1] <= 550):
            core_game[ALL_MAIN_ALL][MAIN_MENU_CONTROL] = False

    #large screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        #play button
        if (pos[0] >= 50 and pos[0] <= 200) and (pos[1] >= 440 and pos[1] <= 490):
            game_playmenu(core_game,core_entities,core_ui,core_sound)
            
        #options button
        elif (pos[0] >= 50 and pos[0] <= 300) and (pos[1] >= 520 and pos[1] <= 570):
            game_optionsmenu(core_game,core_entities,core_ui,core_sound)
            
        #quit button
        elif (pos[0] >= 50 and pos[0] <= 200) and (pos[1] >= 600 and pos[1] <= 650):
            core_game[ALL_MAIN_ALL][MAIN_MENU_CONTROL] = False

def mainmenu_event_display(core_game, core_entities, core_ui, core_sound):
    """Main menu display event

    Displays the ui for the main menu
    when the user is in it
    """

    #small screen
    if core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_SMALL], (0, 0))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_SMALL].blit(core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_IMAGE_SMALL], (0, 0))

        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI][MAINMENU_UI_LOGO_SMALL], (175, 25))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI][MAINMENU_UI_PLAY], (50, 240))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI][MAINMENU_UI_OPTIONS], (50, 320))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI][MAINMENU_UI_QUIT], (50, 400))

    #medium screen    
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_MEDIUM], (0, 0))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_MEDIUM].blit(core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_IMAGE_MEDIUM], (0, 0))

        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI][MAINMENU_UI_LOGO_MEDIUM], (250, 25))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI][MAINMENU_UI_PLAY], (50, 340))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI][MAINMENU_UI_OPTIONS], (50, 420))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI][MAINMENU_UI_QUIT], (50, 500))

    #large screen    
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_LARGE], (0, 0))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_LARGE].blit(core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_IMAGE_LARGE], (0, 0))

        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI][MAINMENU_UI_LOGO_LARGE], (300, 35))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI][MAINMENU_UI_PLAY], (50, 440))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI][MAINMENU_UI_OPTIONS], (50, 520))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI][MAINMENU_UI_QUIT], (50, 600))

#play menu

def playmenu_event_button_down(core_game, core_entities, core_ui, core_sound):
    """Play menu mouse down click event

    Executes when the left mouse button is clicked
    and evaluates which button the user clicked

    The mouse down events are used for
    the button click sound effects

    If the sound effect game option is set
    to off, the clicks will not play
    """
    
    pos = pygame.mouse.get_pos()

    #small screen
    if core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        #max rounds left button
        if (pos[0] >= 258 and pos[0] <= 293) and (pos[1] >= 128 and pos[1] <= 163):
            if core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] > 3:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON].play()
            else:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON_STOP].play()
            
        #max rounds right button
        elif (pos[0] >= 358 and pos[0] <= 393) and (pos[1] >= 128 and pos[1] <= 163):
            if core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] < 10:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON].play()
            else:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON_STOP].play()
            
        #ball speed left button
        elif (pos[0] >= 258 and pos[0] <= 293) and (pos[1] >= 198 and pos[1] <= 233):
            if core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] > 0:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON].play()
            else:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON_STOP].play()
            
        #ball speed right button
        elif (pos[0] >= 508 and pos[0] <= 543) and (pos[1] >= 198 and pos[1] <= 233):
            if core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] < 2:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON].play()
            else:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON_STOP].play()
            
        #ball size left button
        elif (pos[0] >= 258 and pos[0] <= 293) and (pos[1] >= 268 and pos[1] <= 303):
            if core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] > 0:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON].play()
            else:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON_STOP].play()
            
        #ball size right button
        elif (pos[0] >= 508 and pos[0] <= 543) and (pos[1] >= 268 and pos[1] <= 303):
            if core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] < 2:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON].play()
            else:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON_STOP].play()
            
        #start button
        elif (pos[0] >= 258 and pos[0] <= 383) and (pos[1] >= 330 and pos[1] <= 380):
            pass
            
        #back button
        elif (pos[0] >= 258 and pos[0] <= 383) and (pos[1] >= 400 and pos[1] <= 450):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()

    #medium screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        #max rounds left button
        if (pos[0] >= 338 and pos[0] <= 373) and (pos[1] >= 158 and pos[1] <= 193):
            if core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] > 3:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON].play()
            else:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON_STOP].play()
            
        #max rounds right button
        elif (pos[0] >= 438 and pos[0] <= 473) and (pos[1] >= 158 and pos[1] <= 193):
            if core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] < 10:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON].play()
            else:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON_STOP].play()
            
        #ball speed left button
        elif (pos[0] >= 338 and pos[0] <= 373) and (pos[1] >= 248 and pos[1] <= 283):
            if core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] > 0:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON].play()
            else:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON_STOP].play()
            
        #ball speed right button
        elif (pos[0] >= 588 and pos[0] <= 623) and (pos[1] >= 248 and pos[1] <= 283):
            if core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] < 2:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON].play()
            else:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON_STOP].play()
            
        #ball size left button
        elif (pos[0] >= 338 and pos[0] <= 373) and (pos[1] >= 338 and pos[1] <= 373):
            if core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] > 0:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON].play()
            else:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON_STOP].play()
            
        #ball size right button
        elif (pos[0] >= 588 and pos[0] <= 623) and (pos[1] >= 338 and pos[1] <= 373):
            if core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] < 2:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON].play()
            else:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON_STOP].play()
            
        #start button
        elif (pos[0] >= 338 and pos[0] <= 463) and (pos[1] >= 410 and pos[1] <= 460):
            pass
            
        #back button
        elif (pos[0] >= 338 and pos[0] <= 463) and (pos[1] >= 495 and pos[1] <= 545):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()

    #large screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        #max rounds left button
        if (pos[0] >= 512 and pos[0] <= 547) and (pos[1] >= 158 and pos[1] <= 193):
            if core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] > 3:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON].play()
            else:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON_STOP].play()
            
        #max rounds right button
        elif (pos[0] >= 612 and pos[0] <= 647) and (pos[1] >= 158 and pos[1] <= 193):
            if core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] < 10:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON].play()
            else:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON_STOP].play()
            
        #ball speed left button
        elif (pos[0] >= 512 and pos[0] <= 547) and (pos[1] >= 283 and pos[1] <= 318):
            if core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] > 0:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON].play()
            else:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON_STOP].play()
            
        #ball speed right button
        elif (pos[0] >= 762 and pos[0] <= 797) and (pos[1] >= 283 and pos[1] <= 318):
            if core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] < 2:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON].play()
            else:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON_STOP].play()
            
        #ball size left button
        elif (pos[0] >= 512 and pos[0] <= 547) and (pos[1] >= 408 and pos[1] <= 443):
            if core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] > 0:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON].play()
            else:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON_STOP].play()
            
        #ball size right button
        elif (pos[0] >= 762 and pos[0] <= 797) and (pos[1] >= 408 and pos[1] <= 443):
            if core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] < 2:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON].play()
            else:
                if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                    core_sound[ALL_SOUND_BUTTON_STOP].play()
            
        #start button
        elif (pos[0] >= 450 and pos[0] <= 575) and (pos[1] >= 500 and pos[1] <= 550):
            pass
            
        #back button
        elif (pos[0] >= 450 and pos[0] <= 575) and (pos[1] >= 600 and pos[1] <= 650):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()

def playmenu_event_button_up(core_game, core_entities, core_ui, core_sound):
    """"Play menu mouse up click event

    Executes when the left mouse button is released
    and evaluates which button the user clicked

    The mouse up events are used for
    the button event execution
    """
    
    pos = pygame.mouse.get_pos()
    
    #small screen
    if core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        #max rounds left button
        if (pos[0] >= 258 and pos[0] <= 293) and (pos[1] >= 128 and pos[1] <= 163):
            if core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] > 3:
                core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] -= 1
            
        #max rounds right button
        elif (pos[0] >= 358 and pos[0] <= 393) and (pos[1] >= 128 and pos[1] <= 163):
            if core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] < 10:
                core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] += 1
            
        #ball speed left button
        elif (pos[0] >= 258 and pos[0] <= 293) and (pos[1] >= 198 and pos[1] <= 233):
            if core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] > 0:
                core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] -= 1
            
        #ball speed right button
        elif (pos[0] >= 508 and pos[0] <= 543) and (pos[1] >= 198 and pos[1] <= 233):
            if core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] < 2:
                core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] += 1
            
        #ball size left button
        elif (pos[0] >= 258 and pos[0] <= 293) and (pos[1] >= 268 and pos[1] <= 303):
            if core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] > 0:
                core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] -= 1
            
        #ball size right button
        elif (pos[0] >= 508 and pos[0] <= 543) and (pos[1] >= 268 and pos[1] <= 303):
            if core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] < 2:
                core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] += 1
            
        #start button
        elif (pos[0] >= 258 and pos[0] <= 383) and (pos[1] >= 330 and pos[1] <= 380):
            game_exec(core_game,core_entities,core_ui,core_sound)
            return
            
        #back button
        elif (pos[0] >= 258 and pos[0] <= 383) and (pos[1] >= 400 and pos[1] <= 450):
            core_game[ALL_MAIN_ALL][MAIN_MENU_PLAY] = False
            return

    #medium screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        #max rounds left button
        if (pos[0] >= 338 and pos[0] <= 373) and (pos[1] >= 158 and pos[1] <= 193):
            if core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] > 3:
                core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] -= 1
            
        #max rounds right button
        elif (pos[0] >= 438 and pos[0] <= 473) and (pos[1] >= 158 and pos[1] <= 193):
            if core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] < 10:
                core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] += 1
            
        #ball speed left button
        elif (pos[0] >= 338 and pos[0] <= 373) and (pos[1] >= 248 and pos[1] <= 283):
            if core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] > 0:
                core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] -= 1
            
        #ball speed right button
        elif (pos[0] >= 588 and pos[0] <= 623) and (pos[1] >= 248 and pos[1] <= 283):
            if core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] < 2:
                core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] += 1
            
        #ball size left button
        elif (pos[0] >= 338 and pos[0] <= 373) and (pos[1] >= 338 and pos[1] <= 373):
            if core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] > 0:
                core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] -= 1
            
        #ball size right button
        elif (pos[0] >= 588 and pos[0] <= 623) and (pos[1] >= 338 and pos[1] <= 373):
            if core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] < 2:
                core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] += 1
            
        #start button
        elif (pos[0] >= 338 and pos[0] <= 463) and (pos[1] >= 410 and pos[1] <= 460):
            game_exec(core_game,core_entities,core_ui,core_sound)
            return
            
        #back button
        elif (pos[0] >= 338 and pos[0] <= 463) and (pos[1] >= 495 and pos[1] <= 545):
            core_game[ALL_MAIN_ALL][MAIN_MENU_PLAY] = False
            return

    #large screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        #max rounds left button
        if (pos[0] >= 512 and pos[0] <= 547) and (pos[1] >= 158 and pos[1] <= 193):
            if core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] > 3:
                core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] -= 1
            
        #max rounds right button
        elif (pos[0] >= 612 and pos[0] <= 647) and (pos[1] >= 158 and pos[1] <= 193):
            if core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] < 10:
                core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] += 1
            
        #ball speed left button
        elif (pos[0] >= 512 and pos[0] <= 547) and (pos[1] >= 283 and pos[1] <= 318):
            if core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] > 0:
                core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] -= 1
            
        #ball speed right button
        elif (pos[0] >= 762 and pos[0] <= 797) and (pos[1] >= 283 and pos[1] <= 318):
            if core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] < 2:
                core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] += 1
            
        #ball size left button
        elif (pos[0] >= 512 and pos[0] <= 547) and (pos[1] >= 408 and pos[1] <= 443):
            if core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] > 0:
                core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] -= 1
            
        #ball size right button
        elif (pos[0] >= 762 and pos[0] <= 797) and (pos[1] >= 408 and pos[1] <= 443):
            if core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] < 2:
                core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] += 1
            
        #start button
        elif (pos[0] >= 450 and pos[0] <= 575) and (pos[1] >= 500 and pos[1] <= 550):
            game_exec(core_game,core_entities,core_ui,core_sound)
            return
            
        #back button
        elif (pos[0] >= 450 and pos[0] <= 575) and (pos[1] >= 600 and pos[1] <= 650):
            core_game[ALL_MAIN_ALL][MAIN_MENU_PLAY] = False
            return

def playmenu_event_display(core_game, core_entities, core_ui, core_sound):
    """Play menu display event

    Displays the ui for the play menu
    when the user is in it
    """

    #small screen    
    if core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_SMALL], (0, 0))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_SMALL].blit(core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_IMAGE_SMALL], (0, 0))

        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI][MAINMENU_UI_PLAY], (245, 50))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_PLAY][PLAY_MAXROUNDS], (50, 120))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_PLAY][PLAY_BALLSPEED], (50, 190))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_PLAY][PLAY_BALLSIZE], (50, 260))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_PLAY][PLAY_START], (258, 330))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_BACK], (258, 400))
        
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_LEFT], (258, 128))
        playmenu_check_maxrounds(core_game,core_entities,core_ui,core_sound)
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_RIGHT], (358, 128))
        
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_LEFT], (258, 198))
        playmenu_check_ballspeed(core_game,core_entities,core_ui,core_sound)
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_RIGHT], (508, 198))
        
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_LEFT], (258, 268))
        playmenu_check_ballsize(core_game,core_entities,core_ui,core_sound)
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_RIGHT], (508, 268))

    #medium screen        
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_MEDIUM], (0, 0))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_MEDIUM].blit(core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_IMAGE_MEDIUM], (0, 0))

        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI][MAINMENU_UI_PLAY], (338, 50))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_PLAY][PLAY_MAXROUNDS], (130, 150))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_PLAY][PLAY_BALLSPEED], (130, 240))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_PLAY][PLAY_BALLSIZE], (130, 330))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_PLAY][PLAY_START], (338, 410))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_BACK], (338, 495))
        
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_LEFT], (338, 158))
        playmenu_check_maxrounds(core_game,core_entities,core_ui,core_sound)
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_RIGHT], (438, 158))
        
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_LEFT], (338, 248))
        playmenu_check_ballspeed(core_game,core_entities,core_ui,core_sound)
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_RIGHT], (588, 248))
        
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_LEFT], (338, 338))
        playmenu_check_ballsize(core_game,core_entities,core_ui,core_sound)
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_RIGHT], (588, 338))

    #large screen       
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_LARGE], (0, 0))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_LARGE].blit(core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_IMAGE_LARGE], (0, 0))

        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI][MAINMENU_UI_PLAY], (450, 50))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_PLAY][PLAY_MAXROUNDS], (304, 150))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_PLAY][PLAY_BALLSPEED], (304, 275))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_PLAY][PLAY_BALLSIZE], (304, 400))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_PLAY][PLAY_START], (450, 500))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_BACK], (450, 600))
        
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_LEFT], (512, 158))
        playmenu_check_maxrounds(core_game,core_entities,core_ui,core_sound)
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_RIGHT], (612, 158))
        
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_LEFT], (512, 283))
        playmenu_check_ballspeed(core_game,core_entities,core_ui,core_sound)
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_RIGHT], (762, 283))
        
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_LEFT], (512, 408))
        playmenu_check_ballsize(core_game,core_entities,core_ui,core_sound)
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_RIGHT], (762, 408))

#options menu
        
def optionsmenu_event_button_down(core_game, core_entities, core_ui, core_sound):
    """Options menu mouse down click event

    Executes when the left mouse button is clicked
    and evaluates which button the user clicked

    The mouse down events are used for
    the button click sound effects

    If the sound effect game option is set
    to off, the clicks will not play
    """

    pos = pygame.mouse.get_pos()

    #small screen
    if core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        #screen size left button
        if (pos[0] >= 275 and pos[0] <= 310) and (pos[1] >= 133 and pos[1] <= 168):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON_STOP].play()
                
        #screen size right button
        elif (pos[0] >= 510 and pos[0] <= 545) and (pos[1] >= 133 and pos[1] <= 168):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()
                
        #sound effects left button
        elif (pos[0] >= 275 and pos[0] <= 310) and (pos[1] >= 208 and pos[1] <= 243):
            core_sound[ALL_SOUND_BUTTON].play()
                
        #sound effects right button
        elif (pos[0] >= 410 and pos[0] <= 445) and (pos[1] >= 208 and pos[1] <= 243):
            core_sound[ALL_SOUND_BUTTON].play()
                
        #sound music left button
        elif (pos[0] >= 275 and pos[0] <= 310) and (pos[1] >= 283 and pos[1] <= 318):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()
                
        #sound music right button
        elif (pos[0] >= 410 and pos[0] <= 445) and (pos[1] >= 283 and pos[1] <= 318):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()
            
        #back button
        elif (pos[0] >= 278 and pos[0] <= 403) and (pos[1] >= 350 and pos[1] <= 400):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()

    #medium screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        #screen size left button
        if (pos[0] >= 350 and pos[0] <= 385) and (pos[1] >= 158 and pos[1] <= 193):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()
                
        #screen size right button
        elif (pos[0] >= 585 and pos[0] <= 620) and (pos[1] >= 158 and pos[1] <= 193):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()
                
        #sound effects left button
        elif (pos[0] >= 350 and pos[0] <= 385) and (pos[1] >= 273 and pos[1] <= 308):
            core_sound[ALL_SOUND_BUTTON].play()
                
        #sound effects right button
        elif (pos[0] >= 485 and pos[0] <= 520) and (pos[1] >= 273 and pos[1] <= 308):
            core_sound[ALL_SOUND_BUTTON].play()
                
        #sound music left button
        elif (pos[0] >= 350 and pos[0] <= 385) and (pos[1] >= 393 and pos[1] <= 428):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()
                
        #sound music right button
        elif (pos[0] >= 485 and pos[0] <= 520) and (pos[1] >= 393 and pos[1] <= 428):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()
            
        #back button
        elif (pos[0] >= 338 and pos[0] <= 463) and (pos[1] >= 485 and pos[1] <= 535):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()

    #large screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        #screen size left button
        if (pos[0] >= 500 and pos[0] <= 535) and (pos[1] >= 158 and pos[1] <= 193):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()
                
        #screen size right button
        elif (pos[0] >= 735 and pos[0] <= 770) and (pos[1] >= 158 and pos[1] <= 193):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON_STOP].play()
                
        #sound effects left button
        elif (pos[0] >= 500 and pos[0] <= 535) and (pos[1] >= 308 and pos[1] <= 343):
            core_sound[ALL_SOUND_BUTTON].play()
                
        #sound effects right button
        elif (pos[0] >= 635 and pos[0] <= 670) and (pos[1] >= 308 and pos[1] <= 343):
            core_sound[ALL_SOUND_BUTTON].play()
                
        #sound music left button
        elif (pos[0] >= 500 and pos[0] <= 535) and (pos[1] >= 458 and pos[1] <= 493):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()
                
        #sound music right button
        elif (pos[0] >= 635 and pos[0] <= 670) and (pos[1] >= 458 and pos[1] <= 493):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()
            
        #back button
        elif (pos[0] >= 488 and pos[0] <= 613) and (pos[1] >= 575 and pos[1] <= 625):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_sound[ALL_SOUND_BUTTON].play()

def optionsmenu_event_button_up(core_game, core_entities, core_ui, core_sound):
    """"Options menu mouse up click event

    Executes when the left mouse button is released
    and evaluates which button the user clicked

    The mouse up events are used for
    the button event execution
    """

    pos = pygame.mouse.get_pos()
    
    #small screen
    if core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        #screen size left button
        if (pos[0] >= 275 and pos[0] <= 310) and (pos[1] >= 133 and pos[1] <= 168):
            pass
                
        #screen size right button
        elif (pos[0] >= 510 and pos[0] <= 545) and (pos[1] >= 133 and pos[1] <= 168):
            core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] = 1
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN] = pygame.display.set_mode(SCREEN_SIZE_MEDIUM)
                
        #sound effects left button
        elif (pos[0] >= 275 and pos[0] <= 310) and (pos[1] >= 208 and pos[1] <= 243):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] = False
            else:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] = True

            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] == False:
                core_sound[ALL_SOUND_BUTTON].stop()
                core_sound[ALL_SOUND_BUTTON_STOP].stop()
                
        #sound effects right button
        elif (pos[0] >= 410 and pos[0] <= 445) and (pos[1] >= 208 and pos[1] <= 243):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] = False
            else:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] = True

            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] == False:
                core_sound[ALL_SOUND_BUTTON].stop()
                core_sound[ALL_SOUND_BUTTON_STOP].stop()
                
        #sound music left button
        elif (pos[0] >= 275 and pos[0] <= 310) and (pos[1] >= 283 and pos[1] <= 318):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC] = False
            else:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC] = True

            if core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                core_sound[ALL_SOUND_MAINMENU].stop()
                core_sound[ALL_SOUND_MAINMENU_OTHER].play()
            else:
                core_sound[ALL_SOUND_MAINMENU].stop()
                core_sound[ALL_SOUND_MAINMENU_OTHER].stop()
                
        #sound music right button
        elif (pos[0] >= 410 and pos[0] <= 445) and (pos[1] >= 283 and pos[1] <= 318):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC] = False
            else:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC] = True

            if core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                core_sound[ALL_SOUND_MAINMENU].stop()
                core_sound[ALL_SOUND_MAINMENU_OTHER].play()
            else:
                core_sound[ALL_SOUND_MAINMENU].stop()
                core_sound[ALL_SOUND_MAINMENU_OTHER].stop()
            
        #back button
        elif (pos[0] >= 278 and pos[0] <= 403) and (pos[1] >= 350 and pos[1] <= 400):
            core_game[ALL_MAIN_ALL][MAIN_MENU_OPTIONS] = False
            return

    #medium screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        #screen size left button
        if (pos[0] >= 350 and pos[0] <= 385) and (pos[1] >= 158 and pos[1] <= 193):
            core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] = 0
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN] = pygame.display.set_mode(SCREEN_SIZE_SMALL)
                
        #screen size right button
        elif (pos[0] >= 585 and pos[0] <= 620) and (pos[1] >= 158 and pos[1] <= 193):
            core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] = 2
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN] = pygame.display.set_mode(SCREEN_SIZE_LARGE)
                
        #sound effects left button
        elif (pos[0] >= 350 and pos[0] <= 385) and (pos[1] >= 273 and pos[1] <= 308):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] = False
            else:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] = True

            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] == False:
                core_sound[ALL_SOUND_BUTTON].stop()
                core_sound[ALL_SOUND_BUTTON_STOP].stop()
                
        #sound effects right button
        elif (pos[0] >= 485 and pos[0] <= 520) and (pos[1] >= 273 and pos[1] <= 308):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] = False
            else:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] = True

            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] == False:
                core_sound[ALL_SOUND_BUTTON].stop()
                core_sound[ALL_SOUND_BUTTON_STOP].stop()
                
        #sound music left button
        elif (pos[0] >= 350 and pos[0] <= 385) and (pos[1] >= 393 and pos[1] <= 428):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC] = False
            else:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC] = True

            if core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                core_sound[ALL_SOUND_MAINMENU].stop()
                core_sound[ALL_SOUND_MAINMENU_OTHER].play()
            else:
                core_sound[ALL_SOUND_MAINMENU].stop()
                core_sound[ALL_SOUND_MAINMENU_OTHER].stop()
                
        #sound music right button
        elif (pos[0] >= 485 and pos[0] <= 520) and (pos[1] >= 393 and pos[1] <= 428):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC] = False
            else:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC] = True

            if core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                core_sound[ALL_SOUND_MAINMENU].stop()
                core_sound[ALL_SOUND_MAINMENU_OTHER].play()
            else:
                core_sound[ALL_SOUND_MAINMENU].stop()
                core_sound[ALL_SOUND_MAINMENU_OTHER].stop()
            
        #back button
        elif (pos[0] >= 338 and pos[0] <= 463) and (pos[1] >= 485 and pos[1] <= 535):
            core_game[ALL_MAIN_ALL][MAIN_MENU_OPTIONS] = False
            return

    #large screen
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        #screen size left button
        if (pos[0] >= 500 and pos[0] <= 535) and (pos[1] >= 158 and pos[1] <= 193):
            core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] = 1
            core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN] = pygame.display.set_mode(SCREEN_SIZE_MEDIUM)
                
        #screen size right button
        elif (pos[0] >= 735 and pos[0] <= 770) and (pos[1] >= 158 and pos[1] <= 193):
            pass
                
        #sound effects left button
        elif (pos[0] >= 500 and pos[0] <= 535) and (pos[1] >= 308 and pos[1] <= 343):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] = False
            else:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] = True

            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] == False:
                core_sound[ALL_SOUND_BUTTON].stop()
                core_sound[ALL_SOUND_BUTTON_STOP].stop()
                
        #sound effects right button
        elif (pos[0] >= 635 and pos[0] <= 670) and (pos[1] >= 308 and pos[1] <= 343):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS]:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] = False
            else:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] = True

            if core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] == False:
                core_sound[ALL_SOUND_BUTTON].stop()
                core_sound[ALL_SOUND_BUTTON_STOP].stop()
                
        #sound music left button
        elif (pos[0] >= 500 and pos[0] <= 535) and (pos[1] >= 458 and pos[1] <= 493):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC] = False
            else:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC] = True

            if core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                core_sound[ALL_SOUND_MAINMENU].stop()
                core_sound[ALL_SOUND_MAINMENU_OTHER].play()
            else:
                core_sound[ALL_SOUND_MAINMENU].stop()
                core_sound[ALL_SOUND_MAINMENU_OTHER].stop()
                
        #sound music right button
        elif (pos[0] >= 635 and pos[0] <= 670) and (pos[1] >= 458 and pos[1] <= 493):
            if core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC] = False
            else:
                core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC] = True

            if core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
                core_sound[ALL_SOUND_MAINMENU].stop()
                core_sound[ALL_SOUND_MAINMENU_OTHER].play()
            else:
                core_sound[ALL_SOUND_MAINMENU].stop()
                core_sound[ALL_SOUND_MAINMENU_OTHER].stop()
            
        #back button
        elif (pos[0] >= 488 and pos[0] <= 613) and (pos[1] >= 575 and pos[1] <= 625):
            core_game[ALL_MAIN_ALL][MAIN_MENU_OPTIONS] = False
            return

def optionsmenu_event_display(core_game, core_entities, core_ui, core_sound):
    """Options menu display event

    Displays the ui for the options menu
    when the user is in it
    """

    #small screen    
    if core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_SMALL], (0, 0))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_SMALL].blit(core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_IMAGE_SMALL], (0, 0))

        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI][MAINMENU_UI_OPTIONS], (195, 50))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_OPTIONS][OPTIONS_SCREENSIZE], (25, 125))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_OPTIONS][OPTIONS_EFFECTS], (25, 200))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_OPTIONS][OPTIONS_MUSIC], (25, 275))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_BACK], (278, 350))

        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_LEFT], (275, 133))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_SMALL], (310, 125))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_RIGHT], (510, 133))

        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_LEFT], (275, 208))
        optionsmenu_check_effects(core_game,core_entities,core_ui,core_sound)
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_RIGHT], (410, 208))

        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_LEFT], (275, 283))
        optionsmenu_check_music(core_game,core_entities,core_ui,core_sound)
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_RIGHT], (410, 283))

    #medium screen        
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_MEDIUM], (0, 0))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_MEDIUM].blit(core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_IMAGE_MEDIUM], (0, 0))

        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI][MAINMENU_UI_OPTIONS], (275, 50))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_OPTIONS][OPTIONS_SCREENSIZE], (100, 150))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_OPTIONS][OPTIONS_EFFECTS], (100, 265))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_OPTIONS][OPTIONS_MUSIC], (100, 385))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_BACK], (338, 485))

        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_LEFT], (350, 158))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_MEDIUM], (385, 150))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_RIGHT], (585, 158))

        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_LEFT], (350, 273))
        optionsmenu_check_effects(core_game,core_entities,core_ui,core_sound)
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_RIGHT], (485, 273))

        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_LEFT], (350, 393))
        optionsmenu_check_music(core_game,core_entities,core_ui,core_sound)
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_RIGHT], (485, 393))

    #large screen        
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_LARGE], (0, 0))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_LARGE].blit(core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_IMAGE_LARGE], (0, 0))

        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI][MAINMENU_UI_OPTIONS], (387, 50))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_OPTIONS][OPTIONS_SCREENSIZE], (250, 150))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_OPTIONS][OPTIONS_EFFECTS], (250, 300))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_OPTIONS][OPTIONS_MUSIC], (250, 450))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_BACK], (488, 575))

        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_LEFT], (500, 158))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_LARGE], (535, 150))
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_RIGHT], (735, 158))

        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_LEFT], (500, 308))
        optionsmenu_check_effects(core_game,core_entities,core_ui,core_sound)
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_RIGHT], (635, 308))

        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_LEFT], (500, 458))
        optionsmenu_check_music(core_game,core_entities,core_ui,core_sound)
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN].blit(core_ui[ALL_MAIN_UI_COMMON][COMMON_UI_RIGHT], (635, 458))
