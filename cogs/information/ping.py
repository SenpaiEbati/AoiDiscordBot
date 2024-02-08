import datetime
import time
import disnake
from disnake.ext import commands

class Slash_Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Функция для расчета задержки (ping) Discord API Gateway
    async def get_gateway_ping(self):
        start_time = time.time()
        gateway_info = await self.bot.http.request(disnake.http.Route('GET', '/gateway/bot'))
        end_time = time.time()
        ping = round((end_time - start_time) * 1000, 2)
        return ping

    # Функция для расчета задержки (ping) Discord API REST
    async def get_rest_ping(self):
        start_time = time.time()
        await self.bot.http.request(disnake.http.Route('GET', '/gateway/bot'))
        end_time = time.time()
        ping = round((end_time - start_time) * 1000, 2)
        return ping

    # Команда для расчета задержки (ping)
    @commands.slash_command()
    async def ping(self, ctx):
        # Задержка (ping) Discord API Gateway
        gateway_ping = await self.get_gateway_ping()

        # Задержка (ping) Discord API REST
        rest_ping = await self.get_rest_ping()

        # Внутренние расчеты задержки для команды ping
        command_ping = round(self.bot.latency * 1000, 2)

        embed = disnake.Embed(color=0x1E90FF,
                              title="🏓 Pong 🏓",
                              description=f"Internal calculations for this command: **{command_ping}ms**\nDiscord API Gateway: **{gateway_ping}ms**\nDiscord API REST: **{rest_ping}ms**",
                              timestamp=datetime.datetime.now())
        embed.set_footer(
            text=f"Requested information {ctx.author.display_name}"
        )
        await ctx.send(embed=embed)
class NoSlash_Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def get_gateway_ping(self):
        start_time = time.time()
        gateway_info = await self.bot.http.request(disnake.http.Route('GET', '/gateway/bot'))
        end_time = time.time()
        ping = round((end_time - start_time) * 1000, 2)
        return ping

    # Функция для расчета задержки (ping) Discord API REST
    async def get_rest_ping(self):
        start_time = time.time()
        await self.bot.http.request(disnake.http.Route('GET', '/gateway/bot'))
        end_time = time.time()
        ping = round((end_time - start_time) * 1000, 2)
        return ping

    @commands.command()
    async def ping(self, ctx):
        # Задержка (ping) Discord API Gateway
        gateway_ping = await self.get_gateway_ping()

        # Задержка (ping) Discord API REST
        rest_ping = await self.get_rest_ping()

        # Внутренние расчеты задержки для команды ping
        command_ping = round(self.bot.latency * 1000, 2)

        embed = disnake.Embed(color=0x1E90FF,
                              title="🏓 Pong 🏓",
                              description=f"Internal calculations for this command: **{command_ping}ms**\nDiscord API Gateway: **{gateway_ping}ms**\nDiscord API REST: **{rest_ping}ms**",
                              timestamp=datetime.datetime.now())
        embed.set_footer(
            text=f"Requested information {ctx.author.display_name}"
        )
        await ctx.reply(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Slash_Ping(bot))
    bot.add_cog(NoSlash_Ping(bot))