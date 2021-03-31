import tempfile
import requests

class Image:
   def __init__(self, url):
      self.url  = url
      self.type = url.split('.')[-1]

   def __downloadRemoteImage(self):
      request = requests.get(self.url)

      return request

   @property
   def content(self):
      img = self.__downloadRemoteImage()
      return img.content

   @property
   def asFile(self):
      # filename = f'tmp.{self.type}'
      f = tempfile.NamedTemporaryFile(suffix=f'.{self.type}')
      f.write(self.content)
      return f
