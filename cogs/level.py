import disnake
from disnake.ext import commands
from core.bot import AoiBot
import datetime
from core.utils import LanguageClass, LevelUpClass, get_colour

class Level(commands.Cog):
    def __init__(self, bot):
        self.bot: AoiBot = bot

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        if message.author.bot:
            return
        # Начисление опыта за отправку сообщений
        await LevelUpClass.add_exp(LevelUpClass, message, message.author, 1)

    @commands.slash_command(name="level",
                            description="Info about level, exp and rank on the server/Информация об уровне, опыте и ранге на сервере")
    async def level(self, ctx, user: disnake.Member = None):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        if not user:
            user = ctx.author

        user_icon = user.display_avatar
        if not user_icon:
            user_icon = disnake.DefaultAvatar.fuchsia

        exp = await LevelUpClass.get_exp(LevelUpClass,ctx,user)
        level = await LevelUpClass.get_level(LevelUpClass,ctx,user)
        rank = await LevelUpClass.get_rank(LevelUpClass,ctx,user)
        nowlinelevel = (50 * level * level) // 2
        pastlinelevel = (50 * (level-1) * (level-1)) // 2

        embed = disnake.Embed(title=strings["levelinfo_1"] + f"{user.display_name}" + strings["levelinfo_2"],
                              color=get_colour("halloween"),
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
    @commands.command(aliases=["lvl","exp","rank"])
    async def level(self, ctx, user: disnake.Member = None):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        if not user:
            user = ctx.author

        user_icon = user.display_avatar
        if not user_icon:
            user_icon = disnake.DefaultAvatar.fuchsia

        exp = await LevelUpClass.get_exp(LevelUpClass,ctx,user)
        level = await LevelUpClass.get_level(LevelUpClass,ctx,user)
        rank = await LevelUpClass.get_rank(LevelUpClass,ctx,user)
        nowlinelevel = (50 * level * level) // 2
        pastlinelevel = (50 * (level-1) * (level-1)) // 2

        embed = disnake.Embed(title=strings["levelinfo_1"] + f"{user.display_name}" + strings["levelinfo_2"],
                              color=get_colour("halloween"),
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
    bot.add_cog(Level(bot))
    bot.add_cog(NoSlash_Level(bot))