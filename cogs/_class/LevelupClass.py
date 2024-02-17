import disnake
from disnake.ext import commands
import sqlite3

class LevelUpClass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        # Начисление опыта за отправку сообщений
        exp = 1
        self.add_exp(message, message.author, exp)
        

    @commands.Cog.listener()
    async def on_voice_state_update(self, ctx, member: disnake.Member, before, after):
        if member.bot:
            return
        # Начисление опыта за активность в голосовых каналах
        exp = 1
        self.add_exp(ctx, member, exp)
    
    def add_exp(self, ctx, member, exp):
        current_exp = self.get_exp(ctx, member)
        current_exp += exp
        self.set_exp(ctx, member, current_exp)

        # Проверяем, достиг ли участник нового уровня
        if self.level_up_check(ctx, member, current_exp):
            self.level_up(ctx, member)

    def get_exp(self, ctx, member):
        # Получение опыта участника
        conn = sqlite3.connect('..\MyDiscordBot\dataexp.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE guildid = ? AND userid = ?', (ctx.guild.id, member.id))
        user = cursor.fetchone()

        if user is None:
            cursor.execute('INSERT INTO users (guildid, username, userid, level, exp) VALUES (?, ?, ?, ?, ?)', (ctx.guild.id, member.name, member.id, 1, 0))
            conn.commit()
            conn.close()
            return 0

        conn.close()
        return user[5]

    def get_level(self, ctx, member):
        # Получение уровня участника
        conn = sqlite3.connect('..\MyDiscordBot\dataexp.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE guildid = ? AND userid = ?', (ctx.guild.id, member.id))
        user = cursor.fetchone()

        if user is None:
            cursor.execute('INSERT INTO users (guildid, username, userid, level, exp) VALUES (?, ?, ?, ?, ?)', (ctx.guild.id, member.name, member.id, 1, 0))
            conn.commit()
            conn.close()
            return 0

        conn.close()
        return user[4]

    def set_exp(self, ctx, member, exp):
        # Сохранения опыта участника
        conn = sqlite3.connect('..\MyDiscordBot\dataexp.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET exp = ? WHERE guildid = ? AND userid = ?', (exp, ctx.guild.id, member.id))
        conn.commit()
        conn.close()
        pass
    
    def set_level(self, ctx, member, level):
        # Сохранения уровня участника
        conn = sqlite3.connect('..\MyDiscordBot\dataexp.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET level = ? WHERE guildid = ? AND userid = ?', (level, ctx.guild.id, member.id))
        conn.commit()
        conn.close()
        pass

    def level_up_check(self, ctx, member, exp):
        # Проверяем, достиг ли участник нового уровня
        level = self.get_level(ctx, member)
        level_line = (50 * level * level) // 2
        return exp > level_line  

    def level_up(self, ctx, member):
        # Выполняем действия по повышению уровня участника
        newlevel = self.get_level(ctx, member) + 1
        self.set_level(ctx, member, newlevel)
    
    def get_rank(self, ctx, member):
        conn = sqlite3.connect('..\MyDiscordBot\dataexp.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT (SELECT COUNT(*) FROM users AS u WHERE u.guildid = users.guildid AND u.exp > users.exp) + 1 AS user_rank
            FROM users
            WHERE guildid = ? AND userid = ?
        ''', (ctx.guild.id, member.id))

        result = cursor.fetchone()  # Получаем первую строку результата
        conn.close()
        return result[0]

def setup(bot):
    bot.add_cog(LevelUpClass(bot))