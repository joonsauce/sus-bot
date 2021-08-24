import asyncio
import discord
import logging
import os
import praw
import random
import requests
import requests.auth
from discord.ext import commands
from discord.voice_client import VoiceClient
from PIL import Image, ImageOps
from redditAPI import *
from requests import get

# sets the prefix to use the bot
prefix = "s!"
# sets description of the bot
description = "The bot is definitely NOT venting"

# bot logging events

# gets discord logger
logger = logging.getLogger('discord')
# sets discord logging level as debug
logger.setLevel(logging.DEBUG)
# sets the encoding type & specifies file location
handler = logging.FileHandler(filename='../discord.log', encoding='utf-8', mode='w')
# formats how the debug file will look like
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# adds handler
logger.addHandler(handler)

# sets prefix of bot
bot = commands.Bot(command_prefix=prefix)

# removes help command so a custom one can be put in
bot.remove_command('help')

# sets discord activity status
@bot.event
async def on_ready():
    print("Status: OK")
    await bot.change_presence(activity=discord.Game("Not venting"))

# help command; makes bot send description of every command it accepts
@bot.command()
async def help(ctx, *, msg=''):
    embed = discord.Embed(
        color = discord.Colour.dark_red()
    )
    embed.set_author(name="sus bot help")
    if msg == '':
        embed.add_field(name="drip", value='Plays Among Us Drip if user is connected to a voice channel. Usage: s!drip', inline="False")
        embed.add_field(name="join", value='Makes bot join the voice channel the user is in. Usage: s!join', inline="False")
        embed.add_field(name="leave", value='Makes bot leave the voice channel it is in. Usage: s!leave', inline="False")
        embed.add_field(name="suslogo", value='Returns image of susbot Usage: s!suslogo', inline="False")
        embed.add_field(name="pp", value='Pauses and resumes music playing. Usage: s!pp', inline="False")
        embed.add_field(name="q", value='Returns queued songs. Usage: s!q', inline="False")
        embed.add_field(name="roll", value='Makes bot run a virtual roll of dice. Usage: s!roll', inline="False")
        embed.add_field(name="scan", value='Makes bot run an Among Us style medbay scan. Usage: s!scan <user>*', inline="False")
        embed.add_field(name="stop", value='Makes bot stop whatever music is playing. Usage: s!stop', inline="False")
        embed.add_field(name="sus", value='Susses another user. Usage: s!sus <user> <action>', inline="False")
        embed.add_field(name="susimg", value='Returns avatar of tagged user in Among Us suit. Usage: s!susimg <user>*', inline="False")
        embed.add_field(name="susrate", value='Returns susrate of tagged user. Usage: s!susrate <user>*', inline="False")
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
    elif msg == 'q':
        embed.add_field(name="q", value='Returns queued songs. Usage: s!q', inline="False")
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
        embed.add_field(name="susimg", value='Returns avatar of tagged user in Among Us suit. Usage: s!susimg <user>*', inline="False")
    elif msg == 'susrate':
        embed.add_field(name="susrate", value='Returns susrate of tagged user. Usage: s!susrate <user>*', inline="False")
    else:
        pass
    embed.add_field(name="OTHER THINGS TO NOTE", value='Any element with a * beside it means the element is optional.')

    await ctx.send(embed=embed)
