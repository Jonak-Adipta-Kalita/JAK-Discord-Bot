from urllib.request import urlopen
import disnake, asyncio, inspect, credentials, googletrans, aiohttp, random
import src.core.emojis as emojis
import src.core.embeds as embeds
import src.core.functions as funcs
from src.core.bot import JAKDiscordBot
from disnake.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot: JAKDiscordBot):
        self.bot = bot

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
        rules = funcs.get_rules(self.bot.db, ctx.guild)

        await ctx.reply(
            embed=embeds.rules_embed(
                bot=self.bot,
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

    @commands.group(invoke_without_command=True, description="Use Chatbot Commands")
    async def chatbot(self, ctx: commands.Context, command: str = None):
        if command:
            await ctx.reply("Command not Found!!")
            return

    @chatbot.command(name="start", description="Start Chatbot for 5 Minutes")
    async def chatbot_start(self, ctx: commands.Context, ai: str):
        if ai not in JAKDiscordBot.ai_choices:
            await ctx.reply(
                f"AI not Found!! Please choose from {', '.join(JAKDiscordBot.ai_choices)}"
            )
            return

        funcs.add_chatbot(self.bot.db, ctx.guild, ctx.channel, ai)
        await ctx.reply("Started Chatbot in this channel!!")

    @chatbot.command(name="stop", description="Stop Chatbot")
    async def chatbot_stop(self, ctx: commands.Context):
        funcs.remove_chatbot(self.bot.db, ctx.guild, ctx.channel)

        await ctx.reply("Stopped Chatbot in this channel!!")

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

        code_edited = code.replace("```", "").strip()
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

    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    @commands.command(description="Display the Details of a Place")
    async def place_details(self, ctx: commands.Context, place: str):
        place_details = await funcs.get_place_details(place=place)

        await ctx.reply(embed=embeds.place_details_embed(place=place_details))

    @commands.command(description="Create Webhook")
    @commands.bot_has_permissions(manage_webhooks=True)
    @commands.cooldown(rate=1, per=15, type=commands.BucketType.user)
    async def create_webhook(
        self, ctx: commands.Context, member: disnake.Member, *, text
    ):
        for k in await ctx.channel.webhooks():
            if k.user == ctx.me:
                await k.delete()
        webhook = await ctx.channel.create_webhook(name=f"{member}")

        await webhook.send(
            text,
            username=member.name,
            avatar_url=member.avatar.url,
            allowed_mentions=disnake.AllowedMentions(
                roles=False, users=False, everyone=False
            ),
        )

    @commands.command(description="Convert Image to Text", aliases=["ocr"])
    @commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
    async def optical_character_recognition(
        self, ctx: commands.Context, link: str = None
    ):
        attachments = ctx.message.attachments

        if attachments or link:
            msg = await ctx.reply("Identifying Image, this may take some time!!")
            try:
                url = attachments[0].url if attachments else link
                async with aiohttp.ClientSession() as ses:
                    req = await ses.get(url)

                ocr = funcs.convert_image_to_string(req.content)

                msg.delete()

                await ctx.reply(f"```{ocr}```")
            except Exception:
                pass
        else:
            ctx.reply("Provide a Link or a Attachment!!")

    @commands.command(description="Display which members have a certain role")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def has_role(self, ctx: commands.Context, role: disnake.Role):
        members_with_role = [
            member for member in ctx.guild.members if role in member.roles
        ]

        await ctx.reply(
            embed=embeds.has_role_embed(role=role, members=members_with_role)
        )

    @commands.group(
        invoke_without_command=True, description="Display a Astrophotography of a Type"
    )
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def astrophotography(self, ctx: commands.Context, command: str):
        await ctx.reply("Command not Found!!")

    @astrophotography.command(
        name="apod", description="Display the Astronomy Picture of the Day"
    )
    async def astrophotography_apod(self, ctx: commands.Context):
        astrophotography_data = funcs.get_astrophotography_data(
            link=f"https://api.nasa.gov/planetary/apod?api_key={credentials.NASA_API_KEY}"
        )

        title = astrophotography_data["title"]
        try:
            title += f" - {astrophotography_data['copyright']}"
        except KeyError:
            pass

        await ctx.reply(
            embed=embeds.astrophotography_embed(
                title=title,
                description=astrophotography_data["explanation"],
                image_url=astrophotography_data["hdurl"],
            )
        )

    @astrophotography.command(
        name="epic",
        description="Display a random Image of Earth Polychromatic Imaging Camera",
    )
    async def astrophotography_epic(self, ctx: commands.Context):
        astrophotography_data = funcs.get_astrophotography_data(
            link=f"https://api.nasa.gov/EPIC/api/natural?api_key={credentials.NASA_API_KEY}"
        )
        astrophotography_data = astrophotography_data[
            random.randint(0, len(astrophotography_data) - 1)
        ]

        image_splitted = astrophotography_data["image"].split("_")[2]
        year = image_splitted[:4]
        month = image_splitted[:6][-2:]
        day = image_splitted[:8][-2:]

        await ctx.reply(
            embed=embeds.astrophotography_embed(
                title=astrophotography_data["caption"],
                description=f"Taken on: {year}/{month}/{day}",
                image_url=f"https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/png/{astrophotography_data['image']}.png",
            )
        )

    @astrophotography.command(
        name="mars", description="Display a random Image from a Rover in Mars"
    )
    async def astrophotography_mars(self, ctx: commands.Context):
        astrophotography_data = funcs.get_astrophotography_data(
            link=f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={credentials.NASA_API_KEY}"
        )
        astrophotography_data = astrophotography_data["photos"][
            random.randint(0, len(astrophotography_data["photos"]) - 1)
        ]

        await ctx.reply(
            embed=embeds.astrophotography_embed(
                title=astrophotography_data["camera"]["full_name"],
                description=f"Taken on: {astrophotography_data['earth_date'].replace('_', '/')}\nRover Name: {astrophotography_data['rover']['name']}\nRover Landing Date: {astrophotography_data['rover']['landing_date']}",
                image_url=astrophotography_data["img_src"],
            )
        )

    @astrophotography.command(name="search", description="Search Astrophotography")
    async def astrophotography_search(self, ctx: commands.Context, *, query: str):
        astrophotography_data = funcs.get_astrophotography_data(
            link=f"https://images-api.nasa.gov/search?q={query.replace(' ', '+')}"
        )
        if not astrophotography_data["collection"]["items"]:
            await ctx.reply("No Data Found!!")
            return
        astrophotography_data = astrophotography_data["collection"]["items"][
            random.randint(0, len(astrophotography_data["collection"]["items"]) - 1)
        ]

        image_url = ""

        for link in astrophotography_data["links"]:
            if link["rel"] == "preview":
                image_url = link["href"]
                break

        await ctx.reply(
            embed=embeds.astrophotography_embed(
                title=astrophotography_data["data"][0]["title"],
                description=astrophotography_data["data"][0]["description"],
                image_url=image_url,
            )
        )

    @commands.command(description="Get google search results")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def google(self, ctx: commands.Context, *, query: str):
        search_results = await funcs.get_google_search_results(query)

        if not search_results:
            await ctx.reply("No Data Found!!")
            return

        search_results = search_results

        await ctx.reply(
            embed=embeds.google_embed(
                search_results=search_results,
            )
        )

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        member = message.author

        if member == self.bot.user:
            return

        msg = message.content
        channel = message.channel

        guild_prefix = (
            self.bot.db.child("guilds")
            .child(str(message.guild.id))
            .child("prefix")
            .get()
        )

        transaltionData = (
            self.bot.db.child("guilds")
            .child(str(message.guild.id))
            .child("translation")
            .get()
        )
        pronunciationData = (
            self.bot.db.child("guilds")
            .child(str(message.guild.id))
            .child("pronunciation")
            .get()
        )

        if guild_prefix:
            prefixes = self.bot.prefixes + [guild_prefix]
        else:
            prefixes = self.bot.prefixes

        for prefix in prefixes:
            if msg.startswith(prefix) or member == self.bot.user:
                return

        if len(msg) >= 3:

            translation = funcs.translate_text(msg)

            if translation.src != "en":
                language_name = ""
                languages_dict = googletrans.LANGUAGES

                if translation.src in languages_dict:
                    language_name = languages_dict[translation.src].title()

                    if int(transaltionData["id"]) == message.channel.id:
                        await channel.send(
                            embed=embeds.translation_embed(
                                text=msg,
                                translated_text=translation.text,
                                language_name=language_name,
                                language_iso=translation.src,
                                author=member,
                            )
                        )
                        return

                    def translation_check(reaction, user):
                        global author_reacted_translation
                        author_reacted_translation = user
                        return (
                            str(reaction.emoji) == emojis.abc
                            and reaction.message == message
                            and not user.bot
                        )

                    try:
                        await self.bot.wait_for(
                            "reaction_add", check=translation_check, timeout=60.0
                        )
                        await channel.send(
                            embed=embeds.translation_embed(
                                text=msg,
                                translated_text=translation.text,
                                language_name=language_name,
                                language_iso=translation.src,
                                author=member,
                                author_reacted=author_reacted_translation,
                            )
                        )
                    except asyncio.TimeoutError:
                        pass

            else:
                if int(pronunciationData["id"]) == message.channel.id:
                    await channel.send(
                        embed=embeds.pronunciation_embed(
                            text=msg,
                            pronunciation=funcs.pronunciation(msg),
                            author=member,
                        )
                    )
                    return

                def pronunciation_check(reaction, user):
                    global author_reacted_pronunciation
                    author_reacted_pronunciation = user
                    return (
                        str(reaction.emoji) == emojis.abc
                        and reaction.message == message
                        and not user.bot
                    )

                try:
                    await self.bot.wait_for(
                        "reaction_add", check=pronunciation_check, timeout=60.0
                    )
                    await channel.send(
                        embed=embeds.pronunciation_embed(
                            text=msg,
                            pronunciation=funcs.pronunciation(msg),
                            author=member,
                            author_reacted=author_reacted_pronunciation,
                        )
                    )
                except asyncio.TimeoutError:
                    pass

        chatbot_data: list[list] = (
            self.bot.db.child("guilds")
            .child(str(message.guild.id))
            .child("chatbot")
            .get()
        )

        if not chatbot_data:
            return

        for data in chatbot_data:
            if data[0] == message.channel.id:
                if not msg in [f"{prefix}chatbot" for prefix in prefixes]:
                    async with message.channel.typing():
                        response = funcs.chatbot_response(message=msg, ai=data[1])

                    await message.reply(response)
                break

    @commands.Cog.listener()
    async def on_member_join(self, member: disnake.Member):
        try:
            perms = member.guild.me.guild_permissions
            if perms.manage_guild and perms.manage_messages:
                await member.send(f"Welcome to **{member.guild.name}**!!")
        except AttributeError:
            pass
        except disnake.HTTPException:
            pass

    @commands.Cog.listener()
    async def on_member_remove(self, member: disnake.Member):
        try:
            perms = member.guild.me.guild_permissions
            if perms.manage_guild and perms.manage_messages:
                await member.send(
                    f"You just left **{member.guild.name}**, What a Shame!!"
                )
        except AttributeError:
            pass

        except disnake.HTTPException:
            pass

    @commands.Cog.listener()
    async def on_message_delete(self, message: disnake.Message):
        reaction_roles_data_ref = (
            self.bot.db.child("guilds")
            .child(str(message.guild.id))
            .child("reactionRoles")
        )

        reaction_roles_data: list[list] = reaction_roles_data_ref.get()

        if not reaction_roles_data:
            return

        for i, data in enumerate(reaction_roles_data):
            if (
                int(data["channel_id"]) == message.channel.id
                and int(data["message_id"]) == message.id
            ):
                del reaction_roles_data[i]
                reaction_roles_data_ref.set(reaction_roles_data)

                break

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: disnake.RawReactionActionEvent):
        user = await self.bot.fetch_user(payload.user_id)
        reaction = payload.emoji
        channel = await self.bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        guild = message.guild
        member = guild.get_member(user.id)

        if user == self.bot.user:
            return

        reaction_roles_data: list[list] = (
            self.bot.db.child("guilds")
            .child(str(message.guild.id))
            .child("reactionRoles")
            .get()
        )

        if not reaction_roles_data:
            return

        try:
            for data in reaction_roles_data:
                if (
                    int(data["channel_id"]) == channel.id
                    and int(data["message_id"]) == message.id
                ):
                    for reaction_role in data["reactionRoles"]:
                        if str(reaction) == reaction_role["emoji"]["emoji"]:
                            role = guild.get_role(int(reaction_role["role"]["id"]))
                            await member.add_roles(role)
        except KeyError:
            pass

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: disnake.RawReactionActionEvent):
        user = await self.bot.fetch_user(payload.user_id)
        reaction = payload.emoji
        channel = await self.bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        guild = message.guild
        member = guild.get_member(user.id)

        if user == self.bot.user:
            return

        reaction_roles_data: list[list] = (
            self.bot.db.child("guilds")
            .child(str(message.guild.id))
            .child("reactionRoles")
            .get()
        )

        if not reaction_roles_data:
            return

        try:
            for data in reaction_roles_data:
                if (
                    int(data["channel_id"]) == channel.id
                    and int(data["message_id"]) == message.id
                ):
                    for reaction_role in data["reactionRoles"]:
                        if str(reaction) == reaction_role["emoji"]["emoji"]:
                            role = guild.get_role(int(reaction_role["role"]["id"]))
                            await member.add_roles(role)
        except KeyError:
            pass

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: disnake.RawReactionActionEvent):
        user = await self.bot.fetch_user(payload.user_id)
        reaction = payload.emoji
        channel = await self.bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        guild = message.guild
        member = guild.get_member(user.id)

        if user == self.bot.user:
            return

        reaction_roles_data: list[list] = (
            self.bot.db.child("guilds")
            .child(str(message.guild.id))
            .child("reactionRoles")
            .get()
        )

        if not reaction_roles_data:
            return

        try:
            for data in reaction_roles_data:
                if (
                    int(data["channel_id"]) == channel.id
                    and int(data["message_id"]) == message.id
                ):
                    for reaction_role in data["reactionRoles"]:
                        if str(reaction) == reaction_role["emoji"]["emoji"]:
                            role = guild.get_role(int(reaction_role["role"]["id"]))
                            if member.get_role(role.id):
                                await member.remove_roles(role)
        except KeyError:
            pass


def setup(bot: JAKDiscordBot):
    bot.add_cog(Misc(bot))
