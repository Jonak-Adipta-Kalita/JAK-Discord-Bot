import disnake, io, contextlib, textwrap, traceback
from src.core.bot import JAKDiscordBot
from disnake.ext import commands


class Staff(commands.Cog):
    def __init__(self, bot: JAKDiscordBot):
        self.bot = bot

    async def cog_check(self, ctx: commands.Context):
        if not await self.bot.is_owner(ctx.author):
            raise commands.NotOwner(
                "Only the Members of the Dev Team are allowed to use this command!!"
            )

        return True

    @commands.command(hidden=True)
    async def load_cog(self, ctx: commands.Context, extension):
        embed = disnake.Embed(color=0x3498DB)
        self.bot.load_extension(f"src.cogs.{extension}")
        embed.add_field(
            name="Load Extension", value=f"Loaded COG: ``{extension}`` Successfully!!"
        )
        await ctx.reply(embed=embed)

    @commands.command(hidden=True)
    async def unload_cog(self, ctx: commands.Context, extension):
        self.bot.unload_extension(f"src.cogs.{extension}")
        embed = disnake.Embed(color=0x3498DB)
        embed.add_field(
            name="Unload Extension",
            value=f"Unloaded COG: ``{extension}`` Successfully!!",
        )
        await ctx.reply(embed=embed)

    @commands.command(hidden=True, aliases=["reload_cogs"])
    async def reload_cog(self, ctx: commands.Context, extension: str = ""):
        if not extension:

            for cog in tuple(self.bot.extensions):
                self.bot.reload_extension(cog)

            embed = disnake.Embed(color=0x3498DB)
            embed.add_field(
                name="Reload Extension", value=f"Reloaded COGS Successfully!!"
            )
            await ctx.reply(embed=embed)
        else:

            self.bot.reload_extension(f"src.cogs.{extension}")

            embed = disnake.Embed(color=0x3498DB)
            embed.add_field(
                name="Reload Extension",
                value=f"Reloaded COG: ``{extension}`` Successfully!!",
            )
            await ctx.send(embed=embed)

    @commands.command(hidden=True)
    async def eval(self, ctx: commands.Context, *, code: str):
        code = disnake.utils.remove_markdown(code.strip()).strip()

        local_variables = {
            "disnake": disnake,
            "commands": commands,
            "bot": self.bot,
            "client": self.bot,
            "ctx": ctx,
            "channel": ctx.channel,
            "author": ctx.author,
            "guild": ctx.guild,
            "message": ctx.message,
        }

        stdout = io.StringIO()

        try:
            with contextlib.redirect_stdout(stdout):
                exec(
                    f"async def func():\n{textwrap.indent(code, '    ')}",
                    local_variables,
                )
                obj = await local_variables["func"]()
                result = f"{stdout.getvalue()}{obj}\n"
        except Exception as e:
            result = "".join(traceback.format_exception(e, e, e.__traceback__))

        result = result.replace("`", "")
        code = code.replace("`", "")
        if result.replace("\n", "").endswith("None") and result != "None":
            result = result[:-5]

        if len(result) < 2000:
            await ctx.send(f"```py\nIn[0]: {code}\nOut[0]: {result}\n```")
            return


def setup(bot: JAKDiscordBot):
    bot.add_cog(Staff(bot))
