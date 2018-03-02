import codecs

import aiohttp

import discord
from discord.ext import commands

import asyncio
import random
import requests
import copy, os, json
import datetime
import traceback
import time

from .utils import checks

try:
    from bs4 import BeautifulSoup as bs
except ImportError:
    print("BeautifulSoup is not installed, installing it now...")
    from subprocess import check_output
    try:
        check_output("pip3 install beautifulsoup4", shell=True)
    except:
        pass
    from bs4 import BeautifulSoup as bs

class General:
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop, headers={"User-Agent": "AppuSelfBot"})
        self.stopwatches = {}
       
        
    
    @commands.command(pass_context=True)
    async def top100(self, ctx):
        """Top 100 songs and artists"""
        soup = bs(requests.get("https://www.billboard.com/charts/hot-100").text, "html.parser")
        msg = "**Top 100 songs**\n\n"
        for i in range(100):
            n = i + 1
            article = soup.find(class_="chart-row--" + str(n))
            msg += str(n) + ". **" + article.find(class_="chart-row__artist").string.replace("*", "\\*").strip() + "** " + article.find(class_="chart-row__song").string.replace("*", "\\*").strip() + "\n"
            if len(msg) > 1900:
                await self.bot.whisper(msg)
                msg = ""
              
                               
    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, *choices : str):
        """Chooses between multiple choices."""
        await self.bot.say(random.choice(choices))
        
    @commands.command(pass_context=True)
    async def rps(self):
        """Rock, paper, scissors"""
        rng = random.randint(0, 300)
        if rng < 100:
            await self.bot.say(":moyai: **ROCK!** :moyai:")
        elif rng > 100:
            await self.bot.say(":pencil: **PAPER!** :pencil:")
        elif rng > 200:
            await self.bot.say(":scissors: **SCISSORS!** :scissors:")
        else:
            await self.bot.add_reaction(
                ":regional_indicator_e: :regional_indicator_r: :regional_indicator_r: :regional_indicator_o: :regional_indicator_r:")


    @commands.command(pass_context=True)
    async def flip(self):
        """Flips a coin"""
        rng = random.randint(0, 100)
        if rng < 50:
            await self.bot.say("You flipped *HEADS*")
        else:
            await self.bot.say("You flipped *TAILS*")
            
    @commands.command()
    async def lmgtfy(self, *, search_terms : str):
        """Creates a lmgtfy link"""
        search_terms = escape_mass_mentions(search_terms.replace(" ", "+"))
        await self.bot.say("https://lmgtfy.com/?q={}".format(search_terms))
        
    @commands.command(aliases=["sw"], pass_context=True)
    async def stopwatch(self, ctx):
        """Starts/stops stopwatch"""
        author = ctx.message.author
        if not author.id in self.stopwatches:
            self.stopwatches[author.id] = int(time.perf_counter())
            await self.bot.say(author.mention + " Stopwatch started!")
        else:
            tmp = abs(self.stopwatches[author.id] - int(time.perf_counter()))
            tmp = str(datetime.timedelta(seconds=tmp))
            await self.bot.say(author.mention + " Stopwatch stopped! Time: **" + tmp + "**")
            self.stopwatches.pop(author.id, None)
        

        
        
        

       
        

    
        
def setup(bot):
    bot.add_cog(General(bot))

