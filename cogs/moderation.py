from asyncio import sleep
from datetime import datetime, timedelta, timezone
import disnake
from disnake.ext import commands
from core.utils import LanguageClass, get_colour

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ban",
                            description="Command to ban a user permanently/Команда изгнания участника с сервера навечно без права вернуться",
                            default_member_permissions=disnake.Permissions(ban_members=True))
    async def ban(self, ctx, member: disnake.Member, *, reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        if ctx.author == member:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["ban_1"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                text=ctx.author.display_name + strings["mod_serv"]
            )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
        elif ctx.author.guild_permissions.ban_members:
            embed = disnake.Embed(title=strings["ban_title"], color=disnake.Color(0xff0000),timestamp=datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)

            if member.id != self.bot.user.id:
                dm_embed = disnake.Embed(title=strings["ban_title"], color=disnake.Color(0xff0000),timestamp=datetime.now())
                dm_embed.add_field(name=strings["ban_server"], value=ctx.guild.name, inline=False)
                dm_embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
                dm_embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
                await member.send(embed=dm_embed)

            await member.ban() 
        else:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["ban_2"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                text=ctx.author.display_name + strings["mod_serv"]
            )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)

    @commands.slash_command(name="clear",
                            description="Deleting messages by num, by location and by user/Удаление сообщений по кол., по каналам и по юзеру",
                            default_member_permissions=disnake.Permissions(manage_messages=True))
    async def clear(self, ctx, amount: int, channel: disnake.TextChannel = None, user: disnake.User = None):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        if ctx.author.guild_permissions.manage_messages:
            def is_target_message(message):
                if channel and message.channel != channel:
                    return False
                if user and message.author != user:
                    return False
                return True

            if amount <= 0 or amount > 500:
                embed = disnake.Embed(title=strings["clear_error"], 
                                      description=strings["clear_errordescrip"],
                                      color=disnake.Color(0xff0000),
                                      timestamp=datetime.now())
                embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
                await ctx.send(embed=embed)

                await sleep(5)
                await ctx.channel.purge(limit=1)
                return

            if channel and not user:
                deleted = await channel.purge(limit=amount, check=is_target_message)
                await ctx.response.defer()
            elif not channel and user:
                deleted = await ctx.channel.purge(limit=amount, check=is_target_message)
                await ctx.response.defer()
            elif channel and user:
                deleted = await channel.purge(limit=amount, check=is_target_message)
                await ctx.response.defer()
            else:
                deleted = await ctx.channel.purge(limit=amount)
                await ctx.response.defer()

            embed = disnake.Embed(title=strings["clear_title"], 
                                  description=f"{len(deleted)}" + strings["clear_discrip"],
                                  color=get_colour("colour"),
                                  timestamp=datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
        else:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["clear_rights"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
    
    @commands.slash_command(name="deafen",
                            description="Deafen the user in the voice channel/Отключает звук пользователю в голосовом канале",
                            default_member_permissions=disnake.Permissions(deafen_members=True))
    async def deafen(self, ctx, member: disnake.Member, *, reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        if ctx.author.guild_permissions.deafen_members:
            embed = disnake.Embed(title=strings["deafen_title"], color=disnake.Color(0xFFFF33), timestamp=datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)
            
            await member.edit(deafen=True)
        else:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["deafen_rightsdef"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
    
    @commands.slash_command(name="kick",
                            description="Kick out a server member/Выгнать участника сервера",
                            default_member_permissions=disnake.Permissions(kick_members=True))
    async def kick(self, ctx, member: disnake.Member, *, reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        if ctx.author == member:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["no_rights_kick1"],
                                  color=disnake.Color(0xff0000), 
                                  timestamp=datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)

        elif ctx.author.guild_permissions.kick_members:
            embed = disnake.Embed(title=strings["kick_title"], 
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)
            if member.id != self.bot.user.id:
                dm_embed = disnake.Embed(title=strings["kick_title"], 
                                        color=disnake.Color(0xff0000),
                                        timestamp=datetime.now())
                dm_embed.add_field(name=strings["ban_server"], value=ctx.guild.name, inline=False)
                dm_embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
                dm_embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
                await member.send(embed=dm_embed)

            await member.kick()
        else:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["no_rights_kick2"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)

    @commands.slash_command(name="mute",
                            description="Mute the user's microphone/Отключить микрофон пользователя",
                            default_member_permissions=disnake.Permissions(mute_members=True))
    async def mute(self, ctx, member: disnake.Member, *, reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        if ctx.author.guild_permissions.mute_members:
            embed = disnake.Embed(title=strings["mute_title"], 
                                  color=disnake.Color(0xFFFF33),
                                  timestamp=datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)
            
            await member.edit(mute=True)
        else:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["no_rights_mute"], 
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.send(embed=embed)
            
            await sleep(5)
            await ctx.channel.purge(limit=1)
    
    @commands.slash_command(name="timecleaning",
                            description="Same as Clear, but with a time stamp/Тоже самое что и \"Clear\" только с указанием времени",
                            default_member_permissions=disnake.Permissions(manage_messages=True))
    async def timecleaning(self, ctx, amount: int, hours: int = 0, channel: disnake.TextChannel = None, user: disnake.User = None):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        if ctx.author.guild_permissions.manage_messages:
            def is_target_message(message):
                if channel and message.channel != channel:
                    return False
                
                if user and message.author != user:
                    return False
                
                if hours > 0:
                    time_limit = datetime.utcnow() - timedelta(hours=hours)
                    time_limit = time_limit.replace(tzinfo=timezone.utc)
                    return message.created_at > time_limit
                
                return True

            if amount <= 0 or amount > 500:
                embed = disnake.Embed(title=strings["clear_error"], 
                                      description=strings["clear_errordescrip"],
                                      color=disnake.Color(0xff0000),
                                      timestamp=datetime.now())
                embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
                await ctx.send(embed=embed)

                await sleep(5)
                await ctx.channel.purge(limit=1)
                return

            if channel and not user:
                deleted = await channel.purge(limit=amount, check=is_target_message)
                await ctx.response.defer()
            elif not channel and user:
                deleted = await ctx.channel.purge(limit=amount, check=is_target_message)
                await ctx.response.defer()
            elif channel and user:
                deleted = await channel.purge(limit=amount, check=is_target_message)
                await ctx.response.defer()
            else:
                deleted = await ctx.channel.purge(limit=amount,check=is_target_message)
                await ctx.response.defer()

            if len(deleted) == 0:
                embed = disnake.Embed(title=strings["clear_error"], 
                                      description=strings["clear_errordescrip"],
                                      color=disnake.Color(0xff0000),
                                      timestamp=datetime.now())
                embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
                await ctx.send(embed=embed)
            else:
                embed = disnake.Embed(title=strings["clear_title"],
                                      description=f"{len(deleted)}" + strings["clear_discrip"],
                                      color=get_colour("colour"),
                                      timestamp=datetime.now())
                embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
                await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
        else:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["clear_rights"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
    
    @commands.slash_command(name="timeout",
                            description="Encourages user to reflect on their behavior/Побуждает пользователя задуматься о своем поведении",
                            default_member_permissions=disnake.Permissions(moderate_members=True))
    async def timeout(self, ctx, member: disnake.Member, *,days=0,hours=0,minutes=0,seconds=0,reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        if ctx.author.guild_permissions.moderate_members:
            if max(ctx.author.roles) > max(member.roles):
                if isinstance(days,int) and isinstance(hours,int) and isinstance(minutes,int) and isinstance(seconds,int):
                    if days == hours == minutes == seconds == 0:
                        hours = 6
                        time = hours * 60 * 60 
                    else:
                        time = int(seconds) + int(minutes) * 60 + int(hours) * 60 * 60 + int(days) * 24 * 60 * 60
                
                    embed = disnake.Embed(title=strings["timeout_title"], color=disnake.Color(0xff0000),timestamp=datetime.now())
                    embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
                    embed.add_field(name=strings["how_much"], value=f"{days}d {hours}h {minutes}m {seconds}s", inline=False)
                    embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
                    embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
                    await ctx.send(embed=embed)
                    if member.id != self.bot.user.id:
                        dm_embed = disnake.Embed(title=strings["timeout_title"], color=disnake.Color(0xff0000),timestamp=datetime.now())
                        dm_embed.add_field(name=strings["ban_server"], value=ctx.guild.name, inline=False)
                        dm_embed.add_field(name=strings["how_much"], value=f"{days}d {hours}h {minutes}m {seconds}s", inline=False)
                        dm_embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
                        dm_embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
                        await member.send(embed=dm_embed)
                        
                    await member.edit(timeout=time)
                else:
                    embed = disnake.Embed(title=strings["error_timeout"], 
                                          description=strings["error_timeout_discrip"],
                                          color=disnake.Color(0xff0000),
                                          timestamp=datetime.now())
                    embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
                    await ctx.send(embed=embed)

                    await sleep(5)
                    await ctx.channel.purge(limit=1)
            else:
                embed = disnake.Embed(title=strings["no_rights"], 
                                      description=strings["timeout_rights_1"],
                                      color=disnake.Color(0xff0000),
                                      timestamp=datetime.now())
                embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
                await ctx.send(embed=embed)

                await sleep(5)
                await ctx.channel.purge(limit=1)
        else:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["timeout_rights_1"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
    
    @commands.slash_command(name="unban",
                            description="Command to unban a user/Команда, снимающая запрет нахождения на сервере с пользователя",
                            default_member_permissions=disnake.Permissions(ban_members=True))
    async def unban(self, ctx, member: disnake.Member, *, reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        if ctx.author.guild_permissions.ban_members:
            embed = disnake.Embed(title=strings["unban_title"], color=disnake.Color(0x32CD32),timestamp=datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)
            if member.id != self.bot.user.id:
                dm_embed = disnake.Embed(title=strings["unban_title"], color=disnake.Color(0x32CD32),timestamp=datetime.now())
                dm_embed.add_field(name=strings["ban_server"], value=ctx.guild.name, inline=False)
                dm_embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
                dm_embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
                await member.send(embed=dm_embed)

            await member.unban() 
        else:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["unban_rights"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
    
    @commands.slash_command(name="undeafen",
                            description="Undeafen the user in the voice channel/Включает звук пользователю в голосовом канале",
                            default_member_permissions=disnake.Permissions(deafen_members=True))
    async def undeafen(self, ctx, member: disnake.Member, *, reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        if ctx.author.guild_permissions.deafen_members:
            embed = disnake.Embed(title=strings["undeafen_title"], color=disnake.Color(0x32CD32),timestamp=datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)

            await member.edit(deafen=False)
        else:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["undeafen_rights"], 
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
    
    @commands.slash_command(name="unmute",
                            description="Unmute the user's microphone/Включить микрофон пользователя",
                            default_member_permissions=disnake.Permissions(mute_members=True))
    async def unmute(self, ctx, member: disnake.Member, *, reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        if ctx.author.guild_permissions.mute_members:
            embed = disnake.Embed(title=strings["unmute_title"], color=disnake.Color(0x32CD32),timestamp=datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.send(embed=embed)

            await member.edit(mute=False)
        else:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["unmute_rights"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
    
    @commands.slash_command(name="untimeout",
                            description="Takes the user out of timeout/Снимает с пользователя тайм-аут",
                            default_member_permissions=disnake.Permissions(moderate_members=True))
    async def untimeout(self, ctx, member: disnake.Member, *, reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        
        if ctx.author.guild_permissions.moderate_members:
            if max(ctx.author.roles) > max(member.roles):
                embed = disnake.Embed(title=strings["untimeout_title"], color=disnake.Color(0x32CD32),timestamp=datetime.now())
                embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
                embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
                embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
                await ctx.send(embed=embed)

                if member.id != self.bot.user.id:
                    dm_embed = disnake.Embed(title=strings["untimeout_title"], color=disnake.Color(0x32CD32),timestamp=datetime.now())
                    dm_embed.add_field(name=strings["ban_server"], value=ctx.guild.name, inline=False)
                    dm_embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
                    dm_embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
                    await member.send(embed=dm_embed)

                await member.edit(timeout=None)
            else:
                embed = disnake.Embed(title=strings["error_untimeout"],
                                      description=strings["error_untimeout_discrip"], 
                                      color=disnake.Color(0xff0000),
                                      timestamp=datetime.now())
                embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
                await ctx.send(embed=embed)

                await sleep(5)
                await ctx.channel.purge(limit=1)
        else:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["untimeout_rights_discrip"], 
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
    
    @commands.slash_command(name="warn",
                            description="Charges the participant with a warning/Начисляет участнику предупреждение",
                            default_member_permissions=disnake.Permissions(moderate_members=True))
    async def warn(self, ctx, member: disnake.Member, *, reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        
        if ctx.author.guild_permissions.moderate_members:
            embed = disnake.Embed(title=strings["warn_title"], color=disnake.Color(0xFFFF33),timestamp=datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.send(member.mention,embed=embed)

            if member.id != self.bot.user.id:
                dm_embed = disnake.Embed(title=strings["warn_title"], color=disnake.Color(0xFFFF33),timestamp=datetime.now())
                dm_embed.add_field(name=strings["ban_server"], value=ctx.guild.name, inline=False)
                dm_embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
                dm_embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
                await member.send(embed=dm_embed)
        else:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["warn_rights"], 
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)

class NoSlash_Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    

    @commands.command(name="ban",
                      default_member_permissions=disnake.Permissions(ban_members=True))
    async def ban(self, ctx, member: disnake.Member, *, reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        if ctx.author == member:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["ban_1"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                text=ctx.author.display_name + strings["mod_serv"]
            )
            await ctx.reply(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
        elif ctx.author.guild_permissions.ban_members:
            embed = disnake.Embed(title=strings["ban_title"], color=disnake.Color(0xff0000),timestamp=datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.reply(embed=embed)
            
            if member.id != self.bot.user.id:
                dm_embed = disnake.Embed(title=strings["ban_title"], color=disnake.Color(0xff0000),timestamp=datetime.now())
                dm_embed.add_field(name=strings["ban_server"], value=ctx.guild.name, inline=False)
                dm_embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
                dm_embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
                await member.send(embed=dm_embed)

            await member.ban() 
        else:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["ban_2"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                text=ctx.author.display_name + strings["mod_serv"]
            )
            await ctx.reply(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
    
    @commands.command(aliases=["cl","delete","del","clean","cleaning"],
                      default_member_permissions=disnake.Permissions(manage_messages=True))
    async def clear(self, ctx, amount: int, *,channel: disnake.TextChannel = None, user: disnake.User = None):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        if ctx.author.guild_permissions.manage_messages:
            def is_target_message(message):
                if channel and message.channel != channel:
                    return False
                if user and message.author != user:
                    return False
                return True
            amount += 1
            if amount <= 0 or amount > 500:
                embed = disnake.Embed(title=strings["clear_error"], 
                                      description=strings["clear_errordescrip"],
                                      color=disnake.Color(0xff0000),
                                      timestamp=datetime.now())
                embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
                await ctx.send(embed=embed)

                await sleep(5)
                await ctx.channel.purge(limit=1)
                return
            
            if channel and not user:
                deleted = await channel.purge(limit=amount, check=is_target_message)
            elif not channel and user:
                deleted = await ctx.channel.purge(limit=amount, check=is_target_message)
            elif channel and user:
                deleted = await channel.purge(limit=amount, check=is_target_message)
            else:
                deleted = await ctx.channel.purge(limit=amount)
            
            embed = disnake.Embed(title=strings["clear_title"], 
                                  description=f"{len(deleted) - 1}" + strings["clear_discrip"],
                                  color=get_colour("colour"),
                                  timestamp=datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.send(embed=embed)
            await sleep(5)
            await ctx.channel.purge(limit=1)
        else:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["clear_rights"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
    
    @commands.command(aliases=["df", "stun"],
                    default_member_permissions=disnake.Permissions(deafen_members=True))
    async def deafen(self, ctx, member: disnake.Member, *, reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        if ctx.author.guild_permissions.deafen_members:
            embed = disnake.Embed(title=strings["deafen_title"], color=disnake.Color(0xFFFF33), timestamp=datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.reply(embed=embed)
            
            await member.edit(deafen=True)
        else:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["deafen_rightsdef"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.reply(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
    
    @commands.command(aliases=["expel", "kk"],
                            default_member_permissions=disnake.Permissions(kick_members=True))
    async def kick(self, ctx, member: disnake.Member, *, reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        
        if ctx.author == member:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["no_rights_kick1"],
                                  color=disnake.Color(0xff0000), 
                                  timestamp=datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.reply(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)

        elif ctx.author.guild_permissions.kick_members:
            embed = disnake.Embed(title=strings["kick_title"], 
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.reply(embed=embed)

            if member.id != self.bot.user.id:
                dm_embed = disnake.Embed(title=strings["kick_title"], 
                                        color=disnake.Color(0xff0000),
                                        timestamp=datetime.now())
                dm_embed.add_field(name=strings["ban_server"], value=ctx.guild.name, inline=False)
                dm_embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
                dm_embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
                await member.send(embed=dm_embed)

            await member.kick()
        else:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["no_rights_kick2"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.reply(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
    
    @commands.command(aliases=["silence"],
                            default_member_permissions=disnake.Permissions(mute_members=True))
    async def mute(self, ctx, member: disnake.Member, *, reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        
        if ctx.author.guild_permissions.mute_members:
            embed = disnake.Embed(title=strings["mute_title"], 
                                  color=disnake.Color(0xFFFF33),
                                  timestamp=datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.reply(embed=embed)
            
            await member.edit(mute=True)
        else:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["no_rights_mute"], 
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.reply(embed=embed)
            
            await sleep(5)
            await ctx.channel.purge(limit=1)
    
    @commands.command(aliases=["tcl", "tcn","timeclean", "cleanintime","clearintime"],
                        description="Same as Clear, but with a time stamp/Тоже самое что и \"Clear\" только с указанием времени",
                        default_member_permissions=disnake.Permissions(manage_messages=True))
    async def timecleaning(self, ctx, amount: int, hours: int = 0, channel: disnake.TextChannel = None, user: disnake.User = None):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        
        if ctx.author.guild_permissions.manage_messages:
            def is_target_message(message):
                if channel and message.channel != channel:
                    return False
                
                if user and message.author != user:
                    return False
                
                if hours > 0:
                    time_limit = datetime.utcnow() - timedelta(hours=hours)
                    time_limit = time_limit.replace(tzinfo=timezone.utc)
                    return message.created_at > time_limit
                
                return True
            
            amount += 1
            if amount <= 0 or amount > 500:
                embed = disnake.Embed(title=strings["clear_error"], 
                                      description=strings["clear_errordescrip"],
                                      color=disnake.Color(0xff0000),
                                      timestamp=datetime.now())
                embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
                await ctx.send(embed=embed)

                await sleep(5)
                await ctx.channel.purge(limit=1)
                return

            if channel and not user:
                deleted = await channel.purge(limit=amount, check=is_target_message)
            elif not channel and user:
                deleted = await ctx.channel.purge(limit=amount, check=is_target_message)
            elif channel and user:
                deleted = await channel.purge(limit=amount, check=is_target_message)
            else:
                deleted = await ctx.channel.purge(limit=amount,check=is_target_message)

            if len(deleted) == 0:
                embed = disnake.Embed(title=strings["clear_error"], 
                                      description=strings["clear_errordescrip"],
                                      color=disnake.Color(0xff0000),
                                      timestamp=datetime.now())
                embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
                await ctx.send(embed=embed)
            else:
                embed = disnake.Embed(title=strings["clear_title"],
                                      description=f"{len(deleted) - 1}" + strings["clear_discrip"],
                                      color=get_colour("colour"),
                                      timestamp=datetime.now())
                embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
                await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
        else:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["clear_rights"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                    text=ctx.author.display_name + strings["mod_serv"]
                )
            await ctx.send(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
    
    @commands.command(aliases=["tt"],
                            default_member_permissions=disnake.Permissions(moderate_members=True))
    async def timeout(self, ctx, member: disnake.Member, *,days=0,hours=0,minutes=0,seconds=0,reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        
        if ctx.author.guild_permissions.moderate_members:
            if max(ctx.author.roles) > max(member.roles):
                if isinstance(days,int) and isinstance(hours,int) and isinstance(minutes,int) and isinstance(seconds,int):
                    if days == hours == minutes == seconds == 0:
                        hours = 6
                        time = hours * 60 * 60 
                    else:
                        time = int(seconds) + int(minutes) * 60 + int(hours) * 60 * 60 + int(days) * 24 * 60 * 60
                
                    embed = disnake.Embed(title=strings["timeout_title"], color=disnake.Color(0xff0000),timestamp=datetime.now())
                    embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
                    embed.add_field(name=strings["how_much"], value=f"{days}d {hours}h {minutes}m {seconds}s", inline=False)
                    embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
                    embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
                    await ctx.reply(embed=embed)

                    if member.id != self.bot.user.id:
                        dm_embed = disnake.Embed(title=strings["timeout_title"], color=disnake.Color(0xff0000),timestamp=datetime.now())
                        dm_embed.add_field(name=strings["ban_server"], value=ctx.guild.name, inline=False)
                        dm_embed.add_field(name=strings["how_much"], value=f"{days}d {hours}h {minutes}m {seconds}s", inline=False)
                        dm_embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
                        dm_embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
                        await member.send(embed=dm_embed)
                    
                    await member.edit(timeout=time)
                else:
                    embed = disnake.Embed(title=strings["error_timeout"], 
                                          description=strings["error_timeout_discrip"],
                                          color=disnake.Color(0xff0000),
                                          timestamp=datetime.now())
                    embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
                    await ctx.reply(embed=embed)

                    await sleep(5)
                    await ctx.channel.purge(limit=1)
            else:
                embed = disnake.Embed(title=strings["no_rights"], 
                                      description=strings["timeout_rights_1"],
                                      color=disnake.Color(0xff0000),
                                      timestamp=datetime.now())
                embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
                await ctx.reply(embed=embed)

                await sleep(5)
                await ctx.channel.purge(limit=1)
        else:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["timeout_rights_1"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
            await ctx.reply(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
    
    @commands.command(name="unban",
                            default_member_permissions=disnake.Permissions(ban_members=True))
    async def unban(self, ctx, member: disnake.Member, *, reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        
        if ctx.author.guild_permissions.ban_members:
            embed = disnake.Embed(title=strings["unban_title"], color=disnake.Color(0x32CD32),timestamp=datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.reply(embed=embed)
            
            if member.id != self.bot.user.id:
                dm_embed = disnake.Embed(title=strings["unban_title"], color=disnake.Color(0x32CD32),timestamp=datetime.now())
                dm_embed.add_field(name=strings["ban_server"], value=ctx.guild.name, inline=False)
                dm_embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
                dm_embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
                await member.send(embed=dm_embed)

            await member.unban() 
        else:
            embed = disnake.Embed(title=strings["no_rights"], 
                                  description=strings["unban_rights"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
            await ctx.reply(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
    
    @commands.command(aliases=["undf"],
                            default_member_permissions=disnake.Permissions(deafen_members=True))
    async def undeafen(self, ctx, member: disnake.Member, *, reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        
        if ctx.author.guild_permissions.deafen_members:
            embed = disnake.Embed(title=strings["undeafen_title"], color=disnake.Color(0x32CD32),timestamp=datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.reply(embed=embed)

            await member.edit(deafen=False)
        else:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["undeafen_rights"], 
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
            await ctx.reply(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
    
    @commands.command(name="unmute",
                            default_member_permissions=disnake.Permissions(mute_members=True))
    async def unmute(self, ctx, member: disnake.Member, *, reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)
        
        if ctx.author.guild_permissions.mute_members:
            embed = disnake.Embed(title=strings["unmute_title"], color=disnake.Color(0x32CD32),timestamp=datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.reply(embed=embed)

            await member.edit(mute=False)
        else:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["unmute_rights"],
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
            await ctx.reply(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
    
    @commands.command(aliases=["untt"],
                            default_member_permissions=disnake.Permissions(moderate_members=True))
    async def untimeout(self, ctx, member: disnake.Member, *, reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        if ctx.author.guild_permissions.moderate_members:
            if max(ctx.author.roles) > max(member.roles):
                embed = disnake.Embed(title=strings["untimeout_title"], color=disnake.Color(0x32CD32),timestamp=datetime.now())
                embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
                embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
                embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
                await ctx.reply(embed=embed)
                
                if member.id != self.bot.user.id:
                    dm_embed = disnake.Embed(title=strings["untimeout_title"], color=disnake.Color(0x32CD32),timestamp=datetime.now())
                    dm_embed.add_field(name=strings["ban_server"], value=ctx.guild.name, inline=False)
                    dm_embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
                    dm_embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
                    await member.send(embed=dm_embed)

                await member.edit(timeout=None)
            else:
                embed = disnake.Embed(title=strings["error_untimeout"],
                                      description=strings["error_untimeout_discrip"], 
                                      color=disnake.Color(0xff0000),
                                      timestamp=datetime.now())
                embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
                await ctx.reply(embed=embed)

                await sleep(5)
                await ctx.channel.purge(limit=1)
        else:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["untimeout_rights_discrip"], 
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
            await ctx.reply(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)
    
    @commands.command(name="warn",
                            default_member_permissions=disnake.Permissions(moderate_members=True))
    async def warn(self, ctx, member: disnake.Member, *, reason="-"):
        lang = await LanguageClass.get_lang(LanguageClass,ctx)
        strings = await LanguageClass.get_strings(LanguageClass,lang)

        if ctx.author.guild_permissions.moderate_members:
            embed = disnake.Embed(title=strings["warn_title"], color=disnake.Color(0xFFFF33),timestamp=datetime.now())
            embed.add_field(name=strings["ban_member"], value=member.mention, inline=False)
            embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
            embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
            await ctx.send(member.mention,embed=embed)
            
            if member.id != self.bot.user.id:
                dm_embed = disnake.Embed(title=strings["warn_title"], color=disnake.Color(0xFFFF33),timestamp=datetime.now())
                dm_embed.add_field(name=strings["ban_server"], value=ctx.guild.name, inline=False)
                dm_embed.add_field(name=strings["ban_reason"], value=reason, inline=False)
                dm_embed.add_field(name=strings["ban_from"], value=ctx.author.mention, inline=False)
                await member.send(embed=dm_embed)
        else:
            embed = disnake.Embed(title=strings["no_rights"],
                                  description=strings["warn_rights"], 
                                  color=disnake.Color(0xff0000),
                                  timestamp=datetime.now())
            embed.set_footer(
                        text=ctx.author.display_name + strings["mod_serv"]
                    )
            await ctx.reply(embed=embed)

            await sleep(5)
            await ctx.channel.purge(limit=1)

def setup(bot: commands.Bot):
    bot.add_cog(Moderation(bot))
    bot.add_cog(NoSlash_Moderation(bot))