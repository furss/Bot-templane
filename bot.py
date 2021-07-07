import discord
from config import settings #импортируем из config.py настройки
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='!')      #устанавливаем префикс


@bot.event                      #когда бот запустился
async def on_ready():           
    print('Бот включен')       #выводим это в КОНСОЛЬ

@bot.command() #Выводит картинку при команде !test
async def test(ctx):
    await ctx.send("https://i.imgur.com/p3wZM8L.jpg")

#Embed(Команда - !emb)
@bot.command()
async def emb(ctx):
        em = discord.Embed(title='**Название**', description='Описание', color=ctx.author.color)
        
        em.add_field(name='Опция(1)', value='маленькая опция') #(add_field можно дублировать для создания большего кол-во строк)
        em.set_thumbnail(url = 'https://i.imgur.com/pJv1Wyw.jpg') #Маленькая картинка справа от текста
        em.set_image(url = 'https://i.imgur.com/pJv1Wyw.jpg') #Большая картинка снизу
        await ctx.send(embed=em)
#Об других функциях можете почитать в документации


bot.run(settings['Token']) #тут можно ничего не трогать
