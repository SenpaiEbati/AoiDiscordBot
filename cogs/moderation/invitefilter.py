import disnake
from disnake.ext import commands

class Slash_InviteFilter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(description="With this command you can clear message.")
    async def invitefilter(self,inter: disnake.ApplicationCommandInteraction):
        on = "🟢 On"
        off = "🔴 Off"
        embed = disnake.Embed(title='✉️ Invite Filter ✉️',
                            description="The bot can automatically block messages that contain links to other Discord servers.\n This function ignores users with administrator permissions", 
                            color=disnake.Color(0xffffff))
        embed.add_field(name='Active⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Excluded Users⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Excluded Channels', 
                        value=f"{off}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀<Not Set>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀<Not Set>", 
                        inline=False)
        embed.add_field(name="",value="",inline=False)
        embed.add_field(name='Log Recievers⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Server Link Action', 
                        value=f"<Not Set>⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Delete Message + Warn", 
                        inline=False)
        await inter.response.send_message(embed=embed,
                        components=[
                            disnake.ui.Button(label="On/Off", style=disnake.ButtonStyle.primary, custom_id="On/Off"),
                            disnake.ui.Button(label="Excluded Users", style=disnake.ButtonStyle.primary, custom_id="exc users"),
                            disnake.ui.Button(label="Excluded Channels", style=disnake.ButtonStyle.primary, custom_id="exc channel"),
                            disnake.ui.Button(label="Log Recievers", style=disnake.ButtonStyle.primary, custom_id="log"),
                            disnake.ui.Button(label="Server Link Action", style=disnake.ButtonStyle.primary, custom_id="server")]
                            )
    async def help_listener(inter: disnake.MessageInteraction):
        if inter.component.custom_id not in ["On/Off", "exc users","exc channel","log","server"]:
            # We filter out any other button presses except
            # the components we wish to process.
            return

        if inter.component.custom_id == "On/Off":
            await inter.response.send_message("On/Off")

        elif inter.component.custom_id == "exc users":
            await inter.response.send_message("exc users")

        elif inter.component.custom_id == "exc channel":
            await inter.response.send_message("exc channel")

        elif inter.component.custom_id == "log":
            await inter.response.send_message("log")

        elif inter.component.custom_id == "server":
            await inter.response.send_message("server")


class NoSlash_InviteFilter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(description="With this command you can clear message.")
    async def invitefilter(self,ctx):
        if ctx.author.guild_permissions.manage_messages:
            wddw= 1
        else:
            await ctx.send("You do not have permission to clear message.")
        
            
def setup(bot: commands.Bot):
    bot.add_cog(Slash_InviteFilter(bot))
    bot.add_cog(NoSlash_InviteFilter(bot))