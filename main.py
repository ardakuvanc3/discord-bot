import discord
from discord.ext import commands

intents = discord.Intents.all()

class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(command_prefix='/', intents=intents, *args, **kwargs)

bot = MyBot()

@bot.event
async def on_ready():
    print(f'Bot {bot.user} olarak giriş yaptı!')

@bot.event
async def on_command_error(ctx, error):
    print(f'Hata: {error}')

@bot.command(name='merhaba')
async def hello(ctx):
    await ctx.send('Merhaba!')

bot.run('key')