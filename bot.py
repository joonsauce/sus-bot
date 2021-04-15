import discord
import random
from setting import *
from discord.ext import commands
from songs import *
from discord.voice_client import VoiceClient

# different sus commands are listed below

# susout command; a user accuses another user of something suspicious
@bot.command()
async def susout(ctx, arg1, *, arg2):
    await ctx.send('{0.author.mention} sussed {1} of *{2}*'.format(ctx, arg1, arg2))

# susrate command; rates how sus a person is; is a static value
@bot.command()
async def susrate(ctx, *, message):
    if message == "<@!unique-tag":
        await ctx.send(message + "'s susrate is 20%")

# different among us game feature commands below

# medbay command; medbay scans user
@bot.command()
async def scan(ctx):
    if ctx.author.mention == "<@!unique-tag>":
        id = "GREP1"
        ht = "1.80m"
        wt = "67kg"
        c = "Green"
        bt = "O+"
        await ctx.send("ID: " + id + " HT: " + ht + " WT: " + wt + " C: " + c + " BT: " + bt)

# different music bot commands below

# ari command; plays random song from playlist; incomplete
@bot.command()
async def randomsong(ctx, *, message):
    if message == "random":
        song = random.choice(song_list)
    else:
        number = int(message)
        song = song_list[number]
    try:
        channel = ctx.author.voice.channel
        await channel.connect()
    except discord.errors.ClientException:
        await ctx.send("now playing: {0}".format(song))
    except AttributeError:
        await ctx.send("You're not connected to a voice channel.")
    else:
        await ctx.send("now playing: {0}".format(song))

# drip command; plays among us drip
@bot.command()
async def drip(ctx):
    try:
        channel = ctx.author.voice.channel
        await channel.connect()
    except discord.errors.ClientException:
        await ctx.send("Now playing: Among Us Drip")
    except AttributeError:
        await ctx.send("You're not connected to a voice channel.")
    else:
        await ctx.send("Now playing: Among Us Drip")
    drip = discord.utils.get(bot.voice_clients)
    drip.play(discord.FFmpegPCMAudio("drip.mp3"))

# join command; joins voice channel
@bot.command()
async def join(ctx):
    try:
        channel = ctx.author.voice.channel
        await channel.connect()
    except discord.errors.ClientException:
        await ctx.send("Already connected to channel!")
    except AttributeError:
        await ctx.send("You need to be connected to a voice channel to use this command.")
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

# pause command; pauses music playing
@bot.command()
async def pause(ctx):
    music = discord.utils.get(bot.voice_clients)
    if music.is_playing():
        music.pause()
        await ctx.send("Pausing!")
    else:
        await ctx.send("Currently paused!")

# resume command; resumes music
@bot.command()
async def resume(ctx):
    music = discord.utils.get(bot.voice_clients)
    if music.is_paused():
        music.resume()
        await ctx.send("Resuming!")
    else:
        await ctx.send("Currently playing!")

# stop command; stops playing music
@bot.command()
async def stop(ctx):
    music = discord.utils.get(bot.voice_clients)
    if music.is_playing():
        music.stop()
        await ctx.send("Stopping!")
    elif music.is_paused:
        await ctx.send("Music is currently stopped. Music must be playing to stop.")
    else:
        await ctx.send("There is no music playing.")

# test command; tests random stuff
@bot.command()
async def test(ctx):
    await ctx.send("your test subject here")

# runs bot with bot token
bot.run('your-token')

