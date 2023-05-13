from setting import *

# suslogo command; makes bot send the susbot image; you can replace the image with whatever you want and whatever name you want for the command
@bot.command()
async def suslogo(ctx):
    # takes the susbot image in the img folder and sends to channel bot was activated in
    await ctx.send(file=discord.File(open('img/susbot.png', 'rb'), 'susbot.png'))

# susout command; a user accuses another user of something suspicious
@bot.command()
async def sus(ctx, arg1, *, arg2):
    # deletes the command message
    await ctx.message.delete()
    # gets the @ of the user that activated the command, adds the accused (arg1), followed by the action the accused did (arg2)
    await ctx.send('{0.author.mention} sussed {1} of *{2}*'.format(ctx, arg1, arg2))

# susrate command; rates how sus a person is; is a static value
@bot.command()
async def susrate(ctx, *, msg=''):
    # if there is is no message (ie its just s!susrate) it sets the user to be susrated as the user that activated the command
    if not msg:
        user = ctx.author.mention
    # if a user is tagged, the user is susrated instead
    else:
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
    # checks if the profile picture is a gif
    if pfp_url[:-10].endswith("gif"):
        # downloads image
        with requests.get(pfp_url) as r:
            img = r.content
        # saves image
        with open('gifImage.gif', 'wb') as handler:
            handler.write(img)
        # converts image into RGBA mode
        frame = Image.open("gifImage.gif").convert("RGBA")
        # finds the first frame of gif
        frame.seek(0)
        # saves the first frame as the image
        frame.save("image.png")
    # if the profile picture is not a gif
    else:
        # downloads image
        with requests.get(pfp_url) as r:
            img = r.content
        # saves image
        with open('image.png', 'wb') as handler:
            handler.write(img)
    # this is the image that "cuts" the profile picture
    mask = Image.open("img/Red_body_mask.png").convert('L')
    # this is the profile picture
    image = Image.open("image.png")
    # this cuts the profile picture
    cut = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    cut.putalpha(mask)
    # this is the Among Us character iamge
    susimg = Image.open('img/red_body.png')
    # this combines the Among Us character with the cut profile picture
    susimg.paste(cut, (0, 0), cut)
    # saves the image as final.png
    susimg.save('final.png')
    # sends the image back
    await ctx.send(file=discord.File(open('final.png', 'rb'), 'final.png'))
    
# different among us game feature commands below

# medbay command; medbay scans user
@bot.command()
async def scan(ctx):
    user = ctx.author.mention
    status = random.randint(0, 1)
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
