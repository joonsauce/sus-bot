# import bot settings
from setting import *

# roll command; makes bot run a simulated gamble
@bot.command()
async def roll(ctx, *, msg=''):
    if not msg:
        await ctx.send("Please enter the amount of susCash you wish to use. Code: sbroll_nosusCashEntered")
    else:
        try:
            bet = int(msg)
        except ValueError:
            await ctx.send("The amount of susCash you entered is not a number. Code: sbroll_wrongsusCash")
        else:
            if bet <= 0:
                await ctx.send("Please enter a positive number to bet.")
            else:
                data = getRollData()
                if data == -1:
                    await ctx.send("There has been an error. Please try again later. Code: sbroll_getRollData")
                else:
                    user_there = findUser(str(ctx.author.id))
                    if user_there == -1:
                        await ctx.send("There has been an error. Please try again later. Code: sbroll_findUser")
                    elif user_there == -2:
                        response = addUser(str(ctx.author.id))
                        if response == -1:
                            await ctx.send("There has been an error. Please try again later. Code: sbroll_addUser")
                        else:
                            user_there = findUser(str(ctx.author.id))
                            if user_there == -1:
                                await ctx.send("There has been an error. Please try again later. Code: sbroll_findUser")
                            elif user_there == -2:
                                await ctx.send(
                                    "There has been an error. Please try again later. Code: sbroll_unknownfindUser")
                            else:
                                data = getRollData()
                                if data == -1:
                                    await ctx.send(
                                        "There has been an error. Please try again later. Code: sbroll_getRollData")
                                else:
                                    result = verifyResults(data, user_there, bet)
                                    await ctx.send(result)
                    else:
                        result = verifyResults(data, user_there, bet)
                        await ctx.send(result)

# bal command; allows user to check how much susCash they have
@bot.command()
async def bal(ctx):
    data = getRollData()
    if data == -1:
        await ctx.send("There has been an error. Please try again later. Code: sbbal_getRollData")
    else:
        user_there = findUser(str(ctx.author.id))
        if user_there == -1:
            await ctx.send("There has been an error. Please try again later. Code: sbbal_findUser")
        elif user_there == -2:
            response = addUser(str(ctx.author.id))
            if response == -1:
                await ctx.send("There has been an error. Please try again later. Code: sbbal_addUser")
            else:
                user_there = findUser(str(ctx.author.id))
                if user_there == -1:
                    await ctx.send("There has been an error. Please try again later. Code: sbroll_findUser")
                else:
                    pass
        data = getRollData()
        if data == -1:
            await ctx.send("There has been an error. Please try again later. Code: sbroll_getRollData")
        else:
            total = int(data["records"][user_there]["fields"]["sus"])
            await ctx.send("You currently have {0} susCash under your account.".format(total))
