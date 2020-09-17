#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import urllib.request
import os
import sys

url = 'https://launchermeta.mojang.com/mc/game/version_manifest.json'

data = requests.get(url)


def Download_Server(data):
    Download_Manifest_URL = data['versions'][0]['url']
    data = requests.get(Download_Manifest_URL)
    data = data.json()

    Server_Download_URL = data['downloads']['server']['url']

    urllib.request.urlretrieve(Server_Download_URL,
                               'minecraft_server.{0}.jar'.format(Latest_Server_Version))


if data.status_code == 200:
    data = data.json()
    files = os.listdir(os.curdir)

    Latest_Server_Version = data['latest']['release']

    # Checks files for Server Jar

for file in files:
    if '.jar' in file:
        print('Server File Found. Checking for Version...')

        # Checks if Server Version is Latest

        if Latest_Server_Version in file:
            print('Server Version is Latest.')
        else:
            os.remove(file)
            try:
                Download_Server(data)
                print('Updated Server Version to Latest.')
            except Exception as error:
                raise error
            sys.exit()
    else:
        try:
            Download_Server(data)
            print('Installed Latest Server Version.')
        except Exception as error:
            raise error
        sys.exit()
else:
    print('Manifest Site is down. Unable to get data.')
