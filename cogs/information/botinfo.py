import datetime
import disnake
from disnake.ext import commands
from cogs._class.LanguageClass import LanguageClass

class Slash_Botinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(name="botinfo",
                            description="Info about bot Aoi青/Информация о боте Aoi青")
    async def botinfo(self, ctx):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        bot = self.bot.user

        bot_icon = bot.avatar
        if not bot_icon:
            bot_icon = disnake.DefaultAvatar.fuchsia

        if self.bot.status == disnake.Status.online:
            bot_status = strings["online"]
        elif self.bot.status == disnake.Status.idle:
            bot_status = strings["idle"]
        elif self.bot.status == disnake.Status.dnd:
            bot_status = strings["dnd"]
        else:
            bot_status = strings["offline"]

        embed = disnake.Embed(title=strings["botinfo_1"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_thumbnail(url=bot_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
        )
        
        if (await LanguageClass.get_lang(LanguageClass,ctx) == "en"):
            dateUTC = '%m.%d.%Y %I:%M %p'
        else:
            dateUTC = '%d.%m.%Y %H:%M'

        embed.add_field(name=strings["botname"] + f"{bot.name}", 
                        value=strings["botid"] + f"{bot.id}" + "\n" + 
                        strings["botstatus"] + f"{bot_status}" + "\n" +
                        strings["botcreated"] + f"`{bot.created_at.strftime(dateUTC)}`\n"+
                        strings["botdev"] + "senpaiebati(SenpaiEbati)" + "\n" + 
                        strings["botdisnake"] + "\n" +
                        strings["botmaintains_1"] + f"{len(self.bot.guilds)}" + strings["botmaintains_2"], inline=False)
        await ctx.send(embed=embed)

class NoSlash_Botinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="botinfo")
    async def botinfo(self, ctx):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        bot = self.bot.user

        bot_icon = bot.avatar
        if not bot_icon:
            bot_icon = disnake.DefaultAvatar.fuchsia

        if self.bot.status == disnake.Status.online:
            bot_status = strings["online"]
        elif self.bot.status == disnake.Status.idle:
            bot_status = strings["idle"]
        elif self.bot.status == disnake.Status.dnd:
            bot_status = strings["dnd"]
        else:
            bot_status = strings["offline"]

        embed = disnake.Embed(title=strings["botinfo_1"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_thumbnail(url=bot_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
        )
        
        if (await LanguageClass.get_lang(LanguageClass,ctx) == "en"):
            dateUTC = '%m.%d.%Y %I:%M %p'
        else:
            dateUTC = '%d.%m.%Y %H:%M'

        embed.add_field(name=strings["botname"] + f"{bot.name}", 
                        value=strings["botid"] + f"{bot.id}" + "\n" + 
                        strings["botstatus"] + f"{bot_status}" + "\n" +
                        strings["botcreated"] + f"`{bot.created_at.strftime(dateUTC)}`\n"+
                        strings["botdev"] + "senpaiebati(SenpaiEbati)" + "\n" + 
                        strings["botdisnake"] + "\n" +
                        strings["botmaintains_1"] + f"{len(self.bot.guilds)}" + strings["botmaintains_2"], inline=False)
        await ctx.reply(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Slash_Botinfo(bot))
    bot.add_cog(NoSlash_Botinfo(bot))