import os
import discord
import glob
import re
import os
import aiohttp
import asyncio
import random
import requests
import json
import datetime

from discord.ext import commands
from .utils import checks
from __main__ import settings
from .utils.dataIO import dataIO
from .utils.chat_formatting import pagify, box
from time import perf_counter
from random import choice
from subprocess import check_output


try:
    import ffmpy
    ffmpyinstalled = True
except:
    print("You don't have ffmpy installed, installing it now...")
    try:
        check_output("pip3 install ffmpy", shell=True)
        print("FFMpy installed succesfully!")
        import ffmpy
        ffmpyinstalled = True
    except:
        print("FFMpy didn't install succesfully.")
        ffmpyinstalled = False
try:
    from pyshorteners import Shortener
    pyshortenersinstalled = True
except:
    print("You don't have pyshorteners installed, installing it now...")
    try:
        check_output("pip3 install pyshorteners", shell=True)
        print("Pyshorteners installed succesfully!")
        import pyshorteners
        pyshortenersinstalled = True
    except:
        print("Pyshorteners didn't install succesfully.")
        pyshortenersinstalled = False

class Useful:
    """Useful stuff!"""

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json("data/useful/settings.json")
            

    @commands.command(pass_context=True, name="ping", aliases=['pong'])
    async def _ping(self, ctx):
        """Pong!"""
        t1 = perf_counter()
        await self.bot.send_typing(ctx.message.channel)
        t2 = perf_counter()
        time = str((t2 - t1) * 1000) # converting to milliseconds.
        t1 = time.split(".")[0]      # everything before the dot is needed.
        t2 = time.split(".")[1][:2]  # only 2 decimals behind the dot.
        await self.bot.say("Pong! Response time: **{} ms**.".format(t1 + "." + t2))
           
            
      
    @commands.command(pass_context=True, aliases=['invite'])
    async def inviteme(self, ctx):
        """Sends you the bot invite link"""
        embed = discord.Embed(color=0x00ff00, description="Thanks for inviting me! [here](https://discordapp.com/api/oauth2/authorize?client_id=391229316400283650&permissions=0&scope=bot) is my invite link!")
        await self.bot.say(embed=embed)
        
      
def check_folders():
    if not os.path.exists("data/useful"):
        print("Creating data/useful folder...")
        os.makedirs("data/useful")
        
def check_files():
    if not os.path.exists("data/useful/settings.json"):
        print("Creating data/useful/settings.json file...")
        dataIO.save_json("data/useful/settings.json", {'auth_key': 'key_here', 'client_id': 'client_id_here', 'geocodingkey': 'key_here', 'timezonekey': 'key_here'})
        
class ModuleNotFound(Exception):
    pass
        
def setup(bot):
    if not ffmpyinstalled:
        raise ModuleNotFound("FFmpy is not installed, install it with pip3 install ffmpy.")
    if not pyshortenersinstalled:
        raise ModuleNotFound("Pyshorteners is not installed, install it with pip3 install pyshorteners.")
    check_folders()
    check_files()
    bot.remove_command("ping") # to be replaced with a new one that does count response time instead of only a 'pong' response.
    bot.remove_command("servercount") # so there are no conflicts with the admin cog by Tekulvw
    bot.add_cog(Useful(bot))