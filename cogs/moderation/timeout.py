from asyncio import sleep
import datetime
import disnake
from disnake.ext import commands
from cogs._class.LanguageClass import LanguageClass

class Slash_Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="timeout",
                            description="Encourages user to reflect on their behavior/Побуждает пользователя задуматься о своем поведении",
                            default_member_permissions=disnake.Permissions(moderate_members=True))
    async def timeout(self, ctx, member: disnake.Member, *,days=0,hours=0,minutes=0,seconds=0,reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        if ctx.author.guild_permissions.moderate_members:
            if max(ctx.author.roles) > max(member.roles):
                if isinstance(days,int) and isinstance(hours,int) and isinstance(minutes,int) and isinstance(seconds,int):
                    if days == hours == minutes == seconds == 0:
                        hours = 6
                        time = hours * 60 * 60 
                    else:
                        time = int(seconds) + int(minutes) * 60 + int(hours) * 60 * 60 + int(days) * 24 * 60 * 60
                
                    embed = disnake.Embed(title=strings["timeout_title"], color=disnake.Color(0xff0000),timestamp=datetime.datetime.now())
                    embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
                    embed.add_field(name=strings["how_much"], value=f"{days}d {hours}h {minutes}m {seconds}s", inline=False)
                    embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
                    embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
                    await ctx.send(embed=embed)
                    
                    dm_embed = disnake.Embed(title=strings["timeout_title"], color=disnake.Color(0xff0000),timestamp=datetime.datetime.now())
                    dm_embed.add_field(name=strings["ban_server"], value=ctx.guild.name, inline=False)
                    dm_embed.add_field(name=strings["how_much"], value=f"{days}d {hours}h {minutes}m {seconds}s", inline=False)
                    dm_embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
                    dm_embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
                    await member.send(embed=dm_embed)
                    
                    await member.edit(timeout=time)
                else:
                    embed = disnake.Embed(title=strings["error_timeout"], 
                                          description=strings["error_timeout_discrip"],
                                          color=disnake.Color(0xff0000),
                                          timestamp=datetime.datetime.now())
                    embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
                    await ctx.send(embed=embed)

                    await sleep(5)
                    await ctx.channel.purge(limit=1)
            else:
                embed = disnake.Embed(title=strings["no_rights"], 
                                      description=strings["timeout_rights_1"],
                                      color=disnake.Color(0xff0000),
                                      timestamp=datetime.datetime.now())
                embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
                await ctx.send(embed=embed)

                await sleep(5)
                await ctx.channel.purge(limit=1)
        else:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["timeout_rights_1"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)

class NoSlash_Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    

    @commands.command(name="timeout",
                            default_member_permissions=disnake.Permissions(moderate_members=True))
    async def timeout(self, ctx, member: disnake.Member, *,days=0,hours=0,minutes=0,seconds=0,reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        
        if ctx.author.guild_permissions.moderate_members:
            if max(ctx.author.roles) > max(member.roles):
                if isinstance(days,int) and isinstance(hours,int) and isinstance(minutes,int) and isinstance(seconds,int):
                    if days == hours == minutes == seconds == 0:
                        hours = 6
                        time = hours * 60 * 60 
                    else:
                        time = int(seconds) + int(minutes) * 60 + int(hours) * 60 * 60 + int(days) * 24 * 60 * 60
                
                    embed = disnake.Embed(title=strings["timeout_title"], color=disnake.Color(0xff0000),timestamp=datetime.datetime.now())
                    embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
                    embed.add_field(name=strings["how_much"], value=f"{days}d {hours}h {minutes}m {seconds}s", inline=False)
                    embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
                    embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
                    await ctx.reply(embed=embed)
                    
                    dm_embed = disnake.Embed(title=strings["timeout_title"], color=disnake.Color(0xff0000),timestamp=datetime.datetime.now())
                    dm_embed.add_field(name=strings["ban_server"], value=ctx.guild.name, inline=False)
                    dm_embed.add_field(name=strings["how_much"], value=f"{days}d {hours}h {minutes}m {seconds}s", inline=False)
                    dm_embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
                    dm_embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
                    await member.send(embed=dm_embed)
                    
                    await member.edit(timeout=time)
                else:
                    embed = disnake.Embed(title=strings["error_timeout"], 
                                          description=strings["error_timeout_discrip"],
                                          color=disnake.Color(0xff0000),
                                          timestamp=datetime.datetime.now())
                    embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
                    await ctx.reply(embed=embed)

                    await sleep(5)
                    await ctx.channel.purge(limit=1)
            else:
                embed = disnake.Embed(title=strings["no_rights"], 
                                      description=strings["timeout_rights_1"],
                                      color=disnake.Color(0xff0000),
                                      timestamp=datetime.datetime.now())
                embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
                await ctx.reply(embed=embed)

                await sleep(5)
                await ctx.channel.purge(limit=1)
        else:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["timeout_rights_1"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
            await ctx.reply(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)

def setup(bot: commands.Bot):
    bot.add_cog(Slash_Timeout(bot))
    bot.add_cog(NoSlash_Timeout(bot))