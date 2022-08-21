import disnake, inspect, credentials, os, asyncio, aiohttp
import src.core.emojis as emojis
import src.core.embeds as embeds
import src.core.functions as funcs
from src.core.bot import JAKDiscordBot
from disnake.ext import commands
from urllib.request import urlopen


class Misc_(commands.Cog):
    def __init__(self, bot: JAKDiscordBot):
        self.bot = bot

    @commands.slash_command(
        description="Create a Poll",
        options=[
            disnake.Option(
                name="question",
                description="The Question!!",
                type=disnake.OptionType.string,
                required=True,
            ),
            disnake.Option(
                name="option1",
                description="The First Option!!",
                type=disnake.OptionType.string,
                required=True,
            ),
            disnake.Option(
                name="option2",
                description="The Second Option!!",
                type=disnake.OptionType.string,
                required=True,
            ),
            disnake.Option(
                name="option3",
                description="The Third Option!!",
                type=disnake.OptionType.string,
                required=False,
            ),
        ],
    )
    async def poll(
        self,
        inter: disnake.ApplicationCommandInteraction,
        question: str,
        option1: str,
        option2: str,
        option3: str = None,
    ):
        await inter.response.send_message(
            embed=embeds.poll_embed(
                question=question,
                option1=option1,
                option2=option2,
                option3=option3,
            )
        )

        msg = await inter.original_message()

        await msg.add_reaction(emojis.alphabets["regional_indicator_a"])
        await msg.add_reaction(emojis.alphabets["regional_indicator_b"])
        if option3:
            await msg.add_reaction(emojis.alphabets["regional_indicator_c"])

    @commands.slash_command(description="Show the Rules")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def show_rules(self, inter: disnake.ApplicationCommandInteraction):
        rules = funcs.get_rules(self.bot.db, inter.guild)

        await inter.response.send_message(
            embed=embeds.rules_embed(
                bot=self.bot,
                rules=rules,
            )
        )

    @commands.slash_command(description="Show the Latency")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def latency(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(f"Ping: {round(self.bot.latency * 1000)}")

    @commands.slash_command(
        description="Show the Details of a Member",
        options=[
            disnake.Option(
                name="member",
                description="The Member!!",
                type=disnake.OptionType.mentionable,
                required=False,
            )
        ],
    )
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def member_details(
        self,
        inter: disnake.ApplicationCommandInteraction,
        member: disnake.Member = None,
    ):
        if not member:
            member = inter.author
            fetched_member = await self.bot.fetch_user(inter.author.id)
        else:
            fetched_member = await self.bot.fetch_user(member.id)
        await inter.response.send_message(
            embed=embeds.member_details_embed(
                member=member, fetched_member=fetched_member
            )
        )

    @commands.slash_command(description="Show the Server Information")
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def server_stats(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer()
        await inter.edit_original_message(
            embed=embeds.server_stats_embed(guild=inter.guild)
        )

    @commands.slash_command(
        description="Shows the Source of a Message",
        options=[
            disnake.Option(
                name="message_id",
                description="Message ID of the Message to show source of!!",
                type=disnake.OptionType.string,
                required=True,
            )
        ],
    )
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def message_source(
        self,
        inter: disnake.ApplicationCommandInteraction,
        message_id: int,
    ):
        msg = await inter.channel.fetch_message(message_id)
        if not msg or not msg.content.strip():
            await inter.response.send_message(
                "Please provide a non-empty Message!!", ephemeral=True
            )
            return
        await inter.response.send_message(embed=embeds.message_source_embed(msg=msg))

    @commands.slash_command(description="Displays the total number of Commands")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def total_commands(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer()

        available_commands = (
            [command for command in (await funcs.get_commands())["moderation"]]
            + [command for command in (await funcs.get_commands())["fun"]]
            + [command for command in (await funcs.get_commands())["misc"]]
            + [command for command in (await funcs.get_commands())["games"]]
            + [command for command in (await funcs.get_commands())["music"]]
        )
        hidden_commands = [command for command in self.bot.commands if command.hidden]

        await inter.edit_original_message(
            f"Available Commands: {len(available_commands)}\nHidden Commands: {len(hidden_commands)}"
        )

    @commands.slash_command(description="Display the Servers the Bot is in")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def servers_in(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(
            embed=embeds.servers_in_embed(servers=self.bot.guilds)
        )

    @commands.slash_command(
        description="Shorten a URL",
        options=[
            disnake.Option(
                name="url",
                description="URL to Shorten!!",
                type=disnake.OptionType.string,
                required=True,
            )
        ],
    )
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def shorten_url(self, ctx: disnake.ApplicationCommandInteraction, url: str):
        shortened_url = await self.bot.loop.run_in_executor(
            None,
            lambda: urlopen("http://tinyurl.com/api-create.php?url=" + url)
            .read()
            .decode("utf-8"),
        )

        await ctx.response.send_message(f"Your Shortened URL: {shortened_url}")

    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    @commands.slash_command(
        description="Get the Source Code of a command",
        options=[
            disnake.Option(
                name="command",
                description="Command Name!!",
                type=disnake.OptionType.string,
                required=True,
            )
        ],
    )
    async def source_code(self, inter: disnake.ApplicationCommandInteraction, command):
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
            await inter.response.send_message(
                f"https://github.com/Jonak-Adipta-Kalita/JAK-Discord-Bot/tree/main/{main_path}#L{line_no}"
            )
        else:
            await inter.response.send_message("No Command Found!!", ephemeral=True)

    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    @commands.slash_command(
        description="Display all the Prefixes usable for this server"
    )
    async def prefixes(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(", ".join(self.bot.prefixes))

    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    @commands.slash_command(
        description="Display the Details of a Place",
        options=[
            disnake.Option(
                name="place",
                description="Name of the Place you want to know about",
                type=disnake.OptionType.string,
                required=True,
            )
        ],
    )
    async def place_details(
        self, inter: disnake.ApplicationCommandInteraction, place: str
    ):
        place_details = await funcs.get_place_details(place=place)

        await inter.response.send_message(
            embed=embeds.place_details_embed(place=place_details)
        )

    @commands.slash_command(
        description="Create Webhook",
        options=[
            disnake.Option(
                name="member",
                description="The User you want to make a Webhook of",
                type=disnake.OptionType.mentionable,
                required=True,
            ),
            disnake.Option(
                name="text",
                description="Text you want to send after creating the Webhook",
                type=disnake.OptionType.string,
            ),
        ],
    )
    @commands.bot_has_permissions(manage_webhooks=True)
    @commands.cooldown(rate=1, per=15, type=commands.BucketType.user)
    async def create_webhook(
        self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, text
    ):
        for k in await inter.channel.webhooks():
            if k.user == inter.me:
                await k.delete()
        webhook = await inter.channel.create_webhook(name=f"{member}")

        await webhook.send(
            text,
            username=member.name,
            avatar_url=member.avatar.url,
            allowed_mentions=disnake.AllowedMentions(
                roles=False, users=False, everyone=False
            ),
        )

    @commands.slash_command(
        description="Convert Image to Text",
        options=[
            disnake.Option(
                name="link",
                description="Link of the Image",
                type=disnake.OptionType.string,
                required=False,
            )
        ],
    )
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def optical_character_recognition(
        self, inter: disnake.ApplicationCommandInteraction, link: str = None
    ):
        attachments = inter.message.attachments

        if attachments or link:
            inter.response.defer()

            await inter.edit_original_message(
                "Identifying Image, this may take some time!!"
            )

            try:
                url = attachments[0].url if attachments else link
                async with aiohttp.ClientSession() as ses:
                    req = await ses.get(url)

                ocr = funcs.convert_image_to_string(req.content)

                await inter.edit_original_message(f"`{ocr}`")
            except Exception:
                pass
        else:
            inter.edit_original_message("Provide a Link or a Attachment!!")

    @commands.slash_command(
        description="Display which members have a certain role",
        options=[
            disnake.Option(
                name="role",
                description="The role",
                type=disnake.OptionType.role,
                required=True,
            )
        ],
    )
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def has_role(
        self, inter: disnake.ApplicationCommandInteraction, role: disnake.Role
    ):
        members_with_role = [
            member for member in inter.guild.members if role in member.roles
        ]

        await inter.response.send_message(
            embed=embeds.has_role_embed(role=role, members=members_with_role)
        )


def setup(bot: JAKDiscordBot):
    bot.add_cog(Misc_(bot))
