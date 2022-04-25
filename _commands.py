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
    async def delete(self, ctx, n_messages = "5"):
        if str(n_messages) == "all":
            n_messages = "999999"
        await ctx.channel.purge(limit = int(n_messages) + 1)

    #Creates a Stakes Royale Disclaimer embed
    @commands.command()
    @has_guild_permissions(administrator=True)
    async def Dis_(self, ctx):
        e = discord.Embed(title = "***__DISCLAIMER!__**", description = "StakesRoyale is not responsible for, and specifically revokes any liability for any direct or consequential loss arising from any information contained within the site. While the information on the site is meticulously reviewed, researched and statistically evaluated, the reader bears all responsibility on their own investments.\n\nAny information found on the StakesRoyale server should not be used as the sole data basis for any single decision. The StakesRoyale server is merely a platform for sports advisory, and any information inscribed within the server by any moderators/analysts is not always one hundred percent accurate.", color = discord.Color.dark_purple())
        e.set_thumbnail(url = "https://i.imgur.com/QKWCNMI.png")
        e.set_footer(text = "Press The ✅ To Agree To The Disclaimer")
        message = await ctx.send(embed=e)
        await message.add_reaction("✅")
        await ctx.send("__**After you ACCEPT the rules, RE-CLICK the check mark to have access to our discord. All channels and chats will be available on the left!**__")
        await ctx.send("Are you interested in a __**FREE TRIAL**__ of our premium service? Well you’re in luck! For our Grand Opening, all members automatically gain the <@&938291133690298389> role and all of its perks. This is a trial run that will end on __**SEPTEMBER 1ST 2022**__")
        ## (Mammas wanted this added) Please click ✅ to gain access to the server. You will see all our channels on the left. Welcome! @everyone

    #Socials Embed
    @commands.command()
    @has_guild_permissions(administrator=True)
    async def Socials_(self, ctx):
        e = discord.Embed(title = "~***__Socials__***~", color = discord.Color.dark_purple())
        e.set_thumbnail(url = THMB)
        e.add_field(name= "<:tiktok:938338392847052810>", value = "[TikTok｜Link](https://www.tiktok.com/@stakesroyale)",inline = False)
        e.add_field(name = str("\uFEFF"), value = str("\uFEFF"), inline = False)
        e.add_field(name= "<:insta:938339028099559424>", value = "[Instagram｜Link](https://www.instagram.com/stakesroyale/)",inline = False)
        e.add_field(name = str("\uFEFF"), value = str("\uFEFF"), inline = False)
        e.add_field(name= "<:twitter:938339492706799647>", value = "[Twitter｜Link](https://twitter.com/StakesRoyale)",inline = False)
        e.add_field(name = str("\uFEFF"), value = str("\uFEFF"), inline = False)
        #e.add_field(name= "<:youtube:938338677015339008>", value = "[Youtube｜Link](https://www.youtube.com/)",inline = False)
        e.add_field(name= "<:facebook:948020824437309490>", value = "[Facebook｜Link](https://www.facebook.com/people/Stakes-Royale/100078375877692/)",inline = False)
        e.add_field(name = str("\uFEFF"), value = str("\uFEFF"), inline = False)
        e.add_field(name= "<:logo:940097039608471572>", value = "[Website｜Link](http://stakesroyale.com/)",inline = False)
        e.add_field(name = str("\uFEFF"), value = str("\uFEFF"), inline = False)
        #e.set_footer(text = "Do you want somthing here?")
        await ctx.send(embed=e)

    #Coming Soon Embed
    @commands.command()
    @has_guild_permissions(administrator=True)
    async def ComingSoon_(self, ctx):
        chnls = [
            938164154332758036, # hoc pr
            938262365760282674, # hoc pl
            938164656739078144, # bskt pr
            938262963561836555, # bskt pl
            938164434927513630, # fb pr
            938262829402828830, # fb pl
            963190850697965568, # base pr
            963191321605058650, # base pl
            947299260389556244, # nhl fan
            947299742960992286, # nba fan
            947299773675880538  # nfl fan
            ]
        e = discord.Embed(title = "\uFEFF ~***__Coming Soon__***~", description = "Not Quite Ready Yet", color = discord.Color.dark_purple())
        e.set_thumbnail(url = THMB)
        for i in chnls:
            channel = self.client.get_channel(i)
            await channel.purge(limit = 2)
            await channel.send(embed=e)

    #Rules Embed
    @commands.command()
    @has_guild_permissions(administrator=True)
    async def Rules_(self, ctx):
        e = discord.Embed(title = "~***__Rules__***~", color = discord.Color.dark_purple())
        e.set_thumbnail(url = THMB)
        e.add_field(name= "1", value = "Be civil and respectful",inline = False)
        e.add_field(name= "2", value = "No racial, derogatory, NSFW, political, religious, or inappropriate content.",inline = False)
        e.add_field(name= "3", value = "You must be of legal age in your jurisdiction to participate in this server. Unlawful online gambling is strictly prohibited. You must adhere to all the laws in your jurisdiction.",inline = False)
        e.add_field(name= "4", value = "Respect all users, moderators, and administrators at all times. Moderator decisions are final.",inline = False)
        e.add_field(name= "5", value = "Advertising other Discord servers, subreddits, handicapping services, illicit bookie services, or anything that could be seen as intrusive or annoying to other users is prohibited. This includes self-advertisement and posting links that may be harmful to other members and their devices....",inline = False)
        e.add_field(name= "6", value = "...In addition, if someone reaches out to you for picks, you may not sell any Telegram or capping service.",inline = False)
        e.add_field(name= "7", value = "Please do not direct message/tag/mention users, teams, moderators, and administrators without a good reason.",inline = False)
        e.add_field(name= "8", value = "Attempting to evade mutes/bans by using an alternative Discord account is not permitted. Impersonating a muted or banned user can result in an instant ban.",inline = False)
        e.add_field(name= "9", value = "No scamming of any nature ESPECIALLY Discord Nitro.",inline = False)
        e.add_field(name= "10", value = "Concerning chats:-    No touting/selling picks/advertising (unless approved by moderators).-    No begging.-    No score trolling.-    Stay on topic especially during live events.-    No spam or self-promotion (This includes DMing fellow members)",inline = False)
        e.add_field(name= "11", value = "Do not violate the contractual, personal, or intellectual property rights of any party.",inline = False)
        e.add_field(name= "12", value = "False information with the intent to deceive others will result in an immediate ban.",inline = False)
        e.add_field(name= "13", value = "Promoting, advertising, or sending non-related server/content will result in disciplinary actions the degree of which is dependent on the content posted.",inline = False)
        e.add_field(name= "14", value = "The creation and/or joining a mimic server is not allowed.",inline = False)
        e.add_field(name= "15", value = "Most important of all, have fun and enjoy the world of sports",inline = False)

        # e.set_footer(text = "Do you want somthing here?")
        await ctx.send(embed=e)

    #Playoff Bundle Embed
    @commands.command()
    @has_guild_permissions(administrator=True)
    async def PBundle_(self, ctx):
        chnls = [
            967977336626630686, # Perks
            967977235485179994  # Purchase Membership
        ]
        e = discord.Embed(title = "~***__Playoff Bundle__***~", description= "For this year's NBA/NHL playoffs, we will be offering a playoff bundle that will be available to buy April 25th. Once you purchase this bundle, you will be granted the <@&967978976389767199> role and you will be receiving:\n\n- Daily Picks for The NHL/NBA Playoffs\n\n- Exclusive Free-Chats for Daily Advice By our Analyst\n\n- Viewing Parties for These Playoff Games\n\nThe price of the Playoff Bundle will be $55.99 USD / onetime payment.\n\nThe price of the Memberships will be $29.99 USD / monthly payment\n\n***NOTE:*** If you purchase this special package, we will be offering ***6 FREE MONTHS*** of our paid memberships starting September 1st. Moreover, you will be receiving a permanent unique role that will be granting you future deals & benefits. ***Memberships will only be available to purchase on September 1st.***\n\n[CLICK HERE TO UPGRADE](https://upgrade.chat/937560982484553728)", color = discord.Color.dark_purple())
        e.set_thumbnail(url = THMB)
        e2 = discord.Embed(title = "~***__Upgrade Now__***~", description= f"Head out to {chnls[0].mention} to check out all of our memberships and its perks! When you're ready to upgrade:\n\n[CLICK HERE TO UPGRADE](https://upgrade.chat/937560982484553728)", color = discord.Color.dark_purple())
        e2.set_thumbnail(url = THMB)
        await self.client.get_channel(chnls[0]).send(embed=e)
        await self.client.get_channel(chnls[1]).send(embed=e2)


    @commands.command()
    async def shutdown(self, ctx):
        if ctx.author.id == MYID:
            await ctx.channel.purge(limit = 1)
            shutdown_embed = discord.Embed(title='Bot Maintenance', description='I am going to sleep so that Yep can work on my brain!', color = discord.Color.dark_purple())
            await ctx.channel.send(embed=shutdown_embed)
            channel = self.client.get_channel(951714836633493525)
            await channel.edit(name = f'Bot Status: Offline 💀')
            await self.client.logout()
        if ctx.author.id != MYID:
            await ctx.channel.purge(limit = 1)
            errorperm_embed = discord.Embed(title='No?', description='This command is `Yepper` only. You are not allowed to use this.', color = discord.Color.dark_purple())
            errorperm_embed.set_footer(text=ctx.author)
            await ctx.channel.send(embed=errorperm_embed, delete_after=10.0)

def setup(client):
    client.add_cog(_Commands(client))
