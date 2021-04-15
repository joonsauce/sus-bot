import discord
import logging
from discord.ext import commands

prefix = "s!"
description = "When the bot is sus!"

# logs bot events
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# bot setup
bot = commands.Bot(command_prefix=prefix)

# changes discord status
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("yo mama"))
