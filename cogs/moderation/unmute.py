from asyncio import sleep
import disnake
from disnake.ext import commands

class Slash_UnMute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="unmute",
                            description="With this command you can unmute one or more members and give a reason.")
    async def unmute(self, ctx, member: disnake.Member, *, reason="-"):
        if ctx.author.guild_permissions.mute_members:
            embed = disnake.Embed(title='🎙 Unmute 🎙', color=disnake.Color(0x32CD32))
            embed.add_field(name='Member', value=member.mention, inline=False)
            embed.add_field(name='Reason', value=reason, inline=False)
            embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)

            await member.edit(mute=False)
        else:
            embed = disnake.Embed(title='❌ NO RIGHTS ❌', color=disnake.Color(0xff0000))
            val = "You do not have permission to unmute members."
            embed.add_field(name="",value=val, inline=False)
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)

class NoSlash_UnMute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    

    @commands.command(name="unmute",
                      description="With this command you can unmute one or more members and give a reason.")
    async def unmute(self, ctx, member: disnake.Member, *, reason="-"):
        if ctx.author.guild_permissions.mute_members:
            embed = disnake.Embed(title='🎙 Unmute 🎙', color=disnake.Color(0x32CD32))
            embed.add_field(name='Member', value=member.mention, inline=False)
            embed.add_field(name='Reason', value=reason, inline=False)
            embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await ctx.reply(embed=embed)

            await member.edit(mute=False)
        else:
            embed = disnake.Embed(title='❌ NO RIGHTS ❌', color=disnake.Color(0xff0000))
            val = "You do not have permission to unmute members."
            embed.add_field(name="",value=val, inline=False)
            await ctx.reply(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)

        
def setup(bot: commands.Bot):
    bot.add_cog(Slash_UnMute(bot))
    bot.add_cog(NoSlash_UnMute(bot))