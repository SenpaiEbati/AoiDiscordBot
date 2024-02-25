import datetime
import disnake
from disnake.ext import commands
from cogs._class.LanguageClass import LanguageClass

class Slash_InviteFilter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.buttom_onoff_click = 0
        self.link_cleanup = self.bot.get_cog('LinkCleanup').link_cleanup
    @commands.slash_command(name="invitefilter",
                            description="BETA;Removes all discord invitation links/Удаляет все discord ссылки приглашения",
                            default_member_permissions=disnake.Permissions(manage_messages=True))
    async def invitefilter(self,inter: disnake.ApplicationCommandInteraction):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,inter))
        embed = disnake.Embed(title=strings["invitefilter_title"],
                            description=strings["invitefilter_discrip"], 
                            color=disnake.Color(0x1E90FF),
                            timestamp=datetime.datetime.now())
        embed.add_field(name=strings["invitefilter_active"], 
                        value=strings["off"], 
                        inline=False)
        embed.set_footer(
                    text=inter.author.display_name + strings["mod_serv"]
                )
        await inter.response.send_message(embed=embed,
                        components=[
                            disnake.ui.Button(label=strings["on/off"], style=disnake.ButtonStyle.primary, custom_id="On/Off1"),]
                            )
    
    @commands.Cog.listener()
    async def on_button_click(self,inter: disnake.Interaction):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,inter))
        if inter.component.custom_id == "On/Off1":
            onoff = [strings["on"],strings["off"]]
            n = onoff[0]
            if self.buttom_onoff_click == 0:
                n = onoff[0]
                self.buttom_onoff_click = 1
                self.link_cleanup.start()
            else:
                n = onoff[1]
                self.buttom_onoff_click = 0
                self.link_cleanup.cancel()

            embed = disnake.Embed(title=strings["invitefilter_title"],
                                description=strings["invitefilter_discrip"], 
                                color=disnake.Color(0x1E90FF),
                                timestamp=datetime.datetime.now())
            
            embed.insert_field_at(0,name=strings["Active"], 
                        value=f"{n}", 
                        inline=False)
            embed.set_footer(
                    text=inter.author.display_name + strings["mod_serv"]
                )
            await inter.response.edit_message(embed=embed)

class NoSlash_InviteFilter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.buttom_onoff_click = 0
        self.link_cleanup = self.bot.get_cog('LinkCleanup').link_cleanup
    @commands.command(name="invitefilter",
                            default_member_permissions=disnake.Permissions(manage_messages=True))
    async def invitefilter(self,inter: disnake.ApplicationCommandInteraction):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,inter))
        embed = disnake.Embed(title=strings["invitefilter_title"],
                            description=strings["invitefilter_discrip"], 
                            color=disnake.Color(0x1E90FF),
                            timestamp=datetime.datetime.now())
        embed.add_field(name=strings["invitefilter_active"], 
                        value=strings["off"], 
                        inline=False)
        embed.set_footer(
                    text=inter.author.display_name + strings["mod_serv"]
                )
        await inter.reply(embed=embed,
                        components=[
                            disnake.ui.Button(label=strings["on/off"], style=disnake.ButtonStyle.primary, custom_id="On/Off2"),]
                            )
    
    @commands.Cog.listener()
    async def on_button_click(self,inter: disnake.Interaction):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,inter))
        if inter.component.custom_id == "On/Off2":
            onoff = [strings["on"],strings["off"]]
            n = onoff[0]
            if self.buttom_onoff_click == 0:
                n = onoff[0]
                self.buttom_onoff_click = 1
                self.link_cleanup.start()
            else:
                n = onoff[1]
                self.buttom_onoff_click = 0
                self.link_cleanup.cancel()

            embed = disnake.Embed(title=strings["invitefilter_title"],
                                description=strings["invitefilter_discrip"], 
                                color=disnake.Color(0x1E90FF),
                                timestamp=datetime.datetime.now())
            
            embed.insert_field_at(0,name=strings["invitefilter_active"], 
                        value=f"{n}", 
                        inline=False)
            embed.set_footer(
                    text=inter.author.display_name + strings["mod_serv"]
                )
            await inter.response.edit_message(embed=embed)
       
def setup(bot: commands.Bot):
    bot.add_cog(Slash_InviteFilter(bot))
    bot.add_cog(NoSlash_InviteFilter(bot))