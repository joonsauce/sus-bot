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
import selenium
import schedule
import time
from discord.ext import commands
from discord.voice_client import VoiceClient
from functools import reduce
from PIL import Image, ImageOps
from requests import get
from secret import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options

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
