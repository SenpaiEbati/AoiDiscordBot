import disnake
from disnake.ext import commands

class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="With this command you can warn one or more members and give a reason.")
    async def warn(self, ctx, member: disnake.Member, *, reason: str):
        # Проверяем, имеет ли пользователь право выдавать предупреждения
        if ctx.author.guild_permissions.kick_members:
            # Создаем и отправляем сообщение с предупреждением
            embed = disnake.Embed(title='🚨 Warning 🚨', color=disnake.Color.red())
            embed.add_field(name='Member', value=member.mention, inline=False)
            embed.add_field(name='Reason', value=reason, inline=False)
            embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)

            # Отправляем пользователю личное сообщение с предупреждением в формате Embed
            dm_embed = disnake.Embed(title='🚨 Warning 🚨', color=disnake.Color.red())
            dm_embed.add_field(name='Server', value=ctx.guild.name, inline=False)
            dm_embed.add_field(name='Reason', value=reason, inline=False)
            dm_embed.add_field(name='From', value=ctx.author.mention, inline=False)
            await member.send(embed=dm_embed)

        else:
            await ctx.send("You do not have permission to issue alerts.")

def setup(bot: commands.Bot):
    bot.add_cog(Warn(bot))



