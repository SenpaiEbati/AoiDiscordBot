from asyncio import sleep
import datetime
import disnake
from disnake.ext import commands
from cogs._class.LanguageClass import LanguageClass

class Slash_Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command()
    async def clear(self, ctx, amount: int, channel: disnake.TextChannel = None, user: disnake.User = None):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))
        if ctx.author.guild_permissions.manage_messages:
            def is_target_message(message):
                if channel and message.channel != channel:
                    return False
                if user and message.author != user:
                    return False
                return True

            if amount <= 0 or amount > 500:
                embed = disnake.Embed(title=strings["clear_error"], 
                                      description=strings["clear_errordescrip"],
                                      color=disnake.Color(0xff0000),
                                      timestamp=datetime.datetime.now())
                embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
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

            embed = disnake.Embed(title=strings["clear_title"], 
                                  description=f"{len(deleted)}" + strings["clear_discrip"],
                                  color=disnake.Color(0x1E90FF),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
        else:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["clear_rights"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)

class NoSlash_Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def clear(self, ctx, amount: int, channel: disnake.TextChannel = None, user: disnake.User = None):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))
        if ctx.author.guild_permissions.manage_messages:
            def is_target_message(message):
                if channel and message.channel != channel:
                    return False
                if user and message.author != user:
                    return False
                return True

            if amount <= 0 or amount > 500:
                embed = disnake.Embed(title=strings["clear_error"], 
                                      description=strings["clear_errordescrip"],
                                      color=disnake.Color(0xff0000),
                                      timestamp=datetime.datetime.now())
                embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
                await ctx.reply(embed=embed)

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

            embed = disnake.Embed(title=strings["clear_title"], 
                                  description=f"{len(deleted)}" + strings["clear_discrip"],
                                  color=disnake.Color(0x1E90FF),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.reply(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
        else:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["clear_rights"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.reply(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
            
def setup(bot: commands.Bot):
    bot.add_cog(Slash_Clear(bot))
    bot.add_cog(NoSlash_Clear(bot))