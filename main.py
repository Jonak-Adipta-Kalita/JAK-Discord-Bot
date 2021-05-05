import discord, random
from discord.ext import commands

prefix = "!JAK "
client = commands.Bot(command_prefix = prefix)
client.remove_command('help')

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
token = read_token()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('!JAK help'))
    print('Starting The Bot...')
    print('Bot Started...')
    print('Running Bot...')

@client.command()
async def help(ctx):
    await ctx.send(r"""1. `!JAK ` :Default Prefix
2. `!JAK help` :Show all the commands
3. `!JAK ping` :Show the ping
4. `!JAK 8ball <question>` :Play 8ball game
5. `!JAK clear <amount>` :Delete messages as given amount
6. `!JAK kick <@member> reason=<reason>` :kick member/bot
7. `!JAK ban <@member> reason=<reason>` :ban member/bot
8. `!JAK unban <member,tag>` :unban member/bot
9. `!JAK show_rules` :Show the rules """)

@client.command()
async def show_rules(ctx):
    await ctx.send(r"""1. Be Cool
2. Be Awesome
3. Support Each Other
4. Don't Betray Anybody
5. Always Support YOUTUBE not TIKTOK
6. Dont Ask For Roles """)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} is banned')

@client.command()
async def unban(ctx, *, member):
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_user:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator) :
            await ctx.guild.unban(user)
            await ctx.send(f'{member.mention} is unbanned')
            return

@client.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)


@client.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(client.latency * 1000)}')

@client.event
async def on_member_join(member, ctx):
    await ctx.send(f'{member} Just Joined')

@client.event
async def on_member_remove(member, ctx):
    await ctx.send(f'{member} Just Left What A Shame 🤣🤣🤣')

@client.command(aliases = ['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes – definitely.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                "Don't count on it.",
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtfut.',
                'Kinda Lazy to answer.'
    ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

client.run(token)
