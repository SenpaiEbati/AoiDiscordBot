import datetime
import disnake
from disnake.ext import commands
from core.utils import LanguageClass

class Slash_LanguageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.slash_command(name="language",
                            description="Command to change the language from Eng to Rus/Команда для смены языка с английского на русский",
                            default_member_permissions=disnake.Permissions(manage_guild=True))
    async def language(self, inter: disnake.ApplicationCommandInteraction):
        lang = await LanguageClass.get_lang(LanguageClass,inter)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        user = inter.author

        if not inter.author.guild_permissions.manage_guild:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["lang_1"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                text=user.display_name + strings["no_change_conf"]
            )
            await inter.response.send_message(embed=embed)
            return
        
        embed = disnake.Embed(title=strings["lang_3"], 
                              description=strings["lang_4"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_footer(
            text=user.display_name + strings["changed_conf"]
        )

        await inter.response.send_message(
            embed=embed,
            components=[
                disnake.ui.StringSelect(
                    custom_id="fav_language",
                    options=[
                        disnake.SelectOption(label=strings["english"], value="en", emoji="🇬🇧"),
                        disnake.SelectOption(label=strings["russian"], value="ru", emoji="🇷🇺"),
                    ],
                )
            ],
        )

    @commands.Cog.listener()
    async def on_dropdown(self, inter: disnake.MessageInteraction):
        lang = await LanguageClass.get_lang(LanguageClass,inter)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        user = inter.author

        if inter.component.custom_id != "fav_language":
            return
        if not inter.author.guild_permissions.administrator:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["lang_1"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                text=user.display_name + strings["no_changed_conf"]
            )
            await inter.response.send_message(embed=embed)
            return

        await LanguageClass.set_lang(LanguageClass,inter, inter.values[0])
        lang = await LanguageClass.get_lang(LanguageClass,inter)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        

        embed = disnake.Embed(title=strings["lang_3"], 
                              description= strings["lang_5"] + strings["english"] if inter.values[0] == "en" else strings["lang_5"] + strings["russian"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_footer(
            text=user.display_name + strings["changed_conf"]
        )
        await inter.response.edit_message(embed=embed,
                                          components=None)
            
class NoSlash_LanguageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="language",
                      default_member_permissions=disnake.Permissions(manage_guild=True))
    async def language(self, inter: disnake.ApplicationCommandInteraction):
        lang = await LanguageClass.get_lang(LanguageClass,inter)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        user = inter.author
        if not inter.author.guild_permissions.manage_guild:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["lang_1"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                text=user.display_name + strings["no_change_conf"]
            )
            await inter.reply(embed=embed)
            return
        
        embed = disnake.Embed(title=strings["lang_3"], 
                              description=strings["lang_4"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_footer(
            text=user.display_name + strings["changed_conf"]
        )

        await inter.reply(
            embed=embed,
            components=[
                disnake.ui.StringSelect(
                    custom_id="gav_language",
                    options=[
                        disnake.SelectOption(label=strings["english"], value="en", emoji="🇬🇧"),
                        disnake.SelectOption(label=strings["russian"], value="ru", emoji="🇷🇺"),
                    ],
                )
            ],
        )

    @commands.Cog.listener()
    async def on_dropdown(self, inter: disnake.MessageInteraction):
        lang = await LanguageClass.get_lang(LanguageClass,inter)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        user = inter.author
        if inter.component.custom_id != "gav_language":
            return
        if not inter.author.guild_permissions.administrator:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["lang_1"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                text=user.display_name + strings["no_change_conf"]
            )
            await inter.reply(embed=embed)
            return

        
        await LanguageClass.set_lang(LanguageClass,inter, inter.values[0])
        lang = await LanguageClass.get_lang(LanguageClass,inter)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        embed = disnake.Embed(title=strings["lang_3"], 
                              description= strings["lang_5"] + strings["english"] if inter.values[0] == "en" else strings["lang_5"] + strings["russian"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_footer(
            text=user.display_name + strings["changed_conf"]
        )
        await inter.response.edit_message(embed=embed,
                                          components=None)

def setup(bot): 
    bot.add_cog(Slash_LanguageCog(bot))
    bot.add_cog(NoSlash_LanguageCog(bot))