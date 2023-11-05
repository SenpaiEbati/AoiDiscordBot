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
                embed = disnake.Embed(title='❌ ERROR IN CLEARED ❌', color=disnake.Color(0xff0000))
                val = "Failed to delete message. Please enter a number from 1 to 500"
                embed.add_field(name="",value=val, inline=False)
                await ctx.send(embed=embed)

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

            embed = disnake.Embed(title='🗑 Clear 🗑', color=disnake.Color(0x1E90FF))
            val = f"{len(deleted)} messages have been deleted successfully!"
            embed.add_field(name="",value=val, inline=False)
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
        else:
            embed = disnake.Embed(title='❌ NO RIGHTS ❌', color=disnake.Color(0xff0000))
            val = "You do not have permission to clear message."
            embed.add_field(name="",value=val, inline=False)
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)

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
                embed = disnake.Embed(title='❌ ERROR IN CLEARED ❌', color=disnake.Color(0xff0000))
                val = "Failed to delete message. Please enter a number from 1 to 500"
                embed.add_field(name="",value=val, inline=False)
                await ctx.send(embed=embed)

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

            embed = disnake.Embed(title='🗑 Clear 🗑', color=disnake.Color(0x1E90FF))
            val = f"{len(deleted)} messages have been deleted successfully!"
            embed.add_field(name="",value=val, inline=False)
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
        else:
            embed = disnake.Embed(title='❌ NO RIGHTS ❌', color=disnake.Color(0xff0000))
            val = "You do not have permission to clear message."
            embed.add_field(name="",value=val, inline=False)
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
            
def setup(bot: commands.Bot):
    bot.add_cog(Slash_Clear(bot))
    bot.add_cog(NoSlash_Clear(bot))