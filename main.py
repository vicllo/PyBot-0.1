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
async def python(ctx, arg):
    print(arg)
    print(ctx.message.content)
    commandes.exec.main(ctx, arg)
    sys.stdout = console
    with open("listeretour.txt","r") as listeretour:
        for num in listeretour:
            nomfichier = "retour"+num+".txt"
            nomfichier = nomfichier.replace("\n","")
            #print(nomfichier)
            with open(nomfichier,"r") as retour:
                retourcomplet = retour.read().split("\n")
                print(retourcomplet)
                guilde = bot.get_guild(int(retourcomplet[0]))
                print(guilde)
                print(int(retourcomplet[1]))
                canal = guilde.get_channel(int(retourcomplet[1]))
                auteur = retourcomplet[2]
                texte = "```"
                for i in range(3,len(retourcomplet)-1):
                    retourcomplet[i] = re.sub("\"","\\\"",retourcomplet[i])
                    texte = texte+"\n"+str(retourcomplet[i])
                texte = texte+"\n```"
                await canal.send(str(texte))
            os.remove(nomfichier)
            with open("listeretour.txt","r") as listeretour:
                tousretour = listeretour.read()
            nouvretour = tousretour.replace(num,"")
            with open("listeretour.txt","w") as listeretour:
                listeretour.write(nouvretour)

token = os.environ.get("DISCORD_BOT_SECRET")
#lancement
bot.run(token)

