import disnake
from disnake.ext import commands
import datetime
from cogs.levelup.Levelupsystem import LevelUpSystem

class Slash_Level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command()
    async def level(self, ctx, user: disnake.Member = None):
        if not user:
            user = ctx.author

        user_icon = user.display_avatar
        if not user_icon:
            user_icon = disnake.DefaultAvatar.fuchsia

        exp = LevelUpSystem.get_exp(LevelUpSystem,ctx,user)
        level = LevelUpSystem.get_level(LevelUpSystem,ctx,user)
        rank = LevelUpSystem.get_rank(LevelUpSystem,ctx,user)
        nowlinelevel = (50 * level * level) // 2
        pastlinelevel = (50 * (level-1) * (level-1)) // 2

        embed = disnake.Embed(title=f"🏆 Level info about {user.display_name} 🏆",
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
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
        embed.add_field(name=f"**User name:** {user.name}({user.display_name})\n**Rank:** #{rank}\n**Level:** {level}\n**Experience:** {exp}\n**Next level exp:** {nowlinelevel}", 
                        value=f"**Level progress**\n{bar * progress}{empty_bar * (total - progress)} {percentage}%\n{level} lvl⠀⠀⠀⠀{exp}/{nowlinelevel} exp")
        # Отправляем встраиваемое сообщение
        await ctx.send(embed=embed)

class NoSlash_Level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def level(self, ctx, user: disnake.Member = None):
        if not user:
            user = ctx.author

        user_icon = user.display_avatar
        if not user_icon:
            user_icon = disnake.DefaultAvatar.fuchsia

        exp = LevelUpSystem.get_exp(LevelUpSystem,ctx,user)
        level = LevelUpSystem.get_level(LevelUpSystem,ctx,user)
        rank = LevelUpSystem.get_rank(LevelUpSystem,ctx,user)
        nowlinelevel = (50 * level * level) // 2
        pastlinelevel = (50 * (level-1) * (level-1)) // 2

        embed = disnake.Embed(title=f"🏆 Level info about {user.display_name} 🏆",
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
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
        embed.add_field(name=f"**User name:** {user.name}({user.display_name})\n**Rank:** #{rank}\n**Level:** {level}\n**Experience:** {exp}\n**Next level exp:** {nowlinelevel}", 
                        value=f"**Level progress**\n{bar * progress}{empty_bar * (total - progress)} {percentage}%\n{level} lvl⠀⠀⠀⠀{exp}/{nowlinelevel} exp")
        # Отправляем встраиваемое сообщение
        await ctx.reply(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Slash_Level(bot))
    bot.add_cog(NoSlash_Level(bot))