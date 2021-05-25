# various pacakges to be imported
from setting import *
from sus import *
from music import *

# defines next song so songs in queue can be played
def next_song(ctx):
    music = discord.utils.get(bot.voice_clients)
    if len(queue) > 0:
        # checks if there is a song @ song.mp3 and see if removable
        song_there = os.path.isfile("song.mp3")
        if song_there:
            os.remove("song.mp3")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            # song gets downloaded then replaced by song.mp3 so bot can play in vc
            dl = str(links[0])
            ydl.download([dl])
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, "song.mp3")
        music.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda x: next_song(ctx))
        queue.pop(0)
        links.pop(0)

# p command; makes bot play user-specified music
@bot.command()
async def p(ctx, *, msg):
    # checks if bot is already connected to voice channel
    try:
        channel = ctx.author.voice.channel
        await channel.connect()
    # ClientException is thrown when bot is already connected, so it starts to search for song to play
    except discord.errors.ClientException:
        await ctx.send("Searching...")
    # AttributeError is thrown when whoever wrote the command isn't in a voice channel, so stops operation of the command
    except AttributeError:
        await ctx.send("You're not connected to a voice channel.")
        return
    # otherwise, it joins voice channel and starts searching
    else:
        await ctx.send("Searching...")


    # sets the voice channel the bot is referring back to
    music = discord.utils.get(bot.voice_clients)

    # uses YouTube_DL to start music play operations
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        # checks if message is a link
        try:
            get(msg)
        # if an error is thrown, the message isn't a link and searches for the video on YouTube
        except:
            dict = ydl.extract_info(f"ytsearch:{msg}", download=False)['entries'][0]
            song = (dict['webpage_url'])
        # if no error is thrown, the message is a link so it uses it to download the song
        else:
            dict = ydl.extract_info(msg, download=False)
            song = msg

    # checks if there is a song @ song.mp3 and see if removable
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    # if irremovable, PermissionError is spit out, and can then be used to queue songs to it
    except PermissionError:
        queue.append(dict['title'])
        links.append(dict['webpage_url'])
        await ctx.send("Queued!")
        return

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        # song gets downloaded then replaced by song.mp3 so bot can play in vc
        dl = str(song)
        ydl.download([dl])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
    music.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda x: next_song(ctx))

    title = (dict['title'])

    await ctx.send("Now playing: " + title)



# q command; makes bot display the songs in queue
@bot.command()
async def q(ctx):
    if len(queue) == 0:
        await ctx.send("Queue is empty! Use `s!p <song name or song link>` to queue songs!")
    else:
        await ctx.send(queue)

# makes the bot run with the bot token
bot.run('your-token-here')
