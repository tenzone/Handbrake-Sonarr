# Handbrake-Sonarr

## Purpose

The purpose of this project is to help me automate my workflow from download to sonarr import. My current workflow is as follows:

1. Download episodes via sonarr and sabnzbd+
2. Decide which shows i want to keep. Sometimes I just watch then delete shows, other times I keep them. 
3. Move the shows i want to keep to a specified folder
4. Search the folders for .mkv or .mp4 files, then move them to a "working" area
5. Run a HandBrakeCLI command to re-encode all files in that folder to a "completed" folder. The completed folder used to be the drone factory folder. the deprecation of the Drone Factory is what led me to do this.
6. Delete the original files from the "working" folder.

## Execution

This script will shorten my workflow greatly, it now goes as follows:

1. Download episodes
2. Decide shows to keep and move to specified "starting" folder
3. automatically run script via cronjob nightly.

There can be slight issues if your permissions arent correct when handbrake tries to read/write.

### Usage

1. Fill out the appropriate paths at the top. 
2. Enter your own handbrakeCLI command. using a preset is a bit easier to deal with, but a full one-liner will work as well
3. Edit your Sonarr info including the API key, and the sonarr ip address and port.

## Followup

The script is far from perfect, and im sure theres plenty of examples of bad code in it. For example, the importShows command sometimes left a file behind, so i call it again at the end of the script. I think this is fixed, but havent removed the code yet. All in all, it does the trick for me though, at least so for