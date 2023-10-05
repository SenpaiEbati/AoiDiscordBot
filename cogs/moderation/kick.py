import disnake
from disnake.ext import commands

class Slash_Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="With this command you can kick one or more members and give a reason.")
    async def kick(self, ctx, member: disnake.Member, *, reason="-"):
        if ctx.author == member:
            await ctx.send("You ebobo?")
        elif ctx.author.guild_permissions.kick_members:
            embed = disnake.Embed(title='🚪 Kick 🚪', color=disnake.Color(0xff0000))
            embed.add_field(name='Member', value=member.mention, inline=False)
            embed.add_field(name='Reason', value=reason, inline=False)
            embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)
            
            dm_embed = disnake.Embed(title='🚪 Kick 🚪', color=disnake.Color(0xff0000))
            dm_embed.add_field(name='Server', value=ctx.guild.name, inline=False)
            dm_embed.add_field(name='Reason', value=reason, inline=False)
            dm_embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await member.send(embed=dm_embed)

            await member.kick()
        else:
            await ctx.send("You do not have permission to kick members.")

class NoSlash_Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    

    @commands.command(description="With this command you can kick one or more members and give a reason.")
    async def kick(self, ctx, member: disnake.Member, *, reason="-"):
        if ctx.author == member:
            await ctx.send("You ebobo?")
        elif ctx.author.guild_permissions.kick_members:
            embed = disnake.Embed(title='🚪 Kick 🚪', color=disnake.Color(0xff0000))
            embed.add_field(name='Member', value=member.mention, inline=False)
            embed.add_field(name='Reason', value=reason, inline=False)
            embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)
            
            dm_embed = disnake.Embed(title='🚪 Kick 🚪', color=disnake.Color(0xff0000))
            dm_embed.add_field(name='Server', value=ctx.guild.name, inline=False)
            dm_embed.add_field(name='Reason', value=reason, inline=False)
            dm_embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await member.send(embed=dm_embed)

            await member.kick() 
        else:
            await ctx.send("You do not have permission to kick members.")
        
def setup(bot: commands.Bot):
    bot.add_cog(Slash_Kick(bot))
    bot.add_cog(NoSlash_Kick(bot))