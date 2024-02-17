import datetime
import disnake
from disnake.ext import commands
from cogs._class.LanguageClass import LanguageClass

class Slash_Add(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def add(self,ctx: disnake.ApplicationCommandInteraction):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))
        embed = disnake.Embed(title=strings["add_1"],
                              description=strings["add_2"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_footer(
            text=ctx.author.display_name + strings["req info"]
        )
        await ctx.response.send_message(embed=embed,
                        components=[
                            disnake.ui.Button(label=strings["add_3"],url=strings["add_4"]),]
                        )

class NoSlash_Add(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def add(self,ctx: disnake.ApplicationCommandInteraction):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))

        embed = disnake.Embed(title=strings["add_1"], 
                              description=strings["add_2"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_footer(
            text=ctx.author.display_name + strings["req info"]
        )
        await ctx.reply(embed=embed,
                        components=[
                            disnake.ui.Button(label=strings["add_3"],url=strings["add_4"]),]
                            )

def setup(bot: commands.Bot):
    bot.add_cog(Slash_Add(bot))
    bot.add_cog(NoSlash_Add(bot))