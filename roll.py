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

def getRollData():
    response = requests.get(url=roll_api_link, headers=header1,
                            params=params)
    if response.status_code != 200:
        return -1
    else:
        return response.json()

def findUser(number):
    data = getRollData()
    if data == -1:
        return -1
    else:
        data_location = int()
        user_id_list = []
        money_location = str()
        for i in range(len(data["records"])):
            user_id = str(data["records"][i]["fields"]["user_id1"]) + str(
                data["records"][i]["fields"]["user_id2"])
            user_id_list.append(int(user_id))
            if user_id == number:
                data_location = i
                money_location = str(data["records"][data_location]["id"])
                return data_location
        return -2

def postRollData(id1, id2):
    data = '{ "records": [ { "fields": {"user_id1": ' + str(id1) + ', "user_id2": ' + str(
        id2) + ', "sus": 100} }] }'
    response = requests.post(url=roll_api_link, headers=header2,
                             data=data)
    if response.status_code != 200:
        return -1
    else:
        return 1

def addUser(user_id):
    idPart1 = []
    idPart2 = []
    for j in range(len(user_id)):
        if j <= 8:
            idPart1.append(user_id[j])
        else:
            idPart2.append(user_id[j])
    user_id1 = reduce(lambda a, b: a + b, idPart1)
    user_id2 = reduce(lambda a, b: a + b, idPart2)
    response = postRollData(user_id1, user_id2)
    if response != 200:
        return -1
    else:
        return True

def patchResult(location, cash):
    data = '{"fields": {"sus": ' + str(cash) + ' }}'
    url = roll_api_link + location
    response = requests.patch(url=url, headers=header2, data=data)
    if response.status_code != 200:
        return -1
    else:
        return 1

def getResult(total, bet, location):
    rolled = random.randint(1, 10)
    if rolled <= 4:
        final_cash = str(total - bet)
        response = patchResult(location, final_cash)
        if response == -1:
            return "There has been an error. Please try again later."
        else:
            return "Unfortunately, you lost some susCash. You now have {} susCash.".format(final_cash)
    elif rolled > 4 and rolled <= 6:
        final_cash = str(total + bet)
        response = patchResult(location, final_cash)
        if response == -1:
            return "There has been an error. Please try again later."
        else:
            return "You won some susCash! You now have {} susCash.".format(final_cash)
    elif rolled > 6 and rolled <= 8:
        final_cash = str(total - bet)
        response = patchResult(location, final_cash)
        if response == -1:
            return "There has been an error. Please try again later."
        else:
            return "Unfortunately, you lost some susCash. You now have {} susCash.".format(final_cash)
    elif rolled > 8 and rolled <= 10:
        final_cash = str(total + bet)
        response = patchResult(location, final_cash)
        if response == -1:
            return "There has been an error. Please try again later."
        else:
            return "You won some susCash! You now have {} susCash.".format(final_cash)

# roll command; makes bot run a simulated gamble
@bot.command()
async def roll(ctx, *, msg=''):
    if not msg:
        await ctx.send("Please enter the amount of susCash you wish to use.")
    else:
        try:
            bet = int(msg)
        except ValueError:
            await ctx.send("The amount of susCash you entered is not a number.")
        else:
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
                data = getRollData()
                total = int(data["records"][user_there]["fields"]["sus"])
                location = str(data["records"][user_there]["id"])
                if bet > total:
                    await ctx.send("You cannot bet more than the total amount of sus you have.")
                else:
                    rolled = getResult(total, bet, location)
                    await ctx.send(rolled)

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
        data = getRollData()
        total = int(data["records"][user_there]["fields"]["sus"])
        await ctx.send("You currently have {0} susCash under your account.".format(total))
