import disnake
from disnake.ext import commands
import emoji
from core.constants import COG_EMOJIS, HOME


class Dropdown(disnake.ui.Select):
    def __init__(self, data, ctx: commands.Context, utils):
        self.data = data
        self.ctx = ctx
        self.utils = utils

        options = [
            disnake.SelectOption(
                label="Home", description="Return to the main help panel", emoji=HOME
            )
        ]
        for key in data:
            emoji_pattern = emoji.emoji_list(data[key])
            emoji_list = [entry['emoji'] for entry in emoji_pattern]
            if not emoji_pattern:
                number = int(''.join(filter(str.isdigit, data[key])))
            options.append(
                disnake.SelectOption(
                    label=key,
                    description=f"{len([e for e in ctx.bot.slash_commands if e.cog_name == key])} commands",
                    emoji=emoji_list[0] if emoji_pattern else ctx.bot.get_emoji(number),
                )
            )

        super().__init__(
            placeholder="Choose a category.",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        label = interaction.values[0]

        if label not in self.data:
            embed = await self.utils.main_help_embed(self.ctx)
            return await interaction.response.edit_message(embed=embed, view=self.view)

        cog = self.ctx.bot.get_cog(label)
        embed = await self.utils.specific_cog(cog, self.ctx)

        if interaction.author == self.ctx.author:
            return await interaction.response.edit_message(embed=embed, view=self.view)
        await interaction.response.send_message(embed=embed, ephemeral=True)


class DropdownView(disnake.ui.View):
    def __init__(self, data, ctx: commands.Context, utils):
        super().__init__(timeout=600)
        self.add_item(Dropdown(data, ctx, utils))
