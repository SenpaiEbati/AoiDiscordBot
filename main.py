import asyncio
import disnake
from disnake.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()

intents = disnake.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("M."), intents=intents,
                   sync_commands_debug=True,
                   test_guilds = [1152151796870025228])

@bot.event
async def on_ready():
    print("====The bot is ready!====")

bot.load_extensions('cogs') 

YOUR_BOT_TOKEN = os.environ["YOUR_BOT_TOKEN"]
bot.run(YOUR_BOT_TOKEN)