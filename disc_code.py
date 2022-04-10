import os

import discord
from discord.ext import commands
import lolbot as lolbot

TOKEN = "OTU1OTUyMDEwNzQ4OTE5ODY4.YjpJsA.hxd1VNbEhyfoeJUHmcu-4yvDzuM"

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'{bot.user} successfully logged in!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content == 'hello':
        await message.channel.send(f'Hi {message.author}')
    if message.content == 'bye':
        await message.channel.send(f'Goodbye {message.author}')

    await bot.process_commands(message)
    
@bot.command()
async def info(ctx, *, arg='None'):
    
    lolbot.user_input = arg
    lolbot.set_me()
    # print('>>>>',lolbot.me)
    message = lolbot.get_ID()
   
    await ctx.send(message)

@bot.command()
async def ranksolo(ctx, *, arg='None'):
    lolbot.user_input = arg
    lolbot.set_me()
    lolbot.get_stats()
    # print('>>>>',lolbot.me)
    message = lolbot.get_solo()
    
    await ctx.send(message)

@bot.command()
async def teamrank(ctx, arg1='None',arg2='None',arg3='None',arg4='None',arg5='None'):
    lolbot.user_input = arg1
    lolbot.set_me()
    lolbot.get_stats()
    # print('>>>>',lolbot.me)
    message1 = lolbot.get_solo()
    lolbot.user_input = arg2
    lolbot.set_me()
    lolbot.get_stats()
    message2 = lolbot.get_solo()
    lolbot.user_input = arg3
    lolbot.set_me()
    lolbot.get_stats()
    message3 = lolbot.get_solo()
    lolbot.user_input = arg4
    lolbot.set_me()
    lolbot.get_stats()
    message4 = lolbot.get_solo()
    lolbot.user_input = arg5
    lolbot.set_me()
    lolbot.get_stats()
    message5 = lolbot.get_solo()
    messages = [message1, message2, message3, message4, message5]

    pre_message = ''
    final_message = ''
    count = 0
    message = ''

    for message in messages:
        if count < 4:
            if messages[count] != messages[count+1]:
                pre_message = pre_message + "\n" + messages[count] + "\n"
                count = count + 1
    final_message = pre_message + "\n" + messages[4]
    
    await ctx.send(final_message)

@bot.command()
async def teamrank2(ctx, *args):
    lolbot.user_input = args
    lolbot.set_me()
    lolbot.get_stats()
    # print('>>>>',lolbot.me)
    message = lolbot.get_solo()
    await ctx.send(message)

@bot.command()
async def rankflex(ctx, *, arg='None'):
    
    lolbot.user_input = arg
    lolbot.set_me()
    lolbot.get_stats()
    # print('>>>>',lolbot.me)
    message = lolbot.get_flex()
    
    await ctx.send(message)

# @bot.command()
# async def mastery(ctx, *, arg1='None'):
#     lolbot.user_input = arg1
#     lolbot.set_me()
#     lolbot.get_stats()
#     # print('>>>>',lolbot.me)
#     message = lolbot.get_mastery()
#     print(message)
#     await ctx.send(message)

@bot.command()
async def mastery(ctx, arg1, arg2 = 5):
    lolbot.user_input = arg1
    lolbot.max_val = arg2
    lolbot.set_me()
    lolbot.get_stats()
    # print('>>>>',lolbot.me)
    message = lolbot.get_mastery()
    
    await ctx.send(message)

@bot.command()
async def ping(ctx):
    await ctx.send("Ping")

bot.run(TOKEN)
