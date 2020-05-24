# GlitchBot

GlitchBot is a Discord bot capable of databending and datamoshing static images and animated gifs, right in your Discord server!

## Dependencies

GlitchBot is a Python script powered by [discordpy](https://discordpy.readthedocs.io/en/latest/). It uses [glitch_this](https://github.com/TotallyNotChase/glitch-this) to perform databending operations. Please ensure that you discordpy, glitch_this, and all of their respective dependencies installed on your system before running GlitchBot.

## Usage

```python
# Glitchbot.py
BOT_NAME = 'NAME#NUMBER' #Replace this with your bot's name (i.e. 'GlitchBot#1234')
```
```
# token.txt
# Place ONLY your bot's token (from Discord Developer Portal) in this file
```
```bash
$ python3 glitchbot.py
```
Once GlitchBot has been added to a channel and is running, send an image in that channel with the caption '!glitchbot' (no quotes). If you need to restart the bot, send '!glitchbot restart' (no quotes) in the channel. This is useful if you change the code. To keep the bot running on your remote server even after you quit, use [screens](https://linuxize.com/post/how-to-use-linux-screen/).

### Summary of Commands
| Command | Description | Notes |
|---------|----------|------|
| !glitchbot | Glitch captioned image |   |
| !glitchbot restart | Restarts bot and re-reads Python file | If line in .py containing this command has moved, the command will fail |
| !glitchbot status | Sends the bot's online status to channel |   |
| !glitchbot stats | Sends number of glitches performed in the channel | Currently unable to distinguish between different channels with identical names |

## Warning

This script was created just for fun, and has not been extensively tested for performance or security risks. I am also by no means a Python expert... Use at your own discretion!
