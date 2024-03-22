from os import environ
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = environ["BOT_TOKEN"]

THUMBS_UP = "👍"
THUMBS_DOWN = "👎"

LOCATION_EMOJIS = {
    "fastbackwards": "⏪",
    "backwards": "◀️",
    "close": "❌",
    "forwards": "▶️",
    "fastforwards": "⏩",
}

TRASHCAN = "🗑️"

COG_EMOJIS = {
    "Moderation": "🚨",
    "Level": "🏆",
    "Language": "👅",
    "Information": "<:Info:1220651376367898685>",
    "Help": "🔮",
    "Games": "🎮",
    "EmojiChecklist": "<:Emojicheck:1220650471275106334>",
}

HOME = "<:Home:1220318823173984367>"
CATEGORIES = "<:Menu:1220319818650226781>"
LINK = "<:Links:1220314935381463090>"
FIRE = "<:Fire:1220623078086938694>"
INFO = "<:Info:1220651376367898685>"
EMOJICHECK = "<:Emojicheck:1220650471275106334>"
