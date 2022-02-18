import discord
import random
import os

from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
ANNONCE = os.getenv('DISCORD_ANNONCE')

#Variables
bot = commands.Bot(command_prefix = "!",description ="Bot lumino test")

list_OriginalQuestions = ["```Pour ou contre les uniformes scolaires ?```","```Sommes-nous dépendants des ordinateurs?```","```Faut-il obligatoirement être un esprit torturé pour être un grand artiste ?```","```Quel serait ton animal totem ?```","```Si tu pouvais poser une question à Dieu, laquelle serait-elle ?```","```C'est la semaine du compliment alors n'hésitez pas à complimenter votre prochain sur le serveur!```","```Quel plat pourrais-tu manger sans t'en lasser ?```","```La question de l'écologie est importante pour vous ?```","```C'est l'heure de la recommandation cinéma de la semaine! Allez dans le salon dédié pour nous faire part de votre plus beau film!```","```Que pensez-vous en toute honnêteté de la KPOP?```","```Que pensez-vous en toute honnêteté du rap français ?```", "```Faut-il apprendre aux enfants à gérer leur argent à l'école ?```","```Les parents agissent-ils différemment s'ils ont une fille ou un garçon ?```","```Apprenez nous quelque chose d'étonnant sur vous!```","```Les bandes dessinées et les littératures classiques ont-elles les mêmes valeurs ?```"]
list_QuestionsAsked = list_OriginalQuestions

#Event de lancement
@bot.event
async def on_ready():
    print("Ready!")
@bot.command()
async def challengeRestants(ctx):
    valeur = len(list_QuestionsAsked)
    textDisplay = "<@&" + str(ANNONCE) + "> Il reste " + str(valeur) +" questions restantes dans la base de données."
    await ctx.send(textDisplay+" <:teehee:671089198316650524>")
@bot.command()
async def challengeAleatoire(ctx):
	n = random.randint(0,len(list_QuestionsAsked)-1)
	valeur = list_QuestionsAsked[n]
	list_QuestionsAsked.pop(n)
	print(list_QuestionsAsked)
	await ctx.send("<@&" + str(ANNONCE) + ">\n"+valeur)
@bot.command()
async def challengeNumero(ctx, *, indice):
	valeur = list_QuestionsAsked[int(indice)]
	list_QuestionsAsked.pop(int(indice))
	print(list_QuestionsAsked)
	await ctx.send("<@&" + str(ANNONCE) + ">\n"+valeur)

@bot.command()
async def regles(ctx):
	await ctx.send("```Les règles sont simples : toujours répondre à la question qui est posée ou le défi. On ne joue pas les demi-mesures et on répond par oui ou par non quand le besoin y est! \nJe compte sur vous pour ramener à la vie ce petit channel qui n'attend que vos réponses!```")

bot.run(TOKEN)
