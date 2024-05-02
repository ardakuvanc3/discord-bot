import discord
from discord.ext import commands

#pip install requirements.txt

intents = discord.Intents.default()
intents.reactions = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} aktif!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Yasaklı kelimeleri kontrol etmek için
    yasakli_kelimeler = ["kelime1", "kelime2"]  # Yasaklı kelimeleri buraya ekle.
    for kelime in yasakli_kelimeler:
        if kelime in message.content.lower():
            await message.delete()
            await message.channel.send(f"{message.author.mention}, yasaklı bir kelime kullandınız. Lütfen dikkat ediniz.")

    # Linkleri kontrol etmek için
    if "http://" in message.content.lower() or "https://" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, link paylaşımı yapmak yasaktır.")

    await bot.process_commands(message)



@bot.event
async def on_raw_reaction_add(payload):
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
    if payload.emoji.name == 'emojinin_adı': # Emoji adını buraya yaz
        role = discord.utils.get(guild.roles, name="rolün_adı") # Rol ismini buraya yaz
        if role is not None:
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)



@bot.event
async def on_raw_reaction_remove(payload):
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
    if payload.emoji.name == 'emojinin_adı': # Emoji adını buraya yaz
        role = discord.utils.get(guild.roles, name="rolün_adı") # Rol ismini buraya yaz
        if role is not None:
            member = guild.get_member(payload.user_id)
            await member.remove_roles(role)
            
#istediğin zaman çoğaltabilirsin.

bot.run('TOKEN') # TOKEN
