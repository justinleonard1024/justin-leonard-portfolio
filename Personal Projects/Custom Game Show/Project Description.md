# Project Description
**Project Name:** Custom Game Show <br />
**Programming Language:** C# <br />
**Entry Point:** Program.cs <br />

**Assets Location:** <br />
"Icons" and "Images" are resources <br />
"Media" goes in "\<User Name\>\AppData\Local\Custom Game Show" <br />

**Information:** <br />
This project was made as an updated version of "Custom Jeopardy", which is another project in this portfolio. <br />
The original idea came from playing a trivia game with my friends, and I wanted a custom version for ourselves. <br />
I made "Custom Jeopardy" as a simple proof of concept, then "Custom Game Show" as an updated version. <br />
This version was designed to be more than a trivia game, but an entire game show that the user can make using the general setup. <br />
This was made so that anyone could make the game instead of me hard coding in the information. <br />
There needed to be immense customization for any user to have. My friend used the application, and it worked great. <br />

The game has 120 questions or events. There are 10 categories with 12 questions per category. There are 4 rounds with 30 questions each. <br />
Points are added manually and the player with the highest score at the end wins. <br />
At the end, there are three buttons for each contestant. The winner will be pressed, and a video will be played. <br />

The settings menu is for editing the contestant names, game board color, contestant colors, category colors, and media types. <br />
The log menu will display the score, question counter, round number, and opened media for every game played. This is for backup purposes. <br />
The add, view, and edit score menus are for score modification. <br />
The media menu allows the user to play up to 14 custom videos. This can also be done with the numpad keys at any time. <br />
The information menu displays the rules, directories where all assets are stored, and the custom video keys. <br />

Each button can be a question, event, or whatever the host wants. Each question button has a media type setting for different configurations. <br />
The media types are ImageImage, ImageVideoImageImage, ImageVideoImageVideo, VideoImageImage, and VideoImageVideo. <br />
What ever media type the user selects for a specific question will be what assets the program looks for and displays. <br />

For example, if "ImageVideoImageVideo" is the media type of "QuestionX\_Y" where X is the category and Y is the question number: <br />
The program will search for "Prompts/PromptX\_Y.png", "Questions/QuestionX\_Ya.mp4", "Questions/QuestionX\_Yb.png", and "Answers/AnswerX\_Y.mp4". <br />
If the files for the selected media type of a specific question are not present, an error will occur. <br />

The folder "<User Name>\AppData\Local\Custom Game Show" stores the images and videos for the entire application. <br />
The user will modify these files to have whatever media suits the game show they are creating.
