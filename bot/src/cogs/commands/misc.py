from urllib.request import urlopen
import disnake, asyncio, inspect, credentials
import src.core.emojis as emojis
import src.core.embeds as embeds
import src.core.functions as funcs
from src.core.bot import JAKDiscordBot
from disnake.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot: JAKDiscordBot):
        self.bot = bot
        self.chatbot_on: bool = False
        self.chatbot_channel: disnake.TextChannel = None

    @commands.command(description="Create a Poll")
    async def poll(
        self,
        ctx: commands.Context,
        question: str,
        option1: str,
        option2: str,
        option3: str = None,
    ):
        msg = await ctx.reply(
            embed=embeds.poll_embed(
                question=question,
                option1=option1,
                option2=option2,
                option3=option3,
            )
        )
        await msg.add_reaction(emojis.alphabets["regional_indicator_a"])
        await msg.add_reaction(emojis.alphabets["regional_indicator_b"])
        if option3:
            await msg.add_reaction(emojis.alphabets["regional_indicator_c"])

    @commands.command(aliases=["rules"], description="Show the Rules")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def show_rules(self, ctx: commands.Context):
        await ctx.reply(
            embed=embeds.rules_embed(
                bot_name=self.bot.user.name,
                bot_avatar_url=self.bot.user.avatar.url,
            )
        )

    @commands.command(description="Show the Latency", aliases=["ping", "ms"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def latency(self, ctx: commands.Context):
        await ctx.reply(f"Ping: {round(self.bot.latency * 1000)}")

    @commands.command(description="Show the Details of a Member")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def member_details(
        self, ctx: commands.Context, member: disnake.Member = None
    ):
        if not member:
            member = ctx.author
            fetched_member = await self.bot.fetch_user(ctx.author.id)
        else:
            fetched_member = await self.bot.fetch_user(member.id)
        await ctx.reply(
            embed=embeds.member_details_embed(
                member=member, fetched_member=fetched_member
            )
        )

    @commands.command(description="Show the Server Information")
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def server_stats(self, ctx: commands.Context):
        await ctx.reply(embed=embeds.server_stats_embed(guild=ctx.guild))

    @commands.command(description="Shows the Source of a Message")
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def message_source(
        self,
        ctx: commands.Context,
        message_id: int,
    ):
        msg = await ctx.fetch_message(message_id)
        if not msg or not msg.content.strip():
            await ctx.reply("Please provide a non-empty Message!!")
            return
        await ctx.reply(embed=embeds.message_source_embed(msg=msg))

    @commands.group(
        invoke_without_command=True, description="Start Chatbot for 5 Minutes"
    )
    async def chatbot(self, ctx: commands.Context, command: str = None):
        if command:
            await ctx.reply("Command not Found!!")
            return

        if not self.chatbot_on:
            self.chatbot_on = True
            self.chatbot_channel = ctx.channel
            await ctx.reply("Started Chatbot!! Will be Active for 5 Mins!!")

            await asyncio.sleep(300)
            if self.chatbot_on:
                self.chatbot_on = False
                self.chatbot_channel = None
                await ctx.reply("Chatbot Stopped!!")

    @chatbot.command(description="Stop Chatbot")
    async def stop(self, ctx: commands.Context):
        self.chatbot_on = False
        await ctx.reply("Stopped Chatbot!!")

    @commands.Cog.listener("on_message")
    async def on_chatbot_message(self, message: disnake.Message):
        if message.author == self.bot.user or (
            message.content == f"{self.bot.prefixes[0]}chatbot"
            or message.content == f"{self.bot.prefixes[1]}chatbot"
        ):
            return
        if self.chatbot_on and message.channel == self.chatbot_channel:
            response = await funcs.chatbot_response(message=message.content)
            await message.reply(response)

    @commands.command(description="Displays the total number of Commands")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def total_commands(self, ctx: commands.Context):
        available_commands = (
            [command for command in (await funcs.get_commands())["moderation"]]
            + [command for command in (await funcs.get_commands())["fun"]]
            + [command for command in (await funcs.get_commands())["misc"]]
            + [command for command in (await funcs.get_commands())["games"]]
            + [command for command in (await funcs.get_commands())["music"]]
        )
        hidden_commands = [command for command in self.bot.commands if command.hidden]

        await ctx.reply(
            f"Available Commands: {len(available_commands)}\nHidden Commands: {len(hidden_commands)}"
        )

    @commands.command(description="Display the Servers the Bot is in")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def servers_in(self, ctx: commands.Context):
        await ctx.reply(embed=embeds.servers_in_embed(servers=self.bot.guilds))

    @commands.command(description="Shorten a URL")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def shorten_url(self, ctx: commands.Context, *, url: str):
        shortened_url = await self.bot.loop.run_in_executor(
            None,
            lambda: urlopen("http://tinyurl.com/api-create.php?url=" + url)
            .read()
            .decode("utf-8"),
        )

        await ctx.reply(f"Your Shortened URL: {shortened_url}")

    @commands.command(description="Execute Code", aliases=["run_code"])
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def execute_code(self, ctx: commands.Context, language: str, *, code: str):
        if not code.startswith("```") and code.endswith("```"):
            raise commands.BadArgument("Arguments not specified correctly.")

        code_edited = disnake.utils.remove_markdown(code.strip()).strip()
        code_response = funcs.get_code_output(language, code_edited)

        await ctx.reply(f"```{code_response}```")

    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    @commands.command(description="Get the Source Code of a command")
    async def source_code(self, ctx: commands.Context, command):
        cmd = self.bot.get_command(command)
        if cmd:
            source = inspect.unwrap(cmd.callback).__code__
            main_path = (
                f"bot/{''.join(inspect.getfile(source).split('app/')[1])}"
                if not credentials.LOCAL
                else "".join(
                    inspect.getfile(source)
                    .split("JAK Discord Bot\\")[1]
                    .replace("\\", "/")
                )
            )
            line_no = inspect.getsourcelines(source)[1]
            await ctx.reply(
                f"https://github.com/Jonak-Adipta-Kalita/JAK-Discord-Bot/tree/main/{main_path}#L{line_no}"
            )
        else:
            await ctx.reply("No Command Found!!")

    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    @commands.command(description="Display all the Prefixes usable for this server")
    async def prefixes(self, ctx: commands.Context):
        await ctx.reply(", ".join(self.bot.prefixes))


def setup(bot: JAKDiscordBot):
    bot.add_cog(Misc(bot))
