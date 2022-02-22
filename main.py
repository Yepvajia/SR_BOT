from mmap import ACCESS_COPY
import discord
import os
import random
import json
import tweepy
from discord.ext import commands
from discord.ext.commands import has_guild_permissions
from datetime import datetime
from easy_pil import Editor, Canvas, Font, load_image


#discord.py init
intents = discord.Intents().all()
intents.reactions = True
client = discord.Client()
client = commands.Bot(command_prefix = '$', intents=intents, allowed_mentions = discord.AllowedMentions(everyone = True))
client.remove_command('help')

#tweepy init
# API_KEY = "SuIU8eOMLgxolVWdZ4Z157pDR"
# API_KEY_SECRET = "EBFMPIN32XDZxKNG5fORCGQL257maOmnVTVOutDzCvXDPVUAVE"
# BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAADVJZQEAAAAAgZ54%2BMB9Vj3iTce5uNu1MN9xLyM%3DYZ1eJNZlqsHdrkHkKamPycBpTuKX5HsgNHIKMmL4ZMVdZxWszA"
# ACCESS_TOKEN = "1494133144173387779-OFCW33JvaeOo3m6BqAJfxEyDsIyxO0"
# ACCESS_TOKEN_SECRET = "jdc5DV6cEOQtG2G3fV6oHEpEWg0HFLexWylraZ7cLdICf"

# auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)

#GLOBAL DISCORD VARIABLES 
DISCLAIMER_MSG_ID = 943683796228800593
THMB = "https://i.imgur.com/QKWCNMI.png"

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('The Odds'))
    print("we good")

def nmembers(guild):
    return len([m for m in guild.members if not m.bot])
#Deletes Messages
@client.command(pass_context=True)
@has_guild_permissions(administrator=True)
async def delete(ctx, n_messages = 5):
  await ctx.channel.purge(limit = n_messages + 1)

#Creates a Stakes Royale Disclaimer embed
@client.command()
@has_guild_permissions(administrator=True)
async def Dis_(ctx):
    e = discord.Embed(title = "***__DISCLAIMER!__**", description = "StakesRoyale is not responsible for, and specifically revokes any liability for any direct or consequential loss arising from any information contained within the site. While the information on the site is meticulously reviewed, researched and statistically evaluated, the reader bears all responsibility on their own investments.\n\nAny information found on the StakesRoyale server should not be used as the sole data basis for any single decision. The StakesRoyale server is merely a platform for sports advisory, and any information inscribed within the server by any moderators/analysts is not always one hundred percent accurate.", color = discord.Color.dark_purple())
    e.set_thumbnail(url = "https://i.imgur.com/QKWCNMI.png")
    e.set_footer(text = "Press The ✅ To Agree To The Disclaimer")
    message = await ctx.send(embed=e)
    await message.add_reaction("✅")
    #await ctx.send(f"@everyone Welcome! Please click ✅ to gain access to the server. You will see all our channels on the left.")

    ## (Mammas wanted this added) Please click ✅ to gain access to the server. You will see all our channels on the left. Welcome! @everyone


#Socials Embed
@client.command()
@has_guild_permissions(administrator=True)
async def Socials_(ctx):
    e = discord.Embed(title = "Socials", color = discord.Color.dark_purple())
    e.set_thumbnail(url = THMB)
    e.add_field(name= "<:tiktok:938338392847052810>", value = "[TikTok｜Link](https://www.youtube.com/)",inline = False)
    e.add_field(name = str("\uFEFF"), value = str("\uFEFF"), inline = False)
    e.add_field(name= "<:insta:938339028099559424>", value = "[Instagram｜Link](https://www.youtube.com/)",inline = False)
    e.add_field(name = str("\uFEFF"), value = str("\uFEFF"), inline = False)
    e.add_field(name= "<:twitter:938339492706799647>", value = "[Twitter｜Link](https://www.youtube.com/)",inline = False)
    e.add_field(name = str("\uFEFF"), value = str("\uFEFF"), inline = False)
    e.add_field(name= "<:youtube:938338677015339008>", value = "[Youtube｜Link](https://www.youtube.com/)",inline = False)
    e.add_field(name = str("\uFEFF"), value = str("\uFEFF"), inline = False)
    e.add_field(name= "<:logo:938339777948831784>", value = "[Website｜Link](http://stakesroyale.com/)",inline = False)
    e.add_field(name = str("\uFEFF"), value = str("\uFEFF"), inline = False)
    e.set_footer(text = "Do you want somthing here?")
    await ctx.send(embed=e)

#Member Reaction Give
@client.event
async def on_raw_reaction_add(payload):
    guild = client.get_guild(payload.guild_id)
    member = discord.utils.get(guild.members, id=payload.user_id)
    if payload.message_id == DISCLAIMER_MSG_ID:
        if str(payload.emoji) == "✅":
            role = discord.utils.get(guild.roles, name='Members')
            channel = client.get_channel(938335074523435008)
            await member.add_roles(role)
            await channel.edit(name = f'Member Count: {nmembers(member.guild)}')
            print(nmembers(member.guild))


#Member Reaction Remove
@client.event
async def on_raw_reaction_remove(payload):
    guild = client.get_guild(payload.guild_id)
    member = discord.utils.get(guild.members, id=payload.user_id)
    if payload.message_id == DISCLAIMER_MSG_ID:
        if str(payload.emoji) == "✅":
            guild = client.get_guild(payload.guild_id)
            role = discord.utils.get(guild.roles, name='Members')
            channel = client.get_channel(938335074523435008)
            await member.remove_roles(role)
            await channel.edit(name = f'Member Count: {nmembers(member.guild)}')
            print(nmembers(member.guild))



#manual check of member count
@client.command()
@has_guild_permissions(administrator=True)
async def memberCount(ctx):
    member_count = len([m for m in ctx.guild.members if not m.bot])
    e = discord.Embed(title = "Member Count", color = discord.Color.dark_purple())
    e.set_thumbnail(url = THMB)
    e.add_field(name= "Members:", value = f"{member_count}",inline = False)
    e.set_footer(text = "React Symbol")
    channel = client.get_channel(938335074523435008)
    await ctx.send(embed=e)
    await channel.edit(name = f'Member Count: {member_count}')
    print(member_count)

#Update member count on join
@client.event
async def on_member_join(member):
    channel = client.get_channel(938335074523435008)
    await channel.edit(name = f'Member Count: {nmembers(member.guild)}')
    print(nmembers(member.guild))

#Update member count on leave
@client.event
async def on_member_remove(member):
    channel = client.get_channel(938335074523435008)
    await channel.edit(name = f'Member Count: {nmembers(member.guild)}')
    print(nmembers(member.guild))



#Test Json Log
@client.command()
@has_guild_permissions(administrator=True)
async def log(ctx, password): 
    ## V ADD THIS NOW DECLARATION TO THE TOP OF THE OTHER BOT 
    here = os.path.dirname(os.path.abspath(__file__))
    anaFile = os.path.join(here, 'analyst_log.json')
    now = datetime.now()
    date_time = now.strftime('%d/%m/%Y, %H:%M:%S')
    log = {}
    author = str(ctx.message.author)
    log[date_time] = author[:-5]
    with open(anaFile, "r") as file:
        data = json.load(file)
        data.append(log)
    with open(anaFile, "w") as file:
        json.dump(data, file)
    await ctx.send("Done")
    print(log, password)

#Construct Rank Card
def drawRank(member, perc):
    here = os.path.dirname(os.path.abspath(__file__))
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
    editor.bar((207,372), max_width = 1161, height = 76, percentage = int(perc), fill="#321848", radius = 40)
    #321848 (1067/1255)*100
    editor.text((340, 80), str(member)[:-5], font = font, color = "#ffe200")
    editor.text((340, 160), str(member)[-5:], font = font, color = "#ffe200")
    editor.text((340, 250), f"LVL 11", font = font, color = "#ffe200")
    editor.text((760, 250), f"1.06K/1.25K EXP", font = font, color = "#ffe200")
    editor.rectangle((340, 236), width = 900, height = 4, fill = "#ffe200")
    #ffe200

    return editor.image_bytes

#Send Rank Card
@client.command()
# @has_guild_permissions(administrator=True)
async def rank(ctx, perc = 85):
    #creating rank file
    file = discord.File(fp=drawRank(ctx.message.author, perc), filename='rank_card.png')
    await ctx.send(file=file)

def templateMK(sport, template):
    #{"fields" : 6, "bet_type" : "PARLEY", "name0" : None, "body0" : None, "name1" : None, "body1" : None, "name2" : None, "body2" : None, "name3" : None, "body3" : None, "name4" : None, "body4" : None, "name5" : None, "body5" : None}
    if template["fields"] > 6:
        return
    e = discord.Embed(title = f"***__Stakes Royale__***", description = f"\uFEFF \uFEFF \uFEFF \uFEFF ~***__{template['bet_type']}__***~", color = discord.Color.dark_purple())
    e.set_thumbnail(url = THMB)
    for i in range(int(template["fields"])+1):
        if i == 0:
            e.add_field(name = str("\uFEFF"), value = str("\uFEFF"), inline = False)
            e.add_field(name = template[f"name{i}"], value = template[f"body{i}"], inline = False)
        else:
            e.add_field(name = f"__", value = "----------------------------------------------------------------------------", inline = False)
            e.add_field(name = template[f"name{i}"], value = template[f"body{i}"], inline = False)
    e.set_footer(text = f"{sport}")
    print(e)
    return e

def templateCheck(template):
    for i in range(int(template["fields"])+1):
        if template[f"name{i}"] == None or template[f"body{i}"] == None:
            return False
    return True


@client.command()
@has_guild_permissions(administrator=True)
async def footcall(ctx):
    e = templateMK("Football",{"fields" : 4, 
"bet_type" : "PARLEY",
 "name0" : "Big bet lots of money 🤑🤑💸",
 "body0" : "TRUST ME THIS IS THE MOVE ✅",
 "name1" : "🔒 LOCK OF THE WEEK 🔒",
 "body1" : "💰Invest Now💰",
 "name2" : "Is Tom Brady Gay???",
 "body2" : "😎Bigly😎",
 "name3" : "Large Man 🤣",
 "body3" : "On The Move ✅✅✅✅",
 "name4" : "Alright I got one more fo you",
 "body4" : "✅✅✅✅✅✅✅",
 "name5" : None,
 "body5" : None})
    channel = client.get_channel(943684861326131251) 
    await channel.send(embed = e)




client.run('OTQzNjM3NDg2NDczNzExNzM2.Yg185A.6AxeTvjbyJZk24cQI_V3utwOk5g')