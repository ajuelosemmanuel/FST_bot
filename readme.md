# FST Bot

This repository contains all files required to run the [French Sightread Tournament](https://osu.ppy.sh/community/forums/topics/1569884) bot.

## Requirements

In order to run the bot properly, you must :
+ Fill the `config.py` file
+ Fill the `pools` folder with `.txt` files containing each "pool" (eg : `nm.txt`, `hd.txt`, ...).
  + Those pool files contain map links, one per line.
+ Have [Python](https://www.python.org/downloads/) installed on your machine

## Commands

The available commands are :
+ `!join_mp` :
  + Arguments :
    + `mp_id` : The multiplayer lobby id : `https://osu.ppy.sh/community/matches/<mp_id>`
  + Adds the bot to your lobby. To make it work, the bot should be a referee. To do so, send the following private message to `BanchoBot` : `!mp addref <bot_username>`
  + You must send it to the bot directly.
+ `!FST`
  + Arguments :
    + `MOD` : One of the available mods in the pool (case sensitive, so type `NM` instead of `nm`).
  + Picks a random map in the mod pool.
  + You must send it in the multiplayer lobby.

## Running the bot

Once all the requirements are fulfilled, simply run the following command :
```
py bot.py
```

## Guide

First, run the bot.

If you are running the bot on the account that is reffing, make sure to run it before creating the multiplayer lobby.

Once the lobby is created, the bot will automatically join it.

If you are not running the bot on the same account, send the `!join_mp` to the bot. It should send a message in the room.

Then, you can use the commands freely.
