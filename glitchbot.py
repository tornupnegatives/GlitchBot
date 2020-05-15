# Glitchbot is a Discord bot powered by discordpy.
# It listens in the channel for a user to send a supported image file,
# which it will download, databend, and then send back.

import discord
import requests # For HTTP downloads
import random
import string
import sys
import os
from glitch_this import ImageGlitcher

# Useful values
SUPPORTED = ['.jpg', '.jpeg', '.png', '.gif']
BOT_NAME = 'GlitchBot#3610'
LOOP = 0    # Infinite=0
client = discord.Client()

#####################################
# Necessary functions for discordpy #
#####################################
@client.event
async def on_ready():
    print(f'Glitchbot successfully logged on as {client.user}')
    
@client.event
async def on_message(message):

    # Get working channel
    channel = message.channel
    
    # Listen for update command
    if '!glitchbot restart' in message.content.lower():
        print('Received restart command. Restarting...')
        await channel.send('Restarting GlitchBot...')
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    
    # Status
    elif '!glitchbot status' in message.content.lower():
        status = f'{BOT_NAME} is currently online in channel {channel}'
        await channel.send(status)

    # Stats
    elif '!glitchbot stats' in message.content.lower():
        with open('stats.txt', 'r') as stats:
            num_glitch = stats.read().count(f'{channel}')
            await channel.send(
            f'{BOT_NAME} has glitched '
            + f'{num_glitch} images in channel {channel}') 

    # Get the first attachment (if there is one)
    elif len(message.attachments) > 0 and not message.author.bot:
        url = message.attachments[0].url
        type = image_type(url)

        if type != 'invalid':
            print(f'{message.author} uploaded {url}')
            
            # Save image to disk with a shorter filename
            local_url = save_image(url, type)
            
            # Glitch the image file
            glitch_url = do_glitch(local_url, type, channel)
            
            # Send glitch to channel
            await channel.send(file=discord.File(glitch_url))
            
            # Cleanup
            try:
                os.remove(local_url)
                print(f'Removed [{local_url}] from disk')
                os.remove(glitch_url)
                print(f'Removed [{glitch_url}] from disk')
            except:
                print(f'ERROR: Failed to remove files')
        
############################
# Glitchbot helper methods #
############################
def image_type(url):
    for extension in SUPPORTED:
        if url.endswith(extension):
            return extension
    return 'invalid'
    
def save_image(url, type):

    # Download file from web and generate local filepath
    request = requests.get(url, allow_redirects=True)
    local_url = f'tmp/{random_filename(5)}{type}'
    
    # Save to disk and return filepath
    if not os.path.exists('tmp'): # Make tmp directory if necessary
        os.makedirs('tmp')
        
    try:
        with open(local_url, 'wb') as local:
            local.write(request.content)
        print(f'Saved image [{local_url}]')
        return local_url
    except:
        print('ERROR: Failed to save image file to disk')
        
def random_filename(length):
    char_set = string.ascii_lowercase
    return ''.join(random.choice(char_set) for i in range(length))
    
def do_glitch(local_url, type, channel):

    glitcher = ImageGlitcher()
    
    if type != '.gif':
        glitch = glitcher.glitch_image(local_url,
                    random.uniform(6.0, 10.0),
                    scan_lines=bool(random.getrandbits(1)),
                    color_offset=bool(random.getrandbits(1)))

        # Get glitch filepath and save
        glitch_url = '_.'.join(local_url.split('.'))
        glitch.save(glitch_url)
        print(f'Saved static glitch [{glitch_url}]')
        
    else:
        glitch_file, duration_, _  = glitcher.glitch_gif(local_url,
                    random.uniform(6.0, 10.0),
                    glitch_change=random.uniform(-5.0, 5.0),
                    cycle=True,
                    scan_lines=bool(random.getrandbits(1)),
                    color_offset=bool(random.getrandbits(1)))

        # Get glitch filepath and save
        glitch_url = '_.'.join(local_url.split('.'))
        glitch_file[0].save(glitch_url,
                        format='GIF',
                        append_images=glitch_file[1:],
                        save_all=True,
                        duration=duration_,
                        loop=LOOP)
        print(f'Saved animated glitch [{glitch_url}]')

    # Log glitch for stats
    with open('stats.txt', 'a+') as stats:
        stats.write(f'{channel}')

    return glitch_url
    
#######################
# Bot startup script #
#######################

print('GlitchBot successfully loaded onto local machine')

# Get bot token
try:
    with open('token.txt', 'r') as tokenfile:
        token = tokenfile.read()
        print(f'Read token [{token}]')
except:
    sys.exit('FATAL ERROR: Failed to read token')

# Start bot
client.run(token)
