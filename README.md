# sus discord bot

<p align="center">
<img src="img/susbot.png" alt="susbot logo" height=300>
</p>

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

There are a plenty of commands to choose from. The prefix is `s!`
### Command Types
- susrate {user}
  - This command rates a chosen member of the server based on how sus they are. The value is static and does not change.
- susout {user} {action}
  - This command targets a user of doing something sus. The bot will return {author} sussed {user} of {action}.
- randomsong {arg}
  - Two subcommands: `random` or `{number}`
  - The command either plays a random song from the song bank, or a song chosen by a member of the server.
  - The music bot portion of the bot is still in the works, but is coming soon.
- scan
  - This command returns a simulated medbay scan from the video game Among Us. The value is static, set per user in each server.
  - If there is more than one user to use the medbay scan, `<@!usertag>` must be used. If only one person, use `<@usertag>` instead.
- drip
  - This command plays a specific song (in my case, Among Us Drip) in a voice channel. The song can be any you want, as long as it is formatted right.

# License
This project is released under the MIT license, see `LICENSE` for more info.
# The Team
Joonseo Lee - [LinkedIn](https://www.linkedin.com/joonsauce), [Website](http://joonsauce.me)
