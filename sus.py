from setting import *

# suslogo command; makes bot send the susbot image; you can replace the image with whatever you want and whatever name you want for the command
@bot.command()
async def suslogo(ctx):
    # takes the susbot image in the img folder and sends to channel bot was activated in
    await ctx.send(file=discord.File(open('img/susbot.png', 'rb'), 'susbot.png'))

# susout command; a user accuses another user of something suspicious
@bot.command()
async def sus(ctx, arg1='', *, arg2=''):
    # checks for target user and reason and returns error if none
    if not arg1:
        await ctx.send("Please choose a target")
        return
    if not arg2:
        await ctx.send("Please give a reason for the sus")
        return
    # checks if it is user (but this isn't the proper way to do it, so it will be fixed)
    if not arg1.startswith("<"):
        await ctx.send("Please choose a user to target")
        return
    # deletes the command message & sends sus message: format <user> sussed <user2> for <reason>
    await ctx.message.delete()
    await ctx.send('{0.author.mention} sussed {1} of *{2}*'.format(ctx, arg1, arg2))

# susrate command; rates how sus a person is; is a static value
@bot.command()
async def susrate(ctx, *, msg=''):
    # if no follow up message after command, sets user to command user; otherwise user is who is in message
    if not msg:
        user = ctx.author.mention
    else:
        # should probably make a way to error check this
        user = msg
    # generates a random number to use as a percent
    rate = random.randint(0, 100)
    # sends the randomly generatd number as how "sus" a user is
    await ctx.send(user + "'s susrate is " + str(rate) + "%")

# susimg command; makes bot process profile picture into sus picture, command seems a tad bit slower than I want, will optimize soon
@bot.command()
async def susimg(ctx, *, msg: discord.User=''):
    # if no user is tagged defaults the command user as the person to run through the image laundering
    if not msg:
        avatar = ctx.author.display_avatar
    # otherwise it is the tagged user's avatar
    else:
        avatar = msg.display_avatar
    # sets it as a string so the code doesn't freak out
    pfp_url = str(avatar)
    # checks if the profile picture is a gif and saves first frame of image; otherwise, save it as regular png
    if pfp_url[:-10].endswith("gif"):
        with requests.get(pfp_url) as r:
            img = r.content
        with open('gifImage.gif', 'wb') as handler:
            handler.write(img)
        frame = Image.open("gifImage.gif").convert("RGBA")
        frame.seek(0)
        frame.save("image.png")
    else:
        with requests.get(pfp_url) as r:
            img = r.content
        with open('image.png', 'wb') as handler:
            handler.write(img)
    # opens among us character mask and uses it to cut user's avatar
    mask = Image.open("img/Red_body_mask.png").convert('L')
    image = Image.open("image.png")
    cut = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    cut.putalpha(mask)
    # layers among us character image onto user's cut avatar
    susimg = Image.open('img/red_body.png')
    susimg.paste(cut, (0, 0), cut)
    # saves the image as final.png and sends image to server
    susimg.save('final.png')
    await ctx.send(file=discord.File(open('final.png', 'rb'), 'final.png'))
    
# different among us game feature commands below

# medbay command; medbay scans user
@bot.command()
async def scan(ctx):
    # 20% chance of causing error
    status = random.randint(0, 4)
    if status == 0:
        await ctx.send("Error: Cannot scan user")
    else:
        colors = ["Red", "Orange", "Yellow", "Lime", "Green", "Cyan", "Blue", "Purple", "Black", "White", 'Pink', 'Brown']
        colorId = ["RED", "ORA", "YEL", 'LIM', 'GRE', 'CYA', 'BLU', 'PUR', 'BLA', 'WHI', 'PIN', "BRO"]
        colorPicker = random.randint(0, 11)
        playerId = colorId[colorPicker] + "P" + str(random.randint(1, 10))
        height = random.uniform(1.50, 2.00)
        weight = random.randint(40, 100)
        bloodTypes = ["O+", 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-']
        bloodtype = bloodTypes[random.randint(0, 7)]
        await ctx.send("ID: " + playerId + "  HT: " + str(height)[:4] + "  WT: " + str(weight) + "KG" + "  C: " + colors[colorPicker] + "  BT: " + bloodtype)
