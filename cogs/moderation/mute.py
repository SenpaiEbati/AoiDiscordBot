from asyncio import sleep
import datetime
import disnake
from disnake.ext import commands
from cogs._class.LanguageClass import LanguageClass

class Slash_Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def mute(self, ctx, member: disnake.Member, *, reason="-"):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))
        if ctx.author.guild_permissions.mute_members:
            embed = disnake.Embed(title=strings["mute_title"], 
                                  color=disnake.Color(0xFFFF33),
                                  timestamp=datetime.datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)
            
            await member.edit(mute=True)
        else:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["no_rights_mute"], 
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.send(embed=embed)
            
            await sleep(5)
            await ctx.channel.purge(limit=1)

class NoSlash_Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    

    @commands.command()
    async def mute(self, ctx, member: disnake.Member, *, reason="-"):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))
        if ctx.author.guild_permissions.mute_members:
            embed = disnake.Embed(title=strings["mute_title"], 
                                  color=disnake.Color(0xFFFF33),
                                  timestamp=datetime.datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.reply(embed=embed)
            
            await member.edit(mute=True)
        else:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["no_rights_mute"], 
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.reply(embed=embed)
            
            await sleep(5)
            await ctx.channel.purge(limit=1)
        
def setup(bot: commands.Bot):
    bot.add_cog(Slash_Mute(bot))
    bot.add_cog(NoSlash_Mute(bot))