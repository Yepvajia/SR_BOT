from mmap import ACCESS_COPY
import discord
import os
import random
import json
import time
import tweepy
from discord.ext import commands
from discord.ext.commands import has_guild_permissions
from ast import literal_eval
from datetime import datetime
from easy_pil import Editor, Canvas, Font, load_image

from globul import *

def getXP(lvl):
    n = 100
    add = 55
    if lvl == 0:
        return 0
    for i in range(1,lvl):
            n += add
            add += 10
    return n

def getTotalXP(lvl):
    n = 0
    for i in range(lvl+1):
        n += getXP(i)
    return n

def getLVL(exp):
    if exp == None:
        exp = 0
    if exp < 100:
        return 0
    lvl = 0
    n = 0
    while True:
        n += getXP(lvl)
        if n > exp:
            return lvl-1
        lvl += 1

def getXPCap(exp):
    lvl = getLVL(exp)
    lvlCap = getXP(lvl+1)
    curxp = exp
    return (lvl, exp-getTotalXP(lvl), lvlCap)

def aboveKCheck(n):
    if n > 1000:
        return f"{round(n/1000, 2)}K"
    return n

async def update_users(users, user):
    if not str(user.id) in users:
        users[str(user.id)] = 0

async def add_exp(users, user):
    users[str(user.id)] += random.randrange(3,7)

def get_rank(member):
    rankfile = os.path.join(here, 'databases/ranks.json')
    with open(rankfile, "r") as f:
        users = json.load(f)
    if users.get(str(member.id)) == None:
        return 0
    return users.get(str(member.id))

#Construct Rank Card
def drawRank(member):
    exp = get_rank(member)
    lvl , curxp, cap = getXPCap(exp)

    fontFile = os.path.join(here, 'assets/herchampions.ttf')
    bgFile = os.path.join(here, 'assets/card_bg_noking.png')
    image = load_image((str(member.avatar_url)))
    font = Font(fontFile, size=100)
    editor = Editor(bgFile)
    pfp = Editor(image).resize((275,275)).circle_image()

    editor.ellipse((21, 21), 279, 279, fill="#1c0e28")
    #1c0e28
    editor.paste(pfp.image, (23,23))

    editor.rectangle((205,370), 1165, 80, fill = "#ffe200", radius = 40)
    if int((curxp/cap)*100) < 7:
        perc = 0
        bar_height = 0
    else:
        perc = int((curxp/cap)*100)
        bar_height = 76

    if lvl >= 20:
        numtabs = "\t\t\t\t"
    elif lvl > 10 and lvl < 20:
        numtabs = "\t\t\t\t\t\t"
    else:
        numtabs = "\t\t\t\t\t\t\t\t"

    editor.ellipse((207,372), 76, 76, fill="#321848")
    editor.bar((207,372), max_width = 1161, height = bar_height, percentage = perc, fill="#321848", radius = 40)
    #321848 (1067/1255)*100
    #int((curxp/cap)*100)
    editor.text((340, 80), str(member)[:-5], font = font, color = "#ffe200")
    editor.text((340, 160), str(member)[-5:], font = font, color = "#ffe200")
    editor.text((340, 250), f"LVL: {lvl}{numtabs}{aboveKCheck(curxp)} / {aboveKCheck(cap)} xp", font = font, color = "#ffe200")
    # editor.text((760, 250), f"{cap}", font = font, color = "#ffe200")
    editor.rectangle((340, 236), width = 900, height = 4, fill = "#ffe200")
    #ffe200

    return editor.image_bytes