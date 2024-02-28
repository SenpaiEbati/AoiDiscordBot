import disnake
from disnake.ext import commands
from disnake import TextInputStyle
import re
import emoji

class Slash_ListReaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="listreaction",
                            description="",)
    async def listreaction(self, inter: disnake.ApplicationCommandInteraction, name_label_1, *, name_label_2 = None, name_label_3 =  None, name_label_4 = None, name_label_5 = None):
        try:
            if (name_label_5 != None):
                components = [
                    disnake.ui.TextInput(
                        label=name_label_1,
                        placeholder="Lorem ipsum dolor sit amet.",
                        custom_id=name_label_1,
                        style=TextInputStyle.paragraph,
                    ),
                    disnake.ui.TextInput(
                        label=name_label_2,
                        placeholder="Lorem ipsum dolor sit amet.",
                        custom_id=name_label_2,
                        style=TextInputStyle.paragraph,
                    ),
                    disnake.ui.TextInput(
                        label=name_label_3,
                        placeholder="Lorem ipsum dolor sit amet.",
                        custom_id=name_label_3,
                        style=TextInputStyle.paragraph,
                    ),
                    disnake.ui.TextInput(
                        label=name_label_4,
                        placeholder="Lorem ipsum dolor sit amet.",
                        custom_id=name_label_4,
                        style=TextInputStyle.paragraph,
                    ),
                    disnake.ui.TextInput(
                        label=name_label_5,
                        placeholder="Lorem ipsum dolor sit amet.",
                        custom_id=name_label_5,
                        style=TextInputStyle.paragraph,
                    ),
                ]
            elif (name_label_4 != None):
                components = [
                    disnake.ui.TextInput(
                        label=name_label_1,
                        placeholder="Lorem ipsum dolor sit amet.",
                        custom_id=name_label_1,
                        style=TextInputStyle.paragraph,
                    ),
                    disnake.ui.TextInput(
                        label=name_label_2,
                        placeholder="Lorem ipsum dolor sit amet.",
                        custom_id=name_label_2,
                        style=TextInputStyle.paragraph,
                    ),
                    disnake.ui.TextInput(
                        label=name_label_3,
                        placeholder="Lorem ipsum dolor sit amet.",
                        custom_id=name_label_3,
                        style=TextInputStyle.paragraph,
                    ),
                    disnake.ui.TextInput(
                        label=name_label_4,
                        placeholder="Lorem ipsum dolor sit amet.",
                        custom_id=name_label_4,
                        style=TextInputStyle.paragraph,
                    ),
                ]
            elif (name_label_3 != None):
                components = [
                    disnake.ui.TextInput(
                        label=name_label_1,
                        placeholder="Lorem ipsum dolor sit amet.",
                        custom_id=name_label_1,
                        style=TextInputStyle.paragraph,
                    ),
                    disnake.ui.TextInput(
                        label=name_label_2,
                        placeholder="Lorem ipsum dolor sit amet.",
                        custom_id=name_label_2,
                        style=TextInputStyle.paragraph,
                    ),
                    disnake.ui.TextInput(
                        label=name_label_3,
                        placeholder="Lorem ipsum dolor sit amet.",
                        custom_id=name_label_3,
                        style=TextInputStyle.paragraph,
                    ),
                ]
            elif (name_label_2 != None):
                components = [
                    disnake.ui.TextInput(
                        label=name_label_1,
                        placeholder="Lorem ipsum dolor sit amet.",
                        custom_id=name_label_1,
                        style=TextInputStyle.paragraph,
                    ),
                    disnake.ui.TextInput(
                        label=name_label_2,
                        placeholder="Lorem ipsum dolor sit amet.",
                        custom_id=name_label_2,
                        style=TextInputStyle.paragraph,
                    ),
                ]
            else:
                components = [
                    disnake.ui.TextInput(
                        label=name_label_1,
                        placeholder="Lorem ipsum dolor sit amet.",
                        custom_id=name_label_1,
                        style=TextInputStyle.paragraph,
                    ),
                ]

            await inter.response.send_modal(title="Create Tag",custom_id=f"create_tag_low-{inter.id}", components=components)
        except Exception as e:
            await inter.channel.send(f"An error occurred!\n```{e}```")

    @commands.Cog.listener()
    async def on_modal_submit(self, inter: disnake.ModalInteraction):
        try:
            embed = disnake.Embed(color=0x1E90FF)

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

            for key, value in inter.text_values.items():
                updated_value = value
                server_emojis = re.findall(r':[a-zA-Z0-9_]+:', value)
                if server_emojis is not None:
                    for emoji_text in server_emojis:
                        emoji_name = emoji_text.strip(':')
                        emoji_obj = disnake.utils.get(inter.guild.emojis, name=emoji_name)
                        updated_value = re.sub(r':([a-zA-Z0-9_]+):', str(emoji_obj), value)

                embed.add_field(
                    name=f"`{key.capitalize()}`",
                    value=updated_value,
                    inline=False,
                )

            await add_reactions_to_last_message()
        except Exception as e:
            await inter.channel.send(f"An error occurred!\n```{e}```")

    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction: disnake.Reaction, user: disnake.User):
        try:
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
                                line += f" {user.mention}"
                    if emoji_list:
                        for emojigg in emoji_list:
                            if reaction.emoji == emojigg:
                                line += f" {user.mention}"
                    new_value_lines.append(line)

                new_value = '\n'.join(new_value_lines)
                dmembed.set_field_at(i, name=field.name, value=new_value, inline=False)

            await message.edit(embed=dmembed)
        except Exception as e:
            await message.channel.send(f"An error occurred!\n```{e}```")
    
    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction: disnake.Reaction, user: disnake.User):
        try:
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
            await message.channel.send(f"An error occurred!\n```{e}```")

def setup(bot): 
    bot.add_cog(Slash_ListReaction(bot))