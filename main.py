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

extensions = ['template', '_commands']
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


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('The Odds'))
    print("we good")

def nmembers(guild):
    return len([m for m in guild.members if not m.bot])




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
            # print(nmembers(member.guild))


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
            # print(nmembers(member.guild))



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
    print("New Member!")

#Update member count on leave
@client.event
async def on_member_remove(member):
    channel = client.get_channel(938335074523435008)
    await channel.edit(name = f'Member Count: {nmembers(member.guild)}')
    print("New Member!")





#Construct Rank Card
def drawRank(member, perc):
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

if __name__ == '__main__':
    for i in extensions:
        try:
            client.load_extension(i)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(i, error))

client.run('OTQzNjM3NDg2NDczNzExNzM2.Yg185A.6AxeTvjbyJZk24cQI_V3utwOk5g')