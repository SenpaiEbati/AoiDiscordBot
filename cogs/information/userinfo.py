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

        embed = disnake.Embed(title=f"🪪 Info about the {user.display_name} 🪪",
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_thumbnail(url=user_icon)
        embed.set_footer(
            text=f"Requested information {ctx.author.display_name}"
        )
        value_embed = f"**User ID:** {user.id}\n**Status:** {user_status}\n**Created:** `{user.created_at.strftime('%Y.%m.%d %H:%M')}`\n**Joined:** `{user.joined_at.strftime('%Y.%m.%d %H:%M')}`\n**Activity:** {user.activity}"
        embed.add_field(name=f"**User name:** {user.name}({user.display_name})", 
                        value=value_embed, inline=False)
        
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

        embed = disnake.Embed(title=f"🪪 Info about the {user.display_name} 🪪",
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_thumbnail(url=user_icon)
        embed.set_footer(
            text=f"Requested information {ctx.author.display_name}"
        )
        value_embed = f"**User ID:** {user.id}\n**Status:** {user_status}\n**Created:** `{user.created_at.strftime('%Y.%m.%d %H:%M')}`\n**Joined:** `{user.joined_at.strftime('%Y.%m.%d %H:%M')}`\n**Activity:** {user.activity}"
        embed.add_field(name=f"**User name:** {user.name}({user.display_name})", 
                        value=value_embed, inline=False)
        
        await ctx.reply(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Slash_Userinfo(bot))
    bot.add_cog(NoSlash_Userinfo(bot))