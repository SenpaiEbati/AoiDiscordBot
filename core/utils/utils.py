import datetime
from io import TextIOWrapper
import json

import disnake


def update_json(_file: TextIOWrapper, _data: dict) -> None:
    """Update file to match data"""

    _file.seek(0)
    _file.truncate()
    _file.write(json.dumps(_data, indent=4))


def get_colour(colour=None) -> int:
    with open("./dicts/Colour.json") as fp:
        data = json.load(fp)
    if isinstance(colour, str):
        color = data[colour]
    else:
        color = data["colour"]
    return int(color, 16)


async def send_embed(
    channel: disnake.abc.Messageable,
    title: str,
    description: str = None,
    **kwargs
) -> disnake.Message:
    from core.context import Context

    author = kwargs.get("a")
    icon_url = kwargs.get("i_u")
    footer = kwargs.get("f")
    thumbnail = kwargs.get("t")
    image = kwargs.get("i")
    colour = kwargs.get("c")
    
    embed = disnake.Embed(title=title, description=description, colour=get_colour(colour), timestamp=datetime.datetime.now())
    if footer:
        embed.set_footer(text=footer)
    if author:
        embed.set_author(name=author)
        if icon_url:
            embed.set_author(name=author, icon_url=icon_url)
    if thumbnail:
        embed.set_thumbnail(url=thumbnail)
    if image:
        embed.set_image(url=image)

    if isinstance(channel, Context):
        embed.timestamp = channel.message.created_at.now()
        msg = await channel.reply(embed=embed)
    else:
        msg = await channel.send(embed=embed)
    return msg
