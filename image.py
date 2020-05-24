"""
image.py contains routines for downloading images from the web
"""
import os
import random

import requests
import string

SUPPORTED = ['.jpg', '.jpeg', '.png', '.gif']

def getType(imageFile):
    for extension in SUPPORTED:
        if imageFile.endswith(extension):
            return extension
    return 'INVALID'

def randFilename(length):
    charSet = string.ascii_lowercase
    return ''.join(random.choice(charSet) for i in range(length))

def download(webURL, imageType):
    # Download remote file
    request   = requests.get(webURL, allow_redirects=True)
    imageFile = f'tmp/{randFilename(5)}{imageType}'

    # Save to disk and return filepath
    if not os.path.exists('tmp'):
        os.makedirs('tmp')

    try:
        with open(imageFile, 'wb') as local:
            local.write(request.content)
        print(f'Saved image as [{imageFile}]')
        return imageFile

    except:
        print(f'ERROR: Failed to save image [{webURL}] to disk as [{imageFile}]')
