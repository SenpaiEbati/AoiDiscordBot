import disnake
from disnake.ext import commands

class Slash_UnTimeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="With this command you can remove timeout one or more members and give a reason.")
    async def untimeout(self, ctx, member: disnake.Member, *, reason="-"):
        if ctx.author.guild_permissions.moderate_members:
            if max(ctx.author.roles) > max(member.roles):
                embed = disnake.Embed(title='🔓 Timeout 🔓\n⠀⠀removed', color=disnake.Color(0x32CD32))
                embed.add_field(name='Member', value=member.mention, inline=False)
                embed.add_field(name='Reason', value=reason, inline=False)
                embed.add_field(name='From', value=ctx.author.mention, inline=False)
                await ctx.send(embed=embed)
                
                dm_embed = disnake.Embed(title='🔓 Timeout 🔓\n⠀⠀removed', color=disnake.Color(0x32CD32))
                dm_embed.add_field(name='Server', value=ctx.guild.name, inline=False)
                dm_embed.add_field(name='Reason', value=reason, inline=False)
                dm_embed.add_field(name='From', value=ctx.author.mention, inline=False)
                await member.send(embed=dm_embed)

                await member.edit(timeout=None)
            else:
                await ctx.send("You do not have permission to remove timeout members with a higher role.")
        else:
            await ctx.send("You do not have permission to remove timeout members.")

class NoSlash_UnTimeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    

    @commands.command(description="With this command you can timeout one or more members and give a reason.")
    async def untimeout(self, ctx, member: disnake.Member, *, reason="-"):
        if ctx.author.guild_permissions.moderate_members:
            if max(ctx.author.roles) > max(member.roles):
                embed = disnake.Embed(title='🔓 Timeout 🔓\n⠀⠀removed', color=disnake.Color(0x32CD32))
                embed.add_field(name='Member', value=member.mention, inline=False)
                embed.add_field(name='Reason', value=reason, inline=False)
                embed.add_field(name='From', value=ctx.author.mention, inline=False)
                await ctx.send(embed=embed)
                
                dm_embed = disnake.Embed(title='🔓 Timeout 🔓\n⠀⠀removed', color=disnake.Color(0x32CD32))
                dm_embed.add_field(name='Server', value=ctx.guild.name, inline=False)
                dm_embed.add_field(name='Reason', value=reason, inline=False)
                dm_embed.add_field(name='From', value=ctx.author.mention, inline=False)
                await member.send(embed=dm_embed)

                await member.edit(timeout=None)
            else:
                await ctx.send("You do not have permission to remove timeout members with a higher role.")
        else:
            await ctx.send("You do not have permission to remove timeout members.")

def setup(bot: commands.Bot):
    bot.add_cog(Slash_UnTimeout(bot))
    bot.add_cog(NoSlash_UnTimeout(bot))