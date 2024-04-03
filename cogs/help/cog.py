import datetime
import json
import typing

import disnake
from disnake.ext import commands
from core.utils import LanguageClass
from core import Context, AoiBot
from core.constants import (
    CATEGORIES,
    COG_EMOJIS,
    LINK,
    FIRE,
)
from core.utils import get_colour

from . import DropdownView


def get_help(command: str, lang) -> str:
    with open("./dicts/Cmds.json","r", encoding="utf-8") as fp:
        data = json.load(fp)
    try:
        help = data[lang][command]["help"].capitalize()
        return help
    except KeyError:
        return "-"


class HelpUtils:
    def __init__(self, bot: AoiBot):
        self.bot = bot

    async def get_cog_from_str(self, cog_name: str) -> typing.Optional[commands.Cog]:
        cog_name = cog_name.lower()

        for k in self.bot.cogs:
            if k.lower() == cog_name:
                return self.bot.get_cog(k)
        return None

    async def main_help_embed(self, ctx) -> disnake.Embed:
        strings = await LanguageClass.get_strings(LanguageClass,await LanguageClass.get_lang(LanguageClass,ctx))
        description = strings["main_help_embed_desc"]
        cogs = [
            f">  {COG_EMOJIS[k]} **{k}** `({len([e for e in self.bot.slash_commands if e.cog_name == k])})`"
            for k in self.bot.cogs
            if k in COG_EMOJIS
        ]

        return (
            disnake.Embed(
                title=FIRE +" "+ strings["main_help_embed_title"] +" "+ FIRE,
                description=description,
                timestamp=datetime.datetime.now(),
                colour=get_colour("blue"),
            )
            .add_field(
                name=f"{CATEGORIES} " + strings["main_help_embed_categ"] + "\n\u200b",
                value="\n".join(cogs[i] for i in range(0, len(cogs), 2)) + "\n\u200b",
            )
            .add_field(
                name="\u200b\n\u200b",
                value="\n".join(cogs[i] for i in range(1, len(cogs), 2)),
            )
            .add_field(
                name=f"{LINK} "+strings["main_help_embed_links"], value=f"**> ["+strings["main_help_embed_official"]+"](https://discord.gg/RAjhN7FqdR) │ ["+strings["main_help_embed_botinvite"]+"](https://discord.com/oauth2/authorize?client_id=1152289596969861203)**", inline=False
            )
        )

    async def main_help(self, ctx: Context) -> None:
        embed = await self.main_help_embed(ctx)
        await ctx.reply(
            embed=embed, view=DropdownView(COG_EMOJIS, ctx, HelpUtils(self.bot))
        )

    async def specific_command(
        self, command: commands.Command, ctx: Context
    ) -> disnake.Embed:
        strings = await LanguageClass.get_strings(LanguageClass,await LanguageClass.get_lang(LanguageClass,ctx))
        return (
            disnake.Embed(title=strings["help"],colour=get_colour("blue"),timestamp=datetime.datetime.now())
            .add_field(
                name=strings["specific_command_name"], value=f"`{command.name.capitalize()}`", inline=False
            )
            .add_field(
                name=strings["specific_command_alias"],
                value=f"{', '.join(f'`{k}`' for k in command.aliases if command.aliases)} "
                if command.aliases
                else "`none`",
                inline=False,
            )
            .add_field(
                name=strings["specific_command_usage"],
                value=f"`/{command.name}` / `a.{command.name} {command.signature}`"
                if command.signature
                else f"`/{command.name}` / `a.{command.name}`",
                inline=False,
            )
            .add_field(
                name=strings["specific_command_desc"],
                value=f"{get_help(command.name,await LanguageClass.get_lang(LanguageClass,ctx))}"
                if get_help(command.name,await LanguageClass.get_lang(LanguageClass,ctx))
                else strings["specific_command_else"],
                inline=False,
            )
        )

    async def specific_cog(self, cog: commands.Cog, ctx: Context) -> disnake.Embed:
        if cog.qualified_name not in COG_EMOJIS:
            return await self.no_command(ctx)
        
        strings = await LanguageClass.get_strings(LanguageClass,await LanguageClass.get_lang(LanguageClass,ctx))
        commands = [f"- `/{e.name}`" for e in ctx.bot.slash_commands if e.cog_name == cog.qualified_name]

        return (
            disnake.Embed(
                title=f"{COG_EMOJIS[cog.qualified_name]} {cog.qualified_name} {COG_EMOJIS[cog.qualified_name]}",
                description=strings["specific_cog_desc"] + strings[f"{cog.qualified_name}"], colour=get_colour("blue")
            )
            .add_field(
                name="\u200b",
                value="\n".join(commands[i] for i in range(0, len(commands), 2)),
            )
            .add_field(
                name="\u200b",
                value="\n".join(commands[i] for i in range(1, len(commands), 2)),
            )
        )

    async def no_command(self, ctx, cmd) -> disnake.Embed:
        strings = await LanguageClass.get_strings(LanguageClass,await LanguageClass.get_lang(LanguageClass,ctx))
        
        return (
            disnake.Embed(colour=get_colour("blue"))
            .set_author(
                name=f"{cmd}" + strings["not_command!"]
            )
        )

class Help(commands.Cog):
    def __init__(self, bot: AoiBot):
        self.bot = bot
        self.utils = HelpUtils(bot)
    
    @commands.slash_command(name="help",
                            description="Learn what commands exist and their functions/Узнайте какие существуют комманды и их функции")
    async def help(self, ctx, command=None) -> None:
        if not command:
            embed = await self.utils.main_help_embed(ctx)
            return await ctx.send(
                embed=embed, view=DropdownView(COG_EMOJIS, ctx, self.utils)
            )

        cog = await self.utils.get_cog_from_str(command)
        if cog:
            embed = await self.utils.specific_cog(cog, ctx)
            return await ctx.send(embed=embed)

        cmd = self.bot.get_command(command)
        if cmd:
            embed = await self.utils.specific_command(cmd, ctx)
            return await ctx.send(embed=embed)

        embed = await self.utils.no_command(ctx, command)
        return await ctx.send(embed=embed)

class NoSlash_Help(commands.Cog):
    def __init__(self, bot: AoiBot):
        self.bot = bot
        self.utils = HelpUtils(bot)

    @commands.command(
        aliases=[
            "h",
            "commands",
            "cmd",
            "command",
            "?",
            "helpme",
            "helpcommand",
            "cmds",
        ]
    )
    async def help(self, ctx: Context, command=None) -> None:
        if not command:
            embed = await self.utils.main_help_embed(ctx)
            return await ctx.reply(
                embed=embed, view=DropdownView(COG_EMOJIS, ctx, self.utils)
            )

        cog = await self.utils.get_cog_from_str(command)
        if cog:
            embed = await self.utils.specific_cog(cog, ctx)
            return await ctx.reply(embed=embed)

        cmd = self.bot.get_command(command)
        if cmd:
            embed = await self.utils.specific_command(cmd, ctx)
            return await ctx.reply(embed=embed)

        embed = await self.utils.no_command(ctx,command)
        return await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(NoSlash_Help(bot))
    bot.add_cog(Help(bot))
