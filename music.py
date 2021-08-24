from setting import *

# join command; makes the bot join a voice channel; for debugging purposes
@bot.command()
async def join(ctx):
    try:
        channel = ctx.author.voice.channel
        await channel.connect()
    except discord.errors.ClientException:
        await ctx.send("The bot is already connected to the voice channel!")
    except AttributeError:
        await ctx.send("You need to be connected to a voice channel to use this command.")
    else:
        await ctx.send("Connected!")

# leave command; makes the bot leave a voice channel
@bot.command()
async def leave(ctx):
    try:
        channel = ctx.voice_client
        await channel.disconnect()
    except AttributeError:
        await ctx.send("The bot is currently not connected to a voice channel.")
    else:
        await ctx.send("Successfully disconnected!")

# pp command; makes the bot pause/play the song
@bot.command()
async def pp(ctx):
    # sets the voice channel the bot is referring back to
    vc = discord.utils.get(bot.voice_clients)
    if vc.is_playing():
        vc.pause()
        await ctx.send("Pausing!")
    elif vc.is_paused:
        vc.resume()
        await ctx.send("Resuming!")
    else:
        await ctx.send("Nothing is currently playing!")

# stop command; makes the bot stop playing music
@bot.command()
async def stop(ctx):
    # sets the voice channel the bot is referring back to
    vc = discord.utils.get(bot.voice_clients)
    if vc.is_playing():
        vc.stop()
        await ctx.send("Stopping!")
    elif vc.is_paused():
        await ctx.send("Music is currently paused. Music must be playing to stop.")
    else:
        await ctx.send("Nothing is currently playing.")

# drip command; plays among us drip
@bot.command()
async def drip(ctx):
    if ctx.author.bot:
        await ctx.send("You're a bot, fuck you")
    else:
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
        drip.play(discord.FFmpegPCMAudio("music/drip.mp3"))

# roll command; rick rolls
@bot.command()
async def roll(ctx):
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
