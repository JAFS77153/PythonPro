import discord
import random
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

bot.run("MTQ5NTUzNjIzMjY2NTcxMDY3Mg.G1btr_.I7MEl9gzorPrssWh48nNvdV1yICvlqkNekZPpk")
