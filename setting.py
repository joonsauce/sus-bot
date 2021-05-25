import asyncio
import discord
import logging
import os
import random
import requests
import youtube_dl
from discord.ext import commands
from discord.voice_client import VoiceClient
from requests import get

# sets the prefix to use the bot; use whichever, s! is included as it is what I used
prefix = "s!"
# sets description of the bot
description = "Your description here"

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

# properly sets prefix of bot
bot = commands.Bot(command_prefix=prefix)

# sets discord activity status
@bot.event
async def on_ready():
    # again, add whatever presence you want, I just have set a default one
    await bot.change_presence(activity=discord.Game("Not venting"))
