import discord
from discord.ext import commands
import random
import os

# Configuracion de permisos
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Lista de consejos (se elegiran al azar)
consejos_eco = [
    "Ahorro de energia: Apaga luces y aparatos electricos cuando no los uses, cambia a bombillas LED y aprovecha la luz natural siempre que sea posible.",
    "Adios al plastico: Opta por bolsas reutilizables, botellas de acero inoxidable y envases de vidrio en lugar de plasticos de un solo uso.",
    "Movilidad sostenible: Camina, usa bicicleta o transporte público en lugar del auto particular. Si es posible, comparte viajes para reducir emisiones.",
    "Consumo responsable: Compra productos locales y de temporada, reduce el desperdicio de alimentos y elige marcas con practicas sostenibles.",
    "Cuidado del agua: Repara fugas, instala dispositivos ahorradores y reutiliza agua siempre que sea posible.",
    "Reforestacion: Los arboles absorben dioxido de carbono y ayudan a mantener la biodiversidad. Participar en jornadas de reforestacion es una gran forma de contribuir.",
    "Clasificacion: Clasifica papel, vidrio, plastico y metales para que puedan ser reutilizados en lugar de terminar en vertederos.",
    "Energia limpia: Si tienes la posibilidad, instala paneles solares o contrata servicios que ofrezcan energia limpia.",
    "Durabilidad: Evita la cultura del usar y tirar. Prefiere electrodomesticos, ropa y muebles de buena calidad que duren mas tiempo.",
    "Educacion: Habla con tu familia y amigos sobre la importancia de cuidar el planeta, y participa en actividades comunitarias que fomenten la conciencia ecologica."
]

@bot.command()
async def consejo(ctx):
    # Esta linea elige uno de la lista de forma aleatoria
    frase_aleatoria = random.choice(consejos_eco)
    await ctx.send(f"Tip Ecologico: {frase_aleatoria}")
