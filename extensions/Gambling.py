import discord
from discord.ext import commands
import random

class Gambling:
    def __init__(self, bot):
        self.bot = bot

        
    @commands.command()
    async def gamble(self):
        """List of games"""
        embed = discord.Embed(title="Here is a list of games that you can play", color=0x00ff00)
        embed.add_field(name="Slotmachine 🎰", value="[p]slot", inline=True)
        
        await self.bot.say(embed=embed)
        
    @commands.command()
    async def slot(self):
        """Play slots."""
        c1 = random.choice([":sunflower:", ":chicken:", ":ok_hand:", ":gun:", ":video_game:"])
        c2 = random.choice([":sunflower:", ":chicken:", ":ok_hand:", ":gun:", ":video_game:"])
        c3 = random.choice([":sunflower:", ":chicken:", ":ok_hand:", ":gun:", ":video_game:"])
        em = discord.Embed(title=":slot_machine:Slot Machine:slot_machine:", description=c1 + " | " + c2 + " | " + c3, color=discord.Color.dark_purple())
        await self.bot.say(embed=em)
        if c2 == c1 == c3:
            result = "JACKPOT!"
            rc = discord.Color.green()
        elif c1 == c2:
            result = "Two consecutive symbols!"
            rc = discord.Color.green()
        elif c3 == c2:
            result = "Two consecutive symbols!"
            rc = discord.Color.green()
        elif c1 == c3:
            result = "Two consecutive symbols!"
            rc = discord.Color.green()
        else:
            result = "Nothing."
            rc = discord.Color.red()
        emb = discord.Embed(title="Results", description="**" + result + "**", color=rc)
        await self.bot.say(embed=emb)
        
def setup(bot):
    bot.add_cog(Gambling(bot))