# imports all bot settings
from setting import *

# join command; makes the bot join a voice channel; for debugging purposes
@bot.command()
async def join(ctx):
    # checks if the user is ni a voice channel and tries to connect to it
    try:
        # sets channel as the voice channel the user is in
        channel = ctx.author.voice.channel
        # connects to the voice channel
        await channel.connect()
    # if the bot throws a ClientException error, it likely indicates the bot is already in the voice channel, so sends error message
    except discord.errors.ClientException:
        # sends error message
        await ctx.send("The bot is already connected to the voice channel!")
    # if the bot throws an AttributeError, it likely means the user isn't connected to a voice channel, so sends an error message
    except AttributeError:
        # sends error message
        await ctx.send("You need to be connected to a voice channel to use this command.")
    # if no errors are thrown the bot indicates success
    else:
        # sends success message
        await ctx.send("Connected!")

# leave command; makes the bot leave a voice channel
@bot.command()
async def leave(ctx):
    # checks if bot is in a voice channel
    try:
        # sets channel as the voice channel the bot is connected to
        channel = ctx.voice_client
        # makes bot leave the voice channel
        await channel.disconnect()
    # if the bot throws an AttributeError the bot is likely not connected to a voice channel (already disconnected) so throws an error
    except AttributeError:
        # sends error message
        await ctx.send("The bot is currently not connected to a voice channel.")
    # if no errors are thrown the bot indicates success
    else:
        # sends success message
        await ctx.send("Successfully disconnected!")

# pp command; makes the bot pause/play the song
@bot.command()
async def pp(ctx):
    # sets the voice channel the bot is referring back to
    vc = discord.utils.get(bot.voice_clients)
    # checks if the bot is playing anything
    if vc.is_playing():
        # pauses whatever is being played
        vc.pause()
        # sends success message
        await ctx.send("Pausing!")
    # checks if the bot has anything paused
    elif vc.is_paused:
        # resumes whatever is paused
        vc.resume()
        # sends success message
        await ctx.send("Resuming!")
    # if neither of those conditions are met, nothing is playing so it sends message
    else:
        # sends nothing is playing message
        await ctx.send("Nothing is currently playing!")

# stop command; makes the bot stop playing music
@bot.command()
async def stop(ctx):
    # sets the voice channel the bot is referring back to
    vc = discord.utils.get(bot.voice_clients)
    # checks if anything is playing in the voice channel
    if vc.is_playing():
        # stops music from playing
        vc.stop()
        # sends success message
        await ctx.send("Stopping!")
    # if something is paused, the bot indicates that there must be something playing to stop
    elif vc.is_paused():
        # sends error message
        await ctx.send("Music is currently paused. Music must be playing to stop.")
    # if nothing is playing send error message
    else:
        # send error message
        await ctx.send("Nothing is currently playing.")

# drip command; plays among us drip
@bot.command()
async def drip(ctx):
    # checks if the user is a bot and sends message
    if ctx.author.bot:
        # sends a welcome message
        await ctx.send("You're a bot, screw you!")
    # otherwise the code continues
    else:
        # checks if bot is in voice channel
        try:
            # sets channel as the user's voice channel
            channel = ctx.author.voice.channel
            # connects to user's voice channel
            await channel.connect()
        # if bot throws a ClientException, it means bot is already connected to voice channel so continues as normal
        except discord.errors.ClientException:
            # sends success message
            await ctx.send("Now playing: Among Us Drip")
        # if bot throws an AttributeError, it means user isn't connected to a voice channel and sends error message
        except AttributeError:
            # sends error message
            await ctx.send("You're not connected to a voice channel.")
        # if no errors are thrown the code continues as normal
        else:
            # sends success message
            await ctx.send("Now playing: Among Us Drip")
        # sends drip as the voice channel the bot is in
        drip = discord.utils.get(bot.voice_clients)
        # makes bot play sound of choice
        drip.play(discord.FFmpegPCMAudio("music/drip.mp3"))

# roll command; rick rolls; works the same as the drip command
@bot.command()
async def roll(ctx):
    if ctx.author.bot:
        await ctx.send("You're a bot, screw you!")
    else:
        try:
            channel = ctx.author.voice.channel
            await channel.connect()
        except discord.errors.ClientException:
            await ctx.send("Rollin'...")
        except AttributeError:
            await ctx.send("You're not connected to a voice channel.")
        else:
            await ctx.send("Rollin'...")
        drip = discord.utils.get(bot.voice_clients)
        drip.play(discord.FFmpegPCMAudio("music/roll.mp3"))         
    
