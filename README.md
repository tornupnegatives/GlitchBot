# GlitchBot
GlitchBot is a Discord bot capable of databending and datamoshing static images and animated gifs, right in your Discord server!

# Dependencies
GlitchBot is powered by [discordpy](https://discordpy.readthedocs.io/en/latest/). It uses [glitch_this](https://github.com/TotallyNotChase/glitch-this) to perform databending operations. 

On Linux systems, libopenjp and libtiff are also necessary for image manipulation operations through Pillow
```bash
$ sudo apt-get install libopenjp2-7 libtiff5
```

# Usage
GlitchBot expects a file named `token.txt` containing a GitHub Bot API token in the same directory as the script. No additional setup is required.

## Commands
| Command Name | Description |
|--------------|-------------|
| !gb | Databend attached image |
| !gb update | Pull latest version and restart bot |
| !gb stop | Power down bot |
