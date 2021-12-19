import asyncio, dislash
import src.embeds as embeds
import src.functions as funcs
from discord.ext import commands

prefix = funcs.get_prefix()


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx: commands.Context, type: str = "default"):
        if type == "moderation":
            await ctx.message.reply(
                embed=embeds.moderation_help_embed(
                    ctx=ctx,
                    bot_name=self.bot.user.name,
                    bot_avatar_url=self.bot.user.avatar_url,
                )
            )
        elif type == "games":
            await ctx.message.reply(
                embed=embeds.games_help_embed(
                    ctx=ctx,
                    bot_name=self.bot.user.name,
                    bot_avatar_url=self.bot.user.avatar_url,
                )
            )
        elif type == "music":
            await ctx.message.reply(
                embed=embeds.music_help_embed(
                    ctx=ctx,
                    bot_name=self.bot.user.name,
                    bot_avatar_url=self.bot.user.avatar_url,
                )
            )
        elif type == "fun":
            await ctx.message.reply(
                embed=embeds.fun_help_embed(
                    ctx=ctx,
                    bot_name=self.bot.user.name,
                    bot_avatar_url=self.bot.user.avatar_url,
                )
            )
        elif type == "user":
            await ctx.message.reply(
                embed=embeds.user_help_embed(
                    ctx=ctx,
                    bot_name=self.bot.user.name,
                    bot_avatar_url=self.bot.user.avatar_url,
                )
            )
        elif type == "default":
            msg = await ctx.send(
                embed=embeds.help_embed(
                    ctx=ctx,
                    bot_name=self.bot.user.name,
                    bot_avatar_url=self.bot.user.avatar_url,
                ),
                components=[
                    dislash.SelectMenu(
                        custom_id="help_command",
                        placeholder="Choose a Category",
                        max_values=1,
                        options=[
                            dislash.SelectOption(
                                "Moderation Help", "moderation_help_embed"
                            ),
                            dislash.SelectOption("Games Help", "games_help_embed"),
                            dislash.SelectOption("Music Help", "music_help_embed"),
                            dislash.SelectOption("Fun Help", "fun_help_embed"),
                            dislash.SelectOption("User Help", "user_help_embed"),
                        ],
                    )
                ],
            )

            try:
                inter = await msg.wait_for_dropdown(timeout=60.0)

                if (
                    inter.select_menu.selected_options[0].value
                    == "moderation_help_embed"
                ):
                    await inter.reply(
                        embed=embeds.moderation_help_embed(
                            ctx=ctx,
                            bot_name=self.bot.user.name,
                            bot_avatar_url=self.bot.user.avatar_url,
                        )
                    )
                elif inter.select_menu.selected_options[0].value == "games_help_embed":
                    await inter.reply(
                        embed=embeds.games_help_embed(
                            ctx=ctx,
                            bot_name=self.bot.user.name,
                            bot_avatar_url=self.bot.user.avatar_url,
                        )
                    )
                elif inter.select_menu.selected_options[0].value == "music_help_embed":
                    await inter.reply(
                        embed=embeds.music_help_embed(
                            ctx=ctx,
                            bot_name=self.bot.user.name,
                            bot_avatar_url=self.bot.user.avatar_url,
                        )
                    )
                elif inter.select_menu.selected_options[0].value == "fun_help_embed":
                    await inter.reply(
                        embed=embeds.fun_help_embed(
                            ctx=ctx,
                            bot_name=self.bot.user.name,
                            bot_avatar_url=self.bot.user.avatar_url,
                        )
                    )
                elif inter.select_menu.selected_options[0].value == "user_help_embed":
                    await inter.reply(
                        embed=embeds.user_help_embed(
                            ctx=ctx,
                            bot_name=self.bot.user.name,
                            bot_avatar_url=self.bot.user.avatar_url,
                        )
                    )
            except asyncio.TimeoutError:
                await msg.edit(
                    embed=embeds.help_embed(
                        ctx=ctx,
                        bot_name=self.bot.user.name,
                        bot_avatar_url=self.bot.user.avatar_url,
                    ),
                    components=[],
                )
        elif (
            type != "default"
            and type != "moderation"
            and type != "games"
            and type != "music"
            and type != "fun"
        ):
            return


def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))
