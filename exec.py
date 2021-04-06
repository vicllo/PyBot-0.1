# coding: utf8
import requests

def main(programme):
    to_compile = {
        "LanguageChoice": "24",
        "Program": programme,
        "Input": "",
        "CompilerArgs": ""
    }

    retour = requests.post("https://rextester.com/rundotnet/api", to_compile)

    return retour.json()