from asyncio import sleep
import datetime
import disnake
from disnake.ext import commands
from cogs._class.LanguageClass import LanguageClass

class Slash_Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ban",
                            description="Command to ban a user permanently/Команда изгнания участника с сервера навечно без права вернуться",
                            default_member_permissions=disnake.Permissions(ban_members=True))
    async def ban(self, ctx, member: disnake.Member, *, reason="-"):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))

        if ctx.author == member:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["ban_1"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                text=ctx.author.display_name + strings["mod_serv"]
            )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
        elif ctx.author.guild_permissions.ban_members:
            embed = disnake.Embed(title=strings["ban_title"], color=disnake.Color(0xff0000),timestamp=datetime.datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            
            await ctx.send(embed=embed)
            
            dm_embed = disnake.Embed(title=strings["ban_title"], color=disnake.Color(0xff0000),timestamp=datetime.datetime.now())
            dm_embed.add_field(name=strings["ban_server"], value=ctx.guild.name, inline=False)
            dm_embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            dm_embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            
            await member.send(embed=dm_embed)

            await member.ban() 
        else:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["ban_2"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                text=ctx.author.display_name + strings["mod_serv"]
            )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)

class NoSlash_Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    

    @commands.command(name="ban",
                      default_member_permissions=disnake.Permissions(ban_members=True))
    async def ban(self, ctx, member: disnake.Member, *, reason="-"):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))

        if ctx.author == member:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["ban_1"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                text=ctx.author.display_name + strings["mod_serv"]
            )
            await ctx.reply(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
        elif ctx.author.guild_permissions.ban_members:
            embed = disnake.Embed(title=strings["ban_title"], color=disnake.Color(0xff0000),timestamp=datetime.datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            
            await ctx.reply(embed=embed)
            
            dm_embed = disnake.Embed(title=strings["ban_title"], color=disnake.Color(0xff0000),timestamp=datetime.datetime.now())
            dm_embed.add_field(name=strings["ban_server"], value=ctx.guild.name, inline=False)
            dm_embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            dm_embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            
            await member.send(embed=dm_embed)

            await member.ban() 
        else:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["ban_2"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                text=ctx.author.display_name + strings["mod_serv"]
            )
            await ctx.reply(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
        
def setup(bot: commands.Bot):
    bot.add_cog(Slash_Ban(bot))
    bot.add_cog(NoSlash_Ban(bot))