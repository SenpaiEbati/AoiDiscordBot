import datetime
import disnake
from disnake.ext import commands
from cogs._class.LanguageClass import LanguageClass

class Slash_Userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(name="userinfo",
                            description="Basic user information/Основная информация о пользователе")
    async def userinfo(self, ctx, user: disnake.Member = None):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))
        
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

        if (LanguageClass.get_lang(LanguageClass,ctx) == "en"):
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
        
        await ctx.send(embed=embed)

class NoSlash_Userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="userinfo")
    async def userinfo(self, ctx, user: disnake.Member = None):
        strings = LanguageClass.get_strings(LanguageClass,LanguageClass.get_lang(LanguageClass,ctx))
        
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

        if (LanguageClass.get_lang(LanguageClass,ctx) == "en"):
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
    bot.add_cog(Slash_Userinfo(bot))
    bot.add_cog(NoSlash_Userinfo(bot))