import ast
import asyncio
import asyncpraw
import discord
import logging
import os
import random
import re
import requests
import requests.auth
import schedule
import time
from discord.ext import commands
from discord.voice_client import VoiceClient
from functools import reduce
from PIL import Image, ImageOps
from requests import get
from secret import *

# sets the prefix to use the bot
prefix = "s!"
# sets description of the bot
description = "The bot is definitely NOT venting. sus bot template v1.1.0"
# sets intents of bot - you don't need all intents, but it is easy implementation
intents = discord.Intents.all()


# # bot logging events - this is a way to track things if bot crashes, but you can usually look at
# information in the console directly after crash so just going to leave it out
#
# # gets discord logger
# logger = logging.getLogger('discord')
# # sets discord logging level as debug
# logger.setLevel(logging.DEBUG)
# # sets the encoding type & specifies file location
# handler = logging.FileHandler(filename='../discord.log', encoding='utf-8', mode='w')
# # formats how the debug file will look like
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# # adds handler
# logger.addHandler(handler)

# sets prefix of bot & intents
bot = commands.Bot(command_prefix=prefix, intents=intents)

# removes help command so a custom one can be put in
bot.remove_command('help')

# sets discord activity status
@bot.event
async def on_ready():
    print("Status: OK")
    await bot.change_presence(activity=discord.Game("Not venting"))
