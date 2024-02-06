import datetime
import disnake
from disnake.ext import commands

class Slash_Userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command()
    async def userinfo(self, ctx, user: disnake.Member = None):
        if not user:
            user = ctx.author

        user_icon = user.display_avatar
        if not user_icon:
            user_icon = disnake.DefaultAvatar.fuchsia

        if user.status == disnake.Status.online:
            user_status = "🟢 Online"
        elif user.status == disnake.Status.idle:
            user_status = "🌙 Idle"
        elif user.status == disnake.Status.dnd:
            user_status = "⛔️ Do Not Disturb"
        else:
            user_status = "💿 Offline"

        embed = disnake.Embed(color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_author(name=f"Info about {user.display_name}",
                         icon_url=user_icon)
        embed.set_thumbnail(url=user_icon)
        embed.set_footer(
            text=f"Requested information {ctx.author.display_name}"
        )
        value_embed = f"**Basic information**\n**User name:** {user.name}({user.display_name})\n**User ID:** {user.id}\n**Status:** {user_status}\n**Joined:** `{user.joined_at.strftime('%Y.%m.%d %H:%M')}`\n**Created:** `{user.created_at.strftime('%Y.%m.%d %H:%M')}`\n**Activity:** {user.activity}"
        embed.add_field(name="", value=value_embed, inline=False)
        
        await ctx.send(embed=embed)

class NoSlash_Userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def userinfo(self, ctx, user: disnake.Member = None):
        if not user:
            user = ctx.author
            
        user_icon = user.display_avatar
        if not user_icon:
            user_icon = disnake.DefaultAvatar.fuchsia

        if user.status == disnake.Status.online:
            user_status = "🟢 Online"
        elif user.status == disnake.Status.idle:
            user_status = "🌙 Idle"
        elif user.status == disnake.Status.dnd:
            user_status = "⛔️ Do Not Disturb"
        else:
            user_status = "💿 Offline"

        embed = disnake.Embed(color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_author(name=f"Info about {user.display_name}",
                         icon_url=user_icon)
        embed.set_thumbnail(url=user_icon)
        embed.set_footer(
            text=f"Information about {user.display_name}",
        )
        value_embed = f"**Basic information**\n**Username:** {user.name}({user.display_name})\n**User ID:** {user.id}\n**Status:** {user_status}\n**Joined:** `{user.joined_at.strftime('%Y.%m.%d %H:%M')}`\n**Created:** `{user.created_at.strftime('%Y.%m.%d %H:%M')}`\n**Activity:** {user.activity}"
        embed.add_field(name="", value=value_embed, inline=False)
        
        await ctx.reply(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Slash_Userinfo(bot))
    bot.add_cog(NoSlash_Userinfo(bot))