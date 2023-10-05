import disnake
from disnake.ext import commands

class Slash_UnDeafen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="With this command you can undeafen one or more members and give a reason.")
    async def undeafen(self, ctx, member: disnake.Member, *, reason="-"):
        if ctx.author.guild_permissions.deafen_members:
            embed = disnake.Embed(title='🎧 Undeafen 🎧', color=disnake.Color(0x32CD32))
            embed.add_field(name='Member', value=member.mention, inline=False)
            embed.add_field(name='Reason', value=reason, inline=False)
            embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)

            await member.edit(deafen=False)
        else:
            await ctx.send("You do not have permission to undeafen members.")

class NoSlash_UnDeafen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    

    @commands.command(description="With this command you can deafen one or more members and give a reason.")
    async def undeafen(self, ctx, member: disnake.Member, *, reason="-"):
        if ctx.author.guild_permissions.deafen_members:
            embed = disnake.Embed(title='🎧 Undeafen 🎧', color=disnake.Color(0x32CD32))
            embed.add_field(name='Member', value=member.mention, inline=False)
            embed.add_field(name='Reason', value=reason, inline=False)
            embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)
            
            await member.edit(deafen=False)
        else:
            await ctx.send("You do not have permission to undeafen members.")
        
def setup(bot: commands.Bot):
    bot.add_cog(Slash_UnDeafen(bot))
    bot.add_cog(NoSlash_UnDeafen(bot))