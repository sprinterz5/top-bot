#-*- coding: utf8 -*-
import discord
import pyowm
from aiohttp import payload
from discord.ext import commands
from discord import utils, member
import datetime
from discord.utils import get
import speech_recognition as sr
import os
import requests
import youtube_dl

PREFIX="."

client = commands.Bot( command_prefix = PREFIX)
client.remove_command('help')

TOKEN = os.environ.get('BOT_TOKEN')


owm=pyowm.OWM('30f0f24d13edf5250a9b4f7d09983eb8', language="ru")

@client.event
	
async def on_command_error(ctx, error):
	author = ctx.message.author
	if isinstance (error, commands.MissingRequiredArgument):
		await ctx.send(f'{author.mention}, нельзя использовать команду без аргумента!')
	if isinstance (error, commands.MissingPermissions):
		await ctx.send(f'{author.mention}, у вас недостаточно прав!')
	if isinstance (error, commands.CommandNotFound):
		await ctx.send(f'{author.mention}, выбрана неверная команда!')
@client.event

async def on_ready():
	print('Sucsessfully logged!')  # вход
#.help

@client.command(pass_context = True)

async def time(ctx):
	emb=discord.Embed(title='Время сейчас: ', description = 'Вы сможете узнать текущеe время!', colour = discord.Color.green(), url='https://www.timeserver.ru/cities/kz/nur-sultan')
	emb.set_author(name=client.user.name, icon_url=client.user.avatar_url)
	emb.set_footer(text='Спасибо, что не кикнули бота!', icon_url= ctx.author.avatar_url)
#	emb.set_image(url='https://s.sellercheck.ru/pic/9a/d8/nordic-seryy-abstraktnaya-zhivopis-nastennye-chasy-s-geometricheskim-risunkom-minimalistskiy-9ad811627c677b5c5355bde71b3c5dd0-500.jpg')
	emb.set_thumbnail(url='https://s.sellercheck.ru/pic/9a/d8/nordic-seryy-abstraktnaya-zhivopis-nastennye-chasy-s-geometricheskim-risunkom-minimalistskiy-9ad811627c677b5c5355bde71b3c5dd0-500.jpg')

	now_date = datetime.datetime.now()
	emb.add_field(name='Время', value='время: {}'.format(now_date))

	await ctx.send(embed=emb)

@client.command(pass_context = True)

async def weather (ctx, city = 'Нур-Султан'):

	observation=owm.weather_at_place(city)
	w = observation.get_weather()
	temp=w.get_temperature('celsius')["temp"]
	author = ctx.message.author

	emb = discord.Embed(title='Погода', description = f'{author.mention}, узнайте погоду на данный момент!', colour = discord.Color.green())
	emb.set_author(name=client.user.name, icon_url=client.user.avatar_url)
	emb.set_footer(text='Спасибо, что не кикнули бота!', icon_url= ctx.author.avatar_url)
	emb.add_field(name = f'{author.mention}'.format(PREFIX), value = f'{author.mention}, сейчас в городе ' + w.get_detailed_status() + f'!\nТемпература в районе {temp} градусов!')
	await ctx.send(embed=emb)

@client.command(pass_context = True)

async def триста (ctx):
	author = ctx.message.author
	await ctx.send( f'{author.mention}, желаю вам соснуть у тракториста!' )

@client.command(pass_context = True)

async def fuck (ctx, amount=1):
	await ctx.channel.purge(limit=1)
	author = ctx.message.author
	await ctx.send( f'{author.mention}, Я думаю ты хочешь поиграть со мной~\nОднако, просто иди в прон! ' )

@client.command(pass_context = True)

async def rules (ctx, amount = 1):
	await ctx.channel.purge(limit=1)
	author = ctx.message.author
	emb = discord.Embed(title='Правила!', description = f'{author.mention}, здесь основные правила сервера!', colour = discord.Color.green())
	emb.set_author(name=client.user.name, icon_url=client.user.avatar_url)
	emb.set_footer(text='Спасибо, что не кикнули бота!', icon_url= ctx.author.avatar_url)
	emb.add_field(name = f'{author.mention}'.format(PREFIX), value = '\n1. Не распространяйте опасный/запрещённый материал\nВы должны сохранять наш сервер от распространения вирусов, читов/эксплоитов, порнографии, ссылок на серверы с вышеперечисленным. Нарушение этого правила является нарушением не только наших условий, но и условий Discord.\n\n 2) Ведите себя сносно. Т.е не нужно набрасываться на людей с оскорблениями. \n\n 3) Не занимайтесь рекламой\nЕсли вы уверены, что ваша реклама стоит общего внимания - сначала спросите у Модераторов и Аллаха или просто не отправляйте.\n\n4) Слушайтесь Администраторов\nМодератор или какой-либо другой персонаж из ранга аристократов может попросить вас что-либо сделать, например, заткнуться - не испытывайте его терпение.\n\n5) Сохраняйте здравый смысл!\n\n6) Не пойман - не вор!')
	await ctx.send(embed=emb)

@client.command(pass_context=True)

async def hello (ctx, amount = 1):
	await ctx.channel.purge(limit=1)
	author = ctx.message.author

	emb = discord.Embed(title='Вас приветствует discord-бот Айдара!', description = f'{author.mention}, здравия вам! Что хотели бы?', colour = discord.Color.green())
	emb.set_author(name=client.user.name, icon_url=client.user.avatar_url)
	emb.set_footer(text='Спасибо, что не кикнули бота!', icon_url= ctx.author.avatar_url)
	emb.add_field(name = '{}help'.format(PREFIX), value = 'Чтобы перейти к командам!')
	await ctx.send(embed=emb)

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)

async def clear(ctx, amount : int): #создаем асинхронную фунцию бота
	author = ctx.message.author
	
	if amount == 228:
		await ctx.channel.purge(limit = 9999)
		await ctx.send(f'{author.mention}, вы удалили все сообщения!')
	else:
		await ctx.channel.purge (limit = amount) #отправляем обратно аргумент
		await ctx.send(f'{author.mention}, вы удалили ' f'{amount}' ' сообщений! (считая вместе с вашей командой ~clear)')
@client.command(pass_context=True)

async def help(ctx, amount=1): #создаем асинхронную фунцию бота
	await ctx.channel.purge (limit = amount)
	emb = discord.Embed(title='Навигация по командам', description = 'Здесь вы можете увидеть команды!', colour = discord.Color.green())
	emb.set_author(name=client.user.name, icon_url=client.user.avatar_url)
	emb.add_field(name = '{}clear'.format(PREFIX), value = 'Очистка чата')
	emb.add_field(name = '{}hello'.format(PREFIX), value = 'Приветствие/проверка чата')
	emb.add_field(name = '{}rules'.format(PREFIX), value = 'Правила')
	emb.add_field(name = '{}userinfo'.format(PREFIX), value = 'Информация о пользователе')
	emb.add_field(name = '{}serverinfo'.format(PREFIX), value = 'Информация о сервере')
	emb.add_field(name = '{}join'.format(PREFIX), value = 'Присоединение бота к каналу')
	emb.add_field(name = '{}play'.format(PREFIX), value = 'Включение музыки(нужна точная ссылка)')
	emb.add_field(name = '{}leave'.format(PREFIX), value = 'Отключение бота от канала')
	emb.add_field(name = '{}триста'.format(PREFIX), value = 'Фразочка')
	emb.add_field(name = '{}fuck'.format(PREFIX), value = 'Фразочка')
	emb.add_field(name = '{}fuck'.format(PREFIX), value = 'Фразочка')
	emb.add_field(name = '{}fuck'.format(PREFIX), value = 'Фразочка') 
	await ctx.send(embed=emb)

@client.event

async def on_member_join(member):
	channel = client.get_channel(668798551073226756)

	role = discord.utils.get(member.guild.roles, id = 669141705718628382)

	await member.add_roles(role)
	await channel.send(embed = discord.Embed(description = f'Пользователь ``{member.name}``, присоединился к серверу!', color = 0x0c0c0c))

@client.command()
async def send_a (ctx):
	await ctx.author.send('БАН!')

@client.command()
async def send_m (ctx, member: discord.Member):
	await member.send(f'{member.name}, привет от {ctx.author.name}!')

@client.command()
async def join (ctx):
	global voice
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild = ctx.guild)

	if voice and voice.is_connected():
		await voice.move_to(channel)
	else:
		voice = await channel.connect()
		await ctx.send(f'Бот присоединился к каналу: {channel}')

@client.command()
async def leave (ctx):
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild = ctx.guild)

	if voice and voice.is_connected():
		await voice.disconnect()
	else:
		voice = await connect.channel()
		await ctx.send(f'Бот отсоединился от канала: {channel}')

@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile('song.mp3')

    try:
        if song_there:
            os.remove('song.mp3')
            print('[log] Старый файл удален')
    except PermissionError:
        print('[log] Не удалось удалить файл')

    await ctx.send('Пожалуйста ожидайте')

    voice = get(client.voice_clients, guild = ctx.guild)

    ydl_opts = {
        'format' : 'bestaudio/best',
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192'
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('[log] Загружаю музыку...')
        ydl.download([url])

    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            name = file
            print(f'[log] Переименовываю файл: {file}')
            os.rename(file, 'song.mp3')

    voice.play(discord.FFmpegPCMAudio('song.mp3'), after = lambda e: print(f'[log] {name}, музыка закончила свое проигрывание'))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    song_name = name.rsplit('-', 2)
    await ctx.send(f'Сейчас проигрывает музыка: {song_name[0]}')

@client.command()
async def members_info(ctx):
    server_members = ctx.guild.members
    data = "\n".join([i.name for i in server_members])
    
    await ctx.send(data)

@client.event
async def on_ready(*args):
    type = discord.ActivityType.watching
    activity = discord.Activity(name = "за сервером", type = type)
    status = discord.Status.dnd
    await client.change_presence(activity = activity, status = status)
@client.event
async def on_ready(*args):
    type = discord.ActivityType.listening
    activity = discord.Activity(name = "чат", type = type)
    status = discord.Status.dnd
    await client.change_presence(activity = activity, status = status)
@client.command()
async def serverinfo(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author

    guild = ctx.guild
    embed = discord.Embed(title=f"{guild.name}", description=f"Сервер создали {guild.created_at.strftime('%b %#d, %Y')}\n\n"
                                                             f"Регион {guild.region}\n\nГлава сервера {guild.owner}\n\n"
                                                             f"Людей на сервере {guild.member_count}\n\n",  color=0xff0000,timestamp=ctx.message.created_at)

    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f"ID: {guild.id}")

    embed.set_footer(text=f"ID Пользователя: {ctx.author.id}")
    await ctx.send(embed=embed)

@client.command()
async def userinfo(ctx, Member: discord.Member = None ):
    if not Member:
        Member = ctx.author
    roles = (role for role in Member.roles )
    emb = discord.Embed(title='Информация о пользователе.'.format(Member.name), description=f"Участник зашёл на сервер: {Member.joined_at.strftime('%b %#d, %Y')}\n\n "
                                                                                      f"Имя: {Member.name}\n\n"
                                                                                      f"Никнейм: {Member.nick}\n\n"
                                                                                      f"Статус: {Member.status}\n\n"
                                                                                      f"ID: {Member.id}\n\n"
                                                                                      f"Высшая роль: {Member.top_role}\n\n"
                                                                                      f"Аккаунт создан: {Member.created_at.strftime('%b %#d, %Y')}", 
                                                                                      color=0xff0000, timestamp=ctx.message.created_at)

    emb.set_thumbnail(url= Member.avatar_url)
    emb.set_footer(icon_url= Member.avatar_url)
    emb.set_footer(text='Команда вызвана: {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)

client.run(TOKEN)