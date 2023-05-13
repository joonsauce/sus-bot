# imports all bot settings
from setting import *

# saves the servers the bot is connected to & the channels in each server
players = {}

# join command; makes the bot join a voice channel
@bot.command()
async def join(ctx):
    # checks if user in voice channel; otherwise send error message
    if ctx.author.voice is not None:
        # if bot not in channel together; otherwise indicate that bot already in vc
        if discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild) is None:
            # bot joins channel and sends success message
            await ctx.author.voice.channel.connect()
            await ctx.send("Connected!")
        else:
            await ctx.send("The bot is already connected to the voice channel!")
    else:
        await ctx.send("You need to be connected to a voice channel to use this command.")

# leave command; makes the bot leave a voice channel
@bot.command()
async def leave(ctx):
    # checks if bot is in a voice channel; otherwise send error message
    if discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild).is_connected:
        # removes current server from player list for clean dc
        if ctx.guild.id in players:
            players.pop(ctx.guild.id)
        # disconnects the bot and sends success message
        await ctx.message.guild.voice_client.disconnect()
        await ctx.send("Disconnected!")
    else:
        await ctx.send("The bot is not connected to a voice channel.")

# pp command; makes the bot pause/play the song
@bot.command()
async def pp(ctx):
    # checks if the bot is playing anything in the server & sends error message if not in vc
    if ctx.guild.id in players:
        # if the bot is playing something, pause; otherwise send error message
        if players[ctx.guild.id].is_playing():
            players[ctx.guild.id].pause()
            await ctx.send("Pausing...")
        # if the bot is paused, resume
        elif players[ctx.guild.id].is_paused():
            players[ctx.guild.id].resume()
            await ctx.send("Resuming...")
        else:
            await ctx.send("Nothing is currently playing!")
    else:
        await ctx.send("The bot is currently not connected to a voice channel.")

# stop command; makes the bot stop playing music (can be used to skip as well if using queue system)
@bot.command()
async def stop(ctx):
    # checks if bot is playing anything; send error message if not in vc
    if ctx.guild.id in players:
        # if the bot is playing something, pause; otherwise send error message
        if players[ctx.guild.id].is_playing():
            players[ctx.guild.id].stop()
            await ctx.send("Stopping...")
        # if the bot is paused, resume
        elif players[ctx.guild.id].is_paused():
            players[ctx.guild.id].stop()
            await ctx.send("Stopping...")
        else:
            await ctx.send("Nothing is currently playing!")
    else:
        await ctx.send("The bot is not connected to a voice channel.")

# drip command; plays among us drip
@bot.command()
async def drip(ctx):
    # checks if user in voice channel; otherwise send error message
    if ctx.author.voice is not None:
        # if bot not in channel together, join channel
        if discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild) is None:
            await ctx.author.voice.channel.connect()
        # sets the voice channel to play in and plays the set song
        player = ctx.message.voice_client
        # this play can be anything you want, as long as it is findable by bot
        # I might make this into a function that you can use to get whatever song you want, which may not be
        # available locally
        player.play(discord.FFmpegPCMAudio("music/drip.mp3"))
        await ctx.send("Now playing: `Among Us Drip`")
    else:
        await ctx.send("You need to be connected to a voice channel to use this command.")
