from setting import *

# sus command; a user accuses another user of something suspicious
@bot.command()
async def sus(ctx, arg1, *, arg2):
    await ctx.send('{0.author.mention} sussed {1} of *{2}*'.format(ctx, arg1, arg2))

# susrate command; rates how sus a person is; is a static value
@bot.command()
async def susrate(ctx, *, message):
    if message == "<@!unique-tag>":
        await ctx.send(message + "'s susrate is x%")
    elif message == "<@!unique-tag-2>":
        await ctx.send(message + "'s susrate is y%")

# different among us game feature commands below

# medbay command; medbay scans user
@bot.command()
async def scan(ctx):
    if ctx.author.mention == "<@!unique-tag>":
        id = "GREP1"
        ht = "1.80m"
        wt = "67kg"
        c = "Green"
        bt = "O+"
        await ctx.send("ID: " + id + " HT: " + ht + " WT: " + wt + " C: " + c + " BT: " + bt)
    elif ctx.author.mention == "<@!unique-tag-2>":
        id = "CYAP2"
        ht = "1.68m"
        wt = "49kg"
        c = "Cyan"
        bt = "O-"
        await ctx.send("ID: " + id + " HT: " + ht + " WT: " + wt + " C: " + c + " BT: " + bt)