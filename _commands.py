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

class _Commands(commands.Cog):
    def __init__(self, client):
        self.client = client


    #Deletes Messages
    @commands.command(pass_context=True)
    @has_guild_permissions(administrator=True)
    async def delete(self, ctx, n_messages = 5):
        await ctx.channel.purge(limit = n_messages + 1)

    #Creates a Stakes Royale Disclaimer embed
    @commands.command()
    @has_guild_permissions(administrator=True)
    async def Dis_(self, ctx):
        e = discord.Embed(title = "***__DISCLAIMER!__**", description = "StakesRoyale is not responsible for, and specifically revokes any liability for any direct or consequential loss arising from any information contained within the site. While the information on the site is meticulously reviewed, researched and statistically evaluated, the reader bears all responsibility on their own investments.\n\nAny information found on the StakesRoyale server should not be used as the sole data basis for any single decision. The StakesRoyale server is merely a platform for sports advisory, and any information inscribed within the server by any moderators/analysts is not always one hundred percent accurate.", color = discord.Color.dark_purple())
        e.set_thumbnail(url = "https://i.imgur.com/QKWCNMI.png")
        e.set_footer(text = "Press The ✅ To Agree To The Disclaimer")
        message = await ctx.send(embed=e)
        await message.add_reaction("✅")
        #await ctx.send(f"@everyone Welcome! Please click ✅ to gain access to the server. You will see all our channels on the left.")

        ## (Mammas wanted this added) Please click ✅ to gain access to the server. You will see all our channels on the left. Welcome! @everyone


    #Socials Embed
    @commands.command()
    @has_guild_permissions(administrator=True)
    async def Socials_(self, ctx):
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
        e.add_field(name= "<:logo:940097039608471572>", value = "[Website｜Link](http://stakesroyale.com/)",inline = False)
        e.add_field(name = str("\uFEFF"), value = str("\uFEFF"), inline = False)
        e.set_footer(text = "Do you want somthing here?")
        await ctx.send(embed=e)

    @commands.command()
    @has_guild_permissions(administrator=True)
    async def ComingSoon_(self, ctx):
        chnls = [
            938164154332758036, 
            938262365760282674, 
            938164656739078144, 
            938262963561836555, 
            938164434927513630, 
            938262829402828830, 
            947299260389556244, 
            947299742960992286, 
            947299773675880538
            ]
        e = discord.Embed(title = "\uFEFF ~***__Coming Soon__***~", description = "Not Quite Ready Yet", color = discord.Color.dark_purple())
        e.set_thumbnail(url = THMB)
        for i in chnls:
            channel = self.client.get_channel(i)
            await channel.purge(limit = 2)
            await channel.send(embed=e)
    

def setup(client):
    client.add_cog(_Commands(client))