import disnake
from disnake.ext import commands
import datetime
from cogs._class.LevelupClass import LevelUpClass
from cogs._class.LanguageClass import LanguageClass

class Slash_Level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command()
    async def level(self, ctx, user: disnake.Member = None):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))

        if not user:
            user = ctx.author

        user_icon = user.display_avatar
        if not user_icon:
            user_icon = disnake.DefaultAvatar.fuchsia

        exp = LevelUpClass.get_exp(LevelUpClass,ctx,user)
        level = LevelUpClass.get_level(LevelUpClass,ctx,user)
        rank = LevelUpClass.get_rank(LevelUpClass,ctx,user)
        nowlinelevel = (50 * level * level) // 2
        pastlinelevel = (50 * (level-1) * (level-1)) // 2

        embed = disnake.Embed(title=strings["levelinfo_1"] + f"{user.display_name}" + strings["levelinfo_2"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_thumbnail(url=user_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
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
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))

        if not user:
            user = ctx.author

        user_icon = user.display_avatar
        if not user_icon:
            user_icon = disnake.DefaultAvatar.fuchsia

        exp = LevelUpClass.get_exp(LevelUpClass,ctx,user)
        level = LevelUpClass.get_level(LevelUpClass,ctx,user)
        rank = LevelUpClass.get_rank(LevelUpClass,ctx,user)
        nowlinelevel = (50 * level * level) // 2
        pastlinelevel = (50 * (level-1) * (level-1)) // 2

        embed = disnake.Embed(title=strings["levelinfo_1"] + f"{user.display_name}" + strings["levelinfo_2"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_thumbnail(url=user_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
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