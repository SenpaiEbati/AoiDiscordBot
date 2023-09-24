import asyncio
import disnake
from disnake.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot("M.", 
                   sync_commands_debug=True,
                   test_guilds = [1152151796870025228])

@bot.event
async def on_ready():
    print("====The bot is ready!====")

bot.load_extensions('cogs') 

YOUR_BOT_TOKEN = os.environ["YOUR_BOT_TOKEN"]
bot.run(YOUR_BOT_TOKEN)