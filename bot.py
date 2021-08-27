# links the main bot file with the other feature files
# links to the redesigned help command
from help import *
# links to the random sus meme feature
from redditAPI import *
# links to the roll features
from roll import *
# links to the various bot settings
from setting import *
# links to the different "sus" features
from sus import *
# links to the soundboard features
from music import *

# test command; used for test purposes to debug things; just a short message for now but you can use it for whatever other purpose you want
@bot.command()
async def test(ctx):
    # sends the message in the quote
    await ctx.send("You think you're funny huh?")

# makes the bot run with the bot token
bot.run(bot_token)
