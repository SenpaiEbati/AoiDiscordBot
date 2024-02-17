import datetime
import disnake
from disnake.ext import commands
from cogs._class.LanguageClass import LanguageClass

class Slash_Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command()
    async def avatar(self, ctx, user: disnake.Member = None):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))

        if not user:
            user = ctx.author

        user_icon = user.display_avatar
        if not user_icon:
            user_icon = disnake.DefaultAvatar.fuchsia

        embed = disnake.Embed(color=0x1E90FF,
                              title=strings["avatar_1"],
                              description=strings["avatar_2"] + user.display_name,
                              timestamp=datetime.datetime.now())
        embed.set_image(url=user_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req info"]
        )
        await ctx.send(embed=embed)

class NoSlash_Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def avatar(self, ctx, user: disnake.Member = None):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))

        if not user:
            user = ctx.author

        user_icon = user.display_avatar
        if not user_icon:
            user_icon = disnake.DefaultAvatar.fuchsia

        embed = disnake.Embed(color=0x1E90FF,
                              title=strings["avatar_1"],
                              description=strings["avatar_2"] + user.display_name,
                              timestamp=datetime.datetime.now())
        embed.set_image(url=user_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req info"]
        )
        await ctx.reply(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Slash_Avatar(bot))
    bot.add_cog(NoSlash_Avatar(bot))