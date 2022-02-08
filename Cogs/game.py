import asyncio
import discord
from discord.ext import commands
import os
import random




class Game(commands.Cog, name="게임"):

    def __init__(self, bot):
        self.bot = bot



    @commands.command(name="주사위")
    async def dice(self, ctx, start_num:int=None, last_num:int=None):
        if start_num is None:
            dice_num = random.randint(1, 6)
            await ctx.reply(f"나온 숫자는 `{dice_num}` 입니다.")
        else:
            random_num = random.randint(start_num, last_num)
            await ctx.reply(f"나온 숫자는 `{random_num}` 입니다.")

def setup(bot):
    bot.add_cog(Game(bot))