# used to import all bot settings
from setting import *

# help command; makes bot send description of every command it accepts
@bot.command()
async def help(ctx, *, msg=''):
    # sets embed as the discord embed
    embed = discord.Embed(
        # sets the theme of the embed as dark red, but you can change it to whatever you want
        color = discord.Colour.dark_red()
    )
    # sets the title of the embed as "sus bot help"
    embed.set_author(name="sus bot help")
    # if there is no message following the command, it displays all commands this bot has
    if msg == '':
        embed.add_field(name="drip", value='Plays Among Us Drip if user is connected to a voice channel. Usage: s!drip', inline="False")
        embed.add_field(name="join", value='Makes bot join the voice channel the user is in. Usage: s!join', inline="False")
        embed.add_field(name="leave", value='Makes bot leave the voice channel it is in. Usage: s!leave', inline="False")
        embed.add_field(name="suslogo", value='Returns image of susbot Usage: s!suslogo', inline="False")
        embed.add_field(name="pp", value='Pauses and resumes music playing. Usage: s!pp', inline="False")
        embed.add_field(name="roll", value='Makes bot run a virtual roll of dice. Usage: s!roll', inline="False")
        embed.add_field(name="scan", value='Makes bot run an Among Us style medbay scan. Usage: s!scan <user>*', inline="False")
        embed.add_field(name="stop", value='Makes bot stop whatever music is playing. Usage: s!stop', inline="False")
        embed.add_field(name="sus", value='Susses another user. Usage: s!sus <user> <action>', inline="False")
        embed.add_field(name="susimg", value='Returns avatar of tagged user in Among Us character. Usage: s!susimg <user>*', inline="False")
        embed.add_field(name="susmeme", value='Returns a random meme from r/amongusmemes. Usage: s!susmeme', inline="False")
        embed.add_field(name="susrate", value='Returns susrate of tagged user. Usage: s!susrate <user>*', inline="False")
    # below is all of the separate commands you can get info about 
    elif msg == 'drip':
        embed.add_field(name="drip", value='Plays Among Us Drip if user is connected to a voice channel. Usage: s!drip',
                        inline="False")
    elif msg == 'join':
        embed.add_field(name="join", value='Makes bot join the voice channel the user is in. Usage: s!join',
                        inline="False")
    elif msg == 'leave':
        embed.add_field(name="leave", value='Makes bot leave the voice channel it is in. Usage: s!leave',
                        inline="False")
    elif msg == 'suslogo':
        embed.add_field(name="nathansus", value='Returns image of susbot Usage: s!suslogo', inline="False")
    elif msg == 'pp':
        embed.add_field(name="pp", value='Pauses and resumes music playing. Usage: s!pp', inline="False")
    elif msg == 'roll':
        embed.add_field(name="roll", value='Makes bot run a virtual roll of dice. Usage: s!roll', inline="False")
    elif msg == 'scan':
        embed.add_field(name="scan", value='Makes bot run an Among Us style medbay scan of the user. Usage: s!scan',
                        inline="False")
    elif msg == 'stop':
        embed.add_field(name="stop", value='Makes bot stop whatever music is playing. Usage: s!stop', inline="False")
    elif msg == 'sus':
        embed.add_field(name="sus", value='Susses another user. Usage: s!sus <user> <action>', inline="False")
    elif msg == 'susimg':
        embed.add_field(name="susimg", value='Returns avatar of tagged user in Among Us character. Usage: s!susimg <user>*', inline="False")
    elif msg == 'susmeme':
        embed.add_field(name="susmeme", value='Returns a random meme from r/amongusmemes. Usage: s!susmeme', inline="False")
    elif msg == 'susrate':
        embed.add_field(name="susrate", value='Returns susrate of tagged user. Usage: s!susrate <user>*', inline="False")
    
    # adds line indicating that a star means the element is optional
    embed.add_field(name="OTHER THINGS TO NOTE", value='Any element with a * beside it means the element is optional.')
    # makes the bot send the embed as the message
    await ctx.send(embed=embed)
