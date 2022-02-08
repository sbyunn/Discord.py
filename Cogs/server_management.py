import asyncio
import discord
from discord.ext import commands

class Server_Manager(commands.Cog, name="관리"):

    
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="킥")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention}님을(를) 이 서버에서 킥했습니다.")

    @commands.command(name="밴")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention}님의 계정과 IP를 이 서버에서 밴했습니다.")


    @commands.command(name="청소")
    @commands.has_permissions(manage_messages=True)
    async def delete_message(self, ctx, messages_num: int=None):
        deleted_message = await ctx.channel.purge(limit=messages_num + 1)
        await ctx.send(f"`{len(deleted_message) - 1}`개의 메시지를 삭제했어요!", delete_after=2)




def setup(bot):
    bot.add_cog(Server_Manager(bot))