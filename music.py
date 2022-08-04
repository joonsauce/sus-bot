# imports all bot settings
from setting import *

# saves the servers the bot is connected to & the channels in each server
players = {}

# join command; makes the bot join a voice channel; for debugging purposes
@bot.command()
async def join(ctx):
    # checks if user in voice channel
    if ctx.author.voice is not None:
        # if bot not in channel together
        if discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild) is None:
            # bot joins channel and sends success message
            await ctx.author.voice.channel.connect()
            await ctx.send("Connected!")
        else:
            # otherwise sends message to indicate bot already in channel
            await ctx.send("The bot is already connected to the voice channel!")
    # otherwise, alert user to join voice channel first
    else:
        await ctx.send("You need to be connected to a voice channel to use this command.")

# leave command; makes the bot leave a voice channel
@bot.command()
async def leave(ctx):
    # checks if bot is in a voice channel
    if discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild).is_connected:
        # if the server's id is in the players dicts, it means all other dicts have something in it, so it empties the dicts
        if ctx.guild.id in players:
            players.pop(ctx.guild.id)
        # disconnects the bot and sends success message
        await ctx.message.guild.voice_client.disconnect()
        await ctx.send("Disconnected!")
    # otherwise, send error message that the bot is not connected to a voice channel
    else:
        await ctx.send("The bot is not connected to a voice channel.")

# pp command; makes the bot pause/play the song
@bot.command()
async def pp(ctx):
    # checks if the bot is playing anything in the server
    if ctx.guild.id in players:
        # if the bot is playing something, pause
        if players[ctx.guild.id].is_playing():
            players[ctx.guild.id].pause()
            await ctx.send("Pausing...")
        # if the bot is paused, resume
        elif players[ctx.guild.id].is_paused():
            players[ctx.guild.id].resume()
            await ctx.send("Resuming...")
        # send error message
        else:
            await ctx.send("Nothing is currently playing!")
    # send error message
    else:
        await ctx.send("The bot is currently not connected to a voice channel.")

# stop command; makes the bot stop playing music (can be used to skip as well if using queue system)
@bot.command()
async def stop(ctx):
    # if bot is playing something
    if ctx.guild.id in players:
        # if the bot is playing something, pause
        if players[ctx.guild.id].is_playing():
            players[ctx.guild.id].stop()
            await ctx.send("Stopping...")
        # if the bot is paused, resume
        elif players[ctx.guild.id].is_paused():
            players[ctx.guild.id].stop()
            await ctx.send("Stopping...")
        # send error message
        else:
            await ctx.send("Nothing is currently playing!")
    # send error message
    else:
        await ctx.send("The bot is not connected to a voice channel.")

# drip command; plays among us drip
@bot.command()
async def drip(ctx):
    # checks if user in voice channel
    if ctx.author.voice is not None:
        # if bot not in channel together
        if discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild) is None:
            # bot joins channel
            await ctx.author.voice.channel.connect()
        # sets the voice channel to play in and plays the set song
        player = ctx.message.voice_client
        player.play(discord.FFmpegPCMAudio("music/drip.mp3"))
        await ctx.send("Now playing: `Among Us Drip`")
    # otherwise, alert user to join voice channel first
    else:
        await ctx.send("You need to be connected to a voice channel to use this command.")
