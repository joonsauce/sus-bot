from setting import *

reddit = asyncpraw.Reddit(
    client_id = '[your client id]',
    client_secret = '[your client secret]',
    user_agent = '[your user agent]',
)

# susmeme command; sends random meme from r/amongusmemes
@bot.command()
async def susmeme(ctx):
    subreddit = await reddit.subreddit("amongusmemes")
    image_link = await subreddit.random()
    if not image_link.stickied and image_link.over_18 is False \
            and image_link.url.endswith(('jpg', 'jpeg', 'png')):
        embed = discord.Embed(
            colour=discord.Colour.red()
        )
        embed.set_author(name=image_link.title)
        embed.set_image(url=image_link.url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("An error has occured, please try again later.")
