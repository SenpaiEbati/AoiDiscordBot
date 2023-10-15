import disnake
from disnake.ext import commands,tasks

class LinkCleanup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.link_cleanup.stop()

    def cog_unload(self):
        self.link_cleanup.cancel()

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear_links(self, ctx):
        def is_link(message):
            return 'discord.gg' in message.content

        deleted = await ctx.channel.purge(limit=100, check=is_link)
        await ctx.send(f'Deleted {len(deleted)} messages with invite links.')

    @tasks.loop(seconds=15)
    async def link_cleanup(self):
        guilds = self.bot.guilds

        for guild in guilds:
            for channel in guild.text_channels:
                await channel.purge(limit=100, check=lambda m: 'discord.gg' in m.content)

    @link_cleanup.before_loop
    async def before_link_cleanup(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(LinkCleanup(bot))