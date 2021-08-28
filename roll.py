# import bot settings
from setting import *

# defines different header types for api calls
header1 = {
        'Authorization': 'Bearer {}'.format(roll_api_key),
        }
header2 = {
            'Authorization': 'Bearer {}'.format(roll_api_key),
            'Content-Type': 'application/json',
        }

# defines certain parameters for api calls
params = (
        ('maxRecords', 100),
        ('view', 'Grid view'),
    )

# function to GET data from database
def getRollData():
    # sets response as the data received 
    response = requests.get(url=roll_api_link, headers=header1,
                            params=params)
    # if the HTML status code isn't 200 (OK) returns -1
    # I used negative numbers for different types of errors
    if response.status_code != 200:
        # returns error
        return -1
    # if everything goes well returns data
    else:
        # returns data
        return response.json()

# function to check if user is in the database (being worked on for optimization, this code is a bit slow)
def findUser(number):
    # gets data from database
    data = getRollData()
    # if getRollData had an error, the findUser function also returns an error
    if data == -1:
        # returns error
        return -1
    # if no error from getting data, runs the findUser function
    else:
        # variables for different parts of the function
        data_location = int()
        # checks all rows of the database individually
        for i in range(len(data["records"])):
            # sets the user_id to compare to the user's id
            user_id = str(data["records"][i]["fields"]["user_id1"]) + str(
                data["records"][i]["fields"]["user_id2"])
            # if the user's id matches user_id (the user id in the database)
            if user_id == number:
                # returns the location of the user's data
                return i
        # returns -2 if the user isn't in the database
        return -2

# function to POST updated data to database
def postRollData(id1, id2):
    # sets the data to be sent to the databse
    data = '{ "records": [ { "fields": {"user_id1": ' + str(id1) + ', "user_id2": ' + str(
        id2) + ', "sus": 100} }] }'
    # sets response as the response the database generates
    response = requests.post(url=roll_api_link, headers=header2,
                             data=data)
    # if the HTML status code isn't 200 (OK) return an error
    if response.status_code != 200:
        # returns error
        return -1
    # else everything is normal and returns a positive integer (1 means OK)
    else:
        return 1

# function to add new user to database
def addUser(user_id):
    # sets variables to create new entry in database
    idPart1 = []
    idPart2 = []
    # sections off user_id
    for j in range(len(user_id)):
        # the first 9 numbers get added to idPart1
        if j <= 8:
            idPart1.append(user_id[j])
        # the rest of the numbers get added to idPart1
        else:
            idPart2.append(user_id[j])
    # creates one string for user_id1 and user_id2 respectively
    user_id1 = reduce(lambda a, b: a + b, idPart1)
    user_id2 = reduce(lambda a, b: a + b, idPart2)
    # uses postRollData function to update database
    response = postRollData(user_id1, user_id2)
    # if the HTML status code from the postRollData function isn't 200 (OK) return error
    if response == -1:
        # return error
        return -1
    # otherwise everything is normal and returns that it is ok
    else:
        # return that the function worked
        return True

# function to update susCash data in database
def patchResult(location, cash):
    # sets the new data to be inputted into the database
    data = '{"fields": {"sus": ' + str(cash) + ' }}'
    # sets the api link as the location of the user's susCash information
    url = roll_api_link + location
    # PATCHs result to the database
    response = requests.patch(url=url, headers=header2, data=data)
    # if the HTML status code isn't 200 (OK) return error
    if response.status_code != 200:
        # return error
        return -1
    # otherwise everything is normal and return that everything is ok
    else:
        # return that the function worked
        return 1

# function to fetch the results of the command
def getResult(total, bet, location):
    # gets a random integer
    rolled = random.randint(1, 10)
    # all code below is pretty much the same in this function
    # if the random number is less than 4
    if rolled <= 4:
        # the user loses susCash and sets final_cash as the user's original amount of susCash minus the amount they bet
        final_cash = str(total - bet)
        # uses patchResult function to update the change in the users susCash balance
        response = patchResult(location, final_cash)
        # if patchResult had an error, return error message
        if response == -1:
            # returns error message
            return "There has been an error. Please try again later. Code: sbroll_patchResult"
        # otherwise return the result of the roll to the user
        else:
            # returns success message
            return "Unfortunately, you lost some susCash. You now have {} susCash.".format(final_cash)
    elif rolled > 4 and rolled <= 6:
        final_cash = str(total + bet)
        response = patchResult(location, final_cash)
        if response == -1:
            return "There has been an error. Please try again later. Code: sbroll_patchResult"
        else:
            return "You won some susCash! You now have {} susCash.".format(final_cash)
    elif rolled > 6 and rolled <= 8:
        final_cash = str(total - bet)
        response = patchResult(location, final_cash)
        if response == -1:
            return "There has been an error. Please try again later. Code: sbroll_patchResult"
        else:
            return "Unfortunately, you lost some susCash. You now have {} susCash.".format(final_cash)
    elif rolled > 8 and rolled <= 10:
        final_cash = str(total + bet)
        response = patchResult(location, final_cash)
        if response == -1:
            return "There has been an error. Please try again later. Code: sbroll_patchResult"
        else:
            return "You won some susCash! You now have {} susCash.".format(final_cash)

# function to go check through certain cases
def verifyResults(data, user_location, bet):
    # gets the amount of susCash the user has in the database
    total = int(data["records"][user_location]["fields"]["sus"])
    # gets the location of the user's data
    location = str(data["records"][user_location]["id"])
    # if the user has no susCash, return error
    if total == 0:
        # return error
        return "You do not have enough susCash to s!roll at the moment."
    # if user's bet is bigger than the amount of susCash they have, return error
    elif bet > total:
        # return error
        return "You cannot bet more than the total amount of sus you have."
    # run code as normal if nothing is abnormal
    else:
        # gets result from getResult function
        rolled = getResult(total, bet, location)
        # returns result
        return rolled

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
                            await ctx.send("There has been an error. Please try again later. Code: sbroll_unknownfindUser")
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
