import datetime
import disnake
from disnake.ext import commands

class Slash_Botinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command()
    async def botinfo(self, ctx):
        bot = self.bot.user

        bot_icon = bot.avatar
        if not bot_icon:
            bot_icon = disnake.DefaultAvatar.fuchsia

        if self.bot.status == disnake.Status.online:
            bot_status = "🟢 Онлайн"
        elif self.bot.status == disnake.Status.idle:
            bot_status = "🌙 Неактивен"
        elif self.bot.status == disnake.Status.dnd:
            bot_status = "⛔️ Не беспокоить"
        else:
            bot_status = "💿 Не в сети"

        embed = disnake.Embed(color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_author(name=f"Информация о {bot.display_name}",
                         icon_url=bot_icon)
        embed.set_thumbnail(url=bot_icon)
        embed.set_footer(
            text=f"Информацию запросил {ctx.author.display_name}"
        )
        value_embed = f"**Основная информация о боте**\n**Имя бота:** {bot.name}({bot.display_name})\n**ID бота:** {bot.id}\n**Статус:** {bot_status}\n**Создан:** `{bot.created_at.strftime('%Y.%m.%d %H:%M')}`\n**Разработчик бота:** senpaiebati(SenpaiEbati)\nРазработан на **Python**(VS Code) с помощью **Disnake**\nОбслуживает **{len(self.bot.guilds)}** серверов"
        embed.add_field(name="", value=value_embed, inline=False)
        
        await ctx.send(embed=embed)

class NoSlash_Botinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def botinfo(self, ctx):
        bot = self.bot.user

        bot_icon = bot.avatar
        if not bot_icon:
            bot_icon = disnake.DefaultAvatar.fuchsia

        if self.bot.status == disnake.Status.online:
            bot_status = "🟢 Онлайн"
        elif self.bot.status == disnake.Status.idle:
            bot_status = "🌙 Неактивен"
        elif self.bot.status == disnake.Status.dnd:
            bot_status = "⛔️ Не беспокоить"
        else:
            bot_status = "💿 Не в сети"

        embed = disnake.Embed(color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_author(name=f"Информация о {bot.display_name}",
                         icon_url=bot_icon)
        embed.set_thumbnail(url=bot_icon)
        embed.set_footer(
            text=f"Информацию запросил {ctx.author.display_name}"
        )
        value_embed = f"**Основная информация о боте**\n**Имя бота:** {bot.name}({bot.display_name})\n**ID бота:** {bot.id}\n**Статус:** {bot_status}\n**Создан:** `{bot.created_at.strftime('%Y.%m.%d %H:%M')}`\n**Разработчик бота:** senpaiebati(SenpaiEbati)\nРазработан на **Python**(VS Code) с помощью **Disnake**\nОбслуживает **{len(self.bot.guilds)}** серверов"
        embed.add_field(name="", value=value_embed, inline=False)
        
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Slash_Botinfo(bot))
    bot.add_cog(NoSlash_Botinfo(bot))