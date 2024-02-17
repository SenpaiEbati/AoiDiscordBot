import datetime
import disnake
from disnake.ext import commands
from cogs._class.LanguageClass import LanguageClass

class Slash_Channelinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command()
    async def channelinfo(self, ctx, channel: disnake.abc.GuildChannel = None):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))

        if not channel:
            channel = ctx.channel

        server = ctx.guild
        server_icon = server.icon.url if server.icon else None

        channel_name = channel.name
        channel_id = channel.id
        if (LanguageClass.get_lang(LanguageClass,ctx) == "en"):
            dateUTC = '%m.%d.%Y %I:%M %p'
        else:
            dateUTC = '%d.%m.%Y %H:%M'
        creation_date = channel.created_at.strftime(dateUTC)
        
        channel_category = channel.category.name if channel.category else strings["none"]
        is_nsfw = strings["yes"] if channel.is_nsfw() else strings["no"]
        channel_type = str(channel.type)

        embed = disnake.Embed(title=strings["channelinfo_1"], color=0x1E90FF,timestamp=datetime.datetime.now())
        if server_icon:
            embed.set_thumbnail(url=server_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req info"]
        )
        embed.add_field(name=strings["channelname"] + f"{channel_name}", 
                        value=strings["channelid"] + f"{channel_id}\n" + 
                        strings["channeldate"] + f"`{creation_date}`\n" + 
                        strings["channelcateg"] + f"{channel_category}\n" + 
                        strings["channelnsfw"] + f"{is_nsfw}\n" + 
                        strings["channeltype"] + f"{channel_type}", inline=False)
        await ctx.send(embed=embed)

class NoSlash_Channelinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def channelinfo(self, ctx, channel: disnake.abc.GuildChannel = None):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))

        if not channel:
            channel = ctx.channel

        server = ctx.guild
        server_icon = server.icon.url if server.icon else None

        channel_name = channel.name
        channel_id = channel.id
        if (LanguageClass.get_lang(LanguageClass,ctx) == "en"):
            dateUTC = '%m.%d.%Y %I:%M %p'
        else:
            dateUTC = '%d.%m.%Y %H:%M'
        creation_date = channel.created_at.strftime(dateUTC)
        
        channel_category = channel.category.name if channel.category else strings["none"]
        is_nsfw = strings["yes"] if channel.is_nsfw() else strings["no"]
        channel_type = str(channel.type)

        embed = disnake.Embed(title=strings["channelinfo_1"], color=0x1E90FF,timestamp=datetime.datetime.now())
        if server_icon:
            embed.set_thumbnail(url=server_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req info"]
        )
        embed.add_field(name=strings["channelname"] + f"{channel_name}", 
                        value=strings["channelid"] + f"{channel_id}\n" + 
                        strings["channeldate"] + f"`{creation_date}`\n" + 
                        strings["channelcateg"] + f"{channel_category}\n" + 
                        strings["channelnsfw"] + f"{is_nsfw}\n" + 
                        strings["channeltype"] + f"{channel_type}", inline=False)
        await ctx.reply(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Slash_Channelinfo(bot))
    bot.add_cog(NoSlash_Channelinfo(bot))