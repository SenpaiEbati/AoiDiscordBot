import datetime
import json
import os
import sqlite3
import disnake
from disnake.ext import commands

class LanguageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.getsetjson = {}

    @commands.slash_command()
    async def language(self, inter: disnake.ApplicationCommandInteraction):
        LanguageCog.loadjson2(LanguageCog,inter,"..\MyDiscordBot\localizations")
        strings = LanguageCog.get_strings(LanguageCog,LanguageCog.get_lang(LanguageCog,inter))
        user = inter.author
        if not inter.author.guild_permissions.administrator:
            embed = disnake.Embed(title=strings["no rights"], 
                                  description=strings["lang_1"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                text=user.display_name + strings["no changed conf"]
            )
            await inter.response.send_message(embed=embed)
            return
        
        embed = disnake.Embed(title=strings["lang_3"], 
                              description=strings["lang_4"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_footer(
            text=user.display_name + strings["changed conf"]
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
        LanguageCog.loadjson2(LanguageCog,inter,"..\MyDiscordBot\localizations")
        strings = LanguageCog.get_strings(LanguageCog,LanguageCog.get_lang(LanguageCog,inter))
        user = inter.author
        if inter.component.custom_id != "fav_language":
            return
        if not inter.author.guild_permissions.administrator:
            embed = disnake.Embed(title=strings["no rights"], 
                                  description=strings["lang_1"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                text=user.display_name + strings["no changed conf"]
            )
            await inter.response.send_message(embed=embed)
            return

        conn = sqlite3.connect('..\MyDiscordBot\dataconfbot.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM confbot WHERE guildid = ?', (inter.guild.id,))
        conf = cursor.fetchone()

        if conf is None:
            cursor.execute('INSERT INTO confbot (guildid, language) VALUES (?, ?)', (inter.guild.id, inter.values[0]))
            conn.commit()
            conn.close()
        else:
            cursor.execute('UPDATE confbot SET language = ? WHERE guildid = ?', (inter.values[0], inter.guild.id))
            conn.commit()
            conn.close()

        LanguageCog.loadjson2(LanguageCog,inter,"..\MyDiscordBot\localizations")
        strings = LanguageCog.get_strings(LanguageCog,LanguageCog.get_lang(LanguageCog,inter))
        embed = disnake.Embed(title=strings["lang_3"], 
                              description= strings["lang_5"] + strings["english"] if inter.values[0] == "en" else strings["lang_5"] + strings["russian"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_footer(
            text=user.display_name + strings["changed conf"]
        )
        await inter.response.edit_message(embed=embed,
                                          components=None)
   
    def get_lang(self, ctx):
        conn = sqlite3.connect('..\MyDiscordBot\dataconfbot.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM confbot WHERE guildid = ?', (ctx.guild.id,))
        conf = cursor.fetchone()

        if conf is None:
            cursor.execute('INSERT INTO confbot (guildid, language) VALUES (?, ?)', (ctx.guild.id, "ru"))
            conn.commit()

            cursor.execute('SELECT * FROM confbot WHERE guildid = ?', (ctx.guild.id,))
            conf = cursor.fetchone()
            conn.close()
        else:
            conn.close()

        return conf[2]
            
    def loadjson2(self, ctx, path):
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as file:
                self.getsetjson = json.load(file)
        elif os.path.isdir(path):
            for filename in os.listdir(path):
                file_path = os.path.join(path, filename)
                if filename.endswith(".json") and os.path.isfile(file_path):
                    name, ext = os.path.splitext(filename)
                    if (name == LanguageCog.get_lang(self,ctx)):
                        with open(file_path, "r", encoding="utf-8") as file:
                            self.getsetjson = json.load(file)
        else:
            raise RuntimeError("Invalid path: {}".format(path))
    
    def get_strings(self, lang):
        return self.getsetjson.get(lang)

class NoSlash_LanguageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def language(self, inter: disnake.ApplicationCommandInteraction):
        LanguageCog.loadjson2(LanguageCog,inter,"..\MyDiscordBot\localizations")
        strings = LanguageCog.get_strings(LanguageCog,LanguageCog.get_lang(LanguageCog,inter))
        user = inter.author
        if not inter.author.guild_permissions.administrator:
            embed = disnake.Embed(title=strings["no rights"], 
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
            text=user.display_name + strings["changed conf"]
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
        LanguageCog.loadjson2(LanguageCog,inter,"..\MyDiscordBot\localizations")
        strings = LanguageCog.get_strings(LanguageCog,LanguageCog.get_lang(LanguageCog,inter))
        user = inter.author
        if inter.component.custom_id != "gav_language":
            return
        if not inter.author.guild_permissions.administrator:
            embed = disnake.Embed(title=strings["no rights"], 
                                  description=strings["lang_1"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.datetime.now())
            embed.set_footer(
                text=user.display_name + strings["no changed conf"]
            )
            await inter.reply(embed=embed)
            return

        conn = sqlite3.connect('..\MyDiscordBot\dataconfbot.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM confbot WHERE guildid = ?', (inter.guild.id,))
        conf = cursor.fetchone()

        if conf is None:
            cursor.execute('INSERT INTO confbot (guildid, language) VALUES (?, ?)', (inter.guild.id, inter.values[0]))
            conn.commit()
            conn.close()
        else:
            cursor.execute('UPDATE confbot SET language = ? WHERE guildid = ?', (inter.values[0], inter.guild.id))
            conn.commit()
            conn.close()

        LanguageCog.loadjson2(LanguageCog,inter,"..\MyDiscordBot\localizations")
        strings = LanguageCog.get_strings(LanguageCog,LanguageCog.get_lang(LanguageCog,inter))
        embed = disnake.Embed(title=strings["lang_3"], 
                              description= strings["lang_5"] + strings["english"] if inter.values[0] == "en" else strings["lang_5"] + strings["russian"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_footer(
            text=user.display_name + strings["changed conf"]
        )
        await inter.response.edit_message(embed=embed,
                                          components=None)

def setup(bot): 
    bot.add_cog(LanguageCog(bot))
    bot.add_cog(NoSlash_LanguageCog(bot))