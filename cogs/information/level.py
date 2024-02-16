import disnake
from disnake.ext import commands
import datetime
from cogs.information.Levelupsystem import LevelUpSystem
from cogs.configuration.language import LanguageCog

class Slash_Level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command()
    async def level(self, ctx, user: disnake.Member = None):
        LanguageCog.loadjson2(LanguageCog,ctx,"..\MyDiscordBot\localizations")
        strings = LanguageCog.get_strings(LanguageCog,LanguageCog.get_lang(LanguageCog,ctx))

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

        embed = disnake.Embed(title=strings["levelinfo_1"] + f"{user.display_name}" + strings["levelinfo_2"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_thumbnail(url=user_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req info"]
        )
        # Создаем прогресс-бар
        bar = "█"
        empty_bar = "░"
        total = 10
        percentage = int((exp - pastlinelevel) / (nowlinelevel - pastlinelevel) * 100)
        progress = percentage // 10

        # Добавляем прогресс-бар во встраиваемое сообщение
        embed.add_field(name=strings["levelusername"] + f"{user.name}({user.display_name})\n" + 
                        strings["levelrank"] + f"{rank}\n" + 
                        strings["levellevel"] + f"{level}\n" + 
                        strings["levelexp"] + f"{exp}\n" + 
                        strings["levelnextlevelexp"] + f"{nowlinelevel}", 
                        value=strings["levelprogress"] + 
                        f"\n{bar * progress}{empty_bar * (total - progress)} {percentage}%\n{level} lvl⠀⠀⠀⠀{exp}/{nowlinelevel} exp")
        # Отправляем встраиваемое сообщение
        await ctx.send(embed=embed)

class NoSlash_Level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def level(self, ctx, user: disnake.Member = None):
        LanguageCog.loadjson2(LanguageCog,ctx,"..\MyDiscordBot\localizations")
        strings = LanguageCog.get_strings(LanguageCog,LanguageCog.get_lang(LanguageCog,ctx))

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

        embed = disnake.Embed(title=strings["levelinfo_1"] + f"{user.display_name}" + strings["levelinfo_2"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_thumbnail(url=user_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req info"]
        )
        # Создаем прогресс-бар
        bar = "█"
        empty_bar = "░"
        total = 10
        percentage = int((exp - pastlinelevel) / (nowlinelevel - pastlinelevel) * 100)
        progress = percentage // 10

        # Добавляем прогресс-бар во встраиваемое сообщение
        embed.add_field(name=strings["levelusername"] + f"{user.name}({user.display_name})\n" + 
                        strings["levelrank"] + f"{rank}\n" + 
                        strings["levellevel"] + f"{level}\n" + 
                        strings["levelexp"] + f"{exp}\n" + 
                        strings["levelnextlevelexp"] + f"{nowlinelevel}", 
                        value=strings["levelprogress"] + 
                        f"\n{bar * progress}{empty_bar * (total - progress)} {percentage}%\n{level} lvl⠀⠀⠀⠀{exp}/{nowlinelevel} exp")
        # Отправляем встраиваемое сообщение
        await ctx.reply(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Slash_Level(bot))
    bot.add_cog(NoSlash_Level(bot))