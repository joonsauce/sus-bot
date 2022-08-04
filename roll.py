# import bot settings
from setting import *
from roll_functions import *

# roll command; makes bot run a simulated gamble
@bot.command()
async def roll(ctx, *, msg=''):
    if not msg:
        await ctx.send("Please enter the amount of susCash you wish to use.")
    else:
        if msg.isnumeric():
            if float(msg).is_integer():
                if int(msg) <= 0:
                    await ctx.send("Please enter a positive value of susCash to use.")
                    return
                data = getRollData()
                if data == -1:
                    await ctx.send("There has been an error. Please try again later.")
                    return
                user_there = findUser(str(ctx.author.id))
                if user_there == -1:
                    await ctx.send("There has been an error. Please try again later.")
                    return
                if user_there == -2:
                    response = addUser(str(ctx.author.id))
                    if response == -1:
                        await ctx.send("There has been an error. Please try again later.")
                        return
                    user_there = findUser(str(ctx.author.id))
                    if user_there == -1 or user_there == -2:
                        await ctx.send("There has been an error. Please try again later.")
                        return
                    data = getRollData()
                    if data == -1:
                        await ctx.send("There has been an error. Please try again later.")
                        return
                    result = verifyResults(data, user_there, int(msg))
                    await ctx.send(result)

# bal command; allows user to check how much susCash they have
@bot.command()
async def bal(ctx):
    data = getRollData()
    if data == -1:
        await ctx.send("There has been an error. Please try again later.")
    else:
        user_there = findUser(str(ctx.author.id))
        if user_there == -1:
            await ctx.send("There has been an error. Please try again later.")
        elif user_there == -2:
            response = addUser(str(ctx.author.id))
            if response == -1:
                await ctx.send("There has been an error. Please try again later.")
            else:
                user_there = findUser(str(ctx.author.id))
                if user_there == -1:
                    await ctx.send("There has been an error. Please try again later.")
                else:
                    pass
        data = getRollData()
        if data == -1:
            await ctx.send("There has been an error. Please try again later.")
        else:
            total = int(data["records"][user_there]["fields"]["sus"])
            await ctx.send("You currently have {0} susCash under your account.".format(total))
