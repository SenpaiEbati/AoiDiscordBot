from disnake import Embed, Message

from .utils import get_colour


async def create_embed(message: Message, bot) -> Embed:
    avatar = message.guild.get_member(bot.user.id).display_avatar.url
    await bot.get_prefix(message)

    embed = Embed(
        title=f"Hello {message.author.name}",
        description="""
    │ My default prefix is: `a.` │
    │ My prefix for you is: {', '.join(f"`{k}`" for k in prefix if not k.startswith('<@'))} │
    │ Type `a.prefix <prefix> [prefix], [prefix], etc` to change the prefix for you! │
    """,
        colour=get_colour(),
    )
    embed.set_author(name="AoiBot", icon_url=avatar)
    return embed
