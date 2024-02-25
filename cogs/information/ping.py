import datetime
import time
import disnake
from disnake.ext import commands
from cogs._class.LanguageClass import LanguageClass

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
    @commands.slash_command(name="ping",
                            description="Discord API Gateway/REST ping and commands/Пинг Discord API Gateway/REST и команды")
    async def ping(self, ctx):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))
        # Задержка (ping) Discord API Gateway
        gateway_ping = await self.get_gateway_ping()

        # Задержка (ping) Discord API REST
        rest_ping = await self.get_rest_ping()

        # Внутренние расчеты задержки для команды ping
        command_ping = round(self.bot.latency * 10, 2)

        embed = disnake.Embed(color=0x1E90FF,
                              title=strings["ping_1"],
                              description=strings["ping_2"] + f"{command_ping}" + strings["pingms"] + "\n" + 
                              strings["ping_3"] + f"{gateway_ping}" + strings["pingms"] + "\n" + 
                              strings["ping_4"] + f"{rest_ping}" + strings["pingms"],
                              timestamp=datetime.datetime.now())
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
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

    @commands.command(name="ping")
    async def ping(self, ctx):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))
        # Задержка (ping) Discord API Gateway
        gateway_ping = await self.get_gateway_ping()

        # Задержка (ping) Discord API REST
        rest_ping = await self.get_rest_ping()

        # Внутренние расчеты задержки для команды ping
        command_ping = round(self.bot.latency * 10, 2)

        embed = disnake.Embed(color=0x1E90FF,
                              title=strings["ping_1"],
                              description=strings["ping_2"] + f"{command_ping}" + strings["pingms"] + "\n" + 
                              strings["ping_3"] + f"{gateway_ping}" + strings["pingms"] + "\n" + 
                              strings["ping_4"] + f"{rest_ping}" + strings["pingms"],
                              timestamp=datetime.datetime.now())
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
        )
        await ctx.reply(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Slash_Ping(bot))
    bot.add_cog(NoSlash_Ping(bot))