import discord
from discord.ext import commands
import commandes.main
import includes.main
import sys
import os
import re
import traceback
from commandes import *

bot = commands.Bot(command_prefix="!")
console = sys.stdout


#detecter l'allumage du bot
@bot.event
async def on_ready():
    print("Succsfully connected")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("En développement"))

#commande help
@bot.command()
async def help2(ctx):
    await ctx.send(commandes.help.main())

#commande librairies
@bot.command()
async def librairies(ctx):
    await ctx.send(commandes.librairies.main())

#commande test
@bot.command()
async def test(ctx):
    await ctx.send("test")

@bot.command()
async def python(ctx):
    sys.stdout = console
    channel = ctx.channel
    authorid = ctx.author.id
    def check(m):
        return m.channel == channel and m.author.id == authorid
    messagebot = await ctx.send(includes.constants.sendmsg)
    prgm = await bot.wait_for('message', check=check)
    await messagebot.delete(delay=2)
    await ctx.message.delete(delay=2)
    if prgm.content.startswith("```"):
        prgm.content = prgm.content.replace("```python","")
        prgm.content = prgm.content.replace("```","")
    await commandes.exec.main(ctx, prgm, console)
    await commandes.envoi.retour(ctx)

@bot.event
async def on_raw_reaction_add(payload):
    channel = bot.get_channel(payload.channel_id)
    messageReaction = await channel.fetch_message(payload.message_id)
    if messageReaction.author.id == includes.constants.botid and payload.user_id != includes.constants.botid:
        if payload.emoji.name == includes.constants.emotrash:
            await messageReaction.delete()


token = os.environ.get("DISCORD_BOT_SECRET")
#lancement
bot.run(token)

