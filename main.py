from hashlib import new
from mmap import ACCESS_COPY
import discord
import asyncio
import os
import random
import json
import time
import tweepy
from discord.ext import commands, tasks
from discord.ext.commands import has_guild_permissions
from ast import literal_eval
from datetime import datetime
from easy_pil import Editor, Canvas, Font, load_image

from xp import *
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
    channel = client.get_channel(951714836633493525)
    await channel.edit(name = f'Bot Status: Online 🤖')
    updateMembers.start()

#New Member Count Task
@tasks.loop(minutes=20)
async def updateMembers():
    channel = client.get_channel(938335074523435008)  
    guild = client.get_guild(937560982484553728)
    await channel.edit(name = f'Member Count: {len([m for m in guild.members if not m.bot])}')


@client.event
async def on_message(message):
    if not message.content.startswith('$') and str(message.author.id) != "943637486473711736":
        rankfile = os.path.join(here, 'databases/ranks.json')
        with open(rankfile, "r") as f:
            users = json.load(f)

        exp = users.get(str(message.author.id))
        lvl = getLVL(exp)
        await update_users(users, message.author)
        await add_exp(users, message.author)
        # this ened up not being the problem, I just needed to dump the new rank before attempting to send the dm
        # if users.get(str(message.author.id)) == 99:
        #     users[str(message.author.id)] += 1
        exp = users.get(str(message.author.id))
        newlvl = getLVL(exp)

        with open(rankfile, "w") as f:
            json.dump(users, f, indent=2)

        if newlvl > lvl:
            if newlvl == 1:
                await message.author.send(f"**You just leveled up for the first time on Stakes Royale. Congrats! Type $rank to see your custom rank card**")
            else:
                channel = client.get_channel(947976006650695750)
                await channel.send(f"Congrats {message.author.mention}, you have leveled up to level {newlvl}")


    await client.process_commands(message)

# Not really needed: See task updateMembers
# def nmembers(guild):
#     return len([m for m in guild.members if not m.bot])

#Member Reaction Give
@client.event
async def on_raw_reaction_add(payload):
    guild = client.get_guild(payload.guild_id)
    member = discord.utils.get(guild.members, id=payload.user_id)
    if payload.message_id == DISCLAIMER_MSG_ID:
        if str(payload.emoji) == "✅":
            role = discord.utils.get(guild.roles, name='KNIGHT')
            # channel = client.get_channel(938335074523435008)
            await member.add_roles(role)
            #await channel.edit(name = f'Member Count: {nmembers(member.guild)}')
            # print(nmembers(member.guild))


#Member Reaction Remove
@client.event
async def on_raw_reaction_remove(payload):
    guild = client.get_guild(payload.guild_id)
    member = discord.utils.get(guild.members, id=payload.user_id)
    if payload.message_id == DISCLAIMER_MSG_ID:
        if str(payload.emoji) == "✅":
            role = discord.utils.get(guild.roles, name='KNIGHT')
            # channel = client.get_channel(938335074523435008)
            await member.remove_roles(role)
            #await channel.edit(name = f'Member Count: {nmembers(member.guild)}')
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
    pass
    # channel = client.get_channel(938335074523435008)
    # await channel.edit(name = f'Member Count: {nmembers(member.guild)}')
    # print("New Member!")

#Update member count on leave
@client.event
async def on_member_remove(member):
    pass
    # channel = client.get_channel(938335074523435008)
    # await channel.edit(name = f'Member Count: {nmembers(member.guild)}')
    # print("New Member!")


#Send Rank Card
@client.command()
# @has_guild_permissions(administrator=True)
async def rank(ctx):
    #creating rank file
    if ctx.channel.id == 947970181630672936:
        file = discord.File(fp=drawRank(ctx.message.author), filename='rank_card.png')
        await ctx.send(file=file)
    else:
        e = discord.Embed(title = "Use the $rank command in the __ranks__ text chat", color = discord.Color.dark_purple())
        await ctx.send(embed=e)
        await asyncio.sleep(2)
        await ctx.channel.purge(limit = 2)

# @client.command()
# @has_guild_permissions(administrator=True)
# async def tester(ctx, exp = 100):
#     #creating rank file
#     lvl , cap = getXPCap(exp)
#     await ctx.send(f"{lvl} | {cap}")

if __name__ == '__main__':
    for i in extensions:
        try:
            client.load_extension(i)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(i, error))

client.run('OTQzNjM3NDg2NDczNzExNzM2.Yg185A.6AxeTvjbyJZk24cQI_V3utwOk5g')