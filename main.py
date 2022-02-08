import discord
from discord.ext import commands
import os

# Intents Settings
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=";", intents=intents)

# Cogs Settings
cogs_list = []
for filename in os.listdir("Cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")
        cogs_list.append(filename[:-3])

# Bot Ready Settings
@bot.event
async def on_ready():
    print("=======================================")
    print(f"Logged in as {bot.user.name}")
    print("=======================================")


# Bot Load Settings
@bot.command(name="로드")
@commands.is_owner()
async def load_extension(ctx, extension=None):
    if extension is None:
        await ctx.send(":negative_squared_cross_mark: 로드할 파일명을 입력해주세요.\n**명령어 사용법:** `!로드 <extension>`")
    elif extension not in cogs_list:
        await ctx.send(":negative_squared_cross_mark: 존재하지 않는 파일명 입니다.\n**명령어 사용법:** `!로드 <extension>`")
    else:
        bot.load_extension(f"Cogs.{extension}")
        await ctx.send(f":white_check_mark: {extension}을(를) 성공적으로 로드했습니다!")

@bot.command(name="언로드")
@commands.is_owner()
async def unload_extension(ctx, extension=None):
    if extension is None:
        await ctx.send(":negative_squared_cross_mark: 언로드할 파일명을 입력해주세요.\n**명령어 사용법:** `!언로드 <extension>`")
    elif extension not in cogs_list:
        await ctx.send(":negative_squared_cross_mark: 존재하지 않는 파일명 입니다.\n**명령어 사용법:** `!언로드 <extension>`")
    else:
        bot.unload_extension(f"Cogs.{extension}")
        await ctx.send(f":white_check_mark: {extension}을(를) 성공적으로 언로드 했습니다!")

@bot.command(name="리로드")
@commands.is_owner()
async def reload_commands(ctx, extension=None):
    if extension is None:
        for filename in os.listdir("Cogs"):
            if filename.endswith(".py"):
                bot.unload_extension(f"Cogs.{filename[:-3]}")
                bot.load_extension(f"Cogs.{filename[:-3]}")
        await ctx.send(":white_check_mark: 모든 파일을 성공적으로 리로드 했습니다!")
    elif extension not in cogs_list:
        await ctx.send(":negative_squared_cross_mark: 존재하지 않는 파일명 입니다.\n**명령어 사용법:** `!리로드` OR '!리로드 <extension>")
    else:
        bot.unload_extension(f"Cogs.{extension}")
        bot.load_extension(f"Cogs.{extension}")
        await ctx.send(f":white_check_mark: {extension}을(를) 성공적으로 리로드 했습니다!")


bot.run("token") # bot token here