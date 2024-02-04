import disnake
from disnake.ext import commands
import datetime
from cogs.levelup.Levelupsystem import LevelUpSystem

class Slash_LevelUserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def leveluser(self, ctx, user: disnake.Member = None):
        if not user:
            user = ctx.author

        user_icon = user.display_avatar
        if not user_icon:
            user_icon = disnake.DefaultAvatar.fuchsia

        exp = LevelUpSystem.get_exp(LevelUpSystem,user)
        level = LevelUpSystem.get_level(LevelUpSystem,user)
        nowlinelevel = (50 * level * level) // 2
        pastlinelevel = (50 * (level-1) * (level-1)) // 2

        embed = disnake.Embed(color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_author(name=f"Level info about {user.display_name}",
                         icon_url=user_icon)
        embed.set_thumbnail(url=user_icon)
        embed.set_footer(
            text=f"{ctx.author.display_name} requested information"
        )
        # Создаем прогресс-бар
        bar = "█"
        empty_bar = "░"
        total = 10
        percentage = int((exp - pastlinelevel) / (nowlinelevel - pastlinelevel) * 100)
        progress = percentage // 10

        # Добавляем прогресс-бар во встраиваемое сообщение
        embed.add_field(name="", value=f"**User name:** {user.name}({user.display_name})\n**Level:** {level}\n**Experience:** {exp}\n**Next level exp:** {nowlinelevel}\n\n**Level progress**\n[{bar * progress}{empty_bar * (total - progress)}] {percentage}%\n{level} lvl⠀⠀⠀⠀⠀⠀⠀⠀{exp} exp")
        # Отправляем встраиваемое сообщение
        await ctx.send(embed=embed)

class NoSlash_LevelUserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def leveluser(self, ctx, user: disnake.Member = None):
        if not user:
            user = ctx.author

        user_icon = user.display_avatar
        if not user_icon:
            user_icon = disnake.DefaultAvatar.fuchsia

        exp = LevelUpSystem.get_exp(LevelUpSystem,user)
        level = LevelUpSystem.get_level(LevelUpSystem,user)
        nowlinelevel = (50 * level * level) // 2
        pastlinelevel = (50 * (level-1) * (level-1)) // 2

        embed = disnake.Embed(color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_author(name=f"Level info about {user.display_name}",
                         icon_url=user_icon)
        embed.set_thumbnail(url=user_icon)
        embed.set_footer(
            text=f"{ctx.author.display_name} requested information"
        )
        # Создаем прогресс-бар
        bar = "█"
        empty_bar = "░"
        total = 10
        percentage = int((exp - pastlinelevel) / (nowlinelevel - pastlinelevel) * 100)
        progress = percentage // 10

        # Добавляем прогресс-бар во встраиваемое сообщение
        embed.add_field(name="", value=f"**User name:** {user.name}({user.display_name})\n**Level:** {level}\n**Experience:** {exp}\n**Next level exp:** {nowlinelevel}\n\n**Level progress**\n[{bar * progress}{empty_bar * (total - progress)}] {percentage}%\n{level} lvl⠀⠀⠀⠀⠀⠀⠀⠀{exp} exp")
        # Отправляем встраиваемое сообщение
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Slash_LevelUserInfo(bot))
    bot.add_cog(NoSlash_LevelUserInfo(bot))