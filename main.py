import asyncio
import disnake
from disnake.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()

intents = disnake.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("M.","m."), intents=intents,
                   sync_commands_debug=True,
                   test_guilds = [1152151796870025228,977613521351225354])

bot.load_extensions('cogs\moderation') 
bot.load_extensions('cogs\information') 

@bot.event
async def on_ready():
    print("====The bot is ready!====")

YOUR_BOT_TOKEN = os.environ["YOUR_BOT_TOKEN"]
bot.run(YOUR_BOT_TOKEN)