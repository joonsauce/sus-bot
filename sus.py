from setting import *

# suslogo command; makes bot send the susbot image
@bot.command()
async def suslogo(ctx):
    await ctx.send(file=discord.File(open('img/susbot.png', 'rb'), 'susbot.png'))

# susout command; a user accuses another user of something suspicious
@bot.command()
async def sus(ctx, arg1, *, arg2):
    await ctx.message.delete()
    await ctx.send('{0.author.mention} sussed {1} of *{2}*'.format(ctx, arg1, arg2))

# susrate command; rates how sus a person is; is a static value
@bot.command()
async def susrate(ctx, *, msg=''):
    if not msg:
        user = ctx.author.mention
    else:
        user = msg
    rate = random.randint(0, 100)
    await ctx.send(user + "'s susrate is " + str(rate) + "%")

# susimg command; makes bot process profile picture into sus picture (:
@bot.command()
async def susimg(ctx, *, msg: discord.User=''):
    if not msg:
        avatar = ctx.author.avatar_url
    else:
        avatar = msg.avatar_url
    pfp_url = str(avatar)
    with requests.get(pfp_url) as r:
        img = r.content
    with open('image.png', 'wb') as handler:
        handler.write(img)
    mask = Image.open("img/Red_body_mask.png").convert('L')
    image = Image.open("image.png")
    cut = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    cut.putalpha(mask)
    susimg = Image.open('img/red_body.png')
    susimg.paste(cut, (0, 0), cut)
    susimg.save('final.png')
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
