import discord
from discord.ext import commands
import os
import traceback
try:
    import requests
except ImportError:
    print("Requests is not installed, installing it now...")
    from subprocess import check_output
    try:
        check_output("pip3 install requests", shell=True)
    except:
        pass
    try:
        import requests
    except:
        import sys
        sys.exit("Could not install requests, exiting...")
          

class Settings():
    def __init__(self):
        pass
        
    def owner():
        return "196233563954216960"
        
settings = Settings()

bot = commands.Bot("<")  

@bot.event
async def on_ready():
    print("Logged in as " + str(bot.user))
    await bot.change_presence(game=discord.Game(name="<help would help", type=1))

    
if __name__ == "__main__":
    for extension in [f for f in os.listdir("extensions") if os.path.isfile(os.path.join("extensions", f))]:
        extension = "extensions." + extension.split(".")[0];
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}'.format(extension))
            traceback.print_exc()
            

            


bot.run("NDE5MTkxMDMxOTU1NzE4MTU1.DXshlQ.-lkUjaHW4uKRVhSXR8_Q2DJK-m4")
