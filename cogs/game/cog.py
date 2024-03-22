from . import RussianRoulette
from disnake import Embed
from disnake.ext.commands import Cog, command, slash_command
from core import Context
from core.utils import get_colour

class NoSlash_Games(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @command(aliases=["rr", "gun_game", "russianroulette", "gungame"])
    async def russian_roulette(self, ctx: Context):
        embed = Embed(title="Russian Roulette", colour=get_colour("blue")).set_footer(
            text="Dont die!"
        )

        await ctx.reply(embed=embed, view=RussianRoulette(ctx))

class Games(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="russianroulette")
    async def russian_roulette(self, ctx):
        embed = Embed(title="Russian Roulette", colour=get_colour("blue")).set_footer(
            text="Dont die!"
        )

        await ctx.send(embed=embed, view=RussianRoulette(ctx))

def setup(bot):
    bot.add_cog(NoSlash_Games(bot))
    bot.add_cog(Games(bot))