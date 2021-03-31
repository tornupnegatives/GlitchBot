import os
import discord

from Glitcher import Glitcher

class Bot(discord.Client):
    def __init__(self, *args, **kwargs):
      print('Initializing bot...')
      super().__init__(*args, **kwargs)
      
      self.shouldUpdate = 0

    async def on_ready(self):
      print('Successfully loaded bot. Currently online.')

    async def on_message(self, message):
      # Ignore messages from self
      if message.author.id == self.user.id:
        return
        
      elif message.content == '!gb':
        if len(message.attachments) > 0:
            glitcher = Glitcher(message.attachments[0].url)
            glitch = glitcher.glitch()
            
            await message.channel.send(file=discord.File(glitch.name))
            
      elif message.content.startswith('!gb update'):
        await message.channel.send('Requesting update...')
        self.shouldUpdate = 1
        await self.close()

      elif message.content.startswith('!gb stop'):
        await self.close()

      elif message.content.startswith('!gb help'):
        msg = 'GlitchBot v2.0 Commands\n' + \
              '========================\n' + \
              '!gb: glitch attached image\n' + \
              '!mm update: request update from server\n' + \
              '!mm stop: shut down bot'

        await message.channel.send(msg)
