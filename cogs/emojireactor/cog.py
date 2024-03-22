import asyncio
from core.bot import AoiBot
from . import EmojiReactorModal
import datetime
import disnake
from disnake.ext import commands
import re
import emoji
from core.utils import LanguageClass, send_embed, get_colour

class EmojiChecklist(commands.Cog):
    def __init__(self, bot: AoiBot):
        self.bot = bot
        self.lock = False
        self.checkuser = {}

    async def reaction_close_elem(self, reaction: disnake.Reaction, user: disnake.Member):
        try:
            strings = await LanguageClass.get_strings(LanguageClass,await LanguageClass.get_lang(LanguageClass,reaction.message))
            if user.guild_permissions.manage_messages:
                reaction_key = (reaction.message.id, user.id)
                if reaction_key in self.checkuser:
                    del self.checkuser[reaction_key]

                await reaction.message.clear_reactions()
                dmembed = reaction.message.embeds[0].copy()
                dmembed.timestamp = datetime.datetime.now()
                dmembed.set_footer(text=strings["close_elem"])
                await reaction.message.edit(embed=dmembed)

                await asyncio.sleep(5)

                await reaction.message.clear_reactions()
                dmembed = reaction.message.embeds[0].copy()
                dmembed.timestamp = datetime.datetime.now()
                dmembed.set_footer(text=strings["close_elem"])
                await reaction.message.edit(embed=dmembed)
            else:
                await reaction.message.remove_reaction(reaction,user)
        except Exception as e:
            await send_embed(reaction.message.channel,title=strings["an_error"],description=f"{e}", c = get_colour("red"), f = reaction.message.author.display_name + strings["use_utility"])

    @commands.slash_command(name="emojichecklist",
                            description="Add reactions to messages with emojis/Добавьте реакции к сообщениям с эмоджи",)
    async def emojichecklist(self, inter: disnake.ApplicationCommandInteraction, field1, *, field2 = None, field3 =  None, field4 = None, field5 = None):
        try:
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

            await inter.response.send_modal(modal=EmojiReactorModal(inter,result))
        except Exception as e:
            strings = await LanguageClass.get_strings(LanguageClass,await LanguageClass.get_lang(LanguageClass,inter))
            await send_embed(inter.channel,title=strings["an_error"],description=f"{e}", c = get_colour("red"), f = inter.author.display_name + strings["use_utility"])

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction: disnake.Reaction, user: disnake.Member):
        try:
            strings_ru = await LanguageClass.get_strings(LanguageClass,"ru")
            strings_en = await LanguageClass.get_strings(LanguageClass,"en")
            
            if reaction.message.embeds[0].title not in [strings_ru["role_selec"], strings_en["role_selec"]]:
                return
            if reaction.message.embeds[0].footer.text in [strings_ru["close_elem"], strings_en["close_elem"]]:
                return

            message = reaction.message
            if user.bot or message.author.id != self.bot.user.id:
                return
            
            if (reaction.emoji == "❌"):
                await self.reaction_close_elem(reaction, user)
                return
            
            # Создаем кортеж из id сообщения и id пользователя
            reaction_key = (message.id, user.id)

            # Проверяем, есть ли такой кортеж в словаре
            if reaction_key in self.checkuser:
                self.lock = True
                await reaction.message.remove_reaction(reaction, user)
                return
            
            # Добавляем кортеж в качестве ключа в словарь
            self.checkuser[reaction_key] = user

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
            strings = await LanguageClass.get_strings(LanguageClass,await LanguageClass.get_lang(LanguageClass,reaction.message))
            await send_embed(reaction.message.channel,title=strings["an_error"],description=f"{e}", c = get_colour("red"), f = reaction.message.author.display_name + strings["use_utility"])

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction: disnake.Reaction, user: disnake.Member):
        try:
            if self.lock:
                self.lock = False
                return
            
            strings_ru = await LanguageClass.get_strings(LanguageClass,"ru")
            strings_en = await LanguageClass.get_strings(LanguageClass,"en")
            if reaction.message.embeds[0].title not in [strings_ru["role_selec"], strings_en["role_selec"]]:
                return
            if reaction.message.embeds[0].footer.text in [strings_ru["close_elem"], strings_en["close_elem"]]:
                return
            
            message = reaction.message
            if user.bot or message.author.id != self.bot.user.id:
                return
            
            reaction_key = (message.id, user.id)
            if reaction_key in self.checkuser:
                del self.checkuser[reaction_key]

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
            strings = await LanguageClass.get_strings(LanguageClass,await LanguageClass.get_lang(LanguageClass,reaction.message))
            await send_embed(reaction.message.channel,title=strings["an_error"],description=f"{e}", c = get_colour("red"), f = reaction.message.author.display_name + strings["use_utility"])

def setup(bot): 
    bot.add_cog(EmojiChecklist(bot))