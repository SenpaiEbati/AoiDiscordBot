import asyncio
import datetime
import disnake
from disnake.ext import commands
from disnake import TextInputStyle
import re
import emoji
from cogs._class.LanguageClass import LanguageClass

class Slash_EmojiReactor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.livetime = 0
    @commands.slash_command(name="emojireactor",
                            description="Add reactions to messages with emojis/Добавьте реакции к сообщениям с эмоджи",)
    async def emojireactor(self, inter: disnake.ApplicationCommandInteraction, field1, *, field2 = None, field3 =  None, field4 = None, field5 = None, lifetime: str = f"{24 * 60 * 60}"):
        try:
            lang = await LanguageClass.get_lang(LanguageClass,inter)
            strings = await LanguageClass.get_strings(LanguageClass,lang)

            if lifetime.isdigit():
                self.livetime = int(lifetime)
            else:
                embed = disnake.Embed(title=strings["incorrect_argument"], 
                                    description=strings["incorrect_argument_emojireactor"],
                                    color=disnake.Color(0xff0000),
                                    timestamp=datetime.datetime.now())
                embed.set_footer(
                        text=inter.author.display_name + strings["use_utility"]
                )
                await inter.response.send_message(embed=embed)
                return

            result = [] 
            if field1 is not None:
                result.append(field1)
            if field2 is not None:
                result.append(field2)
            if field3 is not None:
                result.append(field3)
            if field4 is not None:
                result.append(field4)
            if field5 is not None:
                result.append(field5)

            placeholderd = strings["placeholde"]
            if (len(result) == 5):
                components = [
                    disnake.ui.TextInput(
                        label=result[0],
                        placeholder=placeholderd,
                        custom_id=result[0],
                        style=TextInputStyle.paragraph,
                    ),
                    disnake.ui.TextInput(
                        label=result[1],
                        placeholder=placeholderd,
                        custom_id=result[1],
                        style=TextInputStyle.paragraph,
                    ),
                    disnake.ui.TextInput(
                        label=result[2],
                        placeholder=placeholderd,
                        custom_id=result[2],
                        style=TextInputStyle.paragraph,
                    ),
                    disnake.ui.TextInput(
                        label=result[3],
                        placeholder=placeholderd,
                        custom_id=result[3],
                        style=TextInputStyle.paragraph,
                    ),
                    disnake.ui.TextInput(
                        label=result[4],
                        placeholder=placeholderd,
                        custom_id=result[4],
                        style=TextInputStyle.paragraph,
                    ),
                ]
            elif (len(result) == 4):
                components = [
                    disnake.ui.TextInput(
                        label=result[0],
                        placeholder=placeholderd,
                        custom_id=result[0],
                        style=TextInputStyle.paragraph,
                    ),
                    disnake.ui.TextInput(
                        label=result[1],
                        placeholder=placeholderd,
                        custom_id=result[1],
                        style=TextInputStyle.paragraph,
                    ),
                    disnake.ui.TextInput(
                        label=result[2],
                        placeholder=placeholderd,
                        custom_id=result[2],
                        style=TextInputStyle.paragraph,
                    ),
                    disnake.ui.TextInput(
                        label=result[3],
                        placeholder=placeholderd,
                        custom_id=result[3],
                        style=TextInputStyle.paragraph,
                    ),
                ]
            elif (len(result) == 3):
                components = [
                    disnake.ui.TextInput(
                        label=result[0],
                        placeholder=placeholderd,
                        custom_id=result[0],
                        style=TextInputStyle.paragraph,
                    ),
                    disnake.ui.TextInput(
                        label=result[1],
                        placeholder=placeholderd,
                        custom_id=result[1],
                        style=TextInputStyle.paragraph,
                    ),
                    disnake.ui.TextInput(
                        label=result[2],
                        placeholder=placeholderd,
                        custom_id=result[2],
                        style=TextInputStyle.paragraph,
                    ),
                ]
            elif (len(result) == 2):
                components = [
                    disnake.ui.TextInput(
                        label=result[0],
                        placeholder=placeholderd,
                        custom_id=result[0],
                        style=TextInputStyle.paragraph,
                    ),
                    disnake.ui.TextInput(
                        label=result[1],
                        placeholder=placeholderd,
                        custom_id=result[1],
                        style=TextInputStyle.paragraph,
                    ),
                ]
            elif (len(result) == 1):
                components = [
                    disnake.ui.TextInput(
                        label=result[0],
                        placeholder=placeholderd,
                        custom_id=result[0],
                        style=TextInputStyle.paragraph,
                    ),
                ]

            await inter.response.send_modal(title=strings["crea_em_reac"],custom_id=f"create_tag_low-{inter.id}", components=components)
        except Exception as e:
            erembed = disnake.Embed(title=strings["an_error"], 
                                description=f"{e}",
                                color=disnake.Color(0xff0000),
                                timestamp=datetime.datetime.now())
            erembed.set_footer(
                    text=inter.author.display_name + strings["use_utility"]
            )
            await inter.channel.send(embed=erembed)

    @commands.Cog.listener()
    async def on_modal_submit(self, inter: disnake.ModalInteraction):
        try:
            lang = await LanguageClass.get_lang(LanguageClass,inter)
            strings = await LanguageClass.get_strings(LanguageClass,lang)

            embed = disnake.Embed(color=0x1E90FF,timestamp=datetime.datetime.now())

            async def add_reactions_to_last_message():
                await inter.response.send_message(embed=embed)
                sendm = inter.channel.last_message
                if sendm:
                    for key, value in inter.text_values.items():
                        emoji_pattern = emoji.emoji_list(value)
                        emoji_list = [entry['emoji'] for entry in emoji_pattern]
                        for emoji_dict in emoji_list:
                            await sendm.add_reaction(emoji_dict)

                    for key, value in inter.text_values.items():
                        server_emojis = re.findall(r':[a-zA-Z0-9_]+:', value)
                        for emoji_text in server_emojis:
                            emoji_name = emoji_text.strip(':')
                            emoji_obj = disnake.utils.get(inter.guild.emojis, name=emoji_name)
                            if emoji_obj is not None:
                                await sendm.add_reaction(emoji_obj)
                    
                    await sendm.add_reaction('❌')

                    await asyncio.sleep(self.livetime)  # 24 часа в секундах
                    await sendm.clear_reactions()
                    embed.timestamp = datetime.datetime.now()
                    embed.set_footer(text=strings["close_elem"])
                    await sendm.edit(embed=embed)

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
            
            embed.set_footer(
                        text=inter.author.display_name + strings["use_utility"]
                )
            await add_reactions_to_last_message()

        except disnake.errors.Forbidden as e:
            erembed = disnake.Embed(title=strings["error_20_emoji"], 
                                description=strings["error_20_emoji_des"],
                                color=disnake.Color(0xFFFF33),
                                timestamp=datetime.datetime.now())
            erembed.set_footer(
                    text=inter.author.display_name + strings["use_utility"]
            )
            await inter.channel.send(embed=erembed)
        except Exception as e:
            erembed = disnake.Embed(title=strings["an_error"], 
                                description=f"{e}",
                                color=disnake.Color(0xff0000),
                                timestamp=datetime.datetime.now())
            erembed.set_footer(
                    text=inter.author.display_name + strings["use_utility"]
            )
            await inter.channel.send(embed=erembed)

    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction: disnake.Reaction, user: disnake.Member):
        try:
            lang = await LanguageClass.get_lang(LanguageClass,reaction.message)
            strings = await LanguageClass.get_strings(LanguageClass,lang)

            message = reaction.message
            if user.bot or message.author != self.bot.user:
                return

            emoji_remove = emoji.emoji_list("❌")
            emoji_remove_mas = [entry['emoji'] for entry in emoji_remove]
            if (reaction.emoji == emoji_remove_mas[0]):
                if user.guild_permissions.manage_messages:
                    await reaction.message.clear_reactions()
                    dmembed = message.embeds[0].copy()
                    dmembed.timestamp = datetime.datetime.now()
                    dmembed.set_footer(text=strings["close_elem"])
                    await message.edit(embed=dmembed)
                else:
                    await reaction.message.remove_reaction(reaction,user)
                return

            embed = message.embeds[0]
            embed_fields = embed.fields
            dmembed = embed.copy()

            for i, field in enumerate(embed_fields):
                value_lines = field.value.split('\n')
                new_value_lines = []
                for line in value_lines:
                    if f"{user.mention}" in line:
                        new_value_lines.append(line)
                        await reaction.message.remove_reaction(reaction,user)
                        return
                    else: 
                        emoji_pattern = emoji.emoji_list(line)
                        emoji_list = [entry['emoji'] for entry in emoji_pattern]
                        server_emojis = re.findall(r':[a-zA-Z0-9_]+:', line)
                        if server_emojis:
                            for emoji_text in server_emojis:
                                emoji_name = emoji_text.strip(':')
                                emoji_obj = disnake.utils.get(message.author.guild.emojis, name=emoji_name)
                                if reaction.emoji == emoji_obj:
                                    if f"{user.mention}" in line:
                                        continue
                                    else:
                                        line += f" {user.mention}"
                        if emoji_list:
                            for emojigg in emoji_list:
                                if reaction.emoji == emojigg:
                                    if f"{user.mention}" in line:
                                        continue
                                    else:
                                        line += f" {user.mention}"
                        new_value_lines.append(line)

                new_value = '\n'.join(new_value_lines)
                dmembed.set_field_at(i, name=field.name, value=new_value, inline=False)

            await message.edit(embed=dmembed)
        except Exception as e:
            erembed = disnake.Embed(title=strings["an_error"], 
                                description=f"{e}",
                                color=disnake.Color(0xff0000),
                                timestamp=datetime.datetime.now())
            erembed.set_footer(
                    text=message.author.display_name + strings["use_utility"]
            )
            await message.channel.send(embed=erembed)
    
    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction: disnake.Reaction, user: disnake.Member):
        try:
            lang = await LanguageClass.get_lang(LanguageClass,reaction.message)
            strings = await LanguageClass.get_strings(LanguageClass,lang)

            message = reaction.message
            if user.bot or message.author != self.bot.user:
                return
            
            embed = message.embeds[0]
            embed_fields = embed.fields
            dmembed = embed.copy()

            for i, field in enumerate(embed_fields):
                value_lines = field.value.split('\n')
                new_value_lines = []
                for line in value_lines:
                    emoji_pattern = emoji.emoji_list(line)
                    emoji_list = [entry['emoji'] for entry in emoji_pattern]
                    server_emojis = re.findall(r':[a-zA-Z0-9_]+:', line)
                    if server_emojis:
                        for emoji_text in server_emojis:
                            emoji_name = emoji_text.strip(':')
                            emoji_obj = disnake.utils.get(message.author.guild.emojis, name=emoji_name)
                            if reaction.emoji == emoji_obj:
                                line = line.replace(f" {user.mention}", "")
                    if emoji_list:
                        for emojigg in emoji_list:
                            if reaction.emoji == emojigg:
                                line = line.replace(f" {user.mention}", "")
                    new_value_lines.append(line)

                new_value = '\n'.join(new_value_lines)
                dmembed.set_field_at(i, name=field.name, value=new_value, inline=False)

            await message.edit(embed=dmembed)
        except Exception as e:
            erembed = disnake.Embed(title=strings["an_error"], 
                                description=f"{e}",
                                color=disnake.Color(0xff0000),
                                timestamp=datetime.datetime.now())
            erembed.set_footer(
                    text=message.author.display_name + strings["use_utility"]
            )
            await message.channel.send(embed=erembed)

def setup(bot): 
    bot.add_cog(Slash_EmojiReactor(bot))