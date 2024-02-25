import datetime
import disnake
from disnake.ext import commands
from cogs._class.LanguageClass import LanguageClass

class Slash_Serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(name="serverinfo",
                            description="Basic information about the server/Основная информация о сервере")
    async def serverinfo(self, ctx):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))
        
        server = ctx.guild

        server_icon = server.icon.url if server.icon else None

        server_name = server.name
        server_id = server.id
        server_owner = server.owner 

        if (LanguageClass.get_lang(LanguageClass,ctx) == "en"):
            dateUTC = '%m.%d.%Y %I:%M %p'
        else:
            dateUTC = '%d.%m.%Y %H:%M'
        creation_date = server.created_at.strftime(dateUTC)
        verific_count = server.verification_level
        role_count = len(server.roles)

        bot_count = sum(1 for member in server.members if member.bot)
        
        online_count = sum(member.status == disnake.Status.online for member in server.members)
        idle_count = sum(member.status == disnake.Status.idle for member in server.members)
        dnd_count = sum(member.status == disnake.Status.dnd for member in server.members)
        offline_count = sum(member.status == disnake.Status.offline for member in server.members)

        member_count = f"● "+ strings["servertotal"] + f": **{server.member_count}**\n● "+strings["serverhumans"] + f": **{server.member_count - bot_count}**\n● "+ strings["serverbots"] +f": **{bot_count}**"
        status_count = f"● "+strings["online"]+f": **{online_count}**\n● "+strings["idle"]+f": **{idle_count}**\n● "+strings["dnd"]+f": **{dnd_count}**\n● "+strings["offline"]+f": **{offline_count}**"
        channel_count = f"● "+strings["serverchanneltotal"]+f": **{len(server.channels)}**\n● "+strings["serverchantexts"]+f": **{len(server.text_channels)}**\n● "+strings["serverchanforums"]+f": **{len(server.forum_channels)}**\n● "+strings["serverchanvoices"]+f": **{len(server.voice_channels)}**"

        embed = disnake.Embed(title=strings["serverinfo_1"], color=0x1E90FF,timestamp=datetime.datetime.now())
        if server_icon:
            embed.set_thumbnail(url=server_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
        )
        embed.add_field(name=strings["servername"]+f"{server_name}", 
                        value=strings["serverid"]+f"{server_id}\n" + 
                        strings["serverowner"] + f"{server_owner}\n" +
                        strings["serverdate"] + f"`{creation_date}`\n" + 
                        strings["serververif"] + f"{verific_count}\n" + 
                        strings["serverrolecount"] + f"{role_count}", inline=False)

        embed.add_field(name=strings["servermember"], value=member_count, inline=True)
        embed.add_field(name=strings["serverstatus"], value=status_count, inline=True)
        embed.add_field(name=strings["serverchannels"], value=channel_count, inline=True)

        await ctx.send(embed=embed)

class NoSlash_Serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="serverinfo")
    async def serverinfo(self, ctx):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))
        
        server = ctx.guild

        server_icon = server.icon.url if server.icon else None

        server_name = server.name
        server_id = server.id
        server_owner = server.owner 

        if (LanguageClass.get_lang(LanguageClass,ctx) == "en"):
            dateUTC = '%m.%d.%Y %I:%M %p'
        else:
            dateUTC = '%d.%m.%Y %H:%M'
        creation_date = server.created_at.strftime(dateUTC)
        verific_count = server.verification_level
        role_count = len(server.roles)

        bot_count = sum(1 for member in server.members if member.bot)
        
        online_count = sum(member.status == disnake.Status.online for member in server.members)
        idle_count = sum(member.status == disnake.Status.idle for member in server.members)
        dnd_count = sum(member.status == disnake.Status.dnd for member in server.members)
        offline_count = sum(member.status == disnake.Status.offline for member in server.members)

        member_count = f"● "+ strings["servertotal"] + f": **{server.member_count}**\n● "+strings["serverhumans"] + f": **{server.member_count - bot_count}**\n● "+ strings["serverbots"] +f": **{bot_count}**"
        status_count = f"● "+strings["online"]+f": **{online_count}**\n● "+strings["idle"]+f": **{idle_count}**\n● "+strings["dnd"]+f": **{dnd_count}**\n● "+strings["offline"]+f": **{offline_count}**"
        channel_count = f"● "+strings["serverchanneltotal"]+f": **{len(server.channels)}**\n● "+strings["serverchantexts"]+f": **{len(server.text_channels)}**\n● "+strings["serverchanforums"]+f": **{len(server.forum_channels)}**\n● "+strings["serverchanvoices"]+f": **{len(server.voice_channels)}**"

        embed = disnake.Embed(title=strings["serverinfo_1"], color=0x1E90FF,timestamp=datetime.datetime.now())
        if server_icon:
            embed.set_thumbnail(url=server_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
        )
        embed.add_field(name=strings["servername"]+f"{server_name}", 
                        value=strings["serverid"]+f"{server_id}\n" + 
                        strings["serverowner"] + f"{server_owner}\n" +
                        strings["serverdate"] + f"`{creation_date}`\n" + 
                        strings["serververif"] + f"{verific_count}\n" + 
                        strings["serverrolecount"] + f"{role_count}", inline=False)

        embed.add_field(name=strings["servermember"], value=member_count, inline=True)
        embed.add_field(name=strings["serverstatus"], value=status_count, inline=True)
        embed.add_field(name=strings["serverchannels"], value=channel_count, inline=True)

        await ctx.reply(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Slash_Serverinfo(bot))
    bot.add_cog(NoSlash_Serverinfo(bot))