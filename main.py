#!/home/pi/.virtualenvs/discord/bin/python

import os
import sys
import git
from Bot import Bot

def getToken():
   with open('token.txt', 'r') as file:
      token = file.readline()
   return token

def updateRepo():
   cwd = os.getcwd()
   repo = git.Repo(cwd)

   current = repo.head.commit
   repo.remotes.origin.pull()

   if current != repo.head.commit:
      print('Updated to latest version\n')
   else:
      print('Already on latest version\n')

# ------------------ BOT STARTUP SCRIPT ----------------------
print('          Welcome to GlitchBot          ')
print('========================================\n')

print('Updating to latest version...')
updateRepo()

print('Initializing...')
bot = Bot()

print('Fetching token...')
token = getToken()

print('Starting service...\n')
bot.run(token)

# If bot closes with update status, update and relaunch
if bot.shouldUpdate == 1:
   print('Update request received...')
   updateRepo()


   os.execv('./main.py', ['\"' + './main.py' + '\"'] + sys.argv)

else:
   print('Shutting down bot...\n')
