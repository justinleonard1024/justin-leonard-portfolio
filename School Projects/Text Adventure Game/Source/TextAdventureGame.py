"""
Text Adventure Game
TextAdventureGame.py
Created by Justin Leonard
"""

class TextAdventureGame:

    def __init__(self):
        self._control = True

        self._floors = [0,1,2,3]
        self._floor0_rooms = ["Basement"]
        self._floor1_rooms = ["Entrance1","Foyer","DiningRoom","Kitchen","LivingRoom","StorageRoom","GameRoom","Bathroom"]
        self._floor2_rooms = ["Entrance2","Hallway","Study","MasterBedroom","Washroom","Guestroom","KidsBedroom","Closet"]
        self._floor3_rooms = ["Attic"]

        self.display_floor0_rooms = ["Basement"]
        self.display_floor1_rooms = ["Entrance","Foyer","Dining Room","Kitchen","Living Room","Storage Room","Game Room","Bathroom"]
        self.display_floor2_rooms = ["Entrance","Hallway","Study","Master Bedroom","Washroom","Guest Room","Kid's Bedroom","Closet"]
        self.display_floor3_rooms = ["Attic"]
        self._display_keys = ["None","Kitchen Key","2nd Floor Key","Study Key","Master Bedroom Key","Guest Room Key","Game Room Key","Closet Key","Basement Key","Attic Key","Exit Key"]

        # keys
        self._GAME_KEY_NONE = 0
        self._GAME_KEY_KITCHEN = 1
        self._GAME_KEY_2NDFLOOR = 2
        self._GAME_KEY_STUDY = 3
        self._GAME_KEY_MASTERBEDROOM = 4
        self._GAME_KEY_GUESTROOM = 5
        self._GAME_KEY_GAMEROOM = 6
        self._GAME_KEY_CLOSET = 7
        self._GAME_KEY_BASEMENT = 8
        self._GAME_KEY_ATTIC = 9
        self._GAME_KEY_EXIT = 10
        self._game_keys = ["None","KitchenKey","2ndFloorKey","StudyKey","MasterBedroomKey","GuestRoomKey","GameRoomKey","ClosetKey","BasementKey","AtticKey","ExitKey"]

        # game states of all rooms
        # order: Entrance, Foyer, DiningRoom, StorageRoom, Hallway, Closet
        self._FLOOR_LOCKED_ENTRANCE = 0
        self._FLOOR_LOCKED_FOYER = 1
        self._FLOOR_LOCKED_DININGROOM = 2
        self._FLOOR_LOCKED_STORAGEROOM = 3
        self._FLOOR_LOCKED_HALLWAY = 4
        self._FLOOR_LOCKED_CLOSET = 5
        self._floor_locked_states = [0,0,0,0,0,0]

        # order: Basement, StorageRoom, GameRoom, Bathroom, Study, Washroom, Guestroom, KidsBedroom, Closet, Attic
        self._FLOOR_EXPLORE_BASEMENT = 0
        self._FLOOR_EXPLORE_STORAGEROOM = 1
        self._FLOOR_EXPLORE_GAMEROOM = 2
        self._FLOOR_EXPLORE_BATHROOM = 3
        self._FLOOR_EXPLORE_STUDY = 4
        self._FLOOR_EXPLORE_WASHROOM = 5
        self._FLOOR_EXPLORE_GUESTROOM = 6
        self._FLOOR_EXPLORE_KIDSBEDROOM = 7
        self._FLOOR_EXPLORE_CLOSET = 8
        self._FLOOR_EXPLORE_ATTIC = 9
        self._floor_explore_states = [0,0,0,0,0,0,0,0,0,0]

        # dynamic
        self._current_room = "Entrance1"
        self._current_key = self._game_keys[self._GAME_KEY_NONE]

    # check

    def _check_room(self):
        """Check what the current room is."""
        temp_room = 0

        # main check
        if(self._current_room.upper() == "BASEMENT"):
            self._f0_r1_basement()
            
        elif(self._current_room.upper() == "ENTRANCE1"):
            self._f1_r0_entrance()
            
        elif(self._current_room.upper() == "FOYER"):
            self._f1_r1_foyer()
            
        elif(self._current_room.upper() == "DININGROOM"):
            self._f1_r2_diningroom()
            
        elif(self._current_room.upper() == "KITCHEN"):
            self._f1_r3_kitchen()
            
        elif(self._current_room.upper() == "LIVINGROOM"):
            self._f1_r4_livingroom()
            
        elif(self._current_room.upper() == "STORAGEROOM"):
            self._f1_r5_storageroom()
            
        elif(self._current_room.upper() == "GAMEROOM"):
            self._f1_r6_gameroom()
            
        elif(self._current_room.upper() == "BATHROOM"):
            self._f1_r7_bathroom()
            
        elif(self._current_room.upper() == "ENTRANCE2"):
            self._f2_r0_entrance()
            
        elif(self._current_room.upper() == "HALLWAY"):
            self._f2_r1_hallway()
            
        elif(self._current_room.upper() == "STUDY"):
            self._f2_r2_study()
            
        elif(self._current_room.upper() == "MASTERBEDROOM"):
            self._f2_r3_masterbedroom()
            
        elif(self._current_room.upper() == "WASHROOM"):
            self._f2_r4_washroom()
            
        elif(self._current_room.upper() == "GUESTROOM"):
            self._f2_r5_guestroom()
            
        elif(self._current_room.upper() == "KIDSBEDROOM"):
            self._f2_r6_kidsbedroom()
            
        elif(self._current_room.upper() == "CLOSET"):
            self._f2_r7_closet()
            
        elif(self._current_room.upper() == "ATTIC"):
            self._f3_r1_attic()
            
        elif(self._current_room.upper() == "EXIT"):
            self._f_exit()

            

    def _check_quit(self):
        """Confirm whether or not the player wants to quit the game"""
        self._print_clear()
        chk = raw_input("Are you sure you want to quit? ('Y' = yes, 'N' = no)> ")
        if(chk.upper() == "Y"):
            self._control = False



    # display

    def _print_clear(self):
        """Clear the screen."""
        print "\n" * 100

    def _print_error(self):
        """A invalid command was processed."""
        print "Invalid command. Please try again"
        temp = raw_input("Press enter to continue ")

    def _print_error_locked(self):
        """The room that the player tried to enter was locked."""
        print "This room is locked. You need a key to enter"
        temp = raw_input("Press enter to continue ")

    def _print_intro(self):
        """Initial introduction sequence when the game starts."""
        self._print_clear()
        print "+-----------------------------------------------------------------------------------+"  
        print "| = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = |"
        print "|{>/-----------------------------------------------------------------------------\\<}|"
        print "|: |                                                                             | :|" 
        print "| :|                                                                             |: |" 
        print "|: |                                                                             | :|"
        print "| :|                                                                             |: |"
        print "|: |                                                                             | :|" 
        print "| :|                                                                             |: |" 
        print "|: |              You wake up confused in the entrance of a mansion              | :|"
        print "| :|                 The exit behind you is sealed up and locked                 |: |" 
        print "|: |     You must explore the house and find the exit key in order to escape     | :|" 
        print "| :|                                                                             |: |"
        print "|: |                                                                             | :|"
        print "| :|                                                                             |: |"
        print "|: |                                                                             | :|"
        print "| :|                                                                             |: |"
        print "|: |                                                                             | :|"
        print "|{>\\-----------------------------------------------------------------------------/<}|"
        print "| = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = |"
        print "+-----------------------------------------------------------------------------------+"
        temp = raw_input("Press enter to continue ")

    def _print_win(self):
        """Win notification when the player finds the final key and leaves the house."""
        self._print_clear()
        print "+-----------------------------------------------------------------------------------+"
        print "| = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = |"
        print "|{>/-----------------------------------------------------------------------------\<}|"
        print "|: |                                                                             | :|"
        print "| :|                                                                             |: |"
        print "|: |                                                                             | :|"
        print "| :|                                                                             |: |"
        print "|: |                                                                             | :|"
        print "| :|                                                                             |: |"
        print "|: |                                                                             | :|"
        print "| :|                                   You Win!                                  |: |"
        print "|: |                                                                             | :|"
        print "| :|                                                                             |: |"
        print "|: |                                                                             | :|"
        print "| :|                                                                             |: |"
        print "|: |                                                                             | :|"
        print "| :|                                                                             |: |"
        print "|: |                                                                             | :|"
        print "|{>\-----------------------------------------------------------------------------/<}|"
        print "| = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = : = |"
        print "+-----------------------------------------------------------------------------------+"
        temp = raw_input("Press enter to continue ")

    def _print_f0_r1_basement(self):
        """The display for the basement."""
        self._print_clear()
        print "-------------------------------------------------------------------------------------------------------------------------------------"
        print "| \\                                       |                                                                                         |"
        print "|   \\                                     |                                                                                         |"
        print "|     \\                                   |           --------------------                                                          |"
        print "|       \\                                 |              |            |                                                             |"
        print "|         \\                               |              |            |                                                             |"
        print "|           \\                             |                                                                                         |"
        print "|             \\                           |                                                          _______________________________|"
        print "|               \\                         |                                                           |  |  |  |  |  |  |  |  |  |   "
        print "|                |                                                                                    |  |  |  |  |  |  |  |  |  |   "
        print "|                |                                                                                    |  |  |  |  |  |  |  |  |  |   "
        print "|                |                                                                                    |  |  |  |  |  |  |  |  |  |   "
        print "|                |                                             /\\                                     |  |  |  |  |  |  |  |  |  |   "
        print "|                |                                             \\/                                     |  |  |  |  |  |  |  |  |  |   "
        print "|                |                                                                                    |  |  |  |  |  |  |  |  |  |   "
        print "|                |                                                                                    |  |  |  |  |  |  |  |  |  |   "
        print "|                |                                                                                    |  |  |  |  |  |  |  |  |  |   "
        print "|               /                         |                                                           |  |  |  |  |  |  |  |  |  |   "
        print "|             /                           |                                                          _______________________________ "
        print "|           /                             |                                                                                         |"
        print "|         /                               |              |            |                                                             |"
        print "|       /                                 |              |            |                                                             |"
        print "|     /                                   |           --------------------                                                          |"
        print "|   /                                     |                                                                                         |"
        print "| /                                       |                                                                                         |"
        print "-------------------------------------------------------------------------------------------------------------------------------------"
        print 
        print "                                                          Floor: 0"
        print "                                                          Room: Basement"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Up (R) = Storage Room"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = (Not Available)"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f1_r0_entrance_locked(self):
        """The display for the entrance when the exit is locked."""
        self._print_clear()
        print "|-------------------------------------------|-------------------------------------------|-------------------------------------------|"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "--------------------------------------------|--------------------   --------------------|--------------------------------------------"
        print "                                            |                     ^                     |"
        print "                                            |                     |                     |"
        print "                                            |                                           |"
        print "                                            |                                           |"
        print "                                            |                                           |"
        print "                                            |                                           |"
        print "                                            |                                           |"
        print "                                            |                                           |"
        print "                                            |                                           |"
        print "                                            |                     |                     |"
        print "                                            |                     V                     |"
        print "                                            --------------------- X ---------------------"
        print 
        print "                                                          Floor: 1"
        print "                                                          Room: Entrance"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Front (W) = Foyer"
        print "                                                          Back (S) = Exit (Locked)"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = Talk to Person"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f1_r0_entrance_unlocked(self):
        """The display for the entrance."""
        self._print_clear()
        print "|-------------------------------------------|-------------------------------------------|-------------------------------------------|"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "--------------------------------------------|--------------------   --------------------|--------------------------------------------"
        print "                                            |                     ^                     |"
        print "                                            |                     |                     |"
        print "                                            |                                           |"
        print "                                            |                                           |"
        print "                                            |                                           |"
        print "                                            |                                           |"
        print "                                            |                                           |"
        print "                                            |                                           |"
        print "                                            |                                           |"
        print "                                            |                     |                     |"
        print "                                            |                     V                     |"
        print "                                            ---------------------   ---------------------"
        print 
        print "                                                          Floor: 1"
        print "                                                          Room: Entrance"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Front (W) = Foyer"
        print "                                                          Back (S) = Exit"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = Talk to Person"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f1_r1_foyer_alllocked(self):
        """The display for the foyer when all rooms are locked."""
        self._print_clear()
        print "-------------------------------------------------------------------------------------------------------------------------------------"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|-------------------------------------------|--------------------   --------------------|-------------------------------------------|"
        print "|                                           |                     ^                     |                                           |"
        print "|                                           |                     |                     |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                             <-                                     -> X                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                     |                     |                                           |"
        print "|                                           |                     V                     |                                           |"
        print "--------------------------------------------|--------------------   --------------------|--------------------------------------------"
        print 
        print "                                                          Floor: 1"
        print "                                                          Room: Foyer"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Front (W) = Living Room"
        print "                                                          Right (D) = Game Room (Locked)"
        print "                                                          Back (S) = Entrance"
        print "                                                          Left (A) = Dining Room"
        print "                                                          Up (R) = 2nd Floor (Locked)"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = (Not Available)"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f1_r1_foyer_gamelocked(self):
        """The display for the foyer when the game room is locked."""
        self._print_clear()
        print "-------------------------------------------------------------------------------------------------------------------------------------"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|-------------------------------------------|--------------------   --------------------|-------------------------------------------|"
        print "|                                           |                     ^                     |                                           |"
        print "|                                           |                     |                     |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                             <-                                     -> X                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                     |                     |                                           |"
        print "|                                           |                     V                     |                                           |"
        print "--------------------------------------------|--------------------   --------------------|--------------------------------------------"
        print 
        print "                                                          Floor: 1"
        print "                                                          Room: Foyer"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Front (W) = Living Room"
        print "                                                          Right (D) = Game Room (Locked)"
        print "                                                          Back (S) = Entrance"
        print "                                                          Left (A) = Dining Room"
        print "                                                          Up (R) = 2nd Floor"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = (Not Available)"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f1_r1_foyer_unlocked(self):
        """The display for the foyer."""
        self._print_clear()
        print "-------------------------------------------------------------------------------------------------------------------------------------"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|-------------------------------------------|--------------------   --------------------|-------------------------------------------|"
        print "|                                           |                     ^                     |                                           |"
        print "|                                           |                     |                     |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                             <-                                     ->                                             |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                     |                     |                                           |"
        print "|                                           |                     V                     |                                           |"
        print "--------------------------------------------|--------------------   --------------------|--------------------------------------------"
        print 
        print "                                                          Floor: 1"
        print "                                                          Room: Foyer"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Front (W) = Living Room"
        print "                                                          Right (D) = Game Room"
        print "                                                          Back (S) = Entrance"
        print "                                                          Left (A) = Dining Room"
        print "                                                          Up (R) = 2nd Floor"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = (Not Available)"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f1_r2_diningroom_locked(self):
        """The display for the dining room when the kitchen is locked."""
        self._print_clear()
        print "-------------------------------------------------------------------------------------------------------------------------------------"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|-------------------- X --------------------|-------------------------------------------|-------------------------------------------|"
        print "|                     ^                     |                                           |                                           |"
        print "|                     |                     |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                        ->                                             |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "--------------------------------------------|-------------------------------------------|--------------------------------------------"
        print 
        print "                                                          Floor: 1"
        print "                                                          Room: Dining Room"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Front (W) = Kitchen (Locked)"
        print "                                                          Right (D) = Foyer"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = (Not Available)"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f1_r2_diningroom_unlocked(self):
        """The display for the dining room."""
        self._print_clear()
        print "-------------------------------------------------------------------------------------------------------------------------------------"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|--------------------   --------------------|-------------------------------------------|-------------------------------------------|"
        print "|                     ^                     |                                           |                                           |"
        print "|                     |                     |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                        ->                                             |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "--------------------------------------------|-------------------------------------------|--------------------------------------------"
        print 
        print "                                                          Floor: 1"
        print "                                                          Room: Dining Room"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Front (W) = Kitchen"
        print "                                                          Right (D) = Foyer"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = (Not Available)"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f1_r3_kitchen(self):
        """The display for the kitchen."""
        self._print_clear()
        print "-------------------------------------------------------------------------------------------------------------------------------------"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "  <-                                        |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                     |                     |                                           |                                           |"
        print "|                     V                     |                                           |                                           |"
        print "|--------------------   --------------------|-------------------------------------------|-------------------------------------------|"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "--------------------------------------------|-------------------------------------------|--------------------------------------------"
        print 
        print "                                                          Floor: 1"
        print "                                                          Room: Kitchen"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Back (S) = Dining Room"
        print "                                                          Left (A) = Bathroom"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = Talk to Person"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f1_r4_livingroom(self):
        """The display for the living room."""
        self._print_clear()
        print "-------------------------------------------------------------------------------------------------------------------------------------"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                        ->                                             |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                     |                     |                                           |"
        print "|                                           |                     V                     |                                           |"
        print "|-------------------------------------------|--------------------   --------------------|-------------------------------------------|"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "--------------------------------------------|-------------------------------------------|--------------------------------------------"
        print 
        print "                                                          Floor: 1"
        print "                                                          Room: Living Room"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Right (D) = Storage Room"
        print "                                                          Back (S) = Foyer"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = (Not Available)"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f1_r5_storageroom_locked(self):
        """The display for the storage room when the basement is locked."""
        self._print_clear()
        print "-------------------------------------------------------------------------------------------------------------------------------------"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                             <-                                        |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|-------------------------------------------|-------------------------------------------|-------------------------------------------|"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "--------------------------------------------|-------------------------------------------|--------------------------------------------"
        print 
        print "                                                          Floor: 1"
        print "                                                          Room: Storage Room"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Left (A) = Living Room"
        print "                                                          Down (F) = Basement (Locked)"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = Talk to Person"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f1_r5_storageroom_unlocked(self):
        """The display for the storage room."""
        self._print_clear()
        print "-------------------------------------------------------------------------------------------------------------------------------------"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                             <-                                        |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|-------------------------------------------|-------------------------------------------|-------------------------------------------|"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "--------------------------------------------|-------------------------------------------|--------------------------------------------"
        print 
        print "                                                          Floor: 1"
        print "                                                          Room: Storage Room"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Left (A) = Living Room"
        print "                                                          Down (F) = Basement"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = Talk to Person"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f1_r6_gameroom(self):
        """The display for the game room."""
        self._print_clear()
        print "-------------------------------------------------------------------------------------------------------------------------------------"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|-------------------------------------------|-------------------------------------------|-------------------------------------------|"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                             <-                                        |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "--------------------------------------------|-------------------------------------------|--------------------------------------------"
        print 
        print "                                                          Floor: 1"
        print "                                                          Room: Game Room"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Left (A) = Foyer"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = Talk to Person"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f1_r7_bathroom(self):
        """The display for the bathroom."""
        self._print_clear()
        print "-------------------------------------------------------------------------------------------------------------------------------------"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                        ->                                             |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "|                                           |                                           |                                           |"
        print "--------------------------------------------|-------------------------------------------|-------------------------------------------|"
        print "                                            |                                           |                                           |"
        print "                                            |                                           |                                           |"
        print "                                            |                                           |                                           |"
        print "                                            |                                           |                                           |"
        print "                                            |                                           |                                           |"
        print "                                            |                                           |                                           |"
        print "                                            |                                           |                                           |"
        print "                                            |                                           |                                           |"
        print "                                            |                                           |                                           |"
        print "                                            |                                           |                                           |"
        print "                                            |                                           |                                           |"
        print "                                            |-------------------------------------------|--------------------------------------------"
        print 
        print "                                                          Floor: 1"
        print "                                                          Room: Bathroom"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Right (D) = Kitchen"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = (Not Available)"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f2_r0_entrance(self):
        """The display for the entrance of the second floor."""
        self._print_clear()
        print "-----------------------|                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |--------------------   --------------------|--------------------   --------------------|---------------------|"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                   ->                                                                                                               |" 
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |--------------------   --------------------|--------------------   --------------------|---------   ---------|" 
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "-----------------------|                                           |                                           |                     |"
        print 
        print "                                                          Floor: 2"
        print "                                                          Room: Entrance"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Right (D) = Hallway"
        print "                                                          Down (F) = 1st Floor"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = (Not Available)"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f2_r1_hallway_init(self):
        """The display for the hallway when all doors are locked."""
        self._print_clear()
        print "-----------------------|                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |-------------------- X --------------------|-------------------- X --------------------|---------------------|"
        print "|                      |                     ^                                           ^                                           |"
        print "|                      |                     |                                           |                                           |"
        print "|                      |                     1                                           2                                           |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                        <-                                                                                                          |" 
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                     1                                           2                                3          |"
        print "|                      |                     |                                           |                                |          |"
        print "|                      |                     V                                           V                                V          |"
        print "|                      |-------------------- X --------------------|--------------------   --------------------|--------- X ---------|" 
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "-----------------------|                                           |                                           |                     |"
        print 
        print "                                                          Floor: 2"
        print "                                                          Room: Hallway"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Front 1 (W1) = Study (Locked)"
        print "                                                          Front 2 (W2) = Master Bedroom (Locked)"
        print "                                                          Back 1 (S1) = Guest Room (Locked)"
        print "                                                          Back 2 (S2) = Kid's Bedroom"
        print "                                                          Back 3 (S3) = Closet (Locked)"
        print "                                                          Left (A) = Entrance"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = (Not Available)"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f2_r1_hallway_unlockcloset(self):
        """The display for the hallway."""
        self._print_clear()
        print "-----------------------|                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |--------------------   --------------------|--------------------   --------------------|---------------------|"
        print "|                      |                     ^                                           ^                                           |"
        print "|                      |                     |                                           |                                           |"
        print "|                      |                     1                                           2                                           |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                        <-                                                                                                          |" 
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                     1                                           2                                3          |"
        print "|                      |                     |                                           |                                |          |"
        print "|                      |                     V                                           V                                V          |"
        print "|                      |--------------------   --------------------|--------------------   --------------------|---------   ---------|" 
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "-----------------------|                                           |                                           |                     |"
        print 
        print "                                                          Floor: 2"
        print "                                                          Room: Hallway"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Front 1 (W1) = Study"
        print "                                                          Front 2 (W2) = Master Bedroom"
        print "                                                          Back 1 (S1) = Guest Room"
        print "                                                          Back 2 (S2) = Kid's Bedroom"
        print "                                                          Back 3 (S3) = Closet"
        print "                                                          Left (A) = Entrance"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = (Not Available)"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f2_r1_hallway_unlockguestroom(self):
        """The display for the hallway when the closet is locked."""
        self._print_clear()
        print "-----------------------|                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |--------------------   --------------------|--------------------   --------------------|---------------------|"
        print "|                      |                     ^                                           ^                                           |"
        print "|                      |                     |                                           |                                           |"
        print "|                      |                     1                                           2                                           |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                        <-                                                                                                          |" 
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                     1                                           2                                3          |"
        print "|                      |                     |                                           |                                |          |"
        print "|                      |                     V                                           V                                V          |"
        print "|                      |--------------------   --------------------|--------------------   --------------------|--------- X ---------|" 
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "-----------------------|                                           |                                           |                     |"
        print 
        print "                                                          Floor: 2"
        print "                                                          Room: Hallway"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Front 1 (W1) = Study"
        print "                                                          Front 2 (W2) = Master Bedroom"
        print "                                                          Back 1 (S1) = Guest Room"
        print "                                                          Back 2 (S2) = Kid's Bedroom"
        print "                                                          Back 3 (S3) = Closet (Locked)"
        print "                                                          Left (A) = Entrance"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = (Not Available)"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f2_r1_hallway_unlockmasterbedroom(self):
        """The display for the hallway when the guest room and closet are locked."""
        self._print_clear()
        print "-----------------------|                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |--------------------   --------------------|--------------------   --------------------|---------------------|"
        print "|                      |                     ^                                           ^                                           |"
        print "|                      |                     |                                           |                                           |"
        print "|                      |                     1                                           2                                           |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                        <-                                                                                                          |" 
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                     1                                           2                                3          |"
        print "|                      |                     |                                           |                                |          |"
        print "|                      |                     V                                           V                                V          |"
        print "|                      |-------------------- X --------------------|--------------------   --------------------|--------- X ---------|" 
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "-----------------------|                                           |                                           |                     |"
        print 
        print "                                                          Floor: 2"
        print "                                                          Room: Hallway"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Front 1 (W1) = Study"
        print "                                                          Front 2 (W2) = Master Bedroom"
        print "                                                          Back 1 (S1) = Guest Room (Locked)"
        print "                                                          Back 2 (S2) = Kid's Bedroom"
        print "                                                          Back 3 (S3) = Closet (Locked)"
        print "                                                          Left (A) = Entrance"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = (Not Available)"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f2_r1_hallway_unlockstudy(self):
        """The display for the hallway when the master bedroom, guest room and closet are locked."""
        self._print_clear()
        print "-----------------------|                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |--------------------   --------------------|-------------------- X --------------------|---------------------|"
        print "|                      |                     ^                                           ^                                           |"
        print "|                      |                     |                                           |                                           |"
        print "|                      |                     1                                           2                                           |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                        <-                                                                                                          |" 
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                     1                                           2                                3          |"
        print "|                      |                     |                                           |                                |          |"
        print "|                      |                     V                                           V                                V          |"
        print "|                      |-------------------- X --------------------|--------------------   --------------------|--------- X ---------|" 
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "-----------------------|                                           |                                           |                     |"
        print 
        print "                                                          Floor: 2"
        print "                                                          Room: Hallway"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Front 1 (W1) = Study"
        print "                                                          Front 2 (W2) = Master Bedroom (Locked)"
        print "                                                          Back 1 (S1) = Guest Room (Locked)"
        print "                                                          Back 2 (S2) = Kid's Bedroom"
        print "                                                          Back 3 (S3) = Closet (Locked)"
        print "                                                          Left (A) = Entrance"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = (Not Available)"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f2_r2_study(self):
        """The display for the study."""
        self._print_clear()
        print "                       --------------------------------------------------------------------------------------------------------------|"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "-----------------------|                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                     |                     |                                           |                     |"
        print "|                      |                     V                     |                                           |                     |"
        print "|                      |--------------------   --------------------|-------------------------------------------|---------------------|"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |" 
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |-------------------------------------------|-------------------------------------------|---------------------|" 
        print 
        print "                                                          Floor: 2"
        print "                                                          Room: Study"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Back (S) = Hallway"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = Talk to Person"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f2_r3_masterbedroom(self):
        """The display for the master bedroom."""
        self._print_clear()
        print "                       --------------------------------------------------------------------------------------------------------------|"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "-----------------------|                                           |                                        ->                       |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                     |                     |                     |"
        print "|                      |                                           |                     V                     |                     |"
        print "|                      |-------------------------------------------|--------------------   --------------------|---------------------|"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |" 
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |-------------------------------------------|-------------------------------------------|---------------------|" 
        print 
        print "                                                          Floor: 2"
        print "                                                          Room: Master Bedroom"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Right (D) = Washroom"
        print "                                                          Back (S) = Hallway"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = Talk to Person"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f2_r4_washroom(self):
        """The display for the washroom."""
        self._print_clear()
        print "                       --------------------------------------------------------------------------------------------------------------|"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "-----------------------|                                           |                                             <-                  |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |-------------------------------------------|-------------------------------------------|---------------------|"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |" 
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |-------------------------------------------|-------------------------------------------|---------------------|" 
        print 
        print "                                                          Floor: 2"
        print "                                                          Room: Washroom"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Left (A) = Master Bedroom"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = (Not Available)"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f2_r5_guestroom(self):
        """The display for the guest room."""
        self._print_clear()
        print "|                      |-------------------------------------------|-------------------------------------------|---------------------|"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |" 
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |--------------------   --------------------|-------------------------------------------|---------------------|" 
        print "|                      |                     ^                     |                                           |                     |"
        print "|                      |                     |                     |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "-----------------------|                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       ---------------------------------------------------------------------------------------------------------------"
        print 
        print "                                                          Floor: 2"
        print "                                                          Room: Guest Room"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Front (W) = Hallway"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = (Not Available)"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f2_r6_kidsbedroom(self):
        """The display for the kid's bedroom."""
        self._print_clear()
        print "|                      |-------------------------------------------|-------------------------------------------|---------------------|"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |" 
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |-------------------------------------------|--------------------   --------------------|---------------------|" 
        print "|                      |                                           |                     ^                     |                     |"
        print "|                      |                                           |                     |                     |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "-----------------------|                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       ---------------------------------------------------------------------------------------------------------------"
        print 
        print "                                                          Floor: 2"
        print "                                                          Room: Kid's Bedroom"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Front (W) = Hallway"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = (Not Available)"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f2_r7_closet_locked(self):
        """The display for the closet when the attic is locked."""
        self._print_clear()
        print "|                      |-------------------------------------------|-------------------------------------------|---------------------|"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |" 
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |-------------------------------------------|-------------------------------------------|---------   ---------|" 
        print "|                      |                                           |                                           |          ^          |"
        print "|                      |                                           |                                           |          |          |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "-----------------------|                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       ---------------------------------------------------------------------------------------------------------------"
        print 
        print "                                                          Floor: 2"
        print "                                                          Room: Closet"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Front (W) = Hallway"
        print "                                                          Up (R) = Attic (Locked)"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = (Not Available)"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f2_r7_closet_unlocked(self):
        """The display for the closet."""
        self._print_clear()
        print "|                      |-------------------------------------------|-------------------------------------------|---------------------|"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |" 
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |                                                                                                             |"
        print "|                      |-------------------------------------------|-------------------------------------------|---------   ---------|" 
        print "|                      |                                           |                                           |          ^          |"
        print "|                      |                                           |                                           |          |          |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "|                      |                                           |                                           |                     |"
        print "-----------------------|                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       |                                           |                                           |                     |"
        print "                       ---------------------------------------------------------------------------------------------------------------"
        print 
        print "                                                          Floor: 2"
        print "                                                          Room: Closet"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Front (W) = Hallway"
        print "                                                          Up (R) = Attic"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = (Not Available)"
        print "                                                          Quit (Q) = Exit Game"

    def _print_f3_r1_attic(self):
        """The display for the attic."""
        self._print_clear()
        print "                                            |-------------------------------------------|"
        print "                                            |\\              _____________              /|"
        print "                                            | \\            |             |            / |"
        print "                                            |  \\           |     -O-     |           /  |"
        print "                                            |   \\          |_____________|          /   |"
        print "                                            |    \\                                 /    |"
        print "                                            |     \\                               /     |"
        print "                                            |      \\                             /      |"
        print "                                            |       |                           |       |"
        print "                                            |       |                           |       |"
        print "                                            |       |                           |       |"
        print "                                            |       |                           |       |"
        print "                                            |       |                           |       |"
        print "                                            |       |                           |       |"
        print "                                            |       |                           |       |"
        print "                                            |       |                           |       |"
        print "                                            |       |                           |       |"
        print "                                            |      /                             \\      |"
        print "                                            |     /                               \\     |"
        print "                                            |    /                                 \\    |"
        print "                                            |   /                                   \\   |"
        print "                                            |  /                                     \\  |"
        print "                                            | /                                       \\ |"
        print "                                            |/                                         \\|"
        print "                                            |--------------------   --------------------|"
        print 
        print "                                                          Floor: 3"
        print "                                                          Room: Attic"
        print "                                                          Keys: " + self._display_keys[self._game_keys.index(self._current_key)]
        print 
        print "                                                          Down (F) = Closet"
        print "                                                          Explore (E) = Look Around"
        print "                                                          Talk (T) = (Not Available)"
        print "                                                          Quit (Q) = Exit Game"

    def _print_eventkey_kitchen(self):
        """The event display message for when the player finds the kitchen key."""
        self._print_clear()
        print "                                                               .---."
        print "                                                              /  .  \\"
        print "                                                             |\\_/|   |"
        print "                                                             |   |  /|"
        print "  .----------------------------------------------------------------' |"
        print " /  .-.                                                              |"
        print "|  /   \\                                                             |"
        print "| |\\_.  |                                                            |"
        print "|\\|  | /|             You have found the Kitchen Key!                |"
        print "| `---' |                                                            |"
        print "|       |                                                            |"
        print "|       |                                                           /"
        print "|       |----------------------------------------------------------'"
        print "\\       |"
        print " \\     /"
        print "  `---'"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _print_eventkey_2ndfloor(self):
        """The event display message for when the player finds the 2nd floor key."""
        self._print_clear()
        print "                                                               .---."
        print "                                                              /  .  \\"
        print "                                                             |\\_/|   |"
        print "                                                             |   |  /|"
        print "  .----------------------------------------------------------------' |"
        print " /  .-.                                                              |"
        print "|  /   \\                                                             |"
        print "| |\\_.  |                                                            |"
        print "|\\|  | /|             You have found the 2nd Floor Key!              |"
        print "| `---' |                                                            |"
        print "|       |                                                            |"
        print "|       |                                                           /"
        print "|       |----------------------------------------------------------'"
        print "\\       |"
        print " \\     /"
        print "  `---'"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _print_eventkey_study(self):
        """The event display message for when the player finds the study key."""
        self._print_clear()
        print "                                                               .---."
        print "                                                              /  .  \\"
        print "                                                             |\\_/|   |"
        print "                                                             |   |  /|"
        print "  .----------------------------------------------------------------' |"
        print " /  .-.                                                              |"
        print "|  /   \\                                                             |"
        print "| |\\_.  |                                                            |"
        print "|\\|  | /|             You have found the Study Key!                  |"
        print "| `---' |                                                            |"
        print "|       |                                                            |"
        print "|       |                                                           /"
        print "|       |----------------------------------------------------------'"
        print "\\       |"
        print " \\     /"
        print "  `---'"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _print_eventkey_masterbedroom(self):
        """The event display message for when the player finds the master bedroom key."""
        self._print_clear()
        print "                                                               .---."
        print "                                                              /  .  \\"
        print "                                                             |\\_/|   |"
        print "                                                             |   |  /|"
        print "  .----------------------------------------------------------------' |"
        print " /  .-.                                                              |"
        print "|  /   \\                                                             |"
        print "| |\\_.  |                                                            |"
        print "|\\|  | /|          You have found the Master Bedroom Key!            |"
        print "| `---' |                                                            |"
        print "|       |                                                            |"
        print "|       |                                                           /"
        print "|       |----------------------------------------------------------'"
        print "\\       |"
        print " \\     /"
        print "  `---'"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _print_eventkey_guestroom(self):
        """The event display message for when the player finds the guest room key."""
        self._print_clear()
        print "                                                               .---."
        print "                                                              /  .  \\"
        print "                                                             |\\_/|   |"
        print "                                                             |   |  /|"
        print "  .----------------------------------------------------------------' |"
        print " /  .-.                                                              |"
        print "|  /   \\                                                             |"
        print "| |\\_.  |                                                            |"
        print "|\\|  | /|            You have found the Guest Room Key!              |"
        print "| `---' |                                                            |"
        print "|       |                                                            |"
        print "|       |                                                           /"
        print "|       |----------------------------------------------------------'"
        print "\\       |"
        print " \\     /"
        print "  `---'"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _print_eventkey_gameroom(self):
        """The event display message for when the player finds the game room key."""
        self._print_clear()
        print "                                                               .---."
        print "                                                              /  .  \\"
        print "                                                             |\\_/|   |"
        print "                                                             |   |  /|"
        print "  .----------------------------------------------------------------' |"
        print " /  .-.                                                              |"
        print "|  /   \\                                                             |"
        print "| |\\_.  |                                                            |"
        print "|\\|  | /|             You have found the Game Room Key!              |"
        print "| `---' |                                                            |"
        print "|       |                                                            |"
        print "|       |                                                           /"
        print "|       |----------------------------------------------------------'"
        print "\\       |"
        print " \\     /"
        print "  `---'"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _print_eventkey_closet(self):
        """The event display message for when the player finds the closet key."""
        self._print_clear()
        print "                                                               .---."
        print "                                                              /  .  \\"
        print "                                                             |\\_/|   |"
        print "                                                             |   |  /|"
        print "  .----------------------------------------------------------------' |"
        print " /  .-.                                                              |"
        print "|  /   \\                                                             |"
        print "| |\\_.  |                                                            |"
        print "|\\|  | /|             You have found the Closet Key!                 |"
        print "| `---' |                                                            |"
        print "|       |                                                            |"
        print "|       |                                                           /"
        print "|       |----------------------------------------------------------'"
        print "\\       |"
        print " \\     /"
        print "  `---'"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _print_eventkey_basement(self):
        """The event display message for when the player finds the basement key."""
        self._print_clear()
        print "                                                               .---."
        print "                                                              /  .  \\"
        print "                                                             |\\_/|   |"
        print "                                                             |   |  /|"
        print "  .----------------------------------------------------------------' |"
        print " /  .-.                                                              |"
        print "|  /   \\                                                             |"
        print "| |\\_.  |                                                            |"
        print "|\\|  | /|             You have found the Basement Key!               |"
        print "| `---' |                                                            |"
        print "|       |                                                            |"
        print "|       |                                                           /"
        print "|       |----------------------------------------------------------'"
        print "\\       |"
        print " \\     /"
        print "  `---'"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _print_eventkey_attic(self):
        """The event display message for when the player finds the attic key."""
        self._print_clear()
        print "                                                               .---."
        print "                                                              /  .  \\"
        print "                                                             |\\_/|   |"
        print "                                                             |   |  /|"
        print "  .----------------------------------------------------------------' |"
        print " /  .-.                                                              |"
        print "|  /   \\                                                             |"
        print "| |\\_.  |                                                            |"
        print "|\\|  | /|             You have found the Attic Key!                  |"
        print "| `---' |                                                            |"
        print "|       |                                                            |"
        print "|       |                                                           /"
        print "|       |----------------------------------------------------------'"
        print "\\       |"
        print " \\     /"
        print "  `---'"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _print_eventkey_exit(self):
        """The event display message for when the player finds the exit key."""
        self._print_clear()
        print "                                                               .---."
        print "                                                              /  .  \\"
        print "                                                             |\\_/|   |"
        print "                                                             |   |  /|"
        print "  .----------------------------------------------------------------' |"
        print " /  .-.                                                              |"
        print "|  /   \\                                                             |"
        print "| |\\_.  |                                                            |"
        print "|\\|  | /|             You have found the Exit Key!                   |"
        print "| `---' |                                                            |"
        print "|       |                                                            |"
        print "|       |                                                           /"
        print "|       |----------------------------------------------------------'"
        print "\\       |"
        print " \\     /"
        print "  `---'"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _print_eventkey_unlock(self):
        """The event display message for when a door is unlocked."""
        self._print_clear()
        print "                                                               .---."
        print "                                                              /  .  \\"
        print "                                                             |\\_/|   |"
        print "                                                             |   |  /|"
        print "  .----------------------------------------------------------------' |"
        print " /  .-.                                                              |"
        print "|  /   \\                                                             |"
        print "| |\\_.  |                                                            |"
        print "|\\|  | /|                    Door Unlocked                           |"
        print "| `---' |                                                            |"
        print "|       |                                                            |"
        print "|       |                                                           /"
        print "|       |----------------------------------------------------------'"
        print "\\       |"
        print " \\     /"
        print "  `---'"
        print "\n\n"
        temp = raw_input("Press enter to continue ")



    # events

    def _event_f0_r1_basement(self):
        """The event display message for when the player explores the basement."""
        self._print_clear()
        print "The basement is cold and dark emitting a shallow uneasiness across the room"
        print "Only one lone flickering light illuminates the unsettling gloomy shadows"
        print "The black soulless walls surrounding the eerie enclosure curse you with uneasiness"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _event_f1_r0_entrance(self):
        """The event display message for when the player explores the entrance."""
        self._print_clear()
        print "Entering the mansion instantly overwhelms you with an unnerving sense of regret"
        print "The old architectural style of the manor mirrors the chilling sensation that is felt by the visitor"
        print "It is immediately clear that there is something not right with this abode"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _event_f1_r1_foyer(self):
        """The event display message for when the player explores the foyer."""
        self._print_clear()
        print "Inside the manor reveals the massive size of the building"
        print "The large foyer contains two old and broken down staircases leading up to the next floor"
        print "The creaking sounds of wood and metal as you move throughout the environment shows the age and instability of this house"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _event_f1_r2_diningroom(self):
        """The event display message for when the player explores the diningroom."""
        self._print_clear()
        print "There is a long dusty table with various broken plates and utensils scattered about"
        print "The smell of decaying flesh is evident throughout the room"
        print "Animal bones are seen with the remnants of other partially consumed food"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _event_f1_r3_kitchen(self):
        """The event display message for when the player explores the kitchen."""
        self._print_clear()
        print "Across the walls of the room exist inactive appliances that were used to cook numerous meals"
        print "There are several charred remains of destroyed structures where a fire was started"
        print "A small light of fire is still slightly shining in the brick oven"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _event_f1_r4_livingroom(self):
        """The event display message for when the player explores the livingroom."""
        self._print_clear()
        print "The dated furniture setup around the room displays the old age of this dwelling"
        print "Many expensive and classic paintings are hanging on the walls along with a grandfather clock in the corner"
        print "The boarded up windows on the back walls still show the lightning strikes coming from the stormy outside world"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _event_f1_r5_storageroom(self):
        """The event display message for when the player explores the storage room."""
        self._print_clear()
        print "There are boxes and other containers that are used for storage"
        print "At the end of the room there is a dark staircase leading down to the basement"
        print "The stone walls and lack of insulation drastically lowers the temperature"
        print "\n\n"
        temp = raw_input("Press enter to continue ")
        
    def _event_f1_r6_gameroom(self):
        """The event display message for when the player explores the game room."""
        self._print_clear()
        print "A pool table is in the middle of the room with all of the balls set up"
        print "There is a radio that is playing muffled classical music"
        print "A bar is set up with high quality wines still unopened on the table"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _event_f1_r7_bathroom(self):
        """The event display message for when the player explores the bathroom."""
        self._print_clear()
        print "The dripping water fills the rusted sink with a think grime"
        print "A small wind is coming from the window which slowly moves the shower curtain"
        print "On top of the cracked toilet seat lay a pile of bricks and stones that came down from the ceiling"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _event_f2_r0_entrance(self):
        """The event display message for when the player explores the 2nd floor entrance."""
        self._print_clear()
        print "The rotting staircase makes a series of loud creaks as you slowly walk up it"
        print "At the top of the staircase lies one large door with several engravings on it"
        print "The light of the next room shines through the crevasse below the door"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _event_f2_r1_hallway(self):
        """The event display message for when the player explores the hallway."""
        self._print_clear()
        print "A large hallway can be seen with five doors on the walls"
        print "Some of the doors seem to be sealed up protecting against intrusion"
        print "There is one light in the middle of the hall"
        print "\n\n"
        temp = raw_input("Press enter to continue ")
        
    def _event_f2_r2_study(self):
        """The event display message for when the player explores the study."""
        self._print_clear()
        print "There is a fireplace with a fierce and warm fire still blazing"
        print "There are several bookcases lining the walls of the room"
        print "In the middle of the room there is a desk with a rocking chair next to the fireplace"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _event_f2_r3_masterbedroom(self):
        """The event display message for when the player explores the master bedroom."""
        self._print_clear()
        print "A king sized bed is present in the middle of the room"
        print "The sheets are nicely made up and match the style of the bed"
        print "There is a destroyed cabinet on the other side of the room which has had it's contents removed"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _event_f2_r4_washroom(self):
        """The event display message for when the player explores the washroom."""
        self._print_clear()
        print "The dripping water fills the rusted sink with a think grime"
        print "A small wind is coming from the window which slowly moves the shower curtain"
        print "The bathtub has a dark green liquid inside of it reeking with a vile scent"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _event_f2_r5_guestroom(self):
        """The event display message for when the player explores the guestroom."""
        self._print_clear()
        print "There is a medium sized bed with the sheets wrinkled in the middle of the room"
        print "There are a few sealed suitcases near the foot of the bed"
        print "On the other side of the room there is a broken mirror with shards of smudged glass on the ground"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _event_f2_r6_kidsbedroom(self):
        """The event display message for when the player explores the kid's bedroom."""
        self._print_clear()
        print "Two small beds with the sheets thrown on the floor are in the corners of this room"
        print "There are toys scattered on the floor some of which are broken"
        print "There is a slight sound of laughing children that can be heard coming from the walls"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _event_f2_r7_closet(self):
        """The event display message for when the player explores the closet."""
        self._print_clear()
        print "There are a few storage containers along with a mop and bucket"
        print "The one hanging light in the middle of the room flickers slowly"
        print "There is a ladder at the back wall that leads up to a dark and gloomy attic"
        print "\n\n"
        temp = raw_input("Press enter to continue ")

    def _event_f3_r1_attic(self):
        """The event display message for when the player explores the attic."""
        self._print_clear()
        print "The attic is dark and broken down"
        print "The only light seen is coming from the moon through the cracked windows"
        print "At the far end of the horrifying room lies a large chest"
        print "\n\n"
        temp = raw_input("Press enter to continue ")



    def _eventkey_f0_r1_basement(self):
        """The event display message for when the player explores the basement and finds a key."""
        self._print_clear()
        print "The basement is cold and dark emitting a shallow uneasiness across the room"
        print "Only one lone flickering light illuminates the unsettling gloomy shadows"
        print "The black soulless walls surrounding the eerie enclosure curse you with uneasiness"
        print "There is a wodden box cracked opened on the ground"
        print "\n\n"
        temp = raw_input("Press enter to search ")
        self._print_eventkey_attic()
        self._current_key = self._game_keys[self._GAME_KEY_ATTIC]



    def _eventkey_f1_r5_storageroom(self):
        """The event display message for when the player explores the storage room and finds a key."""
        self._print_clear()
        print "There are boxes and other containers that are used for storage"
        print "At the end of the room there is a dark staircase leading down to the basement"
        print "The stone walls and lack of insulation drastically lowers the temperature"
        print "There is a metal cabinet that is partially opened"
        print "\n\n"
        temp = raw_input("Press enter to search ")
        self._print_eventkey_kitchen()
        self._current_key = self._game_keys[self._GAME_KEY_KITCHEN]



    def _eventkey_f1_r6_gameroom(self):
        """The event display message for when the player explores the game room and finds a key."""
        self._print_clear()
        print "A pool table is in the middle of the room with all of the balls set up except one"
        print "There is a radio that is playing muffled classical music"
        print "A bar is set up with high quality wines still unopened on the table"
        print "It appears that the eight ball is on the ground cracked open with something inside of it"
        print "\n\n"
        temp = raw_input("Press enter to search ")
        self._print_eventkey_closet()
        self._current_key = self._game_keys[self._GAME_KEY_CLOSET]



    def _eventkey_f1_r7_bathroom(self):
        """The event display message for when the player explores the bathroom and finds a key."""
        self._print_clear()
        print "The dripping water fills the rusted sink with a think grime"
        print "A small wind is coming from the window which slowly moves the shower curtain"
        print "On top of the cracked toilet seat lay a pile of bricks and stones that came down from the ceiling"
        print "Under the rubble inside the toilet lies a small item"
        print "\n\n"
        temp = raw_input("Press enter to search ")
        self._print_eventkey_2ndfloor()
        self._current_key = self._game_keys[self._GAME_KEY_2NDFLOOR]

        

    def _eventkey_f2_r2_study(self):
        """The event display message for when the player explores the study and finds a key."""
        self._print_clear()
        print "There is a fireplace with a fierce and warm fire still blazing"
        print "There are several bookcases lining the walls of the room"
        print "In the middle of the room there is a desk with a rocking chair"
        print "There is an unusual item that seems to be in the fireplace"
        print "\n\n"
        temp = raw_input("Press enter to search ")
        self._print_eventkey_masterbedroom()
        self._current_key = self._game_keys[self._GAME_KEY_MASTERBEDROOM]



    def _eventkey_f2_r4_washroom(self):
        """The event display message for when the player explores the washroom and finds a key."""
        self._print_clear()
        print "The dripping water fills the rusted sink with a think grime"
        print "A small wind is coming from the window which slowly moves the shower curtain"
        print "The bathtub has a dark green liquid inside of it reeking with a vile scent"
        print "There seems to be something at the bottom of the bathtub"
        print "\n\n"
        temp = raw_input("Press enter to search ")
        self._print_eventkey_guestroom()
        self._current_key = self._game_keys[self._GAME_KEY_GUESTROOM]



    def _eventkey_f2_r5_guestroom(self):
        """The event display message for when the player explores the guestroom and finds a key."""
        self._print_clear()
        print "There is a medium sized bed with the sheets wrinkled in the middle of the room"
        print "There are a few sealed suitcases near the foot of the bed"
        print "On the other side of the room there is a broken mirror with shards of smudged glass on the ground"
        print "The suitcase might have a valuable item inside of it"
        print "\n\n"
        temp = raw_input("Press enter to search ")
        self._print_eventkey_gameroom()
        self._current_key = self._game_keys[self._GAME_KEY_GAMEROOM]



    def _eventkey_f2_r6_kidsbedroom(self):
        """The event display message for when the player explores the kid's bedroom and finds a key."""
        self._print_clear()
        print "Two small beds with the sheets thrown on the floor are in the corners of this room"
        print "There are toys scattered on the floor some of which are broken"
        print "There is a slight sound of laughing children that can be heard coming from the walls"
        print "A toy chest is positioned in between the beds"
        print "\n\n"
        temp = raw_input("Press enter to search ")
        self._print_eventkey_study()
        self._current_key = self._game_keys[self._GAME_KEY_STUDY]



    def _eventkey_f2_r7_closet(self):
        """The event display message for when the player explores the closet and finds a key."""
        self._print_clear()
        print "There are a few storage containers along with a mop and bucket"
        print "The one hanging light in the middle of the room flickers slowly"
        print "There is a ladder at the back wall that leads up to a dark and gloomy attic"
        print "There is some sort of object inside of the mop bucket"
        print "\n\n"
        temp = raw_input("Press enter to search ")
        self._print_eventkey_basement()
        self._current_key = self._game_keys[self._GAME_KEY_BASEMENT]



    def _eventkey_f3_r1_attic(self):
        """The event display message for when the player explores the attic and finds a key."""
        self._print_clear()
        print "The attic is dark and broken down"
        print "The only light seen is coming from the moon through the cracked windows"
        print "At the far end of the horrifying room lies a large chest"
        print "The chest seems to have something inside of it"
        print "\n\n"
        temp = raw_input("Press enter to search ")
        self._print_eventkey_exit()
        self._current_key = self._game_keys[self._GAME_KEY_EXIT]



    def _eventnpc_butler(self):
        """The event display message for when the player talks to Jeeves The Butler."""
        self._print_clear()
        print "You find a very tall and well dressed butler tending the entrance to the manor.\n"
        print "Jeeves:  \"Hello master. Welcome to the manor. I hope you enjoy your stay because you can never leave.\""
        print "\n\n"
        temp = raw_input("Press enter to continue ")



    def _eventnpc_chef(self):
        """The event display message for when the player talks to Pierre The Chef."""
        self._print_clear()
        print "Entering the kitchen, you see a stern french chef cooking a meal.\n"
        print "Pierre:  \"What do you want? Can't you see I am busy cooking here? Please don't bother me.\""
        print "\n\n"
        temp = raw_input("Press enter to continue ")



    def _eventnpc_servant(self):
        """The event display message for when the player talks to Elmer The Servant."""
        self._print_clear()
        print "Inside the dark and gloomy room you see a short hunched man in tattered clothing.\n"
        print "Elmer:  \"Hello there. I have been working here for decades. You can't ever leave this place. It keeps you as a prisoner until you lose your mind.\""
        print "\n\n"
        temp = raw_input("Press enter to continue ")



    def _eventnpc_resident(self):
        """The event display message for when the player talks to Edward and John The Residents."""
        self._print_clear()
        print "Upon entering the room, you see two tall suited men playing billiards.\n"
        print "Edward:  \"Who are you? Why are you interupting our game?\""
        print "John:    \"Yeah! Beat it before we make you.\""
        print "\n\n"
        temp = raw_input("Press enter to continue ")



    def _eventnpc_master(self):
        """The event display message for when the player talks to Arthur The Master."""
        self._print_clear()
        print "You meet an older gentleman in a rocking chair by the fireplace reading a book.\n"
        print "Arthur:  \"Greetings! Welcome. Come in come in. If you are looking for a good read, I have the finest library in the world. Make yourself at home.\""
        print "\n\n"
        temp = raw_input("Press enter to continue ")

        

    def _eventnpc_mistress(self):
        """The event display message for when the player talks to Beverly The Mistress."""
        self._print_clear()
        print "You walk in to a dressed up woman tending to her hair.\n"
        print "Beverly:  \"Oh god! Who might you be? Why are you breaking into my room? Don't you have any manners?\""
        print "\n\n"
        temp = raw_input("Press enter to continue ")



    # rooms

    def _f0_r1_basement(self):
        """The game logic for the basement"""
        self._print_f0_r1_basement()
        cmd = raw_input("> ")
        if(cmd.upper() == "UP" or cmd.upper() == "R"):
            self._current_room = "StorageRoom"
            
        elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
            if(self._floor_explore_states[self._FLOOR_EXPLORE_BASEMENT] == 0):
                self._floor_explore_states[self._FLOOR_EXPLORE_BASEMENT] = 1
                self._eventkey_f0_r1_basement()
            
            elif(self._floor_explore_states[self._FLOOR_EXPLORE_BASEMENT] == 1):
                self._event_f0_r1_basement()
                
        elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
            self._check_quit()
        
        else:
            self._print_error()


        
    def _f1_r0_entrance(self):
        """The game logic for the entrance"""
        if(self._floor_locked_states[self._FLOOR_LOCKED_ENTRANCE] == 0):
            self._print_f1_r0_entrance_locked()
            cmd = raw_input("> ")
            if(cmd.upper() == "FRONT" or cmd.upper() == "W"):
                self._current_room = "Foyer"
                
            elif(cmd.upper() == "BACK" or cmd.upper() == "S"):
                if(self._current_key == self._game_keys[self._GAME_KEY_EXIT]):
                    self._print_eventkey_unlock()
                    self._current_key = self._game_keys[self._GAME_KEY_NONE]
                    self._floor_locked_states[self._FLOOR_LOCKED_ENTRANCE] = 1
                else:
                    self._print_error_locked()
            
            elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
                self._event_f1_r0_entrance()
            
            elif(cmd.upper() == "TALK" or cmd.upper() == "T"):
                self._eventnpc_butler()
            
            elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
                self._check_quit()
            
            else:
                self._print_error()
            
        elif(self._floor_locked_states[self._FLOOR_LOCKED_ENTRANCE] == 1):
            self._print_f1_r0_entrance_unlocked()
            cmd = raw_input("> ")
            if(cmd.upper() == "FRONT" or cmd.upper() == "W"):
                self._current_room = "Foyer"
            
            elif(cmd.upper() == "BACK" or cmd.upper() == "S"):
                self._current_room = "Exit"
            
            elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
                self._event_f1_r0_entrance()
            
            elif(cmd.upper() == "TALK" or cmd.upper() == "T"):
                self._eventnpc_butler()
            
            elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
                self._check_quit()
            
            else:
                self._print_error()



    def _f1_r1_foyer(self):
        """The game logic for the foyer"""
        if(self._floor_locked_states[self._FLOOR_LOCKED_FOYER] == 0):
            self._print_f1_r1_foyer_alllocked()
            cmd = raw_input("> ")
            if(cmd.upper() == "FRONT" or cmd.upper() == "W"):
                self._current_room = "LivingRoom"
            
            elif(cmd.upper() == "RIGHT" or cmd.upper() == "D"):
                if(self._current_key == self._game_keys[self._GAME_KEY_GAMEROOM]):
                    self._print_eventkey_unlock()
                    self._current_key = self._game_keys[self._GAME_KEY_NONE]
                    self._floor_locked_states[self._FLOOR_LOCKED_FOYER] = 2
                else:
                    self._print_error_locked()
            
            elif(cmd.upper() == "BACK" or cmd.upper() == "S"):
                self._current_room = "Entrance1"
            
            elif(cmd.upper() == "LEFT" or cmd.upper() == "A"):
                self._current_room = "DiningRoom"
            
            elif(cmd.upper() == "UP" or cmd.upper() == "R"):
                if(self._current_key == self._game_keys[self._GAME_KEY_2NDFLOOR]):
                    self._print_eventkey_unlock()
                    self._current_key = self._game_keys[self._GAME_KEY_NONE]
                    self._floor_locked_states[self._FLOOR_LOCKED_FOYER] = 1
                else:
                    self._print_error_locked()
            
            elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
                self._event_f1_r1_foyer()
            
            elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
                self._check_quit()
            
            else:
                self._print_error()
            
        elif(self._floor_locked_states[self._FLOOR_LOCKED_FOYER] == 1):
            self._print_f1_r1_foyer_gamelocked()
            cmd = raw_input("> ")
            if(cmd.upper() == "FRONT" or cmd.upper() == "W"):
                self._current_room = "LivingRoom"
            
            elif(cmd.upper() == "RIGHT" or cmd.upper() == "D"):
                if(self._current_key == self._game_keys[self._GAME_KEY_GAMEROOM]):
                    self._print_eventkey_unlock()
                    self._current_key = self._game_keys[self._GAME_KEY_NONE]
                    self._floor_locked_states[self._FLOOR_LOCKED_FOYER] = 2
                else:
                    self._print_error_locked()
            
            elif(cmd.upper() == "BACK" or cmd.upper() == "S"):
                self._current_room = "Entrance1"
            
            elif(cmd.upper() == "LEFT" or cmd.upper() == "A"):
                self._current_room = "DiningRoom"
            
            elif(cmd.upper() == "UP" or cmd.upper() == "R"):
                self._current_room = "Entrance2"
            
            elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
                self._event_f1_r1_foyer()
            
            elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
                self._check_quit()
            
            else:
                self._print_error()
            
        elif(self._floor_locked_states[self._FLOOR_LOCKED_FOYER] == 2):
            self._print_f1_r1_foyer_unlocked()
            cmd = raw_input("> ")
            if(cmd.upper() == "FRONT" or cmd.upper() == "W"):
                self._current_room = "LivingRoom"
            
            elif(cmd.upper() == "RIGHT" or cmd.upper() == "D"):
                self._current_room = "GameRoom"
            
            elif(cmd.upper() == "BACK" or cmd.upper() == "S"):
                self._current_room = "Entrance1"
            
            elif(cmd.upper() == "LEFT" or cmd.upper() == "A"):
                self._current_room = "DiningRoom"
            
            elif(cmd.upper() == "UP" or cmd.upper() == "R"):
                self._current_room = "Entrance2"
            
            elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
                self._event_f1_r1_foyer()
            
            elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
                self._check_quit()
            
            else:
                self._print_error()



    def _f1_r2_diningroom(self):
        """The game logic for the diningroom"""
        if(self._floor_locked_states[self._FLOOR_LOCKED_DININGROOM] == 0):
            self._print_f1_r2_diningroom_locked()
            cmd = raw_input("> ")
            if(cmd.upper() == "FRONT" or cmd.upper() == "W"):
                if(self._current_key == self._game_keys[self._GAME_KEY_KITCHEN]):
                    self._print_eventkey_unlock()
                    self._current_key = self._game_keys[self._GAME_KEY_NONE]
                    self._floor_locked_states[self._FLOOR_LOCKED_DININGROOM] = 1
                else:
                    self._print_error_locked()
            
            elif(cmd.upper() == "RIGHT" or cmd.upper() == "D"):
                self._current_room = "Foyer"
                
            elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
                self._event_f1_r2_diningroom()
            
            elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
                self._check_quit()
            
            else:
                self._print_error()
            
        elif(self._floor_locked_states[self._FLOOR_LOCKED_DININGROOM] == 1):
            self._print_f1_r2_diningroom_unlocked()
            cmd = raw_input("> ")
            if(cmd.upper() == "FRONT" or cmd.upper() == "W"):
                self._current_room = "Kitchen"
            
            elif(cmd.upper() == "RIGHT" or cmd.upper() == "D"):
                self._current_room = "Foyer"
            
            elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
                self._event_f1_r2_diningroom()
            
            elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
                self._check_quit()
            
            else:
                self._print_error()



    def _f1_r3_kitchen(self):
        """The game logic for the kitchen"""
        self._print_f1_r3_kitchen()
        cmd = raw_input("> ")
        if(cmd.upper() == "BACK" or cmd.upper() == "S"):
            self._current_room = "DiningRoom"
            
        elif(cmd.upper() == "LEFT" or cmd.upper() == "A"):
            self._current_room = "Bathroom"
            
        elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
            self._event_f1_r3_kitchen()
            
        elif(cmd.upper() == "TALK" or cmd.upper() == "T"):
            self._eventnpc_chef()
            
        elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
            self._check_quit()
            
        else:
            self._print_error()



    def _f1_r4_livingroom(self):
        """The game logic for the livingroom"""
        self._print_f1_r4_livingroom()
        cmd = raw_input("> ")
        if(cmd.upper() == "RIGHT" or cmd.upper() == "D"):
            self._current_room = "StorageRoom"
            
        elif(cmd.upper() == "BACK" or cmd.upper() == "S"):
            self._current_room = "Foyer"
            
        elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
            self._event_f1_r4_livingroom()
            
        elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
            self._check_quit()
        
        else:
            self._print_error()



    def _f1_r5_storageroom(self):
        """The game logic for the storage room"""
        if(self._floor_locked_states[self._FLOOR_LOCKED_STORAGEROOM] == 0):
            self._print_f1_r5_storageroom_locked()
            cmd = raw_input("> ")
            if(cmd.upper() == "LEFT" or cmd.upper() == "A"):
                self._current_room = "LivingRoom"
            
            elif(cmd.upper() == "DOWN" or cmd.upper() == "F"):
                if(self._current_key == self._game_keys[self._GAME_KEY_BASEMENT]):
                    self._print_eventkey_unlock()
                    self._current_key = self._game_keys[self._GAME_KEY_NONE]
                    self._floor_locked_states[self._FLOOR_LOCKED_STORAGEROOM] = 1
                else:
                    self._print_error_locked()
            
            elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
                if(self._floor_explore_states[self._FLOOR_EXPLORE_STORAGEROOM] == 0):
                    self._floor_explore_states[self._FLOOR_EXPLORE_STORAGEROOM] = 1
                    self._eventkey_f1_r5_storageroom()
                    
                elif(self._floor_explore_states[self._FLOOR_EXPLORE_STORAGEROOM] == 1):
                    self._event_f1_r5_storageroom()
            
            elif(cmd.upper() == "TALK" or cmd.upper() == "T"):
                self._eventnpc_servant()
                    
            elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
                self._check_quit()
            
            else:
                self._print_error()
            
        elif(self._floor_locked_states[self._FLOOR_LOCKED_STORAGEROOM] == 1):
            self._print_f1_r5_storageroom_unlocked()
            cmd = raw_input("> ")
            if(cmd.upper() == "LEFT" or cmd.upper() == "A"):
                self._current_room = "LivingRoom"
            
            elif(cmd.upper() == "DOWN" or cmd.upper() == "F"):
                self._current_room = "Basement"
            
            elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
                if(self._floor_explore_states[self._FLOOR_EXPLORE_STORAGEROOM] == 0):
                    self._floor_explore_states[self._FLOOR_EXPLORE_STORAGEROOM] = 1
                    self._eventkey_f1_r5_storageroom()
                    
                elif(self._floor_explore_states[self._FLOOR_EXPLORE_STORAGEROOM] == 1):
                    self._event_f1_r5_storageroom()
            
            elif(cmd.upper() == "TALK" or cmd.upper() == "T"):
                self._eventnpc_servant()
                    
            elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
                self._check_quit()
            
            else:
                self._print_error()



    def _f1_r6_gameroom(self):
        """The game logic for the game room"""
        self._print_f1_r6_gameroom()
        cmd = raw_input("> ")
        if(cmd.upper() == "LEFT" or cmd.upper() == "A"):
            self._current_room = "Foyer"
            
        elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
            if(self._floor_explore_states[self._FLOOR_EXPLORE_GAMEROOM] == 0):
                self._floor_explore_states[self._FLOOR_EXPLORE_GAMEROOM] = 1
                self._eventkey_f1_r6_gameroom()
                
            elif(self._floor_explore_states[self._FLOOR_EXPLORE_GAMEROOM] == 1):
                self._event_f1_r6_gameroom()
            
        elif(cmd.upper() == "TALK" or cmd.upper() == "T"):
            self._eventnpc_resident()
                
        elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
            self._check_quit()
        
        else:
            self._print_error()



    def _f1_r7_bathroom(self):
        """The game logic for the bathroom"""
        self._print_f1_r7_bathroom()
        cmd = raw_input("> ")
        if(cmd.upper() == "RIGHT" or cmd.upper() == "D"):
            self._current_room = "Kitchen"
            
        elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
            if(self._floor_explore_states[self._FLOOR_EXPLORE_BATHROOM] == 0):
                self._floor_explore_states[self._FLOOR_EXPLORE_BATHROOM] = 1
                self._eventkey_f1_r7_bathroom()
                
            elif(self._floor_explore_states[self._FLOOR_EXPLORE_BATHROOM] == 1):
                self._event_f1_r7_bathroom()
                
        elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
            self._check_quit()
        
        else:
            self._print_error()
        


    def _f2_r0_entrance(self):
        """The game logic for the 2nd floor entrance"""
        self._print_f2_r0_entrance()
        cmd = raw_input("> ")
        if(cmd.upper() == "RIGHT" or cmd.upper() == "D"):
            self._current_room = "Hallway"
            
        elif(cmd.upper() == "DOWN" or cmd.upper() == "F"):
            self._current_room = "Foyer"
            
        elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
            self._event_f2_r0_entrance()
            
        elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
            self._check_quit()
        
        else:
            self._print_error()



    def _f2_r1_hallway(self):
        """The game logic for the hallway"""
        if(self._floor_locked_states[self._FLOOR_LOCKED_HALLWAY] == 0):
            self._print_f2_r1_hallway_init()
            cmd = raw_input("> ")
            if(cmd.upper() == "FRONT 1" or cmd.upper() == "W1"):
                if(self._current_key == self._game_keys[self._GAME_KEY_STUDY]):
                    self._print_eventkey_unlock()
                    self._current_key = self._game_keys[self._GAME_KEY_NONE]
                    self._floor_locked_states[self._FLOOR_LOCKED_HALLWAY] = 4
                else:
                    self._print_error_locked()
            
            elif(cmd.upper() == "FRONT 2" or cmd.upper() == "W2"):
                if(self._current_key == self._game_keys[self._GAME_KEY_MASTERBEDROOM]):
                    self._print_eventkey_unlock()
                    self._current_key = self._game_keys[self._GAME_KEY_NONE]
                    self._floor_locked_states[self._FLOOR_LOCKED_HALLWAY] = 3
                else:
                    self._print_error_locked()
            
            elif(cmd.upper() == "BACK 1" or cmd.upper() == "S1"):
                if(self._current_key == self._game_keys[self._GAME_KEY_GUESTROOM]):
                    self._print_eventkey_unlock()
                    self._current_key = self._game_keys[self._GAME_KEY_NONE]
                    self._floor_locked_states[self._FLOOR_LOCKED_HALLWAY] = 2
                else:
                    self._print_error_locked()
            
            elif(cmd.upper() == "BACK 2" or cmd.upper() == "S2"):
                self._current_room = "KidsBedroom"
            
            elif(cmd.upper() == "BACK 3" or cmd.upper() == "S3"):
                if(self._current_key == self._game_keys[self._GAME_KEY_CLOSET]):
                    self._print_eventkey_unlock()
                    self._current_key = self._game_keys[self._GAME_KEY_NONE]
                    self._floor_locked_states[self._FLOOR_LOCKED_HALLWAY] = 1
                else:
                    self._print_error_locked()
            
            elif(cmd.upper() == "LEFT" or cmd.upper() == "A"):
                self._current_room = "Entrance2"
            
            elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
                self._event_f2_r1_hallway()
            
            elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
                self._check_quit()
            
            else:
                self._print_error()
            
        elif(self._floor_locked_states[self._FLOOR_LOCKED_HALLWAY] == 1):
            self._print_f2_r1_hallway_unlockcloset()
            cmd = raw_input("> ")
            if(cmd.upper() == "FRONT 1" or cmd.upper() == "W1"):
                self._current_room = "Study"
            
            elif(cmd.upper() == "FRONT 2" or cmd.upper() == "W2"):
                self._current_room = "MasterBedroom"
            
            elif(cmd.upper() == "BACK 1" or cmd.upper() == "S1"):
                self._current_room = "Guestroom"
            
            elif(cmd.upper() == "BACK 2" or cmd.upper() == "S2"):
                self._current_room = "KidsBedroom"
            
            elif(cmd.upper() == "BACK 3" or cmd.upper() == "S3"):
                self._current_room = "Closet"
            
            elif(cmd.upper() == "LEFT" or cmd.upper() == "A"):
                self._current_room = "Entrance2"
            
            elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
                self._event_f2_r1_hallway()
            
            elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
                self._check_quit()
            
            else:
                self._print_error()
            
        elif(self._floor_locked_states[self._FLOOR_LOCKED_HALLWAY] == 2):
            self._print_f2_r1_hallway_unlockguestroom()
            cmd = raw_input("> ")
            if(cmd.upper() == "FRONT 1" or cmd.upper() == "W1"):
                self._current_room = "Study"
            
            elif(cmd.upper() == "FRONT 2" or cmd.upper() == "W2"):
                self._current_room = "MasterBedroom"
            
            elif(cmd.upper() == "BACK 1" or cmd.upper() == "S1"):
                self._current_room = "Guestroom"
            
            elif(cmd.upper() == "BACK 2" or cmd.upper() == "S2"):
                self._current_room = "KidsBedroom"
            
            elif(cmd.upper() == "BACK 3" or cmd.upper() == "S3"):
                if(self._current_key == self._game_keys[self._GAME_KEY_CLOSET]):
                    self._print_eventkey_unlock()
                    self._current_key = self._game_keys[self._GAME_KEY_NONE]
                    self._floor_locked_states[self._FLOOR_LOCKED_HALLWAY] = 1
                else:
                    self._print_error_locked()
            
            elif(cmd.upper() == "LEFT" or cmd.upper() == "A"):
                self._current_room = "Entrance2"
            
            elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
                self._event_f2_r1_hallway()
            
            elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
                self._check_quit()
            
            else:
                self._print_error()
            
        elif(self._floor_locked_states[self._FLOOR_LOCKED_HALLWAY] == 3):
            self._print_f2_r1_hallway_unlockmasterbedroom()
            cmd = raw_input("> ")
            if(cmd.upper() == "FRONT 1" or cmd.upper() == "W1"):
                self._current_room = "Study"
            
            elif(cmd.upper() == "FRONT 2" or cmd.upper() == "W2"):
                self._current_room = "MasterBedroom"
            
            elif(cmd.upper() == "BACK 1" or cmd.upper() == "S1"):
                if(self._current_key == self._game_keys[self._GAME_KEY_GUESTROOM]):
                    self._print_eventkey_unlock()
                    self._current_key = self._game_keys[self._GAME_KEY_NONE]
                    self._floor_locked_states[self._FLOOR_LOCKED_HALLWAY] = 2
                else:
                    self._print_error_locked()
            
            elif(cmd.upper() == "BACK 2" or cmd.upper() == "S2"):
                self._current_room = "KidsBedroom"
            
            elif(cmd.upper() == "BACK 3" or cmd.upper() == "S3"):
                if(self._current_key == self._game_keys[self._GAME_KEY_CLOSET]):
                    self._print_eventkey_unlock()
                    self._current_key = self._game_keys[self._GAME_KEY_NONE]
                    self._floor_locked_states[self._FLOOR_LOCKED_HALLWAY] = 1
                else:
                    self._print_error_locked()
            
            elif(cmd.upper() == "LEFT" or cmd.upper() == "A"):
                self._current_room = "Entrance2"
            
            elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
                self._event_f2_r1_hallway()
            
            elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
                self._check_quit()
            
            else:
                self._print_error()
            
        elif(self._floor_locked_states[self._FLOOR_LOCKED_HALLWAY] == 4):
            self._print_f2_r1_hallway_unlockstudy()
            cmd = raw_input("> ")
            if(cmd.upper() == "FRONT 1" or cmd.upper() == "W1"):
                self._current_room = "Study"
            
            elif(cmd.upper() == "FRONT 2" or cmd.upper() == "W2"):
                if(self._current_key == self._game_keys[self._GAME_KEY_MASTERBEDROOM]):
                    self._print_eventkey_unlock()
                    self._current_key = self._game_keys[self._GAME_KEY_NONE]
                    self._floor_locked_states[self._FLOOR_LOCKED_HALLWAY] = 3
                else:
                    self._print_error_locked()
            
            elif(cmd.upper() == "BACK 1" or cmd.upper() == "S1"):
                if(self._current_key == self._game_keys[self._GAME_KEY_GUESTROOM]):
                    self._print_eventkey_unlock()
                    self._current_key = self._game_keys[self._GAME_KEY_NONE]
                    self._floor_locked_states[self._FLOOR_LOCKED_HALLWAY] = 2
                else:
                    self._print_error_locked()
            
            elif(cmd.upper() == "BACK 2" or cmd.upper() == "S2"):
                self._current_room = "KidsBedroom"
            
            elif(cmd.upper() == "BACK 3" or cmd.upper() == "S3"):
                if(self._current_key == self._game_keys[self._GAME_KEY_CLOSET]):
                    self._print_eventkey_unlock()
                    self._current_key = self._game_keys[self._GAME_KEY_NONE]
                    self._floor_locked_states[self._FLOOR_LOCKED_HALLWAY] = 1
                else:
                    self._print_error_locked()
            
            elif(cmd.upper() == "LEFT" or cmd.upper() == "A"):
                self._current_room = "Entrance2"
            
            elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
                self._event_f2_r1_hallway()
            
            elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
                self._check_quit()
            
            else:
                self._print_error()



    def _f2_r2_study(self):
        """The game logic for the study"""
        self._print_f2_r2_study()
        cmd = raw_input("> ")
        if(cmd.upper() == "BACK" or cmd.upper() == "S"):
            self._current_room = "Hallway"
            
        elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
            if(self._floor_explore_states[self._FLOOR_EXPLORE_STUDY] == 0):
                self._floor_explore_states[self._FLOOR_EXPLORE_STUDY] = 1
                self._eventkey_f2_r2_study()
                
            elif(self._floor_explore_states[self._FLOOR_EXPLORE_STUDY] == 1):
                self._event_f2_r2_study()
            
        elif(cmd.upper() == "TALK" or cmd.upper() == "T"):
            self._eventnpc_master()
                
        elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
            self._check_quit()
        
        else:
            self._print_error()
        


    def _f2_r3_masterbedroom(self):
        """The game logic for the master bedroom"""
        self._print_f2_r3_masterbedroom()
        cmd = raw_input("> ")
        if(cmd.upper() == "RIGHT" or cmd.upper() == "D"):
            self._current_room = "Washroom"
            
        elif(cmd.upper() == "BACK" or cmd.upper() == "S"):
            self._current_room = "Hallway"
            
        elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
            self._event_f2_r3_masterbedroom()
            
        elif(cmd.upper() == "TALK" or cmd.upper() == "T"):
            self._eventnpc_mistress()
            
        elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
            self._check_quit()
        
        else:
            self._print_error()



    def _f2_r4_washroom(self):
        """The game logic for the washroom"""
        self._print_f2_r4_washroom()
        cmd = raw_input("> ")
        if(cmd.upper() == "LEFT" or cmd.upper() == "A"):
            self._current_room = "MasterBedroom"
            
        elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):    
            if(self._floor_explore_states[self._FLOOR_EXPLORE_WASHROOM] == 0):
                self._floor_explore_states[self._FLOOR_EXPLORE_WASHROOM] = 1
                self._eventkey_f2_r4_washroom()
                
            elif(self._floor_explore_states[self._FLOOR_EXPLORE_WASHROOM] == 1):
                self._event_f2_r4_washroom()
            
        elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
            self._check_quit()
        
        else:
            self._print_error()



    def _f2_r5_guestroom(self):
        """The game logic for the guestroom"""
        self._print_f2_r5_guestroom()
        cmd = raw_input("> ")
        if(cmd.upper() == "FRONT" or cmd.upper() == "W"):
            self._current_room = "Hallway"
            
        elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
            if(self._floor_explore_states[self._FLOOR_EXPLORE_GUESTROOM] == 0):
                self._floor_explore_states[self._FLOOR_EXPLORE_GUESTROOM] = 1
                self._eventkey_f2_r5_guestroom()
                
            elif(self._floor_explore_states[self._FLOOR_EXPLORE_GUESTROOM] == 1):
                self._event_f2_r5_guestroom()
                
        elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
            self._check_quit()
        
        else:
            self._print_error()
        


    def _f2_r6_kidsbedroom(self):
        """The game logic for the kid's bedroom"""
        self._print_f2_r6_kidsbedroom()
        cmd = raw_input("> ")
        if(cmd.upper() == "FRONT" or cmd.upper() == "W"):
            self._current_room = "Hallway"
            
        elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
            if(self._floor_explore_states[self._FLOOR_EXPLORE_KIDSBEDROOM] == 0):
                self._floor_explore_states[self._FLOOR_EXPLORE_KIDSBEDROOM] = 1
                self._eventkey_f2_r6_kidsbedroom()
                
            elif(self._floor_explore_states[self._FLOOR_EXPLORE_KIDSBEDROOM] == 1):
                self._event_f2_r6_kidsbedroom()
            
        elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
            self._check_quit()
        
        else:
            self._print_error()



    def _f2_r7_closet(self):
        """The game logic for the closet"""
        if(self._floor_locked_states[self._FLOOR_LOCKED_CLOSET] == 0):
            self._print_f2_r7_closet_locked()
            cmd = raw_input("> ")
            if(cmd.upper() == "FRONT" or cmd.upper() == "W"):
                self._current_room = "Hallway"
            
            elif(cmd.upper() == "UP" or cmd.upper() == "R"):
                if(self._current_key == self._game_keys[self._GAME_KEY_ATTIC]):
                    self._print_eventkey_unlock()
                    self._current_key = self._game_keys[self._GAME_KEY_NONE]
                    self._floor_locked_states[self._FLOOR_LOCKED_CLOSET] = 1
                else:
                    self._print_error_locked()
            
            elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):        
                if(self._floor_explore_states[self._FLOOR_EXPLORE_CLOSET] == 0):
                    self._floor_explore_states[self._FLOOR_EXPLORE_CLOSET] = 1
                    self._eventkey_f2_r7_closet()
                    
                elif(self._floor_explore_states[self._FLOOR_EXPLORE_CLOSET] == 1):
                    self._event_f2_r7_closet()
            
            elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
                self._check_quit()
            
            else:
                self._print_error()
            
        elif(self._floor_locked_states[self._FLOOR_LOCKED_CLOSET] == 1):
            self._print_f2_r7_closet_unlocked()
            cmd = raw_input("> ")
            if(cmd.upper() == "FRONT" or cmd.upper() == "W"):
                self._current_room = "Hallway"
            
            elif(cmd.upper() == "UP" or cmd.upper() == "R"):
                self._current_room = "Attic"
            
            elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):        
                if(self._floor_explore_states[self._FLOOR_EXPLORE_CLOSET] == 0):
                    self._floor_explore_states[self._FLOOR_EXPLORE_CLOSET] = 1
                    self._eventkey_f2_r7_closet()
                    
                elif(self._floor_explore_states[self._FLOOR_EXPLORE_CLOSET] == 1):
                    self._event_f2_r7_closet()
            
            elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
                self._check_quit()
            
            else:
                self._print_error()



    def _f3_r1_attic(self):
        """The game logic for the attic"""
        self._print_f3_r1_attic()
        cmd = raw_input("> ")
        if(cmd.upper() == "DOWN" or cmd.upper() == "F"):
            self._current_room = "Closet"
            
        elif(cmd.upper() == "EXPLORE" or cmd.upper() == "E"):
            if(self._floor_explore_states[self._FLOOR_EXPLORE_ATTIC] == 0):
                self._floor_explore_states[self._FLOOR_EXPLORE_ATTIC] = 1
                self._eventkey_f3_r1_attic()
                
            elif(self._floor_explore_states[self._FLOOR_EXPLORE_ATTIC] == 1):
                self._event_f3_r1_attic()
            
        elif(cmd.upper() == "QUIT" or cmd.upper() == "Q"):
            self._check_quit()
        
        else:
            self._print_error()


            
    def _f_exit(self):
        """The game logic for the exit"""
        self._print_win()
        self._control = False


        
    # start

    def play(self):
        """Start the game"""
        self._print_intro()
        while(self._control):
            self._check_room()
        

