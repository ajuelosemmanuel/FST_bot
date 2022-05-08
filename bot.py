from lib.osuirc import osuIRC
from lib.functions import parser_pool
from config import *
from datetime import datetime
import re, random

# Connecting to the osu! IRC server
irc = osuIRC(username, password)
irc.connect()

# Parsing the pool
pool = parser_pool(nm, hd, hr, dt, tb, ez, ht)
mp=""

while 1:
    # Getting the messages from the IRC server
    text=irc.recv(2040)
    text_str = text.decode("utf-8")
    if "Emmanuel" in text_str:
        print(text_str)
    # Commands can only be used by referees
    for ref in referees:
        # self-ref and !join_mp command
        if mp=="":
            if username == ref:
                # If self reffing
                if ":BanchoBot!cho@ppy.sh PRIVMSG " + username + " :Created the tournament match" in text_str:
                    # Finding the mp id...
                    mplink = (re.findall("(?<=PRIVMSG " + username +" :Created the tournament match)(.*)(?=)", text_str))[0].strip().split(" ")[0]
                    mp = (re.findall("([^\/]+$)", mplink))[0].strip()
                    # Joining multiplayer lobby
                    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " : " + ref + " : Self-reffing " + mp)
                    # Win condition : Score v2
                    irc.message_mp(mp, "!mp set 2 3")
                    # Connection message
                    irc.message_mp(mp, "[FSTBot] Connecté")

            elif ":"+ref+"!cho@ppy.sh PRIVMSG " + username + " :!join_mp " in text_str:
                # Getting the mp_id
                mp = (re.findall("(?<=PRIVMSG " + username +" :!join_mp)(.*)(?=)", text_str))[0].strip()
                # Logging
                print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " : " + ref + " : !join_mp " + mp)
                # Joining multiplayer lobby
                irc.join_mp(mp)
                # Win condition : Score v2
                irc.message_mp(mp, "!mp set 2 3")
                # Connection message
                irc.message_mp(mp, "[FSTBot] Connecté")
        
        # !FST command
        if mp!="":
            for el in pool["AvailablePools"]:
                if ref+"!cho@ppy.sh PRIVMSG #mp_" + mp + " :!FST " + el in text_str:
                    # Logging
                    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " : " + ref + " : !FST " + el)
                    # Choosing a random map in the pool
                    irc.message_mp(mp, "!mp map "+ random.choice(pool[el]))
                    # Choosing the right mods
                    if el == "TB" or el == "FM":
                        irc.message_mp(mp, "!mp mods freemod")
                    elif el == "NM":
                        irc.message_mp(mp, "!mp mods nf")
                    else:
                        irc.message_mp(mp, "!mp mods nf " + el.lower())