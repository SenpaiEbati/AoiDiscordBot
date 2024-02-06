import disnake
from disnake.ext import commands

class Slash_Add(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command()
    async def add(self,ctx: disnake.ApplicationCommandInteraction):
        embed = disnake.Embed(title="🔗 Add Aoi青",
                              color=0x1E90FF)
        embed.add_field(name="",value="Thanks for your interest! 💋")
        await ctx.response.send_message(embed=embed,
                        components=[
                            disnake.ui.Button(label="Add Aoi青 to Your Server ",url="https://discord.com/api/oauth2/authorize?client_id=1152289596969861203&permissions=8&scope=bot"),]
                            )

class NoSlash_Add(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def add(self,ctx: disnake.ApplicationCommandInteraction):
        embed = disnake.Embed(title="🔗 Add Aoi青",
                              color=0x1E90FF)
        embed.add_field(name="",value="Thanks for your interest! 💋")
        await ctx.reply(embed=embed,
                        components=[
                            disnake.ui.Button(label="Add Aoi青 to Your Server ",url="https://discord.com/api/oauth2/authorize?client_id=1152289596969861203&permissions=8&scope=bot"),]
                            )

def setup(bot: commands.Bot):
    bot.add_cog(Slash_Add(bot))
    bot.add_cog(NoSlash_Add(bot))