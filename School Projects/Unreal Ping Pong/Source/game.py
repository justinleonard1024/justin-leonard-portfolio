"""
Unreal Ping Pong
game.py
Created by Justin Leonard

This is the main file that executes the game
The assets are first stored in lists and then the lists of
assets are compiled into the main lists of their type
The main menu function is executed
"""

#initialize
import pygame
import random
from game_globals import *
from game_main import *
from game_config import *

#initialize pygame
pygame.init()

#game globals
main_all = [0,1,1,3,True,True,True,True,True,False]
main_game = [0,0,30,1,5,5,False,True,[False,True],[True,True,True,True,True,True,True,True,True]]
main_control = [True,False,True,True,True,True,False,False,False,False,False,False,False,False,0,0,True,random.choice(main_game[GAME_LST]),random.choice(main_game[GAME_LST]),random.choice(main_game[GAME_LST])]
main_locations = [0,0,0,0,0,0]

#ui
ui_intro = []
ui_num = []
ui_score = []

for i in range(4):
    ui_intro.append(pygame.image.load("materials/ui/intro/intro_%d.png"%i))

for i in range(11):
    ui_num.append(pygame.image.load("materials/ui/numbers/num_%d.png"%i))

for i in range(11):
    ui_num.append(pygame.image.load("materials/ui/numbers/numlarge_%d.png"%i)) 

for i in range(5):
    ui_score.append(pygame.image.load("materials/ui/score/score_%d.png"%i))

main_ui = []
main_ui.append(pygame.image.load("materials/ui/main_menu/logo_small.png"))
main_ui.append(pygame.image.load("materials/ui/main_menu/logo_medium.png"))
main_ui.append(pygame.image.load("materials/ui/main_menu/logo_large.png"))
main_ui.append(pygame.image.load("materials/ui/main_menu/play.png"))
main_ui.append(pygame.image.load("materials/ui/main_menu/options.png"))
main_ui.append(pygame.image.load("materials/ui/main_menu/quit.png"))

main_ui_common = []
main_ui_common.append(pygame.image.load("materials/ui/common/back.png"))
main_ui_common.append(pygame.image.load("materials/ui/common/small.png"))
main_ui_common.append(pygame.image.load("materials/ui/common/medium.png"))
main_ui_common.append(pygame.image.load("materials/ui/common/large.png"))
main_ui_common.append(pygame.image.load("materials/ui/common/slow.png"))
main_ui_common.append(pygame.image.load("materials/ui/common/fast.png"))
main_ui_common.append(pygame.image.load("materials/ui/common/on.png"))
main_ui_common.append(pygame.image.load("materials/ui/common/off.png"))
main_ui_common.append(pygame.image.load("materials/ui/common/yes.png"))
main_ui_common.append(pygame.image.load("materials/ui/common/no.png"))
main_ui_common.append(pygame.image.load("materials/ui/common/arrow_left.png"))
main_ui_common.append(pygame.image.load("materials/ui/common/arrow_right.png"))

main_ui_play = []
main_ui_play.append(pygame.image.load("materials/ui/play_menu/ball_size.png"))
main_ui_play.append(pygame.image.load("materials/ui/play_menu/ball_speed.png"))
main_ui_play.append(pygame.image.load("materials/ui/play_menu/max_rounds.png"))
main_ui_play.append(pygame.image.load("materials/ui/play_menu/start.png"))

main_ui_options = []
main_ui_options.append(pygame.image.load("materials/ui/options_menu/effects.png"))
main_ui_options.append(pygame.image.load("materials/ui/options_menu/music.png"))
main_ui_options.append(pygame.image.load("materials/ui/options_menu/screen_size.png"))

main_ui_pause = []
main_ui_pause.append(pygame.image.load("materials/ui/pause_menu/pause.png"))
main_ui_pause.append(pygame.image.load("materials/ui/pause_menu/continue.png"))
main_ui_pause.append(pygame.image.load("materials/ui/pause_menu/quit.png"))

#ui background
main_ui_background = []

main_ui_background.append(pygame.display.set_mode(SCREEN_SIZE_MEDIUM))
main_ui_background.append(pygame.Surface(SCREEN_SIZE_SMALL))
main_ui_background.append(pygame.Surface(SCREEN_SIZE_MEDIUM))
main_ui_background.append(pygame.Surface(SCREEN_SIZE_LARGE))
main_ui_background.append(pygame.image.load("materials/backgrounds/mainmenu_field_small.png"))
main_ui_background.append(pygame.image.load("materials/backgrounds/mainmenu_field_medium.png"))
main_ui_background.append(pygame.image.load("materials/backgrounds/mainmenu_field_large.png"))
main_ui_background.append(pygame.Surface(SCREEN_SIZE_SMALL))
main_ui_background.append(pygame.Surface(SCREEN_SIZE_MEDIUM))
main_ui_background.append(pygame.Surface(SCREEN_SIZE_LARGE))
main_ui_background.append(pygame.Surface(SCREEN_SIZE_SMALL))
main_ui_background.append(pygame.Surface(SCREEN_SIZE_MEDIUM))
main_ui_background.append(pygame.Surface(SCREEN_SIZE_LARGE))
main_ui_background.append(pygame.Surface((25, SCREEN_SIZE_SMALL_Y)))
main_ui_background.append(pygame.Surface((25, SCREEN_SIZE_MEDIUM_Y)))
main_ui_background.append(pygame.Surface((25, SCREEN_SIZE_LARGE_Y)))
main_ui_background.append(pygame.Surface((25, SCREEN_SIZE_SMALL_Y)))
main_ui_background.append(pygame.Surface((25, SCREEN_SIZE_MEDIUM_Y)))
main_ui_background.append(pygame.Surface((25, SCREEN_SIZE_LARGE_Y)))
main_ui_background.append(pygame.image.load("materials/backgrounds/final_earth_small.png"))
main_ui_background.append(pygame.image.load("materials/backgrounds/final_earth_medium.png"))
main_ui_background.append(pygame.image.load("materials/backgrounds/final_earth_large.png"))

# all assets
all_game = []
all_game.append(main_all)
all_game.append(main_game)
all_game.append(main_control)
all_game.append(main_locations)

all_entities = []
all_entities.append(pygame.image.load("materials/entities/ball_small.png"))
all_entities.append(pygame.image.load("materials/entities/ball_medium.png"))
all_entities.append(pygame.image.load("materials/entities/ball_large.png"))
all_entities.append(pygame.image.load("materials/entities/player_1.png"))
all_entities.append(pygame.image.load("materials/entities/player_2.png"))
all_entities.append(pygame.time.Clock())

all_ui = []
all_ui.append(ui_intro)
all_ui.append(ui_num)
all_ui.append(ui_score)
all_ui.append(main_ui)
all_ui.append(main_ui_common)
all_ui.append(main_ui_play)
all_ui.append(main_ui_options)
all_ui.append(main_ui_pause)
all_ui.append(main_ui_background)

all_sound = []
all_sound.append(pygame.mixer.Sound("sounds/misc/start.wav"))
all_sound.append(pygame.mixer.Sound("sounds/misc/button.wav"))
all_sound.append(pygame.mixer.Sound("sounds/misc/button_stop.wav"))
all_sound.append(pygame.mixer.Sound("sounds/win/round_win.wav"))

all_sound.append(pygame.mixer.Sound("sounds/music/end.ogg"))
all_sound.append(pygame.mixer.Sound("sounds/music/final.ogg"))
all_sound.append(pygame.mixer.Sound("sounds/music/main.ogg"))
all_sound.append(pygame.mixer.Sound("sounds/music/main_menu.ogg"))
all_sound.append(pygame.mixer.Sound("sounds/music/main_menu_other.ogg"))

#setup
config_settings(all_game,all_entities,all_ui,all_sound)
config_display(all_game,all_entities,all_ui,all_sound)

#main
game_mainmenu(all_game,all_entities,all_ui,all_sound)

#final
config_final(all_game,all_entities,all_ui,all_sound)

#quit pygame
pygame.quit()
