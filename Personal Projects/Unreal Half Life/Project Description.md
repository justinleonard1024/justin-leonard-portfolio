# Project Description
**Project Name:** Unreal Half Life <br />
**Programming Language:** C# <br />
**Entry Point:** Program.cs <br />

**Assets Location:** <br />
"Icons" and "Images" are resources

**Information:** <br />
This project is a game launcher I created for a mod for the game Half-Life 2.
The mod is titled "Unreal Half Life" and uses Half-Life 2 and the source engine as a base.
I created this to test map making and game design, as I was interested in this at the time.

The installer for "Unreal Half Life" will download the launcher to program files.
It will also put my assets into the Half-Life 2 custom folder.
These assets include my custom maps, models, materials, sounds, and scripts.

The reason for the launcher is to run "Unreal Half Life" while also being able to play Half-Life 2 normally.
If you run Half-Life 2 even with my custom files, the game will run normally.
If you run the Unreal Half Life launcher, it will run the mod instead.

The way this works is through a file in the root directory of Half-Life 2 called gameinfo.txt.
The gameinfo file contains information about the game including specifying the directories that have all the assets.
When you press the "Play Game" button in the launcher, it will first modify the gameinfo file.
The asset directories in gameinfo are overwritten to my custom assets folder.
Additionally, other files will be edited to modify the graphics settings specified in the launcher.

Then Half-Life 2 is launched soon after.
Since the gameinfo file now has my assets active, my mod will be used instead.
When Half-Life 2 is exited, the launcher will terminate as well.
As the launcher ends execution, it will return the gameinfo file back to it's original state.
This will allow the game to be run normally once it's executed.