import datetime
import disnake
from disnake import TextInputStyle
from core.utils import send_embed, get_colour
from core.utils.languageclass import LanguageClass
import emoji
import re

# Subclassing the modal.
class EmojiReactorModal(disnake.ui.Modal):
    def __init__(self, inter, result):
        if (len(result) == 5):
            components = [
                disnake.ui.TextInput(
                    label=result[0],
                    placeholder="🦆- Я выбираю быть кря",
                    custom_id=result[0],
                    style=TextInputStyle.paragraph,
                ),
                disnake.ui.TextInput(
                    label=result[1],
                    placeholder="🦅- I'll be a AH-64 Apache.",
                    custom_id=result[1],
                    style=TextInputStyle.paragraph,
                ),
                disnake.ui.TextInput(
                    label=result[2],
                    placeholder="🐦- Я буду воробушком",
                    custom_id=result[2],
                    style=TextInputStyle.paragraph,
                ),
                disnake.ui.TextInput(
                    label=result[3],
                    placeholder="🐉- 我将是一条龙",
                    custom_id=result[3],
                    style=TextInputStyle.paragraph,
                ),
                disnake.ui.TextInput(
                    label=result[4],
                    placeholder="🦝- Я енотик полоскун...",
                    custom_id=result[4],
                    style=TextInputStyle.paragraph,
                ),
            ]
        elif (len(result) == 4):
            components = [
                disnake.ui.TextInput(
                    label=result[0],
                    placeholder="🦆- Я выбираю быть кря",
                    custom_id=result[0],
                    style=TextInputStyle.paragraph,
                ),
                disnake.ui.TextInput(
                    label=result[1],
                    placeholder="🦅- I'll be a AH-64 Apache.",
                    custom_id=result[1],
                    style=TextInputStyle.paragraph,
                ),
                disnake.ui.TextInput(
                    label=result[2],
                    placeholder="🐦- Я буду воробушком",
                    custom_id=result[2],
                    style=TextInputStyle.paragraph,
                ),
                disnake.ui.TextInput(
                    label=result[3],
                    placeholder="🐉- 我将是一条龙",
                    custom_id=result[3],
                    style=TextInputStyle.paragraph,
                ),
            ]
        elif (len(result) == 3):
            components = [
                disnake.ui.TextInput(
                    label=result[0],
                    placeholder="🦆- Я выбираю быть кря",
                    custom_id=result[0],
                    style=TextInputStyle.paragraph,
                ),
                disnake.ui.TextInput(
                    label=result[1],
                    placeholder="🦅- I'll be a AH-64 Apache.",
                    custom_id=result[1],
                    style=TextInputStyle.paragraph,
                ),
                disnake.ui.TextInput(
                    label=result[2],
                    placeholder="🐦- Я буду воробушком",
                    custom_id=result[2],
                    style=TextInputStyle.paragraph,
                ),
            ]
        elif (len(result) == 2):
            components = [
                disnake.ui.TextInput(
                    label=result[0],
                    placeholder="🦆- Я выбираю быть кря",
                    custom_id=result[0],
                    style=TextInputStyle.paragraph,
                ),
                disnake.ui.TextInput(
                    label=result[1],
                    placeholder="🦅- I'll be a AH-64 Apache.",
                    custom_id=result[1],
                    style=TextInputStyle.paragraph,
                ),
            ]
        elif (len(result) == 1):
            components = [
                disnake.ui.TextInput(
                    label=result[0],
                    placeholder="🦆- Я выбираю быть кря",
                    custom_id=result[0],
                    style=TextInputStyle.paragraph,
                ),
            ]
        super().__init__(title="Create Tag", custom_id=f"create_tag_low-{inter.id}", components=components)
    
    async def on_error(self, error: Exception, inter: disnake.ModalInteraction):
        strings = await LanguageClass.get_strings(LanguageClass,await LanguageClass.get_lang(LanguageClass,inter))
        await send_embed(inter.channel,title=strings["an_error"],description=f"{error}", c = get_colour("red"), f = inter.author.display_name + strings["use_utility"])

    async def callback(self, inter: disnake.ModalInteraction):
        strings = await LanguageClass.get_strings(LanguageClass,await LanguageClass.get_lang(LanguageClass,inter))

        embed = disnake.Embed(color=0x1E90FF,timestamp=datetime.datetime.now()).set_footer(text=strings["role_selec"], icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Blue_checkbox-checked.svg/2048px-Blue_checkbox-checked.svg.png")

        for key, value in inter.text_values.items():
            updated_value = value
            server_emojis = re.findall(r':[a-zA-Z0-9_]+:', value)
            if server_emojis is not None:
                for emoji_text in server_emojis:
                    emoji_name = emoji_text.strip(':')
                    emoji_obj = disnake.utils.get(inter.guild.emojis, name=emoji_name)
                    updated_value = re.sub(r':([a-zA-Z0-9_]+):', str(emoji_obj), value)

            embed.add_field(
                name=f"{key.capitalize()}",
                value=updated_value,
                inline=False,
            )
        
        await inter.response.defer(with_message=False)
        message = await inter.channel.send(embed=embed)
        self.message = message 
        for key, value in inter.text_values.items():
            emoji_pattern = emoji.emoji_list(value)
            emoji_list = [entry['emoji'] for entry in emoji_pattern]
            for emoji_dict in emoji_list:
                await message.add_reaction(emoji_dict)

        for key, value in inter.text_values.items():
            server_emojis = re.findall(r':[a-zA-Z0-9_]+:', value)
            for emoji_text in server_emojis:
                emoji_name = emoji_text.strip(':')
                emoji_obj = disnake.utils.get(inter.guild.emojis, name=emoji_name)
                if emoji_obj is not None:
                    await message.add_reaction(emoji_obj)
        
        await message.add_reaction('❌')
        return message

    