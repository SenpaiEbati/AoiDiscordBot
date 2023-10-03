import disnake
from disnake.ext import commands

class Slash_UnBan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="With this command you can unban one or more members and give a reason.")
    async def unban(self, ctx, member: disnake.Member, *, reason="-"):
        if ctx.author.guild_permissions.ban_members:
            embed = disnake.Embed(title='❇️ Unban ❇️', color=disnake.Color.green())
            embed.add_field(name='Member', value=member.mention, inline=False)
            embed.add_field(name='Reason', value=reason, inline=False)
            embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)
            
            dm_embed = disnake.Embed(title='❇️ Unban ❇️', color=disnake.Color.green())
            dm_embed.add_field(name='Server', value=ctx.guild.name, inline=False)
            dm_embed.add_field(name='Reason', value=reason, inline=False)
            dm_embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await member.send(embed=dm_embed)

            await member.unban() 
        else:
            await ctx.send("You do not have permission to unban members.")

class NoSlash_UnBan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    

    @commands.command(description="With this command you can unban one or more members and give a reason.")
    async def unban(self, ctx, member: disnake.Member, *, reason="-"):
        if ctx.author.guild_permissions.ban_members:
            embed = disnake.Embed(title='❇️ Unban ❇️', color=disnake.Color.green())
            embed.add_field(name='Member', value=member.mention, inline=False)
            embed.add_field(name='Reason', value=reason, inline=False)
            embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)
            
            dm_embed = disnake.Embed(title='❇️ Unban ❇️', color=disnake.Color.green())
            dm_embed.add_field(name='Server', value=ctx.guild.name, inline=False)
            dm_embed.add_field(name='Reason', value=reason, inline=False)
            dm_embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await member.send(embed=dm_embed)

            await member.unban() 
        else:
            await ctx.send("You do not have permission to unban members.")
        
def setup(bot: commands.Bot):
    bot.add_cog(Slash_UnBan(bot))
    bot.add_cog(NoSlash_UnBan(bot))