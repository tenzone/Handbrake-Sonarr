import os
import json
import urllib.request
import requests


startingPath = '/path/to/shows/to/keep'
workingPath = '/path/to/holding/folder/for/re-encode'
completedPath = '/path/to/completed/encode'
importPath = '/path/for/sonarr/import'

def get_vids():
    os.chdir(startingPath)
    for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
        for item in filenames:
            if '.mkv' in item or '.mp4' in item:
                os.rename(f'{dirpath}/{item}', f'{workingPath}/{item}')

def transcode():
    os.chdir(workingPath)
    for filenames in os.listdir(workingPath):
        if '.mkv' in filenames or '.mp4' in filenames:
            HandbrakeCliCommand = f'HandBrakeCLI --preset-import-file /path/to/preset -Z \"presetName\" -i {filenames} -o {completedPath}/{filenames}'
            os.system(HandbrakeCliCommand)
            deleteCommand= f'rm -rf {workingPath}/{filenames}'
            os.system(deleteCommand)
            importShows()

def importShows():
    dircontents = os.listdir(completedPath)
    files = []
    for item in dircontents:
        if '.mkv' in item or '.mp4' in item:
            files.append(item)

    for items in files:
        os.mkdir(completedPath + '/' + str(items[:-4]))
        os.rename(completedPath + '/' + items, completedPath + '/' + str(items[:-4]) + '/' + items)


    for release in os.listdir(completedPath):
        APIkey = 'SonarrAPIkeyHERE'
        endpoint = f'http://sonarrip:port/sonarr/api/command?apikey={APIkey}' #the /sonarr may not be needed if you do not set a url base. remove if not needed
        data = {"name": "DownloadedEpisodesScan", "path": f"{importPath}/{release}"}
        r = requests.post(url = endpoint, data = str(data))
        print(json.loads(r.text))



get_vids()
transcode()
importShows() #this was ran again because in testing i was having files left around. this may be redundant.
