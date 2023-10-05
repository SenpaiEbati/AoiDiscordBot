import disnake
from disnake.ext import commands

class Slash_Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="With this command you can warn one or more members and give a reason.")
    async def warn(self, ctx, member: disnake.Member, *, reason="-"):
        if ctx.author.guild_permissions.kick_members:
            embed = disnake.Embed(title='⚠️ Warning ⚠️', color=disnake.Color(0xFFFF33))
            embed.add_field(name='Member', value=member.mention, inline=False)
            embed.add_field(name='Reason', value=reason, inline=False)
            embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)

            dm_embed = disnake.Embed(title='⚠️ Warning ⚠️', color=disnake.Color(0xFFFF33))
            dm_embed.add_field(name='Server', value=ctx.guild.name, inline=False)
            dm_embed.add_field(name='Reason', value=reason, inline=False)
            dm_embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await member.send(embed=dm_embed)
        else:
            await ctx.send("You do not have permission to issue alerts.")

class NoSlash_Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    

    @commands.command(description="With this command you can warn one or more members and give a reason.")
    async def warn(self, ctx, member: disnake.Member, *, reason="-"):
        if ctx.author.guild_permissions.kick_members:
            embed = disnake.Embed(title='⚠️ Warning ⚠️', color=disnake.Color(0xFFFF33))
            embed.add_field(name='Member', value=member.mention, inline=False)
            embed.add_field(name='Reason', value=reason, inline=False)
            embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)
            
            dm_embed = disnake.Embed(title='⚠️ Warning ⚠️', color=disnake.Color(0xFFFF33))
            dm_embed.add_field(name='Server', value=ctx.guild.name, inline=False)
            dm_embed.add_field(name='Reason', value=reason, inline=False)
            dm_embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await member.send(embed=dm_embed)
        else:
            await ctx.send("You do not have permission to issue alerts.")
        
def setup(bot: commands.Bot):
    bot.add_cog(Slash_Warn(bot))
    bot.add_cog(NoSlash_Warn(bot))