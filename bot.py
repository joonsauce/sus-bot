import discord
import logging
import random
from setting import *
from discord.ext import commands

# logger
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# bot setup
bot = commands.Bot(command_prefix=prefix)

# susout command
@bot.command()
async def susout(ctx, arg1, *, arg2):
    await ctx.send('{0.author} accused {1} of *{2}*'.format(ctx, arg1, arg2))
    
# susrate command
@bot.command()
async def susrate(ctx, *, message):
    # of any person; repeat as many times as needed
    if message == "person-tagged":
        await ctx.send(message + "'s susrate is x%")
    # example of this bot
    elif message == "<@!825031801789481025>":
        await ctx.send(message + "'s susrate is 100%")
        
# ari command; incomplete 
@bot.command()
async def ari(ctx, *, message):
    ari_songs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
                 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
    if message == "random":
        response = random.choice(ari_songs)
    await ctx.send(response)

bot.run('your-token')
