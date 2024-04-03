from __future__ import annotations

import asyncio
import inspect
from typing import TYPE_CHECKING, Any, Dict, List, Optional

import disnake
import disnake.abc
import disnake.utils
from disnake.ext.commands import Command, Context, view
from disnake.message import Message

from core.utils import get_colour

if TYPE_CHECKING:
    from disnake.state import ConnectionState

    from core.bot import AoiBot

MISSING: Any = disnake.utils.MISSING


class Context(Context):
    def __init__(
        self,
        *,
        message: Message,
        bot: AoiBot,
        view: view.StringView,
        args: List[Any] = MISSING,
        kwargs: Dict[
            str,
            Any,
        ] = MISSING,
        prefix: Optional[str] = None,
        command: Optional[Command] = None,
        invoked_with: Optional[str] = None,
        invoked_parents: List[str] = MISSING,
        invoked_subcommand: Optional[Command] = None,
        subcommand_passed: Optional[str] = None,
        command_failed: bool = False,
        current_parameter: Optional[inspect.Parameter] = None,
    ):
        self.message: Message = message
        self.bot: AoiBot = bot
        self.args: List[Any] = args or []
        self.kwargs: Dict[
            str,
            Any,
        ] = (
            kwargs or {}
        )
        self.prefix: Optional[str] = prefix
        self.command: Optional[Command] = command
        self.view: view.StringView = view
        self.invoked_with: Optional[str] = invoked_with
        self.invoked_parents: List[str] = invoked_parents or []
        self.invoked_subcommand: Optional[Command] = invoked_subcommand
        self.subcommand_passed: Optional[str] = subcommand_passed
        self.command_failed: bool = command_failed
        self.current_parameter: Optional[inspect.Parameter] = current_parameter
        self._state: ConnectionState = self.message._state

    async def em(self, message, **kwargs):
        return await super().send(
            embed=disnake.Embed(description=message, colour=get_colour()), **kwargs
        )

    async def send(self, content: any = None, **kwargs):
        perms = self.channel.permissions_for(self.me)
        if not perms.send_messages:
            try:
                await self.author.send(
                    "I can't send any messages in that channel. \nPlease give me sufficient permissions to do so."
                )
            except disnake.Forbidden:
                pass
            return

        require_embed_perms = kwargs.pop("embed_perms", False)
        if require_embed_perms and not perms.embed_links:
            kwargs = {}
            content = (
                "Oops! I need **Embed Links** permission to work properly. \n"
                "Please tell a server admin to grant me that permission."
            )
        if isinstance(content, disnake.Embed):
            kwargs["embed"] = content
            content = None
        if isinstance(content, disnake.File):
            kwargs["file"] = content
            content = None

        msg = await super().send(content, **kwargs)
        self.bot.data[self.message] = {"bot": msg}
        
        return msg

    async def reply(self, content: any = None, **kwargs):
        perms = self.channel.permissions_for(self.me)
        if not perms.send_messages:
            try:
                await self.author.send(
                    "I can't send any messages in that channel. \nPlease give me sufficient permissions to do so."
                )
            except disnake.Forbidden:
                pass
            return

        require_embed_perms = kwargs.pop("embed_perms", False)
        if require_embed_perms and not perms.embed_links:
            kwargs = {}
            content = (
                "Oops! I need **Embed Links** permission to work properly. \n"
                "Please tell a server admin to grant me that permission."
            )
        if isinstance(content, disnake.Embed):
            kwargs["embed"] = content
            content = None
        if isinstance(content, disnake.File):
            kwargs["file"] = content
            content = None

        msg = await super().reply(content, **kwargs)
        self.bot.data[self.message] = {"bot": msg}
        
        return msg
