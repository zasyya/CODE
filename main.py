import discord
import random
import time
from discord.ext import commands

intents = discord.Intents.default()

# Create a settings dictionary to store your token
settings = {
    "token": "MTE2MzkwODU1MDAyMDU4MzUzNA.GwBkdI.qj99Ixa8OYql0itwtPhSK_Ak2CsegqK5qeqH_M"
}

intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def chat(ctx):
    await ctx.send(f'Merhaba! Ne hakkında konuşalım?')

@bot.command()
async def bored(ctx):
    await ctx.send(f'Ooo. Ne konuşalım?')

@bot.command()
async def nofriends(ctx):
    await ctx.send(f'Ooo. Ne konuşalım?!')
    
@bot.command()
async def anime(ctx):
    await ctx.send(f'ooo')
    time.sleep (1)
    await ctx.send(f'Bende öyle bir bilgi yok x-x')
    time.sleep (1)
    await ctx.send(f'Ama minecraft konuşabiliriz!')

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)





bot.run("MTE2MzkwODU1MDAyMDU4MzUzNA.GwBkdI.qj99Ixa8OYql0itwtPhSK_Ak2CsegqK5qeqH_M")
