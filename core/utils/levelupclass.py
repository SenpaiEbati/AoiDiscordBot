import datetime
import aiosqlite
import disnake
from .utils import get_colour
from .languageclass import LanguageClass

class LevelUpClass():
    async def add_exp(self, ctx, member, exp):
        current_exp = await self.get_exp(self, ctx, member)
        current_exp += exp
        await self.set_exp(self, ctx, member, current_exp)

        # Проверяем, достиг ли участник нового уровня
        if await self.level_up_check(self, ctx, member, current_exp):
            await self.level_up(self, ctx, member)

            # lang = await LanguageClass.get_lang(LanguageClass,ctx)
            # strings = await LanguageClass.get_strings(LanguageClass,lang)

            # level = await self.get_level(self,ctx,member)
            # rank = await self.get_rank(self,ctx,member)
            # nowlinelevel = (50 * level * level) // 2

            # embed = disnake.Embed(title=strings["next_level"],
            #                         description=strings["next_level_desc1"]+f"{level}\n"+strings["next_level_desc2"]+f"{rank}\n"+strings["next_level_desc3"]+f"{current_exp}\n"+strings["next_level_desc4"]+f"{nowlinelevel}",
            #                         color=get_colour("blue"),
            #                         timestamp=datetime.datetime.now())
            # embed.set_thumbnail(url=member.display_avatar)
            # embed.set_footer(
            #     text=ctx.author.display_name + strings["next_leve_footer"]
            # )
            # await ctx.channel.send(member.mention, embed=embed)
            

    async def get_exp(self, ctx, member):
        # Получение опыта участника
        async with aiosqlite.connect('..\data\database.db') as conn:
            cursor = await conn.cursor()
            await cursor.execute('SELECT * FROM level WHERE guildid = ? AND userid = ?', (ctx.guild.id, member.id))
            user = await cursor.fetchone()

            if user is None:
                await cursor.execute('INSERT INTO level (guildid, username, userid, level, exp) VALUES (?, ?, ?, ?, ?)', (ctx.guild.id, member.name, member.id, 1, 0))
                await conn.commit()
                return 0

            return user[5]

    async def get_level(self, ctx, member):
        # Получение уровня участника
        async with aiosqlite.connect('..\data\database.db') as conn:
            cursor = await conn.cursor()
            await cursor.execute('SELECT * FROM level WHERE guildid = ? AND userid = ?', (ctx.guild.id, member.id))
            user = await cursor.fetchone()

            if user is None:
                await cursor.execute('INSERT INTO level (guildid, username, userid, level, exp) VALUES (?, ?, ?, ?, ?)', (ctx.guild.id, member.name, member.id, 1, 0))
                await conn.commit()
                return 0

            return user[4]

    async def set_exp(self, ctx, member, exp):
        # Сохранение опыта участника
        async with aiosqlite.connect('..\data\database.db') as conn:
            cursor = await conn.cursor()
            await cursor.execute('UPDATE level SET exp = ? WHERE guildid = ? AND userid = ?', (exp, ctx.guild.id, member.id))
            await conn.commit()

    async def set_level(self, ctx, member, level):
        # Сохранение уровня участника
        async with aiosqlite.connect('..\data\database.db') as conn:
            cursor = await conn.cursor()
            await cursor.execute('UPDATE level SET level = ? WHERE guildid = ? AND userid = ?', (level, ctx.guild.id, member.id))
            await conn.commit()

    async def level_up_check(self, ctx, member, exp):
        # Проверяем, достиг ли участник нового уровня
        level = await self.get_level(self, ctx, member)
        level_line = (50 * level * level) // 2
        return exp > level_line  

    async def level_up(self, ctx, member):
        # Выполняем действия по повышению уровня участника
        newlevel = await self.get_level(self, ctx, member) + 1
        await self.set_level(self, ctx, member, newlevel)
    
    async def get_rank(self, ctx, member):
        async with aiosqlite.connect('..\data\database.db') as conn:
            cursor = await conn.cursor()
            await cursor.execute('''
                SELECT (SELECT COUNT(*) FROM level AS u WHERE u.guildid = level.guildid AND u.exp > level.exp) + 1 AS user_rank
                FROM level
                WHERE guildid = ? AND userid = ?
            ''', (ctx.guild.id, member.id))

            result = await cursor.fetchone()  # Получаем первую строку результата
            return result[0]
