import discord
from discord.ext import commands
from .utils import checks
import asyncio
import aiohttp
import time
import sys
import subprocess
import os
import json
import traceback

class Owner:
    def __init__(self, bot):
        self.bot = bot   

    @commands.command(hidden=True)
    @checks.serverowner_or_permissions(administrator=True)
    async def rename(ctx, *, name:str, arg):
        """Renames the bot"""
        await self.bot.user.edit(username=name)
        await ctx.send("My name has been set to {}".format(arg))

    @commands.command(hidden=True)
    @checks.serverowner_or_permissions(administrator=True)
    async def setavatar(ctx, *, url:str=None):
        """Changes the bot's avatar"""
        if ctx.message.attachments:
            url = ctx.message.attachments[0].url
        elif url is None:
            await ctx.send("Please specify an avatar url if you did not attach a file")
            return
        try:
            with aiohttp.Timeout(10):
                async with aiosession.get(url.strip("<>")) as image:
                    await bot.user.edit(avatar=await image.read())
        except Exception as e:
            await ctx.send("Unable to change avatar: {}".format(e))
            return
        await ctx.send(":eyes:")
        
def setup(bot):
    bot.add_cog(Owner(bot))