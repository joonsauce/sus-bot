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

# susout command; a user accuses another user of something suspicious
@bot.command()
async def susout(ctx, arg1, *, arg2):
    await ctx.send('{0.author.mention} accused {1} of *{2}*'.format(ctx, arg1, arg2))
    
# susrate command; rates how sus a person is; is a static value
@bot.command()
async def susrate(ctx, *, message):
    # of any person; repeat as many times as needed
    if message == "person-tagged":
        await ctx.send(message + "'s susrate is x%")
    # example of this bot
    elif message == "<@!825031801789481025>":
        await ctx.send(message + "'s susrate is 100%")
        
# ari command; incomplete; plays random song from a different bot 
@bot.command()
async def ari(ctx, *, message):
    ari_song = []
    if message == "random":
        song = random.choice(ari_song)
    else:
        number = message
        song = ari_song[number]
    channel = ctx.author.voice.channel
    try:
        await channel.connect()
    except:
        await ctx.send("!p {0}".format(song))

# join command; joins voice channel
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

# leave command; leaves voice channel
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

# runs bot with bot token
bot.run('your-token')
