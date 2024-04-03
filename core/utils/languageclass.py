import json
import os
import aiosqlite

class LanguageClass():
    def __init__(self):
        self.get_strings_en = {}
        self.get_strings_ru = {}
    
    async def set_lang(self, ctx, lang):
        async with aiosqlite.connect('..\MyDiscordBot\db\database.db') as conn:
            async with conn.cursor() as cursor:
                await cursor.execute('SELECT * FROM lang_guild WHERE guildid = ?', (ctx.guild.id,))
                conf = await cursor.fetchone()

                if conf is None:
                    await cursor.execute('INSERT INTO lang_guild (guildid, language) VALUES (?, ?)', (ctx.guild.id, lang))
                else:
                    await cursor.execute('UPDATE lang_guild SET language = ? WHERE guildid = ?', (lang, ctx.guild.id))
            
            await conn.commit()

    async def get_lang(self, ctx):
        async with aiosqlite.connect('..\MyDiscordBot\db\database.db') as conn:
            async with conn.cursor() as cursor:
                await cursor.execute('SELECT * FROM lang_guild WHERE guildid = ?', (ctx.guild.id,))
                conf = await cursor.fetchone()

                if conf is None:
                    await cursor.execute('INSERT INTO lang_guild (guildid, language) VALUES (?, ?)', (ctx.guild.id, "en"))
                    await conn.commit()

                    await cursor.execute('SELECT * FROM lang_guild WHERE guildid = ?', (ctx.guild.id,))
                    conf = await cursor.fetchone()
                return conf[2] if conf else None
    
    async def loadjsonmain(self, path):
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

    async def get_strings(self, lang):
        if (lang == "en"):
            return self.get_strings_en.get(lang)
        elif (lang == "ru"):
            return self.get_strings_ru.get(lang)
