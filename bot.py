import discord
import logging
import random
import youtube_dl
import os
from setting import *
from discord.ext import commands
from songs import *
from discord.voice_client import VoiceClient

# logs bot events
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# bot setup
bot = commands.Bot(command_prefix=prefix)

# different sus commands are listed below

# susout command; a user accuses another user of something suspicious
@bot.command()
async def susout(ctx, arg1, *, arg2):
    await ctx.send('{0.author.mention} sussed {1} of *{2}*'.format(ctx, arg1, arg2))

# susrate command; rates how sus a person is; is a static value
@bot.command()
async def susrate(ctx, *, message):
    if message == "user's tag":
        await ctx.send(message + "'s susrate is 20%")

# different among us game feature commands below

# medbay command; medbay scans user
@bot.command()
async def scan(ctx):
    if ctx.author.mention == "user's tag":
        id = "GREP1"
        ht = "1.80m"
        wt = "69kg"
        c = "Green"
        bt = "O+"
        await ctx.send("ID: " + id + " HT: " + ht + " WT: " + wt + " C: " + c + " BT: " + bt)

# ari command; plays random song from a different bot; incomplete
@bot.command()
async def randomsong(ctx, *, message):
    if message == "random":
        song = random.choice(song_bank)
    else:
        number = int(message)
        song = song_bank[number]
    try:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send("now playing: {0}".format(song))
    except discord.errors.ClientException:
        await ctx.send("now playing: {0}".format(song))
    except AttributeError:
        await ctx.send("You're not connected to a voice channel.")
    else:
        await ctx.send("now playing: {0}".format(song))

# different music bot commands below

# join command; joins voice channel
@bot.command()
async def join(ctx):
    try:
        channel = ctx.author.voice.channel
        await channel.connect()
    except discord.errors.ClientException:
        await ctx.send("Already connected to channel!")
    except AttributeError:
        await ctx.send("You're not connected to a voice channel.")
    else:
        await ctx.send("Connected!")

# leave command; leaves voice channel
@bot.command()
async def leave(ctx):
    try:
        channel = ctx.voice_client
        await channel.disconnect()
    except AttributeError:
        await ctx.send("The bot is not connected to a voice channel.")
    else:
        await ctx.send("Successfully disconnected!")

# EVERYTHING BELOW IS INCOMPLETE!

# pause command; pauses music playing
@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently paused!")

# resume command; resumes music
@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Currently playing!")

# stop command; stops playing music
@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()

# runs bot with bot token
bot.run('your-token')

