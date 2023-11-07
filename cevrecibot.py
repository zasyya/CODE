import discord
import random
import time
from discord.ext import commands

intents = discord.Intents.default()

# Create a settings dictionary to store your token
settings = {
    "token": "heyy tokenimle ne işin var!!"
}

intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben çevreci bir botum!')
    time.sleep(1)
    await ctx.send(f'Haydi biraz konuşalım!')


@bot.command()
async def chat(ctx):
    await ctx.send(f'Merhaba! Ne hakkında konuşalım?')

@bot.command()
async def cevre(ctx):
    await ctx.send(f'Çevre ve kirlilik hakkınya birşey yapmak istiyorsanız ne_yaplamliyim komutunu kullan!')

@bot.command()
async def ne_yapmaliyim(ctx):
    await ctx.send(f'Geri dönüşüm ve hangi malzemelerin geri dönüştürülebileceği hakkında bilgi edinin.')
    time.sleep(1)
    await ctx.send(f'Eski eşyaları çöpe atmak yerine geri dönüştürün')
    time.sleep(1)
    await ctx.send(f'Tek kullanımlık ürünlerin kullanımını azaltmak için yeniden kullanılabilir ürünler kullanın.')
    time.sleep(1)
    await ctx.send(f'Hangi ürünlerin ve ambalajların geri dönüşüm için en iyi olduğunu araştırın ve satın alırken bunları seçin.')
    time.sleep(1)
    await ctx.send(f'Su kullanmadığınız zamanlarda musluğu açık bırakmayarak su tasarrufu yapın.')
    time.sleep(1)
    await ctx.send(f'Evde ampuller ve klimalar gibi enerji tasarruflu cihazlar kullanın..')
    time.sleep(1)
    await ctx.send(f'Ulaşım masraflarını azaltmak için yerel kaynaklardan yiyecek satın alın.')
    time.sleep(1)
    await ctx.send(f'Araba kullanmak yerine toplu taşıma araçlarını, bisikletleri ve ayaklarınızı (mümkün olduğunda) kullanmaya çalışın.')
    time.sleep(1)
    await ctx.send(f'Çevre ve kirlilik hakkında başka bir sorun var mı acaba?')

@bot.command()
async def meme(ctx):
    await ctx.send(f'emoji_1')


bot.run("tokenimi çalma")
