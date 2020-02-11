#!/usr/bin/env python3

import os
import json
import urllib.request
import requests

completedPath = '/tank/Working/drone'
importPath = '/mnt/tank/Working/drone'

def importShows():
        for release in os.listdir(completedPath):
        APIkey = 'APIKEY'
        endpoint = f'http://192.168.0.23:2503/sonarr/api/command?apikey={APIkey}'
        data = {"name": "DownloadedEpisodesScan", "path": f"{importPath}/{release}"}
        r = requests.post(url = endpoint, data = str(data))
        print(json.loads(r.text))

if __name__ == '__main__':
    importShows()
