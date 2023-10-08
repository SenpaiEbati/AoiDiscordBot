import disnake
from disnake.ext import commands
from asyncio import sleep
from datetime import datetime, timedelta, timezone

class Slash_TimeClear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="timeclear",description="With this command you can clear message.")
    async def timeclear(self, ctx, amount: int, hours: int = 0, channel: disnake.TextChannel = None, user: disnake.User = None):
        def is_target_message(message):
            if channel and message.channel != channel:
                return False
            
            if user and message.author != user:
                return False
            
            if hours > 0:
                time_limit = datetime.utcnow() - timedelta(hours=hours)
                time_limit = time_limit.replace(tzinfo=timezone.utc)
                return message.created_at > time_limit
            
            return True

        if 0 < amount < 500:
            await ctx.send('Количество сообщений должно быть положительным числом от 1 до 500.')
            await sleep(5)
            await ctx.channel.purge(limit=1)
            return

        if channel and not user:
            deleted = await channel.purge(limit=amount, check=is_target_message)
        elif not channel and user:
            deleted = await ctx.channel.purge(limit=amount, check=is_target_message)
        elif channel and user:
            deleted = await channel.purge(limit=amount, check=is_target_message)
        else:
            deleted = await ctx.channel.purge(limit=amount,check=is_target_message)

        if len(deleted) == 0:
            await ctx.send('Нет сообщений, удовлетворяющие введенным данным ')
            await sleep(5)
            await ctx.channel.purge(limit=1)
        else:
            await ctx.send(f'Удалено {len(deleted)} сообщений.') 

        await sleep(5)
        if len(deleted) > 0:
            await ctx.channel.purge(limit=1)

class NoSlash_TimeClear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    

    @commands.command(name="timeclear",description="With this command you can timeout one or more members and give a reason.")
    async def timeclear(self, ctx, amount: int, hours: int = 0, channel: disnake.TextChannel = None, user: disnake.User = None):
        def is_target_message(message):
            if channel and message.channel != channel:
                return False
            
            if user and message.author != user:
                return False
            
            if hours > 0:
                time_limit = datetime.utcnow() - timedelta(hours=hours)
                time_limit = time_limit.replace(tzinfo=timezone.utc)
                return message.created_at > time_limit
            
            return True

        if 0 < amount < 500:
            await ctx.send('Количество сообщений должно быть положительным числом от 1 до 500.')
            await sleep(5)
            await ctx.channel.purge(limit=1)
            return

        if channel and not user:
            deleted = await channel.purge(limit=amount+1, check=is_target_message)
        elif not channel and user:
            deleted = await ctx.channel.purge(limit=amount+1, check=is_target_message)
        elif channel and user:
            deleted = await channel.purge(limit=amount+1, check=is_target_message)
        else:
            deleted = await ctx.channel.purge(limit=amount+1,check=is_target_message)

        if len(deleted) == 0:
            await ctx.send('Нет сообщений, удовлетворяющие введенным данным ')
        else:
            await ctx.send(f'Удалено {len(deleted)-1} сообщений.') 
        
        await sleep(5)
        await ctx.channel.purge(limit=1)

def setup(bot: commands.Bot):
    bot.add_cog(Slash_TimeClear(bot))
    bot.add_cog(NoSlash_TimeClear(bot))