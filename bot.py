# links the main bot file with the other feature files
from help import *
from redditAPI import *
from roll import *
from setting import *
from sus import *
from music import *

# makes the bot run with the bot token
bot.run(bot_token)
