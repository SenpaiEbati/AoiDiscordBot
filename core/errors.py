import asyncio
import json
import traceback

import disnake
from disnake.ext.commands import (
    BadArgument,
    CheckFailure,
    CommandInvokeError,
    CommandNotFound,
    CommandOnCooldown,
    MemberNotFound,
    MissingPermissions,
    MissingRequiredArgument,
    RoleNotFound,
)

from core.constants import LOCATION_EMOJIS
from core.paginator import Paginator
from core.utils import LanguageClass, get_colour, send_embed, update_json


async def unexpected(ctx, error):
    bot = ctx.bot
    with open(r"../data/dicts/Errors.json", "r+") as k:
        data = json.load(k)
        num = str(len(data))

        data[num] = {
            "author": ctx.author.name,
            "id": ctx.author.id,
            "error": str(error),
            "error_dir": str(dir(error)),
            "command": ctx.command.name,
        }
        update_json(k, data)
    http = f"https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{ctx.message.id}"
    await send_embed(bot.chan, f"{ctx.guild}; {ctx.author}; {ctx.command.name}", error)
    await bot.chan.send(http)
    e = "".join(traceback.format_exception(error, error, error.__traceback__))
    y = Paginator(ctx)
    strings = await LanguageClass.get_strings(LanguageClass,await LanguageClass.get_lang(LanguageClass,ctx))
    await y.paginate(content=f"{e}", name=strings["an_error"])


async def error_handler(ctx, error) -> None:
    strings = await LanguageClass.get_strings(LanguageClass,await LanguageClass.get_lang(LanguageClass,ctx))
    if isinstance(error, MissingPermissions):
        await send_embed(
            ctx, strings["no_rights"], strings["missingperm"], get_colour("red")
        )
    elif isinstance(error, CheckFailure):
        pass
    elif isinstance(error, BadArgument):
        args = error.args[0].strip(".").split()
        _type, param = args[2].strip('"'), args[-1].strip('"')

        await send_embed(
            ctx, strings["incorrect_argument"], strings["badargument1"] + f"{param}" + strings["badargument2"] + f"{_type}" + strings["badargument3"], get_colour("yellow")
        )
    elif isinstance(error, MissingRequiredArgument):
        com = str(ctx.command.signature)
        x = com.split(f"{error.param.name}")
        y = " "
        z = "  "

        for _ in str(ctx.command):
            z += " "
        for _ in error.param.name:
            y += "^"
        for _ in range(0, len(x[0])):
            z += " "

        await send_embed(
            ctx,
            strings["missreqarg1"] + f"{error.param.name}" + strings["missreqarg2"],
            f"```a.{ctx.command} {ctx.command.signature}\n{z}{y}```",
            f= strings["needed"],
            c = "yellow"
        )

    elif isinstance(error, CommandNotFound):
        with open(r"../data/dicts/Suggest.json") as l:
            data = json.load(l)
            if str(ctx.channel.id) in data and data[str(ctx.channel.id)]["Yes"]:
                return
        try:
            y = []
            content = ctx.message.content
            content_replace = content.replace(ctx.prefix, "")

            for cmd in ctx.bot.commands:
                if cmd.name[:1] == content_replace[:1]:
                    if cmd.hidden:
                        pass
                    else:
                        if len(y) == 5:
                            y.append(f"`{cmd.name}`---")
                        else:
                            y.append(f"`{cmd.name}`")
            my_string = ""
            for string in y:
                my_string += f" \n - {str(string)}"
            num = 1
            my_string = my_string.split("---")
            failed_cmd = ctx.message.content.split(" ")
            failed_cmd = failed_cmd[0]
            embed = disnake.Embed(title=strings["an_error"],description=f"{failed_cmd}" + strings["isnotcomm"], colour=get_colour())

            if my_string[0] not in [""]:
                embed.add_field(name=strings["didyoumean"], value=f"{my_string[0]}")

            msg = await ctx.reply(embed=embed)

            def check(e, u):
                return u == ctx.author and e.message.id == msg.id

            left = LOCATION_EMOJIS["backwards"]
            right = LOCATION_EMOJIS["forwards"]
            close = LOCATION_EMOJIS["close"]
            if len(my_string) >= 2:
                if my_string[1] != "":
                    await msg.add_reaction(left)
                    await msg.add_reaction(close)
                    await msg.add_reaction(right)
                    try:
                        (emoji, user) = await ctx.bot.wait_for(
                            "reaction_add", timeout=60.0, check=check
                        )
                        while str(emoji.emoji) != close:
                            if str(emoji.emoji) == right and num == 1:
                                embed = disnake.Embed(
                                    title=strings["an_error"],description=f"{failed_cmd}" + strings["isnotcomm"],colour=get_colour()
                                )
                                embed.add_field(
                                    name=strings["didyoumean"], value=f"{my_string[1]}"
                                )
                                embed.set_footer(text=strings["page2"])
                                await msg.edit(embed=embed)
                                await msg.remove_reaction(
                                    member=ctx.author, emoji=right
                                )
                                num = 2

                            elif str(emoji.emoji) == left and num == 2:
                                embed = disnake.Embed(
                                    title=strings["an_error"],description=f"{failed_cmd}" + strings["isnotcomm"],colour=get_colour()
                                )
                                embed.add_field(
                                    name=strings["didyoumean"], value=f"{my_string[0]}"
                                )
                                embed.set_footer(text=strings["page1"])
                                await msg.edit(embed=embed)
                                await msg.remove_reaction(member=ctx.author, emoji=left)
                                num = 1
                            else:
                                await msg.remove_reaction(
                                    member=ctx.author, emoji=right
                                )
                                await msg.remove_reaction(member=ctx.author, emoji=left)

                            (emoji, user) = await ctx.bot.wait_for(
                                "reaction_add",
                                timeout=60.0,
                                check=lambda r, u: u == ctx.author,
                            )
                        else:
                            embed = disnake.Embed(
                                title=strings["an_error"],
                                description=f"{failed_cmd}" + strings["isnotcomm"],
                                colour=get_colour(),
                            )
                            embed.set_footer(text=strings["Goodbye"])
                            return await msg.edit(embed=embed)

                    except asyncio.TimeoutError:
                        embed = disnake.Embed(
                            title=strings["an_error"],
                            description=f"{failed_cmd}" + strings["isnotcomm"],
                            colour=get_colour(),
                        )
                        embed.set_footer(text=strings["timeoutsession"])
                        return await msg.edit(embed=embed)

        except Exception:
            pass
    elif isinstance(error, MemberNotFound):
        embed = disnake.Embed(
            description=strings["membernotfound"], colour=get_colour()
        )
        await ctx.reply(embed=embed)
    elif isinstance(error, RoleNotFound):
        embed = disnake.Embed(
            description=strings["rolenotfound"], colour=get_colour()
        )
        await ctx.reply(embed=embed)

    elif isinstance(error, CommandOnCooldown):
        embed = disnake.Embed(
            description=strings["commandcooldown1"]+f"{error.retry_after:.2f}"+strings["commandcooldown2"],
            colour=get_colour(),
        )
        await ctx.reply(embed=embed)

    elif isinstance(error, CommandInvokeError):
        if (
            error.args[0]
            == "Command raised an exception: Forbidden: 403 Forbidden (error code: 50013): Missing Permissions"
        ):
            await ctx.em(
                strings["norighsbot"]
            )
        else:
            await unexpected(ctx, error)
    else:
        await unexpected(ctx, error)
