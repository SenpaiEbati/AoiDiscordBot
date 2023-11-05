from asyncio import sleep
import disnake
from disnake.ext import commands

class Slash_Deafen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="With this command you can deafen one or more members and give a reason.")
    async def deafen(self, ctx, member: disnake.Member, *, reason="-"):
        if ctx.author.guild_permissions.deafen_members:
            embed = disnake.Embed(title='🎧 Deafen 🎧', color=disnake.Color(0xFFFF33))
            embed.add_field(name='Member', value=member.mention, inline=False)
            embed.add_field(name='Reason', value=reason, inline=False)
            embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)
            
            await member.edit(deafen=True)
        else:
            embed = disnake.Embed(title='❌ NO RIGHTS ❌', color=disnake.Color(0xff0000))
            val = "You do not have permission to deafen members."
            embed.add_field(name="",value=val, inline=False)
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)

class NoSlash_Deafen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    

    @commands.command(description="With this command you can deafen one or more members and give a reason.")
    async def deafen(self, ctx, member: disnake.Member, *, reason="-"):
        if ctx.author.guild_permissions.deafen_members:
            embed = disnake.Embed(title='🎧 Deafen 🎧', color=disnake.Color(0xFFFF33))
            embed.add_field(name='Member', value=member.mention, inline=False)
            embed.add_field(name='Reason', value=reason, inline=False)
            embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)
            
            await member.edit(deafen=True)
        else:
            embed = disnake.Embed(title='❌ NO RIGHTS ❌', color=disnake.Color(0xff0000))
            val = "You do not have permission to deafen members."
            embed.add_field(name="",value=val, inline=False)
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
        
def setup(bot: commands.Bot):
    bot.add_cog(Slash_Deafen(bot))
    bot.add_cog(NoSlash_Deafen(bot))