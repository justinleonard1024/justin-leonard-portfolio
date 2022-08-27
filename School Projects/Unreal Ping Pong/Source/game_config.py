"""
Unreal Ping Pong
game_config.py
Created by Justin Leonard

Contains functions for game configurations
Game settings are obtained and set
The initial display and entity settings are also initialized
"""

#initialize
import os
import pygame
import string
import ConfigParser
from game_globals import *

#functions
def config_display(core_game, core_entities, core_ui, core_sound):
    """Sets the initial display settings

    Title of program and screen size are set
    Entities and surfaces are filled
    Main menu music is played
    """

    #display
    pygame.display.set_caption("Unreal Ping Pong")

    if core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 0:
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN] = pygame.display.set_mode(SCREEN_SIZE_SMALL)
        
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 1:
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN] = pygame.display.set_mode(SCREEN_SIZE_MEDIUM)
        
    elif core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] == 2:
        core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_SCREEN] = pygame.display.set_mode(SCREEN_SIZE_LARGE)

    #surfaces
    core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_SMALL].fill((255,255,255))
    core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_MEDIUM].fill((255,255,255))
    core_ui[ALL_MAIN_UI_BACKGROUND][MAINMENU_UIBG_BACK_LARGE].fill((255,255,255))

    core_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_SMALL].fill((255,255,255))
    core_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_MEDIUM].fill((255,255,255))
    core_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_GAME_LARGE].fill((255,255,255))

    core_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_SMALL].fill((255,255,255))
    core_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_MEDIUM].fill((255,255,255))
    core_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_RESET_LARGE].fill((255,255,255))

    core_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_BORDER_BLUE_SMALL].fill((0, 128, 255))
    core_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_BORDER_BLUE_MEDIUM].fill((0, 128, 255))
    core_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_BORDER_BLUE_LARGE].fill((0, 128, 255))

    core_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_BORDER_RED_SMALL].fill((255, 128, 0))
    core_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_BORDER_RED_MEDIUM].fill((255, 128, 0))
    core_ui[ALL_MAIN_UI_BACKGROUND][BACKGROUND_BORDER_RED_LARGE].fill((255, 128, 0))

    #music
    if core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC]:
        core_sound[ALL_SOUND_MAINMENU].play()

def config_settings(core_game, core_entities, core_ui, core_sound):
    """Get or set the initial game options from a file

    The file "game_settings.ini" is used and stored in AppData
    If the file does not exist or is corrupt, it will be remade and defualted
    If the values for the sections are corrupt, they will defaulted
    The directory for the file will also be created if it does not exist
    
    If there is no file or content corruption, the variables for
    the game options will be set to those in the settings file
    
    The default values for the game options are
    Screen size: Medium
    Sound effects: On
    Screen music: On
    """
    
    #config
    config_game = ConfigParser.ConfigParser()
    config_dir = string.replace(os.getenv('APPDATA'), "\\", "/") + '/UnrealGames/Pong/'

    #directory for this game exists
    if os.path.exists(config_dir):

        #reads file
        if os.path.exists(config_dir + 'game_settings.ini'):
            config_game.read(config_dir + 'game_settings.ini')

        #settings file for this game exists and has all config info
        if os.path.exists(config_dir + 'game_settings.ini') and (config_game.has_section('GameSettings') and \
                  config_game.has_option('GameSettings', 'settings_maxrounds') and \
                  config_game.has_option('GameSettings', 'settings_ball_speed') and \
                  config_game.has_option('GameSettings', 'settings_ball_size')) and \
                 (config_game.has_section('GameOptions') and \
                  config_game.has_option('GameOptions', 'options_screen') and \
                  config_game.has_option('GameOptions', 'options_sound_effects') and \
                  config_game.has_option('GameOptions', 'options_sound_music')):
            
            config_game.read(config_dir + 'game_settings.ini')

            #get values
            config_maxrounds = config_game.getint('GameSettings', 'settings_maxrounds')
            config_ball_speed = config_game.getint('GameSettings', 'settings_ball_speed')
            config_ball_size = config_game.getint('GameSettings', 'settings_ball_size')

            config_screen = config_game.getint('GameOptions', 'options_screen')
            config_sound_effects = config_game.getboolean('GameOptions', 'options_sound_effects')
            config_sound_music = config_game.getboolean('GameOptions', 'options_sound_music')

            #game settings
            if config_maxrounds < 3 or config_maxrounds > 10:
                core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] = 3
            else:
                core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] = config_maxrounds
                
            if config_ball_speed < 0 or config_ball_speed > 2:
                core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] = 1
            else:
                core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] = config_ball_speed
                
            if config_ball_size < 0 or config_ball_size > 2:
                core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] = 1
            else:
                core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] = config_ball_size

            #game options
            if config_screen < 0 or config_screen > 2:
                core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] = 1
            else:
                core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] = config_screen

            core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] = config_sound_effects
            core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC] = config_sound_music

        #settings file for this game does not exist or it does not have config info
        elif os.path.exists(config_dir + 'game_settings.ini') == False or (config_game.has_section('GameSettings') and \
                  config_game.has_option('GameSettings', 'settings_maxrounds') and \
                  config_game.has_option('GameSettings', 'settings_ball_speed') and \
                  config_game.has_option('GameSettings', 'settings_ball_size')) and \
                 (config_game.has_section('GameOptions') and \
                  config_game.has_option('GameOptions', 'options_screen') and \
                  config_game.has_option('GameOptions', 'options_sound_effects') and \
                  config_game.has_option('GameOptions', 'options_sound_music')) == False:

            config_file_new = open(config_dir + 'game_settings.ini','w+')

            core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] = 3
            core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] = 1
            core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] = 1

            core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] = 1
            core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] = True
            core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC] = True

            config_game.add_section('GameSettings')
            config_game.set('GameSettings', 'settings_maxrounds',core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS])
            config_game.set('GameSettings', 'settings_ball_speed',core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL])
            config_game.set('GameSettings', 'settings_ball_size',core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL])

            config_game.add_section('GameOptions')
            config_game.set('GameOptions', 'options_screen',core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN])
            config_game.set('GameOptions', 'options_sound_effects',core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS])
            config_game.set('GameOptions', 'options_sound_music',core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC])
            config_game.write(config_file_new)
            config_file_new.close()

    #directory for this game does not exist   
    else:
        
        os.makedirs(os.getenv('APPDATA') +'\\UnrealGames\\Pong' )
        config_file_new = open(config_dir + 'game_settings.ini','w+')
        
        core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] = 3
        core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] = 1
        core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] = 1

        core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] = 1
        core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] = True
        core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC] = True

        config_game.add_section('GameSettings')
        config_game.set('GameSettings', 'settings_maxrounds',core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS])
        config_game.set('GameSettings', 'settings_ball_speed',core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL])
        config_game.set('GameSettings', 'settings_ball_size',core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL])

        config_game.add_section('GameOptions')
        config_game.set('GameOptions', 'options_screen',core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN])
        config_game.set('GameOptions', 'options_sound_effects',core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS])
        config_game.set('GameOptions', 'options_sound_music',core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC])
        config_game.write(config_file_new)
        config_file_new.close()

def config_final(core_game, core_entities, core_ui, core_sound):
    """Final game options write

    Game options are written to the game settings file
    
    File or directory corruption will be corrected and a
    new file or directory will be created with defualt settings
    """
    
    #config
    config_game = ConfigParser.ConfigParser()
    config_dir = string.replace(os.getenv('APPDATA'), "\\", "/") + '/UnrealGames/Pong/'

    #directory for this game exists
    if os.path.exists(config_dir):

        #reads file
        if os.path.exists(config_dir + 'game_settings.ini'):
            config_game.read(config_dir + 'game_settings.ini')

        #settings file for this game exists and has all config info
        if os.path.exists(config_dir + 'game_settings.ini') and (config_game.has_section('GameSettings') and \
                  config_game.has_option('GameSettings', 'settings_maxrounds') and \
                  config_game.has_option('GameSettings', 'settings_ball_speed') and \
                  config_game.has_option('GameSettings', 'settings_ball_size')) and \
                 (config_game.has_section('GameOptions') and \
                  config_game.has_option('GameOptions', 'options_screen') and \
                  config_game.has_option('GameOptions', 'options_sound_effects') and \
                  config_game.has_option('GameOptions', 'options_sound_music')):
            
            config_file = open(config_dir + 'game_settings.ini','w')
            config_game.set('GameSettings', 'settings_maxrounds',core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS])
            config_game.set('GameSettings', 'settings_ball_speed',core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL])
            config_game.set('GameSettings', 'settings_ball_size',core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL])
            config_game.set('GameOptions', 'options_screen',core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN])
            config_game.set('GameOptions', 'options_sound_effects',core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS])
            config_game.set('GameOptions', 'options_sound_music',core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC])
            config_game.write(config_file)
            config_file.close()

        #settings file for this game does not exist or it does not have config info
        elif os.path.exists(config_dir + 'game_settings.ini') == False or (config_game.has_section('GameSettings') and \
                  config_game.has_option('GameSettings', 'settings_maxrounds') and \
                  config_game.has_option('GameSettings', 'settings_ball_speed') and \
                  config_game.has_option('GameSettings', 'settings_ball_size')) and \
                 (config_game.has_section('GameOptions') and \
                  config_game.has_option('GameOptions', 'options_screen') and \
                  config_game.has_option('GameOptions', 'options_sound_effects') and \
                  config_game.has_option('GameOptions', 'options_sound_music')) == False:

            config_file_new = open(config_dir + 'game_settings.ini','w+')

            core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] = 3
            core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] = 1
            core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] = 1

            core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] = 1
            core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] = True
            core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC] = True

            config_game.add_section('GameSettings')
            config_game.set('GameSettings', 'settings_maxrounds',core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS])
            config_game.set('GameSettings', 'settings_ball_speed',core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL])
            config_game.set('GameSettings', 'settings_ball_size',core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL])

            config_game.add_section('GameOptions')
            config_game.set('GameOptions', 'options_screen',core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN])
            config_game.set('GameOptions', 'options_sound_effects',core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS])
            config_game.set('GameOptions', 'options_sound_music',core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC])
            config_game.write(config_file_new)
            config_file_new.close()

    #directory for this game does not exist   
    else:
        
        os.makedirs(os.getenv('APPDATA') +'\\UnrealGames\\Pong' )
        config_file_new = open(config_dir + 'game_settings.ini','w+')
        
        core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS] = 3
        core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL] = 1
        core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL] = 1

        core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN] = 1
        core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS] = True
        core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC] = True

        config_game.add_section('GameSettings')
        config_game.set('GameSettings', 'settings_maxrounds',core_game[ALL_MAIN_ALL][MAIN_MAX_ROUNDS])
        config_game.set('GameSettings', 'settings_ball_speed',core_game[ALL_MAIN_ALL][MAIN_SPEED_BALL])
        config_game.set('GameSettings', 'settings_ball_size',core_game[ALL_MAIN_ALL][MAIN_SIZE_BALL])

        config_game.add_section('GameOptions')
        config_game.set('GameOptions', 'options_screen',core_game[ALL_MAIN_ALL][MAIN_SIZE_SCREEN])
        config_game.set('GameOptions', 'options_sound_effects',core_game[ALL_MAIN_ALL][MAIN_SOUND_EFFECTS])
        config_game.set('GameOptions', 'options_sound_music',core_game[ALL_MAIN_ALL][MAIN_SOUND_MUSIC])
        config_game.write(config_file_new)
        config_file_new.close()
