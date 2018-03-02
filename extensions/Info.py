import discord
from discord.ext import commands

import asyncio
import random
import requests
import copy, os, json
import datetime
import traceback
import time
    
class Info:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True, no_pm=True, invoke_without_command=True)
    async def userinfo(self, ctx, *, member : discord.Member = None):
        """Shows info about a member.
        This cannot be used in private messages. If you don't specify
        a member then the info returned will be yours.
        """
        channel = ctx.message.channel
        if member is None:
            member = ctx.message.author

        e = discord.Embed(color=0x00ff00)
        roles = [role.name.replace('@', '@\u200b') for role in member.roles]
        shared = sum(1 for m in self.bot.get_all_members() if m.id == member.id)
        voice = member.voice_channel
        if voice is not None:
            other_people = len(voice.voice_members) - 1
            voice_fmt = '{} with {} others' if other_people else '{} by themselves'
            voice = voice_fmt.format(voice.name, other_people)
        else:
            voice = 'Not connected.'

        e.set_author(name=str(member), icon_url=member.avatar_url or member.default_avatar_url)
        e.set_footer(text='Member since').timestamp = member.joined_at
        e.add_field(name='ID', value=member.id)
        e.add_field(name='Servers', value='%s shared' % shared)
        e.add_field(name='Voice', value=voice)
        e.add_field(name='Created', value=member.created_at.strftime("%d %b %Y %H:%M"))
        e.add_field(name='Roles', value=', '.join(roles))
        e.colour = member.colour

        if member.avatar:
            e.set_image(url=member.avatar_url)

        await self.bot.say(embed=e)
        
    @commands.command(pass_context=True, no_pm=True)
    async def serverinfo(self, ctx):
        """Shows server's informations"""
        server = ctx.message.server
        online = len([m.status for m in server.members
                      if m.status == discord.Status.online or
                      m.status == discord.Status.idle])
        total_users = len(server.members)
        text_channels = len([x for x in server.channels
                             if x.type == discord.ChannelType.text])
        voice_channels = len([x for x in server.channels
                             if x.type == discord.ChannelType.voice])
        passed = (ctx.message.timestamp - server.created_at).days
        created_at = ("Since {}. That's over {} days ago!"
                      "".format(server.created_at.strftime("%d %b %Y %H:%M"),
                                passed))

        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        embed = discord.Embed(
            description=created_at,
            color=0x00ff00)
        embed.set_image(url=server.icon_url)
        embed.set_thumbnail(url=server.icon_url)
        embed.add_field(name="Region", value=str(server.region), inline=False)
        embed.add_field(name="Users", value="{}/{}".format(online, total_users), inline=False)
        embed.add_field(name="Text Channels", value=text_channels, inline=True)
        embed.add_field(name="Voice Channels", value=voice_channels, inline=True)
        embed.add_field(name="Roles", value=len(server.roles), inline=False)
        embed.add_field(name="Owner", value=str(server.owner), inline=False)
        embed.set_footer(text="Server ID: " + server.id)

        if server.icon_url:
            embed.set_author(name=server.name, url=server.icon_url)
            embed.set_thumbnail(url=server.icon_url)
        else:
            embed.set_author(name=server.name)

        try:
            await self.bot.say(embed=embed)
        except discord.HTTPException:
            await self.bot.say("I need the `Embed links` permission "
                               "to send this")  
         
         
                               
def setup(bot):
    bot.add_cog(Info(bot))