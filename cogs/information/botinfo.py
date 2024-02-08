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
            bot_status = "🟢 Online"
        elif self.bot.status == disnake.Status.idle:
            bot_status = "🌙 Idle"
        elif self.bot.status == disnake.Status.dnd:
            bot_status = "⛔️ Do Not Disturb"
        else:
            bot_status = "💿 Offline"

        embed = disnake.Embed(title="🪪 Info about the bot Aoi青 🪪",
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_thumbnail(url=bot_icon)
        embed.set_footer(
            text=f"Requested information {ctx.author.display_name}"
        )
        embed.add_field(name=f"Bot name: {bot.name}", 
                        value=f"**Bot ID:** {bot.id}\n**Status:** {bot_status}\n**Created:** `{bot.created_at.strftime('%Y.%m.%d %H:%M')}`\n**Bot Developer:** senpaiebati(SenpaiEbati)\nDeveloped in **Python**(VS Code) with **Disnake**\nMaintains **{len(self.bot.guilds)}** Servers", inline=False)
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
            bot_status = "🟢 Online"
        elif self.bot.status == disnake.Status.idle:
            bot_status = "🌙 Idle"
        elif self.bot.status == disnake.Status.dnd:
            bot_status = "⛔️ Do Not Disturb"
        else:
            bot_status = "💿 Offline"

        embed = disnake.Embed(title="🪪 Info about the bot Aoi青 🪪",
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_thumbnail(url=bot_icon)
        embed.set_footer(
            text=f"Requested information {ctx.author.display_name}"
        )
        embed.add_field(name=f"Bot name: {bot.name}", 
                        value=f"**Bot ID:** {bot.id}\n**Status:** {bot_status}\n**Created:** `{bot.created_at.strftime('%Y.%m.%d %H:%M')}`\n**Bot Developer:** senpaiebati(SenpaiEbati)\nDeveloped in **Python**(VS Code) with **Disnake**\nMaintains **{len(self.bot.guilds)}** Servers", inline=False)
        await ctx.reply(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Slash_Botinfo(bot))
    bot.add_cog(NoSlash_Botinfo(bot))