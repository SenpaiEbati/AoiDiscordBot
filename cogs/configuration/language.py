import datetime
import disnake
from disnake.ext import commands
from cogs._class.LanguageClass import LanguageClass

class Slash_LanguageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def language(self, inter: disnake.ApplicationCommandInteraction):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,inter))

        user = inter.author

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
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass, inter))

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

        LanguageClass.set_lang(LanguageClass,inter, inter.values[0])
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass, inter))

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

    @commands.command()
    async def language(self, inter: disnake.ApplicationCommandInteraction):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,inter))
        user = inter.author
        if not inter.author.guild_permissions.administrator:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["lang_1"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                text=user.display_name + strings["no changed conf"]
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
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,inter))
        user = inter.author
        if inter.component.custom_id != "gav_language":
            return
        if not inter.author.guild_permissions.administrator:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["lang_1"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                text=user.display_name + strings["no_changed_conf"]
            )
            await inter.reply(embed=embed)
            return

        
        LanguageClass.set_lang(LanguageClass,inter, inter.values[0])
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,inter))
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