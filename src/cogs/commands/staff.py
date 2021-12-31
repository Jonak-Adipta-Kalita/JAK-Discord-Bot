import disnake
from disnake.ext import commands


class Staff(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def load_cog(self, ctx: commands.Context, extension):
        embed = disnake.Embed(color=disnake.Color.blue())
        self.bot.load_extension(f"src.cogs.{extension}")
        embed.add_field(
            name="Load Extension", value=f"Loaded COG: ``{extension}`` Successfully!!"
        )
        await ctx.send(embed=embed)

    @commands.command(hidden=True)
    async def unload_cog(self, ctx: commands.Context, extension):
        self.bot.unload_extension(f"src.cogs.{extension}")
        embed = disnake.Embed(color=disnake.Color.blue())
        embed.add_field(
            name="Unload Extension",
            value=f"Unloaded COG: ``{extension}`` Successfully!!",
        )
        await ctx.send(embed=embed)

    @commands.command(hidden=True, aliases=["reload_cogs"])
    async def reload_cog(self, ctx: commands.Context, extension: str = ""):
        if not extension:

            for cog in tuple(self.bot.extensions):
                self.bot.reload_extension(cog)

            embed = disnake.Embed(color=disnake.Color.blue())
            embed.add_field(
                name="Reload Extension", value=f"Reloaded COGS Successfully!!"
            )
            await ctx.send(embed=embed)
        else:

            self.bot.reload_extension(f"src.cogs.{extension}")

            embed = disnake.Embed(color=disnake.Color.blue())
            embed.add_field(
                name="Reload Extension",
                value=f"Reloaded COG: ``{extension}`` Successfully!!",
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Staff(bot))
