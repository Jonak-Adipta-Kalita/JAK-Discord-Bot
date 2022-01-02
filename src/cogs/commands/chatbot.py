import disnake, asyncio
import src.core.functions as funcs
from disnake.ext import commands


class ChatBot(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.chatbot_on: bool = False
        self.chatbot_channel: disnake.TextChannel = None

    @commands.group(description="Start Chatbot")
    async def chatbot(self, ctx: commands.Context, command: str = None):
        if command:
            await ctx.reply("Command not Found")
            return

        self.chatbot_on = True
        self.chatbot_channel = ctx.channel
        await ctx.reply("Started Chatbot!! Will be Active for 5 Mins")

        await asyncio.sleep(300)

        self.chatbot_on = False
        self.chatbot_channel = None
        await ctx.reply("Chatbot Stopped!!")

    @chatbot.command(description="Stop Chatbot")
    async def stop(self, ctx: commands.Context):
        self.chatbot_on = False
        await ctx.reply("Stopped Chatbot!!")

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        if message.author == self.bot.user:
            return
        if self.chatbot_on and message.channel == self.chatbot_channel:
            response = await funcs.chatbot_response(message=message.content)
            if response:
                await message.reply(response)
            else:
                await message.reply("Something went Wrong!!")


def setup(bot: commands.Bot):
    bot.add_cog(ChatBot(bot))
