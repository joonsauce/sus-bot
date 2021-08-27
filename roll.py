# imports discord settings
from setting import *

# defines different header types for api calls
header1 = {
        'Authorization': 'Bearer {}'.format('your api key'),
        }
header2 = {
            'Authorization': 'Bearer {}'.format('your api key'),
            'Content-Type': 'application/json',
        }

# defines parameters for api calls
params = (
        ('maxRecords', 100),
        ('view', 'Grid view'),
    )

# roll command; makes bot run a simulated gamble
@bot.command()
async def roll(ctx, *, msg=''):
    # if there is no message (just the command is run) an error is thrown
    if not msg:
        # asks user to enter amount they wish to use
        await ctx.send("Please enter the amount of susCash you wish to use.")
    # if there is a message the following code is run
    else:
        # checks if the message is a numer
        try:
            # tries to set bet as an integer
            bet = int(msg)
        # if ValueError is thrown, the message was not a number and error is thrown
        except ValueError:
            # sends error message
            await ctx.send("The amount of susCash you entered is not a number.")
        # if the message is a number the following code is run
        else:
            # sets id as the user's unique id
            id = str(ctx.author.id)
            # gets data from database (i used airtable for ease of use) using headers and parameters defined above        
            response = requests.get('https://api.airtable.com/v0/your-table/Table%201', headers=header1,
                                    params=params)
            # the collected data is saved as a .json file
            data = response.json()
            # variable to set the location of the user in the json file
            data_location = int()
            # variable to list all of the user ids in the database (this part is being worked on for optimization)
            user_id_list = []
            # checks every file under the records (rows) in the database
            for i in range(len(data["records"])):
                # sets user_id as the concatenated id (the id was originally split in two due to database restrictions)
                user_id = str(data["records"][i]["fields"]["user_id1"]) + str(data["records"][i]["fields"]["user_id2"])
                # adds the concatenated id into user_id_list
                user_id_list.append(int(user_id))
                # if the user's unique id is the concatenated id, break the loop and set i as where the user's data is
                if user_id == id:
                    data_location = i
                    # sets the location of the user's data
                    money_location = str(data["records"][data_location]["id"])
                    break
            # after the loop iterates through all users and the user doesn't exist, the code below adds them to the database
            if int(ctx.author.id) not in user_id_list:
                # variables for the first and second sections of the user id
                idsplit1 = []
                idsplit2 = []
                # splits the user id in two
                for j in range(len(id)):
                    # up to the 9th number is added to idsplit1 and the rest is added to idsplit2
                    if j <= 8:
                        idsplit1.append(id[j])
                    else:
                        idsplit2.append(id[j])
                # variables to combine the user ids into one string
                user_id1 = str()
                user_id2 = str()
                # loop to create combine the split user ids into one string
                for r in range(len(idsplit1)):
                    user_id1 += idsplit1[r]
                    user_id2 += idsplit2[r]
                # sets the data being sent to the database
                post = '{ "records": [ { "fields": {"user_id1": ' + str(user_id1) + ', "user_id2": ' + str(
                    user_id2) + ', "sus": 100} }] }'
                # POSTs data to the database
                response = requests.post('https://api.airtable.com/v0/your-table/Table%201', headers=header2,
                                         data=post)
            # the total amount of susCash the user has is called here
            total = int(data["records"][data_location]["fields"]["sus"])
            # if the amount the user tries to bet is larger than the amount of susCash they have an error is thrown
            if bet > total:
                # send error message
                await ctx.send("You cannot bet more than the total amount of sus you have.")
            # otherwise the code is run as normal
            else:
                # generates a random integer to determine the path of the user
                rolled = random.randint(1, 10)
                # different outcomes
                if rolled <= 4:
                        # sets final_cash to be PATCHed to the database and announced to the user
                        final_cash = str(total - bet)
                        # sets the data packet the bot will send to the database
                        change_sus = '{"fields": {"sus": ' + str(final_cash) + ' }}'
                        # sets the url of the database and the location of user data (this will be moved sometime in the near future)
                        url = 'https://api.airtable.com/v0/your-table/Table%201/' + str(money_location)
                        # updates the databse to the new amount of susCash the user now has
                        response = requests.patch(url=url, headers=header2,
                                          data=change_sus)
                        # sends result of the roll
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
