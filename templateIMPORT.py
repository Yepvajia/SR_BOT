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

#Builds the mains calls template embed
def templateMK(sport, template):
    #{"fields" : 6, "bet_type" : "PARLAY", "name0" : None, "body0" : None, "name1" : None, "body1" : None, "name2" : None, "body2" : None, "name3" : None, "body3" : None, "name4" : None, "body4" : None, "name5" : None, "body5" : None}
    description = None
    typeDic = {"check" : ["PROPS", "PARLAY", "STRAIGHT-BET"], "PROPS" : f"\uFEFF \uFEFF \uFEFF \uFEFF \uFEFF ~***__{template['bet_type']}__***~", "PARLAY" : f"\uFEFF \uFEFF \uFEFF \uFEFF ~***__{template['bet_type']}__***~", "STRAIGHT-BET" : f"~***__{template['bet_type']}__***~"}
    if int(template["fields"]) > 6:
        return
    if template['bet_type'] in typeDic["check"]:
        description = typeDic[template['bet_type']]
    e = discord.Embed(title = f"***__Stakes Royale__***", description = description, color = discord.Color.dark_purple())
    e.set_thumbnail(url = THMB)
    for i in range(int(template["fields"])+1):
        if i == 0:
            # e.add_field(name = str("\uFEFF"), value = str("\uFEFF"), inline = False)
            e.add_field(name = template[f"name{i}"], value = "🔒" + template[f"body{i}"], inline = False)
        else:
            e.add_field(name = f"__", value = "----------------------------------------------------------------------------", inline = False)
            e.add_field(name = template[f"name{i}"], value = "🔒" + template[f"body{i}"], inline = False)
    e.set_footer(text = f"{sport}")
    if description != None:
        return e

#Checks if any of the "fields" are None
def templateCheck(template):
    for i in range(int(template["fields"])+1):
        if template[f"name{i}"] == None or template[f"body{i}"] == None:
            return False
    return True

#Checks if any of the "fields" are None just for the weekly/schedule template (template with no body)
def templateCheckWK(template):
    for i in range(int(template["fields"])+1):
        if template[f"body{i}"] == None:
            return False
    return True

#Log msg author
def log(auth): 
    ## V ADD THIS NOW DECLARATION TO THE TOP OF THE OTHER BOT 
    author = str(auth)
    anaFile = os.path.join(here, 'databases/analyst_log.json')
    now = datetime.now()
    date_time = now.strftime('%d/%m/%Y, %H:%M:%S')
    log = {}
    log[date_time] = author[:-5]
    with open(anaFile, "r") as file:
        data = json.load(file)
        data.append(log)
    with open(anaFile, "w") as file:
        json.dump(data, file, indent=2)
    print(log, " LOGGED")

#Builds the weekly/schedule template embed
def weeklyMK(template, type):
    #{"fields" : 6, "bet_type" : "PARLEY", "name0" : None, "body0" : None, "name1" : None, "body1" : None, "name2" : None, "body2" : None, "name3" : None, "body3" : None, "name4" : None, "body4" : None, "name5" : None, "body5" : None}
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    description = type
    e = discord.Embed(title = f"***__Stakes Royale__***", description = description, color = discord.Color.dark_purple())
    e.set_thumbnail(url = THMB)
    for i in range(int(template["fields"])+1):
        if i == 0:
            # e.add_field(name = str("\uFEFF"), value = str("\uFEFF"), inline = False)
            e.add_field(name = week[i], value = "🔒" + template[f"body{i}"], inline = False)
        else:
            e.add_field(name = f"__", value = "----------------------------------------------------------------------------", inline = False)
            e.add_field(name = week[i], value = "🔒" + template[f"body{i}"], inline = False)
    e.set_footer(text = f"Stakes Royale")
    return e

#Builds the winrate template embed
def winrateMK(template):
    #{"fields" : 6, "bet_type" : "PARLAY", "name0" : None, "body0" : None, "name1" : None, "body1" : None, "name2" : None, "body2" : None, "name3" : None, "body3" : None, "name4" : None, "body4" : None, "name5" : None, "body5" : None}
    bet_type = ["STRAIGHT-BET", "PARLAY", "PROPS"]
    description = "***__~WIN RATE~__***"
    e = discord.Embed(title = f"***__Stakes Royale__***", description = description, color = discord.Color.dark_purple())
    e.set_thumbnail(url = THMB)
    for i in range(int(template["fields"])+1):
        if i == 0:
            # e.add_field(name = str("\uFEFF"), value = str("\uFEFF"), inline = False)
            e.add_field(name = bet_type[i], value = "🔒" + template[f"body{i}"], inline = False)
        else:
            e.add_field(name = f"__", value = "----------------------------------------------------------------------------", inline = False)
            e.add_field(name = bet_type[i], value = "🔒" + template[f"body{i}"], inline = False)
    e.set_footer(text = f"Stakes Royale")
    return e

def pollMK(sport, template):
    #{"fields" : 6, "bet_type" : "PARLAY", "name0" : None, "body0" : None, "name1" : None, "body1" : None, "name2" : None, "body2" : None, "name3" : None, "body3" : None, "name4" : None, "body4" : None, "name5" : None, "body5" : None}
    emo_ls = ["1️⃣", "2️⃣" , "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
    if int(template["fields"]) > 6:
        return
    description = "\uFEFF \uFEFF \uFEFF \uFEFF \uFEFF***__~POLLS~__***"
    e = discord.Embed(title = f"***__Stakes Royale__***", description = description, color = discord.Color.dark_purple())
    e.set_thumbnail(url = THMB)
    for i in range(int(template["fields"])+1):
        if i == 0:
            # e.add_field(name = str("\uFEFF"), value = str("\uFEFF"), inline = False)
            e.add_field(name = emo_ls[i] + template[f"name{i}"], value = template[f"body{i}"], inline = False)
        else:
            e.add_field(name = f"__", value = "----------------------------------------------------------------------------", inline = False)
            e.add_field(name = emo_ls[i] + template[f"name{i}"], value = template[f"body{i}"], inline = False)
    e.set_footer(text = f"{sport}")
    if description != None:
        return e

if __name__ == '__main__':
    pass
