import disnake
from disnake.ext import commands
import sqlite3

class LevelUpSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        # Начисление опыта за отправку сообщений
        exp = 1
        self.add_exp(message.author, exp)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: disnake.Member):
        if member.bot:
            return
        # Начисление опыта за активность в голосовых каналах
        exp = 1
        self.add_exp(member, exp)
    
    def add_exp(self, member, exp):
        current_exp = self.get_exp(member)
        current_exp += exp
        self.set_exp(member, current_exp)

        # Проверяем, достиг ли участник нового уровня
        if self.level_up_check(member, current_exp):
            self.level_up(member)

    def get_exp(self, member):
        # Получение опыта участника
        conn = sqlite3.connect('..\MyDiscordBot\dataexp.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE userid = ?', (member.id,))
        user = cursor.fetchone()

        if user is None:
            cursor.execute('INSERT INTO users (username, userid, level, exp) VALUES (?, ?, ?, ?)', (member.name, member.id, 1, 0))
            conn.commit()
            conn.close()
            return 0

        conn.close()
        return user[4]

    def get_level(self, member):
        # Получение уровня участника
        conn = sqlite3.connect('..\MyDiscordBot\dataexp.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE userid = ?', (member.id,))
        user = cursor.fetchone()

        if user is None:
            cursor.execute('INSERT INTO users (username, userid, level, exp) VALUES (?, ?, ?, ?)', (member.name, member.id, 1, 0))
            conn.commit()
            conn.close()
            return 0

        conn.close()
        return user[3]

    def set_exp(self, member, exp):
        # Сохранения опыта участника
        conn = sqlite3.connect('..\MyDiscordBot\dataexp.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET exp = ? WHERE userid = ?', (exp, member.id))
        conn.commit()
        conn.close()
        pass
    
    def set_level(self, member, level):
        # Сохранения уровня участника
        conn = sqlite3.connect('..\MyDiscordBot\dataexp.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET level = ? WHERE userid = ?', (level, member.id))
        conn.commit()
        conn.close()
        pass

    def level_up_check(self, member, exp):
        # Проверяем, достиг ли участник нового уровня
        level = self.get_level(member)
        level_line = (50 * level * level) // 2
        return exp >= level_line  

    def level_up(self, member):
        # Выполняем действия по повышению уровня участника
        newlevel = self.get_level(member) + 1
        self.set_level(member, newlevel)

def setup(bot):
    bot.add_cog(LevelUpSystem(bot))