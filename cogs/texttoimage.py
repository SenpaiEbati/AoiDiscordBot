import disnake
from disnake.ext import commands
from core.bot import AoiBot
import datetime
from core.utils import LanguageClass, get_colour, send_embed
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
import io
from asyncio import sleep

class TextToImage(commands.Cog):
    def __init__(self, bot):
        self.bot: AoiBot = bot

    @commands.slash_command(name="texttoimage", default_member_permissions=disnake.Permissions(administrator=False))
    async def texttoimage(self, ctx, prompt):
        await ctx.response.defer(with_message=False)
        # Set up our initial generation parameters.
        answers = self.bot.stability_api.generate(
            prompt=prompt,
            samples=1,
            sampler=generation.SAMPLER_K_DPMPP_2M
        )
        lang = await LanguageClass.get_lang(LanguageClass, ctx)
        strings = await LanguageClass.get_strings(LanguageClass, lang)

        embed = disnake.Embed(
            title=strings["texttoimage_title"],
            color=get_colour("halloween"),
            timestamp=datetime.datetime.now()
        ).set_footer(
            text=strings["texttoimage_footer"]
        )

        # Set up our warning if the adult content filter is tripped.
        # If not, save and upload the generated image.
        try:
            for resp in answers:
                for artifact in resp.artifacts:
                    if artifact.finish_reason == generation.FILTER:
                        embed.add_field(
                            name=strings["texttoimage_filter_name"],
                            value=strings["texttoimage_filter_value"]
                        )
                    if artifact.type == generation.ARTIFACT_IMAGE:
                        img_bytes = io.BytesIO(artifact.binary)
                        img_bytes.seek(0)
                        img = disnake.File(img_bytes, filename='generated_image.png')
                        embed.set_image(
                            url="attachment://generated_image.png"
                        )
                        await ctx.send(file=img, embed=embed)
                        return
        except Exception as e:
            await sleep(5)
            await ctx.channel.purge(limit=1)
            await send_embed(ctx.channel,title=strings["texttoimage_error_title"],description=strings["texttoimage_error_desc"], c = get_colour("yellow"), f = strings["texttoimage_footer"])

def setup(bot: commands.Bot):
    bot.add_cog(TextToImage(bot))
