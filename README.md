# sus bot

<p align="center">
<img src="img/susbot.png" alt="susbot logo" height=300>
</p>

# The bot is being largely redeveloped for optimization

# Table of Contents
- [Sus Discord Bot](#sus-discord-bhot)
- [Table of Contents](#table-of-contents)
- [About the Project](#about-the-project)
- [Usage](#usage)
  - [Command Types](#command-types)
- [License](#license)
- [The Team](#the-team)
# About the Project
A discord bot with influence from the popular indie video game Among Us, with features 
that combines some qualities of other bots. The bot was intended to be used within one server, 
so many parts are very server-specific. There is no public link for this bot. However, you can modify and 
use this bot however you like under the MIT license.
# Usage
At the moment, the bot is configured to be customized per server; some commands need to be 
hardwired in by the person who wants to use them.

There are a plenty of commands to choose from. The prefix is `s!`. You can change the prefix to what you want in setting.py
### Command Types (Among Us variants)
- susrate {user}
  - This command rates a chosen member of the server based on how sus they are. The value is random and changes each time the command is run.
  - Tagging another user is optional.
- sus {user} {action}
  - This command targets a user of doing something sus. The bot will return {author} sussed {user} of {action}.
  - A user must be tagged and an action must be filled out.
- scan
  - This command returns a simulated medbay scan from the video game Among Us. The value is random, and changes each time the command is run.
  - Added a random element where it may spit out an error; simulating impostors not being able to actually medbay scan.
- susimg {user}
  - Puts the command user or the targeted user's profile picture (avatar) into the Among Us character suit.
  - Tagging a user is optional.
### Command Types (Music bot variants)
- pp
  - Pauses or resumes the music that is playing. It is toggled, so you can use pp to pause AND resume music.
- join
  - Makes the bot join the voice channel the command writer is in.
- leave
  - Makes the bot leave the voice channel it is in.
- stop
  - Makes the bot stop the music playing. Stopping the currently playing music will make the next song in the queue play if there is a song in the queue.
- drip
  - This command plays a specific song (in my case, Among Us Drip) in a voice channel. The song can be any you want, as long as it is formatted right. You must download the song yourself, the song isn't included in this repo.
- roll
  - Was meant to be a "gambling" feature but was converted into Rick Roll player.

# License
This project is released under the MIT license, see `LICENSE` for more info.
# The Team
Joonseo Lee - [LinkedIn](https://www.linkedin.com/joonsauce), [Website](http://joonsauce.me)
