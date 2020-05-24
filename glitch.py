"""
glitch.py contains the routine to generate databent images and GIFs
 using the glitch_this module
"""
import random

from glitch_this import ImageGlitcher

LOOP = 0 # Loop GIFs forver

def image(imageFile, imageType):

    # Setup ImageGlitcher parameters
    glitcher      = ImageGlitcher()
    amount        = round(random.uniform(6.0,10.0), 2)
    scanlines     = bool(random.getrandbits(1))
    colorOffset   = bool(random.getrandbits(1))

    glitchFile = '_.'.join(imageFile.split('.'))

    if imageType == '.gif':
        # GIF-specific parameters
        cycle = bool(random.getrandbits(1))
        change = round(random.uniform(1.0, 3.0), 2)

        # Account for potential glitch_amount overflow
        while (amount + change) >= 10.0:
            change -= 0.1
        while(amount - change) <= 0.1:
            change += 0.1

        glitch, duration_, _  = glitcher.glitch_gif(src_gif=imageFile,
                                                    glitch_amount=amount,
                                                    glitch_change=change,
                                                    cycle=False,
                                                    color_offset=colorOffset,
                                                    scan_lines=scanlines)

        # Save file
        try:
            glitch[0].save(glitchFile,
                        format='GIF',
                        append_images=glitch[1:],
                        save_all=True,
                        duration=duration_,
                        loop=LOOP)
        except:
            print(f'ERROR: Failed to save GIF glitch [{glitchFile}]')
            return

    else:
        glitch = glitcher.glitch_image(src_img=imageFile,
                                        glitch_amount=amount,
                                        color_offset=colorOffset,
                                        scan_lines=scanlines)

        # Save file
        try:
            glitch.save(glitchFile)
        except:
            print(f'ERROR: Failed to save static glitch [{glitchFile}]')
            return

    return glitchFile
