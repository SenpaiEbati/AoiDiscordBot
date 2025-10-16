import datetime
import disnake
from disnake.ext import commands
from core.utils import LanguageClass
import time

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="add",
                            description="Add Aoi青 to Your Server/Добавь Aoi青 на свой сервер")
    async def add(self,ctx: disnake.ApplicationCommandInteraction):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        embed = disnake.Embed(title=strings["add_1"],
                              description=strings["add_2"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
        )
        await ctx.response.send_message(embed=embed,
                        components=[
                            disnake.ui.Button(label=strings["add_3"],url=strings["add_4"]),]
                        )
    
    @commands.slash_command(name="avatar",
                            description="Look at your avatar!/Посмотри на свою аватарку!")
    async def avatar(self, ctx, user: disnake.Member = None):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        if not user:
            user = ctx.author

        user_icon = user.display_avatar
        if not user_icon:
            user_icon = disnake.DefaultAvatar.fuchsia

        embed = disnake.Embed(color=0x1E90FF,
                              title=strings["avatar_1"],
                              description=strings["avatar_2"] + user.display_name,
                              timestamp=datetime.datetime.now())
        embed.set_image(url=user_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
        )
        await ctx.send(embed=embed)
    
    @commands.slash_command(name="botinfo",
                            description="Info about bot Aoi青/Информация о боте Aoi青")
    async def botinfo(self, ctx):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        bot = self.bot.user

        bot_icon = bot.avatar
        if not bot_icon:
            bot_icon = disnake.DefaultAvatar.fuchsia

        if self.bot.status == disnake.Status.online:
            bot_status = strings["online"]
        elif self.bot.status == disnake.Status.idle:
            bot_status = strings["idle"]
        elif self.bot.status == disnake.Status.dnd:
            bot_status = strings["dnd"]
        else:
            bot_status = strings["offline"]

        embed = disnake.Embed(title=strings["botinfo_1"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_thumbnail(url=bot_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
        )
        
        if (await LanguageClass.get_lang(LanguageClass,ctx) == "en"):
            dateUTC = '%m.%d.%Y %I:%M %p'
        else:
            dateUTC = '%d.%m.%Y %H:%M'

        embed.add_field(name=strings["botname"] + f"{bot.name}", 
                        value=strings["botid"] + f"{bot.id}" + "\n" + 
                        strings["botstatus"] + f"{bot_status}" + "\n" +
                        strings["botcreated"] + f"`{bot.created_at.strftime(dateUTC)}`\n"+
                        strings["botdev"] + "senpaiebati(SenpaiEbati)" + "\n" + 
                        strings["botdisnake"] + "\n" +
                        strings["botmaintains_1"] + f"{len(self.bot.guilds)}" + strings["botmaintains_2"], inline=False)
        await ctx.send(embed=embed)

    @commands.slash_command(name="channelinfo",
                            description="Basic information about the channel/Основная информация о канале")
    async def channelinfo(self, ctx, channel: disnake.abc.GuildChannel = None):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        if not channel:
            channel = ctx.channel

        server = ctx.guild
        server_icon = server.icon.url if server.icon else None

        channel_name = channel.name
        channel_id = channel.id
        if (await LanguageClass.get_lang(LanguageClass,ctx) == "en"):
            dateUTC = '%m.%d.%Y %I:%M %p'
        else:
            dateUTC = '%d.%m.%Y %H:%M'
        creation_date = channel.created_at.strftime(dateUTC)
        
        channel_category = channel.category.name if channel.category else strings["none"]
        is_nsfw = strings["yes"] if channel.is_nsfw() else strings["no"]
        channel_type = str(channel.type)

        embed = disnake.Embed(title=strings["channelinfo_1"], color=0x1E90FF,timestamp=datetime.datetime.now())
        if server_icon:
            embed.set_thumbnail(url=server_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
        )
        embed.add_field(name=strings["channelname"] + f"{channel_name}", 
                        value=strings["channelid"] + f"{channel_id}\n" + 
                        strings["channeldate"] + f"`{creation_date}`\n" + 
                        strings["channelcateg"] + f"{channel_category}\n" + 
                        strings["channelnsfw"] + f"{is_nsfw}\n" + 
                        strings["channeltype"] + f"{channel_type}", inline=False)
        await ctx.send(embed=embed)
    
    @commands.slash_command(name="ping",
                            description="Discord API Gateway/REST ping and commands/Пинг Discord API Gateway/REST и команды")
    async def ping(self, ctx):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        # Функция для расчета задержки (ping) Discord API Gateway
        async def get_gateway_ping(self):
            start_time = time.time()
            gateway_info = await self.bot.http.request(disnake.http.Route('GET', '/gateway/bot'))
            end_time = time.time()
            ping = round((end_time - start_time) * 1000, 2)
            return ping
        # Функция для расчета задержки (ping) Discord API REST
        async def get_rest_ping(self):
            start_time = time.time()
            await self.bot.http.request(disnake.http.Route('GET', '/gateway/bot'))
            end_time = time.time()
            ping = round((end_time - start_time) * 1000, 2)
            return ping
        
        # Задержка (ping) Discord API Gateway
        gateway_ping = await get_gateway_ping(self)

        # Задержка (ping) Discord API REST
        rest_ping = await get_rest_ping(self)

        # Внутренние расчеты задержки для команды ping
        command_ping = round(self.bot.latency * 1000, 2)

        embed = disnake.Embed(color=0x1E90FF,
                              title=strings["ping_1"],
                              description=strings["ping_2"] + f"{command_ping}" + strings["pingms"] + "\n" + 
                              strings["ping_3"] + f"{gateway_ping}" + strings["pingms"] + "\n" + 
                              strings["ping_4"] + f"{rest_ping}" + strings["pingms"],
                              timestamp=datetime.datetime.now())
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
        )
        await ctx.send(embed=embed)

    @commands.slash_command(name="serverinfo",
                            description="Basic information about the server/Основная информация о сервере")
    async def serverinfo(self, ctx):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        
        server = ctx.guild

        server_icon = server.icon.url if server.icon else None

        server_name = server.name
        server_id = server.id
        server_owner = server.owner 

        if (await LanguageClass.get_lang(LanguageClass,ctx) == "en"):
            dateUTC = '%m.%d.%Y %I:%M %p'
        else:
            dateUTC = '%d.%m.%Y %H:%M'
        creation_date = server.created_at.strftime(dateUTC)
        verific_count = server.verification_level
        role_count = len(server.roles)
        
        bot_count = sum(1 for member in server.members if member.bot)
        
        online_count = sum(member.status == disnake.Status.online for member in server.members)
        idle_count = sum(member.status == disnake.Status.idle for member in server.members)
        dnd_count = sum(member.status == disnake.Status.dnd for member in server.members)
        offline_count = sum(member.status == disnake.Status.offline for member in server.members)

        member_count = f"● "+ strings["servertotal"] + f": **{server.member_count}**\n● "+strings["serverhumans"] + f": **{server.member_count - bot_count}**\n● "+ strings["serverbots"] +f": **{bot_count}**"
        status_count = f"● "+strings["online"]+f": **{online_count}**\n● "+strings["idle"]+f": **{idle_count}**\n● "+strings["dnd"]+f": **{dnd_count}**\n● "+strings["offline"]+f": **{offline_count}**"
        channel_count = f"● "+strings["serverchanneltotal"]+f": **{len(server.channels)}**\n● "+strings["serverchantexts"]+f": **{len(server.text_channels)}**\n● "+strings["serverchanforums"]+f": **{len(server.forum_channels)}**\n● "+strings["serverchanvoices"]+f": **{len(server.voice_channels)}**"

        embed = disnake.Embed(title=strings["serverinfo_1"], color=0x1E90FF,timestamp=datetime.datetime.now())
        if server_icon:
            embed.set_thumbnail(url=server_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
        )
        embed.add_field(name=strings["servername"]+f"{server_name}", 
                        value=strings["serverid"]+f"{server_id}\n" + 
                        strings["serverowner"] + f"{server_owner}\n" +
                        strings["serverdate"] + f"`{creation_date}`\n" + 
                        strings["serververif"] + f"{verific_count}\n" + 
                        strings["serverrolecount"] + f"{role_count}", inline=False)

        embed.add_field(name=strings["servermember"], value=member_count, inline=True)
        embed.add_field(name=strings["serverstatus"], value=status_count, inline=True)
        embed.add_field(name=strings["serverchannels"], value=channel_count, inline=True)

        await ctx.send(embed=embed)
    
    @commands.slash_command(name="userinfo",
                            description="Basic user information/Основная информация о пользователе")
    async def userinfo(self, ctx, user: disnake.Member = None):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        
        if not user:
            user = ctx.author

        user_icon = user.display_avatar
        if not user_icon:
            user_icon = disnake.DefaultAvatar.fuchsia

        if self.bot.status == disnake.Status.online:
            user_status = strings["online"]
        elif self.bot.status == disnake.Status.idle:
            user_status = strings["idle"]
        elif self.bot.status == disnake.Status.dnd:
            user_status = strings["dnd"]
        else:
            user_status = strings["offline"]

        if (await LanguageClass.get_lang(LanguageClass,ctx) == "en"):
            dateUTC = '%m.%d.%Y %I:%M %p'
        else:
            dateUTC = '%d.%m.%Y %H:%M'

        embed = disnake.Embed(title=strings["userinfo_1"] + f"{user.display_name}" + strings["userinfo_2"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_thumbnail(url=user_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
        )
        value_embed = strings["userid"] + f"{user.id}\n" + strings["userstatus"] + f"{user_status}\n" + strings["usercreated"] + f"`{user.created_at.strftime(dateUTC)}`\n" + strings["userjoined"] + f"`{user.joined_at.strftime(dateUTC)}`\n" + strings["useractiviti"] + f"{user.activity.name}"
        embed.add_field(name=strings["username"] + f"{user.name}({user.display_name})", 
                        value=value_embed, inline=False)
        
        await ctx.send(embed=embed)

class NoSlash_Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="add")
    async def add(self,ctx: disnake.ApplicationCommandInteraction):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        embed = disnake.Embed(title=strings["add_1"], 
                              description=strings["add_2"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
        )
        await ctx.reply(embed=embed,
                        components=[
                            disnake.ui.Button(label=strings["add_3"],url=strings["add_4"]),]
                            )

    @commands.command(aliases=["ava", "icon"])
    async def avatar(self, ctx, user: disnake.Member = None):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        if not user:
            user = ctx.author

        user_icon = user.display_avatar
        if not user_icon:
            user_icon = disnake.DefaultAvatar.fuchsia

        embed = disnake.Embed(color=0x1E90FF,
                              title=strings["avatar_1"],
                              description=strings["avatar_2"] + user.display_name,
                              timestamp=datetime.datetime.now())
        embed.set_image(url=user_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
        )
        await ctx.reply(embed=embed)

    @commands.command(aliases=["infobot","bot", "aoi","binfo"])
    async def botinfo(self, ctx):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        bot = self.bot.user

        bot_icon = bot.avatar
        if not bot_icon:
            bot_icon = disnake.DefaultAvatar.fuchsia

        if self.bot.status == disnake.Status.online:
            bot_status = strings["online"]
        elif self.bot.status == disnake.Status.idle:
            bot_status = strings["idle"]
        elif self.bot.status == disnake.Status.dnd:
            bot_status = strings["dnd"]
        else:
            bot_status = strings["offline"]

        embed = disnake.Embed(title=strings["botinfo_1"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_thumbnail(url=bot_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
        )
        
        if (await LanguageClass.get_lang(LanguageClass,ctx) == "en"):
            dateUTC = '%m.%d.%Y %I:%M %p'
        else:
            dateUTC = '%d.%m.%Y %H:%M'

        embed.add_field(name=strings["botname"] + f"{bot.name}", 
                        value=strings["botid"] + f"{bot.id}" + "\n" + 
                        strings["botstatus"] + f"{bot_status}" + "\n" +
                        strings["botcreated"] + f"`{bot.created_at.strftime(dateUTC)}`\n"+
                        strings["botdev"] + "senpaiebati(SenpaiEbati)" + "\n" + 
                        strings["botdisnake"] + "\n" +
                        strings["botmaintains_1"] + f"{len(self.bot.guilds)}" + strings["botmaintains_2"], inline=False)
        await ctx.reply(embed=embed)

    @commands.command(aliases=["channel","infochannel", "cinfo"])
    async def channelinfo(self, ctx, channel: disnake.abc.GuildChannel = None):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        if not channel:
            channel = ctx.channel

        server = ctx.guild
        server_icon = server.icon.url if server.icon else None

        channel_name = channel.name
        channel_id = channel.id
        if (await LanguageClass.get_lang(LanguageClass,ctx) == "en"):
            dateUTC = '%m.%d.%Y %I:%M %p'
        else:
            dateUTC = '%d.%m.%Y %H:%M'
        creation_date = channel.created_at.strftime(dateUTC)
        
        channel_category = channel.category.name if channel.category else strings["none"]
        is_nsfw = strings["yes"] if channel.is_nsfw() else strings["no"]
        channel_type = str(channel.type)

        embed = disnake.Embed(title=strings["channelinfo_1"], color=0x1E90FF,timestamp=datetime.datetime.now())
        if server_icon:
            embed.set_thumbnail(url=server_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
        )
        embed.add_field(name=strings["channelname"] + f"{channel_name}", 
                        value=strings["channelid"] + f"{channel_id}\n" + 
                        strings["channeldate"] + f"`{creation_date}`\n" + 
                        strings["channelcateg"] + f"{channel_category}\n" + 
                        strings["channelnsfw"] + f"{is_nsfw}\n" + 
                        strings["channeltype"] + f"{channel_type}", inline=False)
        await ctx.reply(embed=embed)

    @commands.command(name="ping")
    async def ping(self, ctx):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        # Функция для расчета задержки (ping) Discord API Gateway
        async def get_gateway_ping(self):
            start_time = time.time()
            gateway_info = await self.bot.http.request(disnake.http.Route('GET', '/gateway/bot'))
            end_time = time.time()
            ping = round((end_time - start_time) * 1000, 2)
            return ping
        # Функция для расчета задержки (ping) Discord API REST
        async def get_rest_ping(self):
            start_time = time.time()
            await self.bot.http.request(disnake.http.Route('GET', '/gateway/bot'))
            end_time = time.time()
            ping = round((end_time - start_time) * 1000, 2)
            return ping
        # Задержка (ping) Discord API Gateway
        gateway_ping = await get_gateway_ping(self)

        # Задержка (ping) Discord API REST
        rest_ping = await get_rest_ping(self)

        # Внутренние расчеты задержки для команды ping
        command_ping = round(self.bot.latency * 1000, 2)

        embed = disnake.Embed(color=0x1E90FF,
                              title=strings["ping_1"],
                              description=strings["ping_2"] + f"{command_ping}" + strings["pingms"] + "\n" + 
                              strings["ping_3"] + f"{gateway_ping}" + strings["pingms"] + "\n" + 
                              strings["ping_4"] + f"{rest_ping}" + strings["pingms"],
                              timestamp=datetime.datetime.now())
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
        )
        await ctx.reply(embed=embed)
    
    @commands.command(aliases=["server","infoserver", "sinfo"])
    async def serverinfo(self, ctx):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        
        server = ctx.guild

        server_icon = server.icon.url if server.icon else None

        server_name = server.name
        server_id = server.id
        server_owner = server.owner 

        if (await LanguageClass.get_lang(LanguageClass,ctx) == "en"):
            dateUTC = '%m.%d.%Y %I:%M %p'
        else:
            dateUTC = '%d.%m.%Y %H:%M'
        creation_date = server.created_at.strftime(dateUTC)
        verific_count = server.verification_level
        role_count = len(server.roles)

        bot_count = sum(1 for member in server.members if member.bot)
        
        online_count = sum(member.status == disnake.Status.online for member in server.members)
        idle_count = sum(member.status == disnake.Status.idle for member in server.members)
        dnd_count = sum(member.status == disnake.Status.dnd for member in server.members)
        offline_count = sum(member.status == disnake.Status.offline for member in server.members)

        member_count = f"● "+ strings["servertotal"] + f": **{server.member_count}**\n● "+strings["serverhumans"] + f": **{server.member_count - bot_count}**\n● "+ strings["serverbots"] +f": **{bot_count}**"
        status_count = f"● "+strings["online"]+f": **{online_count}**\n● "+strings["idle"]+f": **{idle_count}**\n● "+strings["dnd"]+f": **{dnd_count}**\n● "+strings["offline"]+f": **{offline_count}**"
        channel_count = f"● "+strings["serverchanneltotal"]+f": **{len(server.channels)}**\n● "+strings["serverchantexts"]+f": **{len(server.text_channels)}**\n● "+strings["serverchanforums"]+f": **{len(server.forum_channels)}**\n● "+strings["serverchanvoices"]+f": **{len(server.voice_channels)}**"

        embed = disnake.Embed(title=strings["serverinfo_1"], color=0x1E90FF,timestamp=datetime.datetime.now())
        if server_icon:
            embed.set_thumbnail(url=server_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
        )
        embed.add_field(name=strings["servername"]+f"{server_name}", 
                        value=strings["serverid"]+f"{server_id}\n" + 
                        strings["serverowner"] + f"{server_owner}\n" +
                        strings["serverdate"] + f"`{creation_date}`\n" + 
                        strings["serververif"] + f"{verific_count}\n" + 
                        strings["serverrolecount"] + f"{role_count}", inline=False)

        embed.add_field(name=strings["servermember"], value=member_count, inline=True)
        embed.add_field(name=strings["serverstatus"], value=status_count, inline=True)
        embed.add_field(name=strings["serverchannels"], value=channel_count, inline=True)

        await ctx.reply(embed=embed)
    
    @commands.command(aliases=["user", "member", "infouser","infomember","uinfo"])
    async def userinfo(self, ctx, user: disnake.Member = None):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        
        if not user:
            user = ctx.author

        user_icon = user.display_avatar
        if not user_icon:
            user_icon = disnake.DefaultAvatar.fuchsia

        if self.bot.status == disnake.Status.online:
            user_status = strings["online"]
        elif self.bot.status == disnake.Status.idle:
            user_status = strings["idle"]
        elif self.bot.status == disnake.Status.dnd:
            user_status = strings["dnd"]
        else:
            user_status = strings["offline"]

        if (await LanguageClass.get_lang(LanguageClass,ctx) == "en"):
            dateUTC = '%m.%d.%Y %I:%M %p'
        else:
            dateUTC = '%d.%m.%Y %H:%M'

        embed = disnake.Embed(title=strings["userinfo_1"] + f"{user.display_name}" + strings["userinfo_2"],
                              color=0x1E90FF,
                              timestamp=datetime.datetime.now())
        embed.set_thumbnail(url=user_icon)
        embed.set_footer(
            text=ctx.author.display_name + strings["req_info"]
        )
        value_embed = strings["userid"] + f"{user.id}\n" + strings["userstatus"] + f"{user_status}\n" + strings["usercreated"] + f"`{user.created_at.strftime(dateUTC)}`\n" + strings["userjoined"] + f"`{user.joined_at.strftime(dateUTC)}`\n" + strings["useractiviti"] + f"{user.activity}"
        embed.add_field(name=strings["username"] + f"{user.name}({user.display_name})", 
                        value=value_embed, inline=False)
        
        await ctx.reply(embed=embed)
    
def setup(bot: commands.Bot):
    bot.add_cog(Information(bot))
    bot.add_cog(NoSlash_Information(bot))