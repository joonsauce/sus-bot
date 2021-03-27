import asyncio
import time
import discord
import os
import pandas
import json
import random
from discord.ext import commands
from setting import *

# discord gateway intents
intents = discord.Intents.default()
allowed_mentions = discord.AllowedMentions(everyone=False,
                                           users=True,
                                           roles=False)

# bot instance
bot = discord.ext.commands.Bot(command_prefix=prefix,
                               intents=intents,
                               description=description,
                               case_insensitive=True,
                               allowed_mentions=allowed_mentions)

TOKEN = 'insert token here'

client = discord.Client()

@bot.command()
async def sus(ctx):
    await ctx.send(f"Say something")

    def check(message):
        return message.author == ctx.author and len(message.attachments) == 1

    msg = discord.Message
    try:
        msg = await bot.wait_for('message', check=check, timeout=60)
    except asyncio.TimeoutError:
        await ctx.send('Timed out. Please try again in a minute')

@client.event
async def on_message(message):
    ari_songs = [

    ]


    if message.author == client.user:
        return

    if 'sus' in message.content.lower():
        await message.channel.send('SUS!!!111!!!!!!')

    if message.content == 'sus p ari':
        response = random.choice(ari_songs)
        await message.channel.send()




client.run(TOKEN)