from asyncio import sleep
import datetime
import disnake
from disnake.ext import commands
from cogs._class.LanguageClass import LanguageClass

class Slash_UnBan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="unban",
                            description="Command to unban a user/Команда, снимающая запрет нахождения на сервере с пользователя",
                            default_member_permissions=disnake.Permissions(ban_members=True))
    async def unban(self, ctx, member: disnake.Member, *, reason="-"):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))
        if ctx.author.guild_permissions.ban_members:
            embed = disnake.Embed(title=strings["unban_title"], color=disnake.Color(0x32CD32),timestamp=datetime.datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)
            
            dm_embed = disnake.Embed(title=strings["unban_title"], color=disnake.Color(0x32CD32),timestamp=datetime.datetime.now())
            dm_embed.add_field(name=strings["ban_server"], value=ctx.guild.name, inline=False)
            dm_embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            dm_embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await member.send(embed=dm_embed)

            await member.unban() 
        else:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["unban_rights"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)

class NoSlash_UnBan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    

    @commands.command(name="unban",
                            default_member_permissions=disnake.Permissions(ban_members=True))
    async def unban(self, ctx, member: disnake.Member, *, reason="-"):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))
        if ctx.author.guild_permissions.ban_members:
            embed = disnake.Embed(title=strings["unban_title"], color=disnake.Color(0x32CD32),timestamp=datetime.datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.reply(embed=embed)
            
            dm_embed = disnake.Embed(title=strings["unban_title"], color=disnake.Color(0x32CD32),timestamp=datetime.datetime.now())
            dm_embed.add_field(name=strings["ban_server"], value=ctx.guild.name, inline=False)
            dm_embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            dm_embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await member.send(embed=dm_embed)

            await member.unban() 
        else:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["unban_rights"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
            await ctx.reply(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)

def setup(bot: commands.Bot):
    bot.add_cog(Slash_UnBan(bot))
    bot.add_cog(NoSlash_UnBan(bot))