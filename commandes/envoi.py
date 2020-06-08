import os
import re

async def retour(ctx):
    with open('listeretour.txt',"r") as listeretour:
        for cle in listeretour:
            if cle != "":
                cle = cle.replace("\n","")
                fichier = 'retours/retour'+cle+".txt"
                with open(fichier,"r") as retour:
                    retour = retour.read().split("\n")
                    texte = "```"
                    for i in range(3, len(retour) - 1):
                        retour[i] = re.sub("\"", "\\\"", retour[i])
                        texte = texte + "\n" + str(retour[i])
                    texte = texte + "\n```"
                    await ctx.send(str(texte))
                os.remove(fichier)
                os.remove("messages/message"+str(cle)+".py")
            newlisteretour = listeretour.read().replace(cle,"")
    with open("listeretour.txt","w") as listeretour:
        listeretour.write("")
