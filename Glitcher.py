import random
import tempfile
from Image import Image
from glitch_this import ImageGlitcher

class Glitcher:
   def __init__(self, url):
      self.image = Image(url)

   @property
   def __glitcherWithParams(self):
      self.imGltch = ImageGlitcher()
      amount = round(random.uniform(6.0,10.0), 2)
      scanlines = bool(random.getrandbits(1))
      colorOffset = bool(random.getrandbits(1))

      return amount, scanlines, colorOffset

   def __glitchGIF(self, src, dest):
      amount, scanlines, colorOffset = self.__glitcherWithParams
      # cycle = bool(random.getrandbits(1))
      change = round(random.uniform(1.0, 3.0), 2)

      # Account for potential glitch_amount overflow
      while (amount + change) >= 10.0:
         change -= 0.1
      while(amount - change) <= 0.1:
         change += 0.1

      glitch, duration_, _  = self.imGltch.glitch_gif(src_gif=src.name,
                                                    glitch_amount=amount,
                                                    glitch_change=change,
                                                    cycle=False,
                                                    color_offset=colorOffset,
                                                    scan_lines=scanlines)

      try:
         glitch[0].save(dest.name,
                        format='GIF',
                        append_images=glitch[1:],
                        save_all=True,
                        duration=duration_,
                        loop=0)
      except:
         print(f'ERROR: Failed to save GIF glitch [{dest.name}]')

   def __glitchStatic(self, src, dest):
      amount, scanlines, colorOffset = self.__glitcherWithParams

      glitch = self.imGltch.glitch_image(src_img=src.name,
                                        glitch_amount=amount,
                                        color_offset=colorOffset,
                                        scan_lines=scanlines)

      # Save file
      try:
         glitch.save(dest.name)
      except:
         print(f'ERROR: Failed to save static glitch [{dest.name}]')

   def glitch(self):
      imgFile = self.image.asFile
      suffix = self.image.type
      glitchFile = tempfile.NamedTemporaryFile(suffix=f'.{suffix}')

      if suffix == 'gif':
         self.__glitchGIF(imgFile, glitchFile)
      else:
         self.__glitchStatic(imgFile, glitchFile)

      imgFile.close()
      return glitchFile
