import datetime
import disnake
from disnake.ext import commands

class Slash_Channelinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command()
    async def channelinfo(self, ctx, channel: disnake.abc.GuildChannel = None):
        if not channel:
            channel = ctx.channel

        server = ctx.guild
        server_icon = server.icon.url if server.icon else None

       
        channel_name = channel.name
        channel_id = channel.id
        creation_date = channel.created_at.strftime('%Y.%m.%d %H:%M')
        
        channel_category = channel.category.name if channel.category else "None"
        is_nsfw = "Yes" if channel.is_nsfw() else "No"
        channel_type = str(channel.type)

        embed = disnake.Embed(title="📝 Channel Info 📝", color=0x1E90FF,timestamp=datetime.datetime.now())
        if server_icon:
            embed.set_thumbnail(url=server_icon)
        embed.set_footer(
            text=f"Requested information {ctx.author.display_name}"
        )
        embed.add_field(name="Channel Name:", value=channel_name, inline=True)
        embed.add_field(name="Channel ID:", value=channel_id, inline=True)
        embed.add_field(name="Creation Date:", value=creation_date, inline=True)

        embed.add_field(name="Channel Category:", value=channel_category, inline=True)
        embed.add_field(name="NSFW Channel:", value=is_nsfw, inline=True)
        embed.add_field(name="Channel Type:", value=channel_type, inline=True)

        await ctx.send(embed=embed)

class NoSlash_Channelinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def channelinfo(self, ctx, channel: disnake.abc.GuildChannel = None):
        if not channel:
            channel = ctx.channel

        server = ctx.guild
        server_icon = server.icon.url if server.icon else None

       
        channel_name = channel.name
        channel_id = channel.id
        creation_date = channel.created_at.strftime('%Y-%m-%d %H:%M')
        
        channel_category = channel.category.name if channel.category else "None"
        is_nsfw = "Yes" if channel.is_nsfw() else "No"
        channel_type = str(channel.type)

        embed = disnake.Embed(title="📝 Channel Info 📝", color=0x1E90FF,timestamp=datetime.datetime.now())
        if server_icon:
            embed.set_thumbnail(url=server_icon)
        embed.set_footer(
            text=f"Requested information {ctx.author.display_name}"
        )
        embed.add_field(name="Channel Name:", value=channel_name, inline=True)
        embed.add_field(name="Channel ID:", value=channel_id, inline=True)
        embed.add_field(name="Creation Date:", value=creation_date, inline=True)

        embed.add_field(name="Channel Category:", value=channel_category, inline=True)
        embed.add_field(name="NSFW Channel:", value=is_nsfw, inline=True)
        embed.add_field(name="Channel Type:", value=channel_type, inline=True)

        await ctx.reply(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Slash_Channelinfo(bot))
    bot.add_cog(NoSlash_Channelinfo(bot))