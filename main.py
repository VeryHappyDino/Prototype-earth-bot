import os
import discord
import random
import requests

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

consiglio1 = ""
consiglio2 = ""

client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f"Connesso come {client.user.name}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("/consigli_acqua"):
        risultato = random.choice(["Docce brevi: Riduci la durata delle docce","Chiudi il rubinetto: Non lasciarlo aperto quando ti lavi i denti o ti fai la barba.", "Ripara perdite: Controlla e ripara eventuali perdite da rubinetti, tubi e cisterne.","Ripara perdite: Controlla e ripara eventuali perdite da rubinetti, tubi e cisterne.","Elettrodomestici efficienti: Scegli modelli che consumano meno acqua.","Acqua di pioggia: Raccogli e utilizza l acqua piovana per usi non potabili.","Innaffia con intelligenza: Bagna le piante nelle ore più fresche e considera un sistema di irrigazione a goccia.","Innaffia con intelligenza: Bagna le piante nelle ore più fresche e considera un sistema di irrigazione a goccia.","Innaffia con intelligenza: Bagna le piante nelle ore più fresche e considera un sistema di irrigazione a goccia.","Piante autoctone: Scegli piante che richiedono meno acqua.","Toilette a basso consumo: Installa o utilizza modelli che utilizzano meno acqua per scarico.","Riutilizzo dell acqua: Ad esempio, l'acqua di cottura per annaffiare.","Evita sprechi alimentari: Poiché la produzione di cibo richiede acqua.","Lavaggio auto intelligente: Usa secchio e spugna piuttosto che il tubo.","Educazione: Insegna agli altri l importanza del risparmio idrico."])
        await message.channel.send(f"{risultato}")
    if message.content.startswith("/help"):
        risultato2 = ("usa il comando /consigli_acqua per ricevere consigli su come risparmiare l'acqua")
        await message.channel.send(f"{risultato2}")

# Inserisci il tuo token del bot Discord qui
TOKEN = 'MTE2NTIyNzkxMzEyNjM0Njg0Mw.GAD7T_.XiZ6Lu4Owf3eV4BtDhNV4lJSN3nDyBJCbyX4NQ'

client.run(TOKEN)




















