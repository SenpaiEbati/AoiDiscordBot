import json
import os
import sqlite3
import disnake
from disnake.ext import commands

class LanguageClass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.get_strings_en = {}
        self.get_strings_ru = {}
    
    def set_lang(self, ctx, lang):
        conn = sqlite3.connect('..\MyDiscordBot\data\dataconfbot.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM confbot WHERE guildid = ?', (ctx.guild.id,))
        conf = cursor.fetchone()

        if conf is None:
            cursor.execute('INSERT INTO confbot (guildid, language) VALUES (?, ?)', (ctx.guild.id, lang))
        else:
            cursor.execute('UPDATE confbot SET language = ? WHERE guildid = ?', (lang, ctx.guild.id))
        
        conn.commit()
        conn.close()

        pass

    def get_lang(self, ctx):
        conn = sqlite3.connect('..\MyDiscordBot\data\dataconfbot.db')
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
    
    def loadjsonmain(self, path):
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as file:
                self.getsetjson = json.load(file)
        elif os.path.isdir(path):
            for filename in os.listdir(path):
                file_path = os.path.join(path, filename)
                if filename.endswith(".json") and os.path.isfile(file_path):
                    name, ext = os.path.splitext(filename)
                    if (name == "en"):
                        with open(file_path, "r", encoding="utf-8") as file:
                            self.get_strings_en = json.load(file)
                    elif (name == "ru"):
                        with open(file_path, "r", encoding="utf-8") as file:
                            self.get_strings_ru = json.load(file)
        else:
            raise RuntimeError("Invalid path: {}".format(path))

    def get_strings(self, lang):
        if (lang == "en"):
            return self.get_strings_en.get(lang)
        elif (lang == "ru"):
            return self.get_strings_ru.get(lang)
    
def setup(bot): 
    bot.add_cog(LanguageClass(bot))