import disnake, os, asyncio, itertools, credentials, discord_together
import src.core.functions as funcs
import src.core.embeds as embeds
import firebase_admin, firebase_admin.db, firebase_admin.credentials
from disnake.ext import commands


class JAKDiscordBot(commands.Bot):
    def __init__(self):
        firebase_admin.initialize_app(
            credential=firebase_admin.credentials.Certificate(
                {
                    "type": credentials.FIREBASE_TYPE,
                    "project_id": credentials.FIREBASE_PROJECT_ID,
                    "private_key_id": credentials.FIREBASE_PRIVATE_KEY_ID,
                    "private_key": credentials.FIREBASE_PRIVATE_KEY,
                    "client_email": credentials.FIREBASE_CLIENT_EMAIL,
                    "client_id": credentials.FIREBASE_CLIENT_ID,
                    "auth_uri": credentials.FIREBASE_AUTH_URI,
                    "token_uri": credentials.FIREBASE_TOKEN_URI,
                    "auth_provider_x509_cert_url": credentials.FIREBASE_AUTH_PROVIDER_X509_CERT_URL,
                    "client_x509_cert_url": credentials.FIREBASE_CLIENT_X509_CERT_URL,
                }
            )
        ) if not len(firebase_admin._apps) else firebase_admin.get_app()

        self.support_server: disnake.Guild = None
        self.together_control: discord_together.DiscordTogether = None
        self.db: firebase_admin.db.Reference = firebase_admin.db.reference(
            url=credentials.FIREBASE_DATABASE_URL
        )
        self.prefixes = ["$", "!JAK "]

        self.bad_words: list[str] = None
        self._8ball_responses: list[str] = None

        self.tictactoe_players: list = []
        self.tictactoe_player1: str = ""
        self.tictactoe_player2: str = ""
        self.tictactoe_turn: str = ""
        self.tictactoe_game_over: bool = True
        self.tictactoe_board: list = []
        self.tictactoe_winning_conditions: list = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]

        self.hangman_game_over: bool = True
        self.hangman_player: disnake.Member = None
        self.hangman_guesses: list = []
        self.hangman_guesses_left: int = 0
        self.hangman_words: list[str] = None
        self.hangman_word: str = None

        self.chatbot_on: bool = False
        self.chatbot_channel: disnake.TextChannel = None

        super().__init__(
            command_prefix=self.get_prefix,
            intents=disnake.Intents.all(),
            help_command=None,
            description="JAK Discord Bot is a Multi Purpose Bot, Made with `disnake`. It has features like: Moderation, Games, Music, Translation, Meme, Jokes, Discord Together, Chatbot, etc. It is made by xxJonakAdiptaxx#2464",
        )

        self.load_extension("jishaku")
        self.load_extension("src.cogs.help")
        self.load_extension("src.cogs.staff")

        for files in os.listdir(f"./src/cogs/commands/"):
            if files.endswith(".py"):
                self.load_extension(f"src.cogs.commands.{files[:-3]}")

        for files in os.listdir(f"./src/cogs/slash/"):
            if files.endswith(".py"):
                self.load_extension(f"src.cogs.slash.{files[:-3]}")

    async def on_connect(self):
        print("Bot is Connected!!")

    async def on_disconnect(self):
        print("Bot is Disconnected!!")

    async def on_ready(self):
        self.support_server = self.get_guild(752800104112717826)

        self.together_control = await discord_together.DiscordTogether(
            credentials.TOKEN
        )

        self.bad_words = await funcs.get_profanity_words()
        self.hangman_words = await funcs.get_hangman_words()
        self._8ball_responses = await funcs.get_8ball_responses()

        for type_, message in itertools.cycle(
            [
                ("listening", f"{self.prefixes[0]}help"),
                (
                    "watching",
                    f"{len(self.guilds)} {'Servers' if len(self.guilds) != 1 else 'Server'}!!",
                ),
            ]
        ):
            await self.change_presence(
                status=disnake.Status.online,
                activity=disnake.Activity(
                    type=disnake.ActivityType.listening
                    if type_ == "listening" and type_ != "watching"
                    else disnake.ActivityType.watching,
                    name=message,
                ),
            )
            await asyncio.sleep(60)

    async def get_prefix(self, message: disnake.Message):
        guild_prefix: str = (
            self.db.child("guilds").child(str(message.guild.id)).child("prefix").get()
        )

        if guild_prefix:
            prefixes = [guild_prefix]
        else:
            prefixes = self.prefixes

        return commands.when_mentioned_or(*prefixes)(self, message)

    async def on_message(self, message: disnake.Message):
        member = message.author

        if member == self.user:
            return

        msg = message.content

        if msg in [f"<@!{self.user.id}>", f"<@{self.user.id}>"]:
            await message.reply(
                embed=embeds.ping_bot_embed(
                    bot=self, servers=len(self.guilds), prefixes=self.prefixes
                )
            )

        await self.process_commands(message)

    async def on_guild_join(self, guild: disnake.Guild):
        if not self.db:
            return

        self.db.child("guilds").child(str(guild.id)).set(
            {
                "id": guild.id,
                "name": guild.name,
                "owner": f"{guild.owner.name}#{guild.owner.discriminator}",
            }
        )

    async def on_guild_remove(self, guild: disnake.Guild):
        if not self.db:
            return

        self.db.child("guilds").child(str(guild.id)).delete()

    async def on_guild_update(self, before: disnake.Guild, after: disnake.Guild):
        if not self.db:
            return

        guild = self.db.child("guilds").child(str(before.id))

        if after.name != before.name:
            name_guild_data: dict = guild.get()
            name_guild_data.update({"name": after.name})

            guild.set(name_guild_data)

        if after.owner != before.owner:
            owner_guild_data: dict = guild.get()
            owner_guild_data.update({"owner": after.owner})

            guild.set(owner_guild_data)

    async def on_command_error(
        self, ctx: commands.Context, error: commands.CommandError
    ):
        print(error)
        if isinstance(error, commands.CheckFailure):
            pass
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.NotOwner):
            await ctx.reply(
                embed=embeds.error_embed(
                    "Only the Members of Dev Team are allowed to use this command!!"
                )
            )
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply(
                embed=embeds.error_embed(
                    f"You don't have the Appropriate Permissions to run this command!! Permissions Missing: {', '.join([error.replace('_', ' ').title() for error in error.missing_permissions])}"
                )
            )
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply(
                embed=embeds.error_embed(
                    f"Bot doesn't have the Appropriate Permissions to run this command!! Permissions Missing: {', '.join([error.replace('_', ' ').title() for error in error.missing_permissions])}"
                )
            )
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(
                embed=embeds.error_embed(
                    "Please make sure to provide all the required Arguments!!"
                )
            )
        elif isinstance(error, commands.BadArgument):
            await ctx.reply(
                embed=embeds.error_embed(
                    "Please make sure to provide the Arguments correctly!!"
                )
            )
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.reply(
                embed=embeds.error_embed(
                    f"This Command is currently in Cooldown for you!! Try again in {int(error.retry_after)} seconds!!"
                )
            )
        else:
            await ctx.reply(embed=embeds.error_embed(repr(error)))

    async def on_slash_command_error(
        self, inter: disnake.ApplicationCommandInteraction, error: commands.CommandError
    ):
        print(error)
        if isinstance(error, commands.MissingPermissions):
            await inter.response.send_message(
                embed=embeds.error_embed(
                    f"You don't have the Appropriate Permissions to run this command!! Permissions Missing: {', '.join([error.replace('_', ' ').title() for error in error.missing_permissions])}"
                ),
                ephemeral=True,
            )
        elif isinstance(error, commands.MissingRequiredArgument):
            await inter.response.send_message(
                embed=embeds.error_embed(
                    "Please make sure to provide all the required Arguments!!"
                ),
                ephemeral=True,
            )
        elif isinstance(error, commands.BotMissingPermissions):
            await inter.response.send_message(
                embed=embeds.error_embed(
                    f"Bot doesn't have the Appropriate Permissions to run this command!! Permissions Missing: {', '.join([error.replace('_', ' ').title() for error in error.missing_permissions])}"
                ),
                ephemeral=True,
            )
        elif isinstance(error, commands.BadArgument):
            await inter.response.send_message(
                embed=embeds.error_embed(
                    "Please make sure to provide the Arguments correctly!!"
                ),
                ephemeral=True,
            )
        elif isinstance(error, commands.CommandOnCooldown):
            await inter.response.send_message(
                embed=embeds.error_embed(
                    f"This Command is currently in Cooldown for you!! Try again in {int(error.retry_after)} seconds!!"
                ),
                ephemeral=True,
            )
        else:
            await inter.response.send_message(
                embed=embeds.error_embed(repr(error)), ephemeral=True
            )

    def tictactoe_check_winner(self, winning_conditions, mark):
        for condition in winning_conditions:
            if (
                self.tictactoe_board[condition[0]] == mark
                and self.tictactoe_board[condition[1]] == mark
                and self.tictactoe_board[condition[2]] == mark
            ):
                self.tictactoe_game_over = True
