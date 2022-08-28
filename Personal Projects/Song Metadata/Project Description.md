# Project Description
**Project Name:** Song Metadata <br />
**Programming Language:** JavaScript, HTML, Mp3tag Scripts <br />
**Entry Point:** Not Applicable <br />

**Assets Location:** <br />
Not Applicable

**Information:** <br />
This project contains scripts used with the program Mp3tag.
Mp3tag is a program used to edit and organize the metadata of audio files.
I use this program to modify my personal music library.

One feature of this program is to create scripts using the metadata of the selected audio files.
It can create HTML files to display a web page and scripts using the metadata.
The program comes with it's own scripting commands that allow you to use the metadata and scripting to create the HTML document.

For example, you can use the $loop(<metadata>) command to loop through whatever data you want.
If you do $loop(%_filename%), it will loop whatever code is in the block the number of files there are.
An example would be:

$loop(%_filename%)
<p>%_filename%</p>
$loopend()

This script will loop the HTML code and create a number of <p> equal to the number of files and the content will be the file names.
You can add JavaScript to the document in conjunction with the Mp3tag commands to create interesting scripts.

The "PlaylistSelector" script is used to select the playlists the songs will be added to.
I used a specific metadata tag to store a list of custom playlists I have in iTunes.
I have each smart playlist in iTunes set to match the playlist values in that specific tag.
You select the playlists you want for each song then it will display the list of the tags in order.
After that, you use Mp3tag to copy over the data.

The "SaveToText" script is used to simply select songs from a song list and save those songs to a text file.
The file will have the number of songs in the list and the songs that were selected.