# Project Description
**Project Name:** Display Reversal <br />
**Programming Language:** C# <br />
**Entry Point:** Program.cs <br />

**Assets Location:** <br />
"nircmd.exe" in "Applications" goes in the same folder as the application <br />
"Icons" are resources

**Information:** <br />
This project was made when I recently started using 2 monitors for my computer's display.
I noticed that some applications only open in the screen that is set to the primary display.
You can't change where the application opens, nor move it when it is running.

To get around this, I made Display Reversal to toggle the primary display between the two monitors.
I use the Windows command line tool "nircmd" to set the primary display.

When the program is executed, it will check which screen is set as the primary display.
If the primary display is screen 1, it will change it to screen 2.
If the primary display is screen 2, it will change it to screen 1.
It executes immediately and seamlessly changes the primary display.