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

        embed = disnake.Embed(color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_author(name=f"Info about {bot.display_name}",
                         icon_url=bot_icon)
        embed.set_thumbnail(url=bot_icon)
        embed.set_footer(
            text=f"Requested information {ctx.author.display_name}"
        )
        value_embed = f"**Basic information about the bot**\n**Bot name:** {bot.name}({bot.display_name})\n**Bot ID:** {bot.id}\n**Status:** {bot_status}\n**Created:** `{bot.created_at.strftime('%Y.%m.%d %H:%M')}`\n**Bot Developer:** senpaiebati(SenpaiEbati)\nDeveloped in **Python**(VS Code) with **Disnake**\nMaintains **{len(self.bot.guilds)}** Servers"
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
            bot_status = "🟢 Online"
        elif self.bot.status == disnake.Status.idle:
            bot_status = "🌙 Idle"
        elif self.bot.status == disnake.Status.dnd:
            bot_status = "⛔️ Do Not Disturb"
        else:
            bot_status = "💿 Offline"

        embed = disnake.Embed(color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_author(name=f"Info about {bot.display_name}",
                         icon_url=bot_icon)
        embed.set_thumbnail(url=bot_icon)
        embed.set_footer(
            text=f"Requested information {ctx.author.display_name}"
        )
        value_embed = f"**Basic information about the bot**\n**Bot name:** {bot.name}({bot.display_name})\n**Bot ID:** {bot.id}\n**Status:** {bot_status}\n**Created:** `{bot.created_at.strftime('%Y.%m.%d %H:%M')}`\n**Bot Developer:** senpaiebati(SenpaiEbati)\nDeveloped in **Python**(VS Code) with **Disnake**\nMaintains **{len(self.bot.guilds)}** Servers"
        embed.add_field(name="", value=value_embed, inline=False)
        
        await ctx.reply(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Slash_Botinfo(bot))
    bot.add_cog(NoSlash_Botinfo(bot))