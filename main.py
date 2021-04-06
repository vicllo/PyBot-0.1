# coding: utf8

import discord
from discord.ext import commands
import constants
import exec
import sys
import os

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
console = sys.stdout




#detecter l'allumage du bot
@bot.event
async def on_ready():
    print("Successfully connected !")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("!python"))


@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    serveur = member.guild.id
    print(channel,serveur)
    if serveur == 682539277330284585:
        if channel is not None:
            await channel.send('Bienvenue sur le serveur général {0.mention}, merci d\'écrire ici ton prénom, nom ainsi que ta classe afin que tu sois assigné(e) à ta classe.'.format(member))
    elif serveur == 707200285436805141:
        if channel is not None:
            await channel.send('Bienvenue sur le serveur des 2nde {0.mention}, merci d\'écrire ici ton prénom, nom ainsi que ta classe afin que tu sois assigné(e) à ta classe.'.format(member))
    else:
        if channel is not None:
            await channel.send('Bienvenue sur le serveur {0.mention}.'.format(member))

#commande test
@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def python(ctx):
    sys.stdout = console
    channel = ctx.channel
    authorid = ctx.author.id
    parametres = ["Result","Warnings","Errors","Stats"]
    def check(m):
        return m.channel == channel and m.author.id == authorid
    messagebot = await ctx.send(constants.sendmsg)
    prgm = await bot.wait_for('message', check=check)
    await messagebot.delete(delay=2)
    await ctx.message.delete(delay=2)
    if prgm.content.startswith("```"):
        prgm.content = prgm.content.replace("```python","")
        prgm.content = prgm.content.replace("```","")
    retour_api = exec.main(prgm.content)
    retour_txt = "\n".join([parametre+" :\n"+retour_api[parametre] for parametre in parametres if retour_api[parametre]])
    try:
        await ctx.send("```"+retour_txt+"```")
    except discord.errors.HTTPException:
        await ctx.send("```Votre programme a retourné plus de 2000 caractères, veuillez raccourcir sa sortie```")


@bot.event
async def on_raw_reaction_add(payload):
    channel = bot.get_channel(payload.channel_id)
    messageReaction = await channel.fetch_message(payload.message_id)
    if messageReaction.author.id == constants.botid and payload.user_id != constants.botid:
        if payload.emoji.name == constants.emotrash:
            await messageReaction.delete()


print("Let's go")
token = os.environ['TOKEN']
bot.run("Njg5OTM0OTY4Mjg1Mjk4ODA4.Xwtyrg.b9KPlxtFXp4mFWuCqv7aVkRYwK8")

