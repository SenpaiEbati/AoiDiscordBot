from __future__ import annotations

from stability_sdk import client

import asyncio
import datetime
import os
from typing import List

import aiohttp
from disnake import (
    Activity,
    ActivityType,
    AllowedMentions,
    Intents,
    Message,
    __version__,
)
from disnake.ext.commands import AutoShardedBot, CommandSyncFlags, when_mentioned_or
from disnake.ext.tasks import loop
from core.utils import LanguageClass
from .constants import (
    BOT_TOKEN,
    STABILITY_KEY
)
from .context import Context
from .database import Database
from .errors import error_handler
from .utils import run_check, run_executed, run_precheck
from .utils.commands.eval import run_eval

class AoiBot(AutoShardedBot):
    def __init__(self):

        intents=Intents.default()
        intents.message_content = True
        intents.voice_states = True
        intents.members = True
        intents.presences = True
        intents.guild_messages = True
        intents.reactions = True

        super().__init__(
            command_prefix=self.get_prefix,
            intents=intents,
            case_insensitive=True,
            strip_after_prefix=True,
            owner_ids=[397794392896700430],
            allowed_mentions=AllowedMentions.none(),
            help_command=None,
            command_sync_flags=CommandSyncFlags(sync_commands=True)
        )

        self.launch_time = datetime.datetime.now()
        self.COGS: list = list()
        self.time_limit: int = 120
        self.discord_colour = 0x36393F
        self.data = {}
        
        self.add_check(self.bot_check)
        self.after_invoke(self.after_command)
        self.loop.create_task(self.connect_database())

        for file in os.listdir("./cogs/"):
            if not file.startswith("_"):
                self.COGS.append(f"cogs.{file}")
        
    async def connect_database(self):
        self.db = await Database.create()
    
    async def find_prefix(self, user_id: int) -> List[str]:
        result = await self.db.fetchone(
            "SELECT prefixes FROM prefix WHERE user_id = ?", (user_id,)
        )

        if not result:
            return ["a."]
        return result[0].split(" | ")

    async def insert_prefix(self, user_id: int, prefixes: List[str]) -> None:
        prefixes = " | ".join(prefixes)

        result = await self.db.fetchone(
            "SELECT prefixes FROM prefix WHERE user_id = ?", (user_id,)
        )
        if not result:
            return await self.db.update(
                "INSERT INTO prefix VALUES (?, ?)", (user_id, prefixes)
            )
        await self.db.update(
            "UPDATE prefix SET prefixes = ? where user_id = ?", (prefixes, user_id)
        )

    async def get_prefix(self, message: Message) -> List[str]:
        prefixes = await self.find_prefix(message.author.id)
        return when_mentioned_or(*prefixes)(self, message)

    async def process_commands(self, message: Message) -> None:
        ctx = await self.get_context(message, cls=Context)
        await self.invoke(ctx)

    def setup(self) -> None:
        print("Cogs:")
        print(", ".join(self.COGS))
        for filename in self.COGS:
            if filename.endswith("py"):
                self.load_extension(f"{filename[:-3]}")
            else:
                self.load_extension(filename)
        print("-----------------------------------")
        print(
            f"Loaded Cogs Successfully! Total Cogs: {len(self.COGS)}\n-----------------------------------"
        )

    @loop(seconds=60)
    async def log_data(self) -> None:
        await self.db.update(
            "INSERT INTO general_data VALUES (?, ?, ?, ?, ?, ?)",
            (
                datetime.datetime.now().isoformat(),
                self.latency * 1000,
                len(self.users),
                len(self.guilds),
                len([c for c in self.get_all_channels()]),
                __version__,
            ),
        )

    @log_data.before_loop
    async def log_data_pre(self) -> None:
        await self.wait_until_ready()
    
    @loop(seconds=540)
    async def update_presence(self) -> None:
        await self.change_presence(
            activity=Activity(
                type=ActivityType.playing, name="🟦 a.help | ping me for prefix"
            )
        )
        await asyncio.sleep(180)
        await self.change_presence(
            activity=Activity(
                type=ActivityType.playing,
                name=f"🩵 {len(self.users)} Members in {len(self.guilds)} Servers!",
            )
        )
        await asyncio.sleep(180)
        await self.change_presence(
            activity=Activity(
                type=ActivityType.playing,
                name=f"🆒 {len([e for e in self.commands if not e.hidden])} commands",
            )
        )
        await asyncio.sleep(180)

    def run(self) -> None:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("Setting up...")
        print("-----------------------------------")
        self.setup()
        print("Running the bot...")
        print("-----------------------------------")
        try:
            self.loop.run_until_complete(super().start(BOT_TOKEN, reconnect=True))
        except KeyboardInterrupt:
            self.loop.run_until_complete(super().close())
            # cancel all tasks lingering
        finally:
            self.loop.close()

    async def on_ready(self) -> None:
        if self.command_sync_flags != None:
            print("-----------------------------------")
        else:
            print("Command synchronization task is not performed")
            print("-----------------------------------")
        self.update_presence.start()
        print("Client Ready!")
        print("-----------------------------------")
        self.log_data.start()
        print("Guilds:")
        guild_ids = [guild.id for guild in self.guilds]
        print(guild_ids)
        print("-----------------------------------")
        await LanguageClass.loadjsonmain(LanguageClass, './aoibot/localizations')
        print("Language pack loaded!")
        print("-----------------------------------")
        # Set up our connection to the API.
        self.stability_api = client.StabilityInference(
            key=STABILITY_KEY, # API Key reference.
            verbose=True, # Print debug messages.
            engine="stable-diffusion-xl-1024-v1-0", # Set the engine to use for generation.
            # Check out the following link for a list of available engines: https://platform.stability.ai/docs/features/api-parameters#engine
        )
        print("Stability Ai Client Ready!")
        print("-----------------------------------")
        selected_channel = self.get_guild(1152151796870025228).get_channel(
            1223514729532751882
        )
        self.chan = selected_channel
        self.dev = await self.fetch_user(397794392896700430)
        guild = self.get_guild(1152151796870025228)
        role = guild.get_role(1213359286810574919)
        print("Admins:")
        for k in role.members:
            print(k)
            self.owner_ids.append(k.id)
        print("-----------------------------------")
        self.client = aiohttp.ClientSession()
    
    async def on_message_edit(self, before: Message, after: Message) -> None:
        if before.author.bot:
            return
        if before.content == after.content:
            return
        time_difference = after.edited_at - before.created_at
        if time_difference.seconds > self.time_limit:
            return
        ctx = await self.get_context(after)
        if ctx.command:
            if before in self.data:
                if ctx.command.name in ["eval", "evaldir", "evalreturn"]:
                    code = " ".join(after.content.split(" ")[1:])
                    msg = await run_eval(ctx, code, eval=ctx.command.name)
                    try:
                        bot_msg = self.data[before]["bot"]
                        return await bot_msg.edit(content=msg)
                    except Exception:
                        return
            await self.process_commands(after)
        
    async def on_command_error(self, context, exception) -> None:
        await error_handler(context, exception)
    
    async def on_guild_remove(self, guild) -> None:
        selected_channel1 = self.get_guild(1152151796870025228).get_channel(
            1223514729532751882
        )
        await selected_channel1.send(f"I have left {guild.name}.")
    
    async def bot_check(self, ctx) -> bool:
        return await run_check(self, ctx)

    async def on_message(self, message) -> None:
        await run_precheck(self, message)
        return await super().on_message(message)
    
    async def after_command(self, ctx):
        await run_executed(ctx)

    async def close(self) -> None:
        await self.client.close()
        return await super().close()