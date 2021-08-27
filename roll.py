from setting import *

# defines different header types for api calls
header1 = {
        'Authorization': 'Bearer {}'.format('your api key'),
        }
header2 = {
            'Authorization': 'Bearer {}'.format('your api key'),
            'Content-Type': 'application/json',
        }

# defines certain parameters for api calls
params = (
        ('maxRecords', 100),
        ('view', 'Grid view'),
    )

# roll command; makes bot run a simulated gamble
@bot.command()
async def roll(ctx, *, msg=''):
    if not msg:
        await ctx.send("Please enter the amount of sus you wish to use.")
    else:
        id = str(ctx.author.id)
        response = requests.get('https://api.airtable.com/v0/your-table/Table%201', headers=header1,
                                params=params)
        data = response.json()
        data_location = int()
        user_id_list = []
        for i in range(len(data["records"])):
            user_id = str(data["records"][i]["fields"]["user_id1"]) + str(data["records"][i]["fields"]["user_id2"])
            user_id_list.append(int(user_id))
            if user_id == id:
                data_location = i
                break
        money_location = str(data["records"][data_location]["id"])
        if int(ctx.author.id) not in user_id_list:
            idsplit1 = []
            idsplit2 = []
            for j in range(len(id)):
                if j <= 8:
                    idsplit1.append(id[j])
                else:
                    idsplit2.append(id[j])
            user_id1 = str()
            user_id2 = str()
            for r in range(len(idsplit1)):
                user_id1 += idsplit1[r]
                user_id2 += idsplit2[r]
            post = '{ "records": [ { "fields": {"user_id1": ' + str(user_id1) + ', "user_id2": ' + str(
                user_id2) + ', "sus": 100} }] }'
            response = requests.post('https://api.airtable.com/v0/your-table/Table%201', headers=header2,
                                     data=post)
        total = int(data["records"][data_location]["fields"]["sus"])
        try:
            bet = int(msg)
        except ValueError:
            await ctx.send("The amount of susCash you entered is not a number.")
        else:
            if bet > total:
                await ctx.send("You cannot bet more than the total amount of sus you have.")
            rolled = random.randint(1, 10)
            if rolled <= 4:
                final_cash = str(total - bet)
                change_sus = '{"fields": {"sus": ' + str(final_cash) + ' }}'
                url = 'https://api.airtable.com/v0/your-table/Table%201/' + str(money_location)
                response = requests.patch(url=url, headers=header2,
                                          data=change_sus)
                await ctx.send(
                    "Unfortunately, you lost some susCash. You now have {} susCash.".format(final_cash))
            elif rolled > 4 and rolled <= 6:
                final_cash = str(total + bet)
                change_sus = '{"fields": {"sus": ' + str(final_cash) + ' }}'
                url = 'https://api.airtable.com/v0/your-table/Table%201/' + str(money_location)
                response = requests.patch(url=url, headers=header2,
                                          data=change_sus)
                await ctx.send(
                    "You won some susCash! You now have {} susCash.".format(final_cash))
            elif rolled > 6 and rolled <= 8:
                final_cash = str(total - bet)
                change_sus = '{"fields": {"sus": ' + str(final_cash) + ' }}'
                url = 'https://api.airtable.com/v0/your-table/Table%201/' + str(money_location)
                response = requests.patch(url=url, headers=header2,
                                          data=change_sus)
                await ctx.send(
                    "Unfortunately, you lost some susCash. You now have {} susCash.".format(final_cash))
            elif rolled > 8 and rolled <= 10:
                final_cash = str(total + bet)
                change_sus = '{"fields": {"sus": ' + str(final_cash) + ' }}'
                url = 'https://api.airtable.com/v0/your-table/Table%201/' + str(money_location)
                response = requests.patch(url=url, headers=header2,
                                          data=change_sus)
                await ctx.send(
                    "You won some susCash! You now have {} susCash.".format(final_cash))

# bal command; allows user to check how much susCash they have
@bot.command()
async def bal(ctx):
    id = str(ctx.author.id)
    response = requests.get('https://api.airtable.com/v0/your-table/Table%201', headers=header1,
                            params=params)
    data = response.json()
    data_location = int()
    user_id_list = []
    for i in range(len(data["records"])):
        user_id = str(data["records"][i]["fields"]["user_id1"]) + str(data["records"][i]["fields"]["user_id2"])
        user_id_list.append(int(user_id))
        if user_id == id:
            data_location = i
            break
    if int(ctx.author.id) not in user_id_list:
        idsplit1 = []
        idsplit2 = []
        for j in range(len(id)):
            if j <= 8:
                idsplit1.append(id[j])
            else:
                idsplit2.append(id[j])
        user_id1 = str()
        user_id2 = str()
        for r in range(len(idsplit1)):
            user_id1 += idsplit1[r]
            user_id2 += idsplit2[r]
        post = '{ "records": [ { "fields": {"user_id1": ' + str(user_id1) + ', "user_id2": ' + str(
            user_id2) + ', "sus": 100} }] }'
        response = requests.post('https://api.airtable.com/v0/your-table/Table%201', headers=header2,
                                 data=post)
        response = requests.get('https://api.airtable.com/v0/your-table/Table%201', headers=header1,
                                params=params)
        data = response.json()
        for j in range(len(data["records"])):
            user_id = str(data["records"][j]["fields"]["user_id1"]) + str(data["records"][j]["fields"]["user_id2"])
            user_id_list.append(int(user_id))
            if user_id == id:
                data_location = j
                break
    total = int(data["records"][data_location]["fields"]["sus"])
    await ctx.send("You currently have {0} susCash under your account.".format(total))
