import datetime
import disnake
from disnake.ext import commands

class Slash_Serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command()
    async def serverinfo(self, ctx):
        server = ctx.guild

        server_icon = server.icon.url if server.icon else None

        server_name = server.name
        server_id = server.id
        server_owner = server.owner 

        creation_date = server.created_at.strftime('%Y.%m.%d %H:%M')
        verific_count = server.verification_level
        role_count = len(server.roles)

        bot_count = sum(1 for member in server.members if member.bot)
        
        online_count = sum(member.status == disnake.Status.online for member in server.members)
        idle_count = sum(member.status == disnake.Status.idle for member in server.members)
        dnd_count = sum(member.status == disnake.Status.dnd for member in server.members)
        offline_count = sum(member.status == disnake.Status.offline for member in server.members)

        member_count = f"● 👥 Total: **{server.member_count}**\n● 👤 Human: **{server.member_count - bot_count}**\n● 🤖 Bot: **{bot_count}**"
        status_count = f"● 🟢 Online: **{online_count}**\n● 🌙 Idle: **{idle_count}**\n● ⛔️ DoNotDisturb: **{dnd_count}**\n● 💿 Offline: **{offline_count}**"
        channel_count = f"● 🗂️ Total: **{len(server.channels)}**\n● ✏️ Text: **{len(server.text_channels)}**\n● 🗯️ Forums: **{len(server.forum_channels)}**\n● 🔊 Voices: **{len(server.voice_channels)}**"

        embed = disnake.Embed(title="📊 Server Info 📊", color=0x1E90FF,timestamp=datetime.datetime.now())
        if server_icon:
            embed.set_thumbnail(url=server_icon)
        embed.set_footer(
            text=f"Requested information {ctx.author.display_name}"
        )
        embed.add_field(name=f"Server Name: {server_name}", 
                        value=f"**Server ID:** {server_id}\n**Server Owner:** {server_owner}\n**Creation Date:** `{creation_date}`\n**Verification level:** {verific_count}\n**Role Count:** {role_count}", inline=False)

        embed.add_field(name="Member:", value=member_count, inline=True)
        embed.add_field(name="By status:", value=status_count, inline=True)
        embed.add_field(name="Channel:", value=channel_count, inline=True)

        await ctx.send(embed=embed)

class NoSlash_Serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(description="With this command you can clear message.")
    async def serverinfo(self, ctx):
        server = ctx.guild

        server_icon = server.icon.url if server.icon else None

        server_name = server.name
        server_id = server.id
        server_owner = server.owner 

        creation_date = server.created_at.strftime('%Y.%m.%d %H:%M')
        verific_count = server.verification_level
        role_count = len(server.roles)

        bot_count = sum(1 for member in server.members if member.bot)
        
        online_count = sum(member.status == disnake.Status.online for member in server.members)
        idle_count = sum(member.status == disnake.Status.idle for member in server.members)
        dnd_count = sum(member.status == disnake.Status.dnd for member in server.members)
        offline_count = sum(member.status == disnake.Status.offline for member in server.members)

        member_count = f"● 👥 Total: **{server.member_count}**\n● 👤 Human: **{server.member_count - bot_count}**\n● 🤖 Bot: **{bot_count}**"
        status_count = f"● 🟢 Online: **{online_count}**\n● 🌙 Idle: **{idle_count}**\n● ⛔️ DoNotDisturb: **{dnd_count}**\n● 💿 Offline: **{offline_count}**"
        channel_count = f"● 🗂️ Total: **{len(server.channels)}**\n● ✏️ Text: **{len(server.text_channels)}**\n● 🗯️ Forums: **{len(server.forum_channels)}**\n● 🔊 Voices: **{len(server.voice_channels)}**"

        embed = disnake.Embed(title="📊 Server Info 📊", color=0x1E90FF,timestamp=datetime.datetime.now())
        if server_icon:
            embed.set_thumbnail(url=server_icon)
        embed.set_footer(
            text=f"Requested information {ctx.author.display_name}"
        )
        embed.add_field(name=f"Server Name: {server_name}", 
                        value=f"**Server ID:** {server_id}\n**Server Owner:** {server_owner}\n**Creation Date:** `{creation_date}`\n**Verification level:** {verific_count}\n**Role Count:** {role_count}", inline=False)

        embed.add_field(name="Member:", value=member_count, inline=True)
        embed.add_field(name="By status:", value=status_count, inline=True)
        embed.add_field(name="Channel:", value=channel_count, inline=True)

        await ctx.reply(embed=embed)
            
def setup(bot: commands.Bot):
    bot.add_cog(Slash_Serverinfo(bot))
    bot.add_cog(NoSlash_Serverinfo(bot))