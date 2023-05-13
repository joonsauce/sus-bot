# links the main bot file with the other feature files
from help import *
from redditAPI import *
from roll import *
from setting import *
from sus import *
from music import *

# test command; used for test purposes to debug things; just a short message for now but you can use it for whatever other purpose you want
@bot.command()
async def test(ctx):
    await ctx.send("You think you're funny huh?")

# makes the bot run with the bot token
bot.run(bot_token)
