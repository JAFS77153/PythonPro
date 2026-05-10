import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')
    await ctx.send(f'Puedes usar los siguientes comandos: ')
    await ctx.send("Comandos: $hello, $heh (numero), $password (numero), $repeat (palabra), $add (numero)(numero), $mem, $duck, $gato, $plastico (botella, bolsa, plato, cubiertos, pajilla)")

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx, longitud: int):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(longitud):
        password += random.choice(elements)
    await ctx.send("Tu clave es:  " + password)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def mem(ctx):
    imagenes = os.listdir('images')
    image = random.choice(imagenes)
    with open(f'images/{image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def gato(ctx):
    imagenes = os.listdir('imagesGatos')
    image = random.choice(imagenes)
    with open(f'imagesGatos/{image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def plastico(ctx, content: str):
    objetos = {"botella": "400 - 500 años", "bolsa": "450 - 500 años", "plato": "50 - 80 años", "cubiertos": "50 - 80 años", "pajilla": "100 - 200 años"}
    vida = objetos[content]
    await ctx.send(f"{content} se tarda en descomponer {vida} años")

bot.run("MTQ5NTUzNjIzMjY2NTcxMDY3Mg.G1btr_.I7MEl9gzorPrssWh48nNvdV1yICvlqkNekZPpk")
