import disnake
from disnake.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot()


@bot.event
async def on_ready():
    print("Бот готов!")

bot.load_extension("cogs.ping")  # Примечание: расширение .py указывать не нужно




YOUR_BOT_TOKEN = os.environ["YOUR_BOT_TOKEN"]
bot.run(YOUR_BOT_TOKEN)