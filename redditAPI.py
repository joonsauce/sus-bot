# imports discord bot settings
from setting import *

# sets parameters for using AsyncPRAW
reddit = asyncpraw.Reddit(
    client_id = reddit_id,
    client_secret = reddit_secret,
    user_agent = reddit_agent,
)

# susmeme command; sends random meme from r/amongusmemes
@bot.command()
async def susmeme(ctx):
    # sets the subreddit the bot pulls the information from, just change the string to the subreddit you want
    subreddit = await reddit.subreddit("amongusmemes")
    # gets a random post from the subreddit
    image_link = await subreddit.random()
    # makes bot verify if the post is stickied or nsfw and that the link is an image
    if not image_link.stickied and image_link.over_18 is False \
            and image_link.url.endswith(('jpg', 'jpeg', 'png')):
        # sets embed as discord embed
        embed = discord.Embed(
            # sets color theme for embed
            colour=discord.Colour.red()
        )
        # sets title of embed as the title of the post
        embed.set_author(name=image_link.title)
        # sets the image as the image linked with the random post
        embed.set_image(url=image_link.url)
        # makes bot send the embed as a message
        await ctx.send(embed=embed)
    # if verification fails, send out an error message; this may be changed to repeat until it works
    else:
        # makes bot send error message 
        await ctx.send("An error has occured, please try again later.")
