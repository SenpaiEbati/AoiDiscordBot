import disnake
from disnake.ext import commands

class NoSlash_InviteFilter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.buttom_onoff_click = 0
        self.link_cleanup = self.bot.get_cog('LinkCleanup').link_cleanup
    @commands.command(description="With this command you can link clear.")
    async def invitefilter(self,inter: disnake.ApplicationCommandInteraction):
        embed = disnake.Embed(title='✉️ Invite Filter ✉️',
                            description="The bot can automatically block messages that contain links to other Discord servers.\n This function ignores users with administrator permissions", 
                            color=disnake.Color(0x1E90FF))
        embed.add_field(name='Active', 
                        value=f"🔴 Off", 
                        inline=False)
        await inter.send(embed=embed,
                        components=[
                            disnake.ui.Button(label="On/Off", style=disnake.ButtonStyle.primary, custom_id="On/Off"),]
                            )
    
    @commands.Cog.listener()
    async def on_button_click(self,inter: disnake.Interaction):
        if inter.component.custom_id == "On/Off":
            onoff = ["🟢 On","🔴 Off"]
            n = onoff[0]
            if self.buttom_onoff_click == 0:
                n = onoff[0]
                self.buttom_onoff_click = 1
                self.link_cleanup.start()
            else:
                n = onoff[1]
                self.buttom_onoff_click = 0
                self.link_cleanup.cancel()

            embed = disnake.Embed(title='✉️ Invite Filter ✉️',
                                description="The bot can automatically block messages that contain links to other Discord servers.\n This function ignores users with administrator permissions", 
                                color=disnake.Color(0x1E90FF))
            
            embed.insert_field_at(0,name='Active', 
                        value=f"{n}", 
                        inline=False)
            await inter.response.edit_message(embed=embed)
       
def setup(bot: commands.Bot):
    bot.add_cog(NoSlash_InviteFilter(bot))