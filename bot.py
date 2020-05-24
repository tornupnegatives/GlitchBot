"""
Glitchbot is a Discord bot powered by discordpy.
It listens in the channel for a user to send a supported image file,
which it will download, databend, and then send back.
"""

import sys
import os

import discord

import image
import glitch

# Useful values
client    = discord.Client()
BOT_NAME  = 'GlitchBot'
TOKEN     = ''

@client.event
async def on_ready():
    print(f'Glitchbot is online as {client.user}')
    
@client.event
async def on_message(message):

    # Get working channel
    channel = message.channel
    
    # Ignore messages from self
    if message.author == client.user:
        return
        
    """
    # Ignore messages from other bots
    if message.author.bot:
        return
    """
    
    # Listen for commands
    if '!glitchbot' in message.content or '!gb' in message.content:
    
        # For updating code on-the-fly (BUGGY!)
        if 'restart' in message.content:
            print(f'{message.author} issued restart command from {channel}.')
            await channel.send('Restarting GlitchBot...')
            
            try:
                os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
            except:
                print('ERROR: Failed to restart Glitchbot.')
                await channel.send('Could not restart GlitchBot. Try again later.')
                
        # Get bot operating status
        elif 'status' in message.content:
            status = f'{BOT_NAME} is currently online in channel {channel}'
            
            await channel.send(status)
            
        # Send number of glitches processed in channel
        # NOTE: Cannot distinguish between channels with idenitcal names
        elif 'stats' in message.content:
            with open('stats.txt', 'r') as stats:
                glitchCount = stats.read().count(f'{channel}')

                await channel.send(
                f'{BOT_NAME} has glitched '
                + f'{glitchCount} images in channel {channel}')
             
        # Stop execution of bot from within channel
        elif 'shutdown' in message.content:
            print(f'{message.author} issued shutdown command from {channel}.')
            await channel.send("Glitchbot is shutting down...")
            await client.close()
            
        elif len(message.attachments) > 0:
            webURL    = message.attachments[0].url
            imageType = image.getType(webURL)
            
            if imageType != 'INVALID':

                # Download remote file
                imageFile = image.download(webURL, imageType)
                glitchFile = glitch.image(imageFile, imageType)

                # Log glitch for stats
                with open('stats.txt', 'a+') as stats:
                    stats.write(f'\n{channel}')
                
                await channel.send(file=discord.File(glitchFile))
        
                # Cleanup
                try:
                    os.remove(imageFile)
                    print(f'Removed [{imageFile}] from disk')
                    os.remove(glitchFile)
                    print(f'Removed [{glitchFile}] from disk')
                except:
                    print(f'ERROR: Failed to remove files: [{imageFile}], '
                          + f'[{glitchFile}]')

        elif 'help' in message.content:
            await channel.send('---glitchbot help---\n'
            + 'invoke with \'!glitchbot\' or \'!gb\'\n'
            + '!gb                returns glitch of captioned image\n'
            + '!gb zalgo <text>   returns zalgo text\n'
            + '!gb stats          get # glitches in channel\n'
            + '!gb status         get online status\n'
            + '!gb restart        restart bot if stuck\n'
            + '!gb shutdown       take bot offline')
    
#######################
# Bot startup script #
#######################
print('GlitchBot successfully loaded onto local machine')

# Start bot
client.run(TOKEN)
