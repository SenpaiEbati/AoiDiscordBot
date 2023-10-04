import disnake
from disnake.ext import commands

class Slash_Deafen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="With this command you can deafen one or more members and give a reason.")
    async def deafen(self, ctx, member: disnake.Member, *, reason="-"):
        if ctx.author.guild_permissions.moderate_members:
            embed = disnake.Embed(title='🎧 Deafen 🎧', color=disnake.Color.yellow())
            embed.add_field(name='Member', value=member.mention, inline=False)
            embed.add_field(name='Reason', value=reason, inline=False)
            embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)
            
            await member.edit(deafen=True)
        else:
            await ctx.send("You do not have permission to deafen members.")

class NoSlash_Deafen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    

    @commands.command(description="With this command you can deafen one or more members and give a reason.")
    async def deafen(self, ctx, member: disnake.Member, *, reason="-"):
        if ctx.author.guild_permissions.moderate_members:
            embed = disnake.Embed(title='🎧 Deafen 🎧', color=disnake.Color.yellow())
            embed.add_field(name='Member', value=member.mention, inline=False)
            embed.add_field(name='Reason', value=reason, inline=False)
            embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)
            
            await member.edit(deafen=True)
        else:
            await ctx.send("You do not have permission to deafen members.")
        
def setup(bot: commands.Bot):
    bot.add_cog(Slash_Deafen(bot))
    bot.add_cog(NoSlash_Deafen(bot))