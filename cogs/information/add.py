import disnake
from disnake.ext import commands
from cogs.configuration.language import LanguageCog

class Slash_Add(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def add(self,ctx: disnake.ApplicationCommandInteraction):
        LanguageCog.loadjson2(LanguageCog,ctx,"..\MyDiscordBot\localizations")
        strings = LanguageCog.get_strings(LanguageCog,LanguageCog.get_lang(LanguageCog,ctx))

        embed = disnake.Embed(title=strings["add_1"],
                              description=strings["add_2"],
                              color=0x1E90FF)
        await ctx.response.send_message(embed=embed,
                        components=[
                            disnake.ui.Button(label=strings["add_3"],url=strings["add_4"]),]
                        )

class NoSlash_Add(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def add(self,ctx: disnake.ApplicationCommandInteraction):
        LanguageCog.loadjson2(LanguageCog,ctx,"..\MyDiscordBot\localizations")
        strings = LanguageCog.get_strings(LanguageCog,LanguageCog.get_lang(LanguageCog,ctx))

        embed = disnake.Embed(title=strings["add_1"], 
                              description=strings["add_2"],
                              color=0x1E90FF)
        await ctx.reply(embed=embed,
                        components=[
                            disnake.ui.Button(label=strings["add_3"],url=strings["add_4"]),]
                            )

def setup(bot: commands.Bot):
    bot.add_cog(Slash_Add(bot))
    bot.add_cog(NoSlash_Add(bot))