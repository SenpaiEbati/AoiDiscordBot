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
                    placeholder="🎃 Счастливого хеллуина !!",
                    custom_id=result[0],
                    style=TextInputStyle.paragraph,
                    max_length=1024,
                ),
                disnake.ui.TextInput(
                    label=result[1],
                    placeholder="😈 Используйте смайлики хеллуина)",
                    custom_id=result[1],
                    style=TextInputStyle.paragraph,
                    max_length=1024,
                ),
                disnake.ui.TextInput(
                    label=result[2],
                    placeholder="🍬 Сладость или пакость !!!",
                    custom_id=result[2],
                    style=TextInputStyle.paragraph,
                    max_length=1024,
                ),
                disnake.ui.TextInput(
                    label=result[3],
                    placeholder="👻 Буууууууууу",
                    custom_id=result[3],
                    style=TextInputStyle.paragraph,
                    max_length=1024,
                ),
                disnake.ui.TextInput(
                    label=result[4],
                    placeholder="👽 Не бойся меня я друг...",
                    custom_id=result[4],
                    style=TextInputStyle.paragraph,
                    max_length=1024,
                ),
            ]
        elif (len(result) == 4):
            components = [
                disnake.ui.TextInput(
                    label=result[0],
                    placeholder="🎃 Счастливого хеллуина !!",
                    custom_id=result[0],
                    style=TextInputStyle.paragraph,
                    max_length=1024,
                ),
                disnake.ui.TextInput(
                    label=result[1],
                    placeholder="😈 Используйте смайлики хеллуина)",
                    custom_id=result[1],
                    style=TextInputStyle.paragraph,
                    max_length=1024,
                ),
                disnake.ui.TextInput(
                    label=result[2],
                    placeholder="🍬 Сладость или пакость !!!",
                    custom_id=result[2],
                    style=TextInputStyle.paragraph,
                    max_length=1024,
                ),
                disnake.ui.TextInput(
                    label=result[3],
                    placeholder="👻 Буууууууууу",
                    custom_id=result[3],
                    style=TextInputStyle.paragraph,
                    max_length=1024,
                ),
            ]
        elif (len(result) == 3):
            components = [
                disnake.ui.TextInput(
                    label=result[0],
                    placeholder="🎃 Счастливого хеллуина !!",
                    custom_id=result[0],
                    style=TextInputStyle.paragraph,
                    max_length=1024,
                ),
                disnake.ui.TextInput(
                    label=result[1],
                    placeholder="😈 Используйте смайлики хеллуина)",
                    custom_id=result[1],
                    style=TextInputStyle.paragraph,
                    max_length=1024,
                ),
                disnake.ui.TextInput(
                    label=result[2],
                    placeholder="🍬 Сладость или пакость !!!",
                    custom_id=result[2],
                    style=TextInputStyle.paragraph,
                    max_length=1024,
                ),
            ]
        elif (len(result) == 2):
            components = [
                disnake.ui.TextInput(
                    label=result[0],
                    placeholder="🎃 Счастливого хеллуина !!",
                    custom_id=result[0],
                    style=TextInputStyle.paragraph,
                    max_length=1024,
                ),
                disnake.ui.TextInput(
                    label=result[1],
                    placeholder="😈 Используйте смайлики хеллуина)",
                    custom_id=result[1],
                    style=TextInputStyle.paragraph,
                    max_length=1024,
                ),
            ]
        elif (len(result) == 1):
            components = [
                disnake.ui.TextInput(
                    label=result[0],
                    placeholder="🎃 Счастливого хеллуина !!",
                    custom_id=result[0],
                    style=TextInputStyle.paragraph,
                    max_length=1024,
                ),
            ]
        super().__init__(title="Create Tag", custom_id=f"create_tag_low-{inter.id}", components=components)
    
    async def on_error(self, error: Exception, inter: disnake.ModalInteraction):
        strings = await LanguageClass.get_strings(LanguageClass,await LanguageClass.get_lang(LanguageClass,inter))
        await send_embed(inter.channel,title=strings["an_error"],description=f"{error}", c = get_colour("red"), f = inter.author.display_name + strings["use_utility"])

    async def callback(self, inter: disnake.ModalInteraction):
        strings = await LanguageClass.get_strings(LanguageClass, await LanguageClass.get_lang(LanguageClass, inter))

        embed = disnake.Embed(color=get_colour("colour"), timestamp=datetime.datetime.now()).set_footer(text=strings["role_selec"], icon_url="https://cdn-icons-png.flaticon.com/512/10629/10629607.png")

        for key, value in inter.text_values.items():
            updated_value = value
            server_emojis = re.findall(r':[a-zA-Z0-9_]+:', value)
            if server_emojis:
                for emoji_text in server_emojis:
                    emoji_name = emoji_text.strip(':')
                    emoji_obj = disnake.utils.get(inter.guild.emojis, name=emoji_name)
                    if emoji_obj:
                        updated_value = updated_value.replace(emoji_text, str(emoji_obj))

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
                if emoji_obj:
                    await message.add_reaction(emoji_obj)

        await message.add_reaction('❌')
        return message


    