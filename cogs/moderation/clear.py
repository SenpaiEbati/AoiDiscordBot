from asyncio import sleep
import disnake
from disnake.ext import commands

class Slash_Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(description="With this command you can clear message.")
    async def clear(self, ctx, amount: int, channel: disnake.TextChannel = None, user: disnake.User = None):
        if ctx.author.guild_permissions.manage_messages:
            def is_target_message(message):
                if channel and message.channel != channel:
                    return False
                if user and message.author != user:
                    return False
                return True

            if amount <= 0 or amount > 500:
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
                deleted = await ctx.channel.purge(limit=amount)

            await ctx.send(f'Удалено {len(deleted)} сообщений.')
            await sleep(5)
            await ctx.channel.purge(limit=1)
        else:
            await ctx.send("You do not have permission to clear message.")
class NoSlash_Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(description="With this command you can clear message.")
    async def clear(self, ctx, amount: int, channel: disnake.TextChannel = None, user: disnake.User = None):
        if ctx.author.guild_permissions.manage_messages:
            def is_target_message(message):
                if channel and message.channel != channel:
                    return False
                if user and message.author != user:
                    return False
                return True
            
            if amount <= 0 or amount > 500:
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
                deleted = await ctx.channel.purge(limit=amount+1)

            await ctx.send(f'Удалено {len(deleted)-1} сообщений.')
            await sleep(5)
            await ctx.channel.purge(limit=1)
        else:
            await ctx.send("You do not have permission to clear message.")
            
def setup(bot: commands.Bot):
    bot.add_cog(Slash_Clear(bot))
    bot.add_cog(NoSlash_Clear(bot))