import disnake, asyncio
import src.core.emojis as emojis
import src.core.embeds as embeds
import src.core.functions as funcs
from disnake.ext import commands

prefix = funcs.get_prefix()


class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.embed_blank_value: str = "\u200b"
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
        rules = [
            (f"{emojis.numbers['one']}   No Negativity", self.embed_blank_value),
            (f"{emojis.numbers['two']}   No Spamming", self.embed_blank_value),
            (f"{emojis.numbers['three']}   No Swearing", self.embed_blank_value),
            (
                f"{emojis.numbers['four']}   No Discriminatory Or Hate Speech",
                self.embed_blank_value,
            ),
            (f"{emojis.numbers['five']}   No NSFW Content", self.embed_blank_value),
            (
                f"{emojis.numbers['six']}   No Potentially Harmful Content",
                self.embed_blank_value,
            ),
        ]

        await ctx.reply(
            embed=embeds.rules_embed(
                bot_name=self.bot.user.name,
                bot_avatar_url=self.bot.user.avatar.url,
                rules=rules,
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
        if message.author == self.bot.user or message.content == f"{prefix}chatbot":
            return
        if self.chatbot_on and message.channel == self.chatbot_channel:
            response = await funcs.chatbot_response(message=message.content)
            if response:
                await message.reply(response)
            else:
                await message.reply("Something went Wrong!!")

    @commands.command(description="Displays the total number of Commands")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def total_commands(self, ctx: commands.Context):
        available_commands = [
            command for command in self.bot.commands if not command.hidden
        ]
        hidden_commands = [command for command in self.bot.commands if command.hidden]

        await ctx.reply(
            f"Available Commands: {len(available_commands)}\nHidden Commands: {len(hidden_commands)}"
        )

    @commands.command(description="Display the Servers the Bot is in")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def servers_in(self, ctx: commands.Context):
        await ctx.reply(embed=embeds.servers_in_embed(servers=self.bot.guilds))

    @commands.command(description="Change the Prefix")
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def change_prefix(self, ctx: commands.Context, new_prefix: str):
        pass


def setup(bot: commands.Bot):
    bot.add_cog(Misc(bot))
