# sus bot

<p align="center">
<img src="img/susbot.png" alt="susbot logo" height=300>
</p>

## Discord.py has been discontinued, so the bot will be rewritten using Nextcord at a later point in time, as the development has been paused for the time being
There is a list of things being worked on for this bot in the [projects](https://github.com/joonsauce/susbot/projects) section of this repo.

# Table of Contents
- [About the Project](#about-the-project)
- [Usage](#usage)
  - [Features](#features)
- [License](#license)
- [The Team](#the-team)
# About the Project
A discord bot with influence from the popular indie video game Among Us, with features 
that mimic parts from Among Us. The bot is designed to be used within just one server, 
and therefore does not have a public link to make this bot join your server. However, you may modify 
and use this bot however you like. If you do use this template in a public bot, please give credit to this 
repository in some way. 
# Usage
The bot is *customizable*; it is configured to your taste for your own server. This means that I don't provide anywhere to 
host the bot, you have to find it yourself. To host you can just run `bot.py` in your choice of IDE or find a hosting provider.
All of the commands have been designed to be customized, guides for customizing all of them will come soon. The default prefix 
to use the bot is `s!`, but you can change that in `setting.py`. All of the required libraries are listed at the top of `setting.py`, 
but you still need to install `PyNaCl` and `FFMPEG` to use all of the bot's features. You do NOT need `FFMPEG` or `PyNaCl` if you do 
not plan to use the built-in soundboard feature. To install `PyNaCl`, run `pip install PyNaCl`. Susbot uses the Airtable API to deal 
with the virtual currencies. Therefore, to use the virtual currency system as intended, you need to have an Airtable account set up 
and a table ready to go. Instructions on how to do this will come soon. The repo does not include a file (which I called `secret.py` 
which includes all the sensitive information such as the API link and the Discord Bot token) but a template for this file will be added 
soon.
### Features
- bal
  - Allows user to see how much susCash they have as a part of the gambling feature
  - susCash has no monetary value anywhere in the world
- drip
  - Soundboard command that allows user to play a specific sound effect in a voice channel. The sound can be whatever you want, as long as the formatting is correct. The sound file is not included with this repo.
- join
  - Makes the bot join the voice channel the user is in
- leave
  - Makes the bot leave the voice channel the bot is in
- pp
  - Makes the bot play or pause the sound that is being played
- roll
  - Gambling feature where the user can gamble with a virtual currency called susCash
  - susCash has no monetary value anywhere in the world
  - Currently the odds are 4/6, but can be adjusted and new seeding features are being worked on
- scan
  - This command returns a simulated medbay scan from the video game Among Us. The value is random, and changes each time the command is run.
  - Added a random element where it may spit out an error; simulating impostors not being able to actually medbay scan.
- stop
  - Makes the bot stop the sound playing.
- sus {user} {action}
  - This command targets a user of doing something sus. The bot will return {author} sussed {user} of {action}.
  - A user must be tagged and an action must be filled out.
- susimg {user}
  - Puts the command user or the tagged user's profile picture (avatar) into the Among Us character suit.
  - Tagging a user is optional.
- susmeme
  - Sends random meme from a Reddit subreddit of choice with the original Reddit post caption as the title
- susrate {user}
  - This command rates a chosen member of the server based on how sus they are. The value is random and changes each time the command is run.
  - Tagging another user is optional.

# License
This project is released under the MIT license, see `LICENSE` for more info.
# The Team
Joonseo Lee - [LinkedIn](https://www.linkedin.com/joonsauce), [Website](https://joonsauce.me)
