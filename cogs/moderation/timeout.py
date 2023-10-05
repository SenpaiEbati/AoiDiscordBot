import disnake
from disnake.ext import commands

class Slash_Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="With this command you can timeout one or more members and give a reason.")
    async def timeout(self, ctx, member: disnake.Member, *,days=0,hours=0,minutes=0,seconds=0,reason="-"):
        if ctx.author.guild_permissions.moderate_members:
            if max(ctx.author.roles) > max(member.roles):
                if isinstance(days,int) and isinstance(hours,int) and isinstance(minutes,int) and isinstance(seconds,int):
                    if days == hours == minutes == seconds == 0:
                        hours = 6
                        time = hours * 60 * 60 
                    else:
                        time = int(seconds) + int(minutes) * 60 + int(hours) * 60 * 60 + int(days) * 24 * 60 * 60
                
                    embed = disnake.Embed(title='🔒 Timeout 🔒', color=disnake.Color(0xff0000))
                    embed.add_field(name='Member', value=member.mention, inline=False)
                    embed.add_field(name='How much', value=f"{days}d {hours}h {minutes}m {seconds}s", inline=False)
                    embed.add_field(name='Reason', value=reason, inline=False)
                    embed.add_field(name='From', value=ctx.author.mention, inline=False)
                    await ctx.send(embed=embed)
                    
                    dm_embed = disnake.Embed(title='🔒 Timeout 🔒', color=disnake.Color(0xff0000))
                    dm_embed.add_field(name='Server', value=ctx.guild.name, inline=False)
                    dm_embed.add_field(name='How much', value=f"{days}d {hours}h {minutes}m {seconds}s", inline=False)
                    dm_embed.add_field(name='Reason', value=reason, inline=False)
                    dm_embed.add_field(name='From', value=ctx.author.mention, inline=False)
                    await member.send(embed=dm_embed)
                    
                    await member.edit(timeout=time)
                else:
                    await ctx.send("The time you enter must be in the form of numbers, not letters or symbols.")
            else:
                await ctx.send("You do not have permission to timeout members with a higher role.")
        else:
            await ctx.send("You do not have permission to timeout members.")

class NoSlash_Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    

    @commands.command(description="With this command you can timeout one or more members and give a reason.")
    async def timeout(self, ctx, member: disnake.Member, *,days=0,hours=0,minutes=0,seconds=0,reason="-"):
        if ctx.author.guild_permissions.moderate_members:
            if max(ctx.author.roles) > max(member.roles):
                if isinstance(days,int) and isinstance(hours,int) and isinstance(minutes,int) and isinstance(seconds,int):
                    if days == hours == minutes == seconds == 0:
                        hours = 6
                        time = hours * 60 * 60 
                    else:
                        time = int(seconds) + int(minutes) * 60 + int(hours) * 60 * 60 + int(days) * 24 * 60 * 60
                
                    embed = disnake.Embed(title='🔒 Timeout 🔒', color=disnake.Color(0xff0000))
                    embed.add_field(name='Member', value=member.mention, inline=False)
                    embed.add_field(name='How much', value=f"{days}d {hours}h {minutes}m {seconds}s", inline=False)
                    embed.add_field(name='Reason', value=reason, inline=False)
                    embed.add_field(name='From', value=ctx.author.mention, inline=False)
                    await ctx.send(embed=embed)
                    
                    dm_embed = disnake.Embed(title='🔒 Timeout 🔒', color=disnake.Color(0xff0000))
                    dm_embed.add_field(name='Server', value=ctx.guild.name, inline=False)
                    dm_embed.add_field(name='How much', value=f"{days}d {hours}h {minutes}m {seconds}s", inline=False)
                    dm_embed.add_field(name='Reason', value=reason, inline=False)
                    dm_embed.add_field(name='From', value=ctx.author.mention, inline=False)
                    await member.send(embed=dm_embed)
                    
                    await member.edit(timeout=time)
                else:
                    await ctx.send("The time you enter must be in the form of numbers, not letters or symbols.")
            else:
                await ctx.send("You do not have permission to timeout members with a higher role.")
        else:
            await ctx.send("You do not have permission to timeout members.")

def setup(bot: commands.Bot):
    bot.add_cog(Slash_Timeout(bot))
    bot.add_cog(NoSlash_Timeout(bot))