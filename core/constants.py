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