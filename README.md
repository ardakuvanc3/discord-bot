# Gereklilikler

* "pip install requirements.txt" komutu ile gerekli kütüphanelerin yüklenmesinin yapılması.
* Token bilgisi verilesi.
* Rollerin ve emojilerin düzenlenmesi.
* Aşağıdaki kodun çoğaltılıp rollere göre düzenlenmesi
 ```dart
@bot.event
async def on_raw_reaction_add(payload):
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
    if payload.emoji.name == 'emojinin_adı': # Emoji adını buraya yaz
        role = discord.utils.get(guild.roles, name="rolün_adı") # Rol ismini buraya yaz
        if role is not None:
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
 ``` 
