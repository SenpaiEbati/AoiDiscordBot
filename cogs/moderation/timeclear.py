import disnake
from disnake.ext import commands
from asyncio import sleep
from datetime import datetime, timedelta, timezone
from cogs._class.LanguageClass import LanguageClass

class Slash_TimeClear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="timecleaning",
                            description="Same as Clear, but with a time stamp/Тоже самое что и \"Clear\" только с указанием времени",
                            default_member_permissions=disnake.Permissions(manage_messages=True))
    async def timecleaning(self, ctx, amount: int, hours: int = 0, channel: disnake.TextChannel = None, user: disnake.User = None):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        if ctx.author.guild_permissions.manage_messages:
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

            if amount <= 0 or amount > 500:
                embed = disnake.Embed(title=strings["clear_error"], 
                                      description=strings["clear_errordescrip"],
                                      color=disnake.Color(0xff0000),
                                      timestamp=datetime.now())
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
                deleted = await ctx.channel.purge(limit=amount,check=is_target_message)

            if len(deleted) == 0:
                embed = disnake.Embed(title=strings["clear_error"], 
                                      description=strings["clear_errordescrip"],
                                      color=disnake.Color(0xff0000),
                                      timestamp=datetime.now())
                embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
                await ctx.send(embed=embed)
            else:
                embed = disnake.Embed(title=strings["clear_title"],
                                      description=f"{len(deleted)}" + strings["clear_discrip"],
                                      color=disnake.Color(0x1E90FF),
                                      timestamp=datetime.now())
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
                                  timestamp=datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)

class NoSlash_TimeClear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    

    @commands.command(name="timecleaning",
                        description="Same as Clear, but with a time stamp/Тоже самое что и \"Clear\" только с указанием времени",
                        default_member_permissions=disnake.Permissions(manage_messages=True))
    async def timecleaning(self, ctx, amount: int, hours: int = 0, channel: disnake.TextChannel = None, user: disnake.User = None):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        
        if ctx.author.guild_permissions.manage_messages:
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

            if amount <= 0 or amount > 500:
                embed = disnake.Embed(title=strings["clear_error"], 
                                      description=strings["clear_errordescrip"],
                                      color=disnake.Color(0xff0000),
                                      timestamp=datetime.now())
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
                deleted = await ctx.channel.purge(limit=amount,check=is_target_message)

            if len(deleted) == 0:
                embed = disnake.Embed(title=strings["clear_error"], 
                                      description=strings["clear_errordescrip"],
                                      color=disnake.Color(0xff0000),
                                      timestamp=datetime.now())
                embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
                await ctx.reply(embed=embed)
            else:
                embed = disnake.Embed(title=strings["clear_title"],
                                      description=f"{len(deleted)}" + strings["clear_discrip"],
                                      color=disnake.Color(0x1E90FF),
                                      timestamp=datetime.now())
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
                                  timestamp=datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.reply(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
            
def setup(bot: commands.Bot):
    bot.add_cog(Slash_TimeClear(bot))
    bot.add_cog(NoSlash_TimeClear(bot))