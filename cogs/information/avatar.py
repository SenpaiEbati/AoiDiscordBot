import datetime
import disnake
from disnake.ext import commands

class Slash_Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command()
    async def avatar(self, ctx, user: disnake.Member = None):
        if not user:
            user = ctx.author

        user_icon = user.display_avatar
        if not user_icon:
            user_icon = disnake.DefaultAvatar.fuchsia

        embed = disnake.Embed(color=0x1E90FF,
                              title="🖼️ Avatar 🖼️",
                              description=f"Avatar of {user.display_name}",
                              timestamp=datetime.datetime.now())
        embed.set_image(url=user_icon)
        embed.set_footer(
            text=f"Requested information {ctx.author.display_name}"
        )
        await ctx.send(embed=embed)
class NoSlash_Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def avatar(self, ctx, user: disnake.Member = None):
        if not user:
            user = ctx.author

        user_icon = user.display_avatar
        if not user_icon:
            user_icon = disnake.DefaultAvatar.fuchsia

        embed = disnake.Embed(color=0x1E90FF,
                              title="🖼️ Avatar 🖼️",
                              description=f"Avatar of {user.display_name}",
                              timestamp=datetime.datetime.now())
        embed.set_image(url=user_icon)
        embed.set_footer(
            text=f"Requested information {ctx.author.display_name}"
        )
        await ctx.reply(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Slash_Avatar(bot))
    bot.add_cog(NoSlash_Avatar(bot))