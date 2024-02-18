from asyncio import sleep
import datetime
import disnake
from disnake.ext import commands
from cogs._class.LanguageClass import LanguageClass

class Slash_Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def warn(self, ctx, member: disnake.Member, *, reason="-"):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))
        if ctx.author.guild_permissions.moderate_members:
            embed = disnake.Embed(title=strings["warn_title"], color=disnake.Color(0xFFFF33),timestamp=datetime.datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.send(member.mention,embed=embed)

            dm_embed = disnake.Embed(title=strings["warn_title"], color=disnake.Color(0xFFFF33),timestamp=datetime.datetime.now())
            dm_embed.add_field(name=strings["ban_server"], value=ctx.guild.name, inline=False)
            dm_embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            dm_embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await member.send(embed=dm_embed)
        else:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["warn_rights"], 
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)

class NoSlash_Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    

    @commands.command()
    async def warn(self, ctx, member: disnake.Member, *, reason="-"):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))
        if ctx.author.guild_permissions.moderate_members:
            embed = disnake.Embed(title=strings["warn_title"], color=disnake.Color(0xFFFF33),timestamp=datetime.datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.send(member.mention,embed=embed)

            dm_embed = disnake.Embed(title=strings["warn_title"], color=disnake.Color(0xFFFF33),timestamp=datetime.datetime.now())
            dm_embed.add_field(name=strings["ban_server"], value=ctx.guild.name, inline=False)
            dm_embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            dm_embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await member.send(embed=dm_embed)
        else:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["warn_rights"], 
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
            await ctx.reply(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
        
def setup(bot: commands.Bot):
    bot.add_cog(Slash_Warn(bot))
    bot.add_cog(NoSlash_Warn(bot))