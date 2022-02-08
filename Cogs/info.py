import asyncio
import discord
from discord.ext import commands
import time

class info(commands.Cog, name="정보"):
    
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="핑")
    async def ping(self, ctx):
        await ctx.send('Pong!')

    
    @commands.command(name="프로필", help="특정 사용자의 프로필 이미지와 ID를 확인합니다.")
    async def profile(self, ctx, member: discord.Member=None):
        if member is None:
            embed = discord.Embed(title="프로필")
            embed.add_field(name="이름", value=ctx.author.name)
            embed.add_field(name="아이디", value=ctx.author.id)
            embed.add_field(name="서버 닉네임", value=ctx.author.display_name)
            embed.add_field(name="서버 가입일", value=str(ctx.author.joined_at)[:19])
            embed.add_field(name="디스코드 가입일", value=str(ctx.author.created_at)[:19])
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        
        if member == ctx.author:
            embed = discord.Embed(title="프로필")
            embed.add_field(name="이름", value=ctx.author.name)
            embed.add_field(name="아이디", value=ctx.author.id)
            embed.add_field(name="서버 닉네임", value=ctx.author.display_name)
            embed.add_field(name="서버 가입일", value=str(ctx.author.joined_at)[19])
            embed.add_field(name="디스코드 가입일", value=str(ctx.author.created_at)[:19])
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        
        else:
            embed = discord.Embed(title="프로필")
            embed.add_field(name="이름", value=member.name)
            embed.add_field(name="서버 닉네임", value=member.display_name)
            embed.add_field(name="아이디", value=member.id)
            embed.add_field(name="서버 가입일", value=str(member.joined_at)[:19])
            embed.add_field(name="디스코드 가입일", value=str(member.created_at)[:19])
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text=f"{ctx.author}님이 요청함", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)


    @commands.command(name = "타이머")
    async def timer(self, ctx, sleep_time: int):
        await asyncio.sleep(sleep_time)
        await ctx.author.send(f"{ctx.author.mention}님 {sleep_time}초가 다되었어요")

    @commands.command(name="닉네임")
    async def change_nickname(self, ctx, *, new_nickname: str=None):
        if new_nickname is None:
            await ctx.send(":negative_squared_cross_mark: 변경할 닉네임을 입력해주세요...")
        
        elif new_nickname == ctx.author.display_name:
            await ctx.send(":negative_squared_cross_mark: 새롭게 변경할 닉네임을 입력해주세요...")
        
        else:
            await ctx.author.edit(nick=new_nickname)
            await ctx.send(f":arrows_counterclockwise: {ctx.author.mention}님 닉네임 변경에 성공했어요! 새롭게 변경된 닉네임은 ``{new_nickname}``입니다!")

    @change_nickname.error
    async def nink_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("봇이 닉네임 변경하기 권한이 없거나 한글봇보다 높은 권한을 가진 사람은 한글봇이 닉네임을 변경하지 못해요...")


def setup(bot):
    bot.add_cog(info(bot))