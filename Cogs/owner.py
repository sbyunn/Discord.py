import asyncio
import discord
from discord.ext import commands



class owner_only(commands.Cog, name="소유자_전용"):
    
    def __init__(self, bot):
        self.bot = bot
    
    # Bot Status Settingss
    @commands.command(name="봇")
    @commands.is_owner()
    async def status_online(self, ctx, cmd, cmd2):
        if cmd is None:
            await ctx.send(":negative_squared_cross_mark: 실행할 명령을 입력해 주세요.")
        elif cmd == "상태":
            if cmd2 is None:
                await ctx.send("변경할 상태를 입력해주세요.")
            elif cmd2 == "온라인":
                await ctx.bot.change_presence(status=discord.Status.online)
                await ctx.send("봇의 상태를 성공적으로 변경했습니다.")
            elif cmd2 == "자리비움":
                await ctx.bot.change_presence(status=discord.Status.idle)
                await ctx.send(":white_check_mark: 봇의 상태를 자리비움으로 변경했습니다!")
            elif cmd2 == "방해금지":
                await ctx.bot.change_presence(status=discord.Status.dnd)
                await ctx.send(":white_check_mark: 봇의 상태를 방해금지으로 변경했습니다!")
            elif cmd2 == "오프라인":
                await ctx.bot.change_presence(status=discord.Status.offline)
                await ctx.send(":white_check_mark: 봇의 상태를 오프라인으로 변경했습니다!")
            else:
                await ctx.send(":negative_squared_cross_mark: 잘못된 상태입니다...\n상태종류: 온라인, 자리비움, 방해금지, 오프라인")
        else:
            pass




def setup(bot):
    bot.add_cog(owner_only(bot))