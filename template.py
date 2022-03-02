from mmap import ACCESS_COPY
import discord
import asyncio
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
from templateIMPORT import *

class Template(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_role("Analyst")
    async def prevcall(self, ctx, password, *,template : literal_eval):
        ## Analyst Calls Sender PREVIEW
        await ctx.channel.purge(limit = 1)
        SPORT = "Preview"
        if password == PASSWORD:
            if templateCheck(template):
                if templateMK(SPORT, template) != None:
                    log(ctx.message.author) 
                    e = templateMK(SPORT, template) 
                    await ctx.send(embed = e)
                    await asyncio.sleep(10)
                    await ctx.channel.purge(limit = 1)
                elif templateMK(SPORT, template) == None:
                    await ctx.send("ERROR CHECK BET TYPE")
            elif not templateCheck(template):
                await ctx.send("ERROR CHECK TEMPLATE")
        elif password != PASSWORD:
            await ctx.send("ERROR CHECK PASSWORD")


    @commands.command()
    @commands.has_role("Analyst")
    async def footcall(self, ctx, password, *,template : literal_eval):
        ## Analyst Calls Sender for Football
        await ctx.channel.purge(limit = 1)
        CHANNEL = 938164270296870922
        SPORT = "Football"
        #Player props exception
        if template["bet_type"] == "PROPS":
            CHANNEL = 938164342535372802
        if password == PASSWORD:
            if templateCheck(template):
                if templateMK(SPORT, template) != None:
                    log(ctx.message.author) 
                    channel = self.client.get_channel(CHANNEL)
                    e = templateMK(SPORT, template)
                    await channel.send("<@&938291133690298389>")
                    await channel.send(embed = e)
                elif templateMK(SPORT, template) == None:
                    await ctx.send("ERROR CHECK BET TYPE")
            elif not templateCheck(template):
                await ctx.send("ERROR CHECK TEMPLATE")
        elif password != PASSWORD:
            await ctx.send("ERROR CHECK PASSWORD")

    @commands.command()
    @commands.has_role("Analyst")
    async def nhlcall(self, ctx, password, *,template : literal_eval):
        ## Analyst Calls Sender for Hockey
        await ctx.channel.purge(limit = 1)
        CHANNEL = 938163989756649592
        SPORT = "Hockey"
        #Player props exception
        if template["bet_type"] == "PROPS":
            CHANNEL = 938164064591437854
        if password == PASSWORD:
            if templateCheck(template):
                if templateMK(SPORT, template) != None:
                    log(ctx.message.author) 
                    channel = self.client.get_channel(CHANNEL)
                    e = templateMK(SPORT, template)
                    await channel.send("<@&938291133690298389>") 
                    await channel.send(embed = e)
                elif templateMK(SPORT, template) == None:
                    await ctx.send("ERROR CHECK BET TYPE")
            elif not templateCheck(template):
                await ctx.send("ERROR CHECK TEMPLATE")
        elif password != PASSWORD:
            await ctx.send("ERROR CHECK PASSWORD")

    @commands.command()
    @commands.has_role("Analyst")
    async def basketcall(self, ctx, password, *,template : literal_eval):
        ## Analyst Calls Sender for Basketball
        await ctx.channel.purge(limit = 1)
        CHANNEL = 938164524798857256
        SPORT = "Basketball"
        #Player props exception
        if template["bet_type"] == "PROPS":
            CHANNEL = 938164584714489886
        if password == PASSWORD:
            if templateCheck(template):
                if templateMK(SPORT, template) != None:
                    log(ctx.message.author) 
                    channel = self.client.get_channel(CHANNEL)
                    e = templateMK(SPORT, template)
                    await channel.send("<@&938291133690298389>") 
                    await channel.send(embed = e)
                elif templateMK(SPORT, template) == None:
                    await ctx.send("ERROR CHECK BET TYPE")
            elif not templateCheck(template):
                await ctx.send("ERROR CHECK TEMPLATE")
        elif password != PASSWORD:
            await ctx.send("ERROR CHECK PASSWORD")

    ###
    ##
    #
    #Results COMMAND
    #
    ##
    ###
    @commands.command()
    @commands.has_role("Analyst")
    async def results(self, ctx, sport, password, *,template : literal_eval):
        ## Analyst Calls Sender for Football
        await ctx.channel.purge(limit = 1)
        CHANNEL = 937562590534582303
        SPORT = sport
        #Player props exception
        if password == PASSWORD:
            if templateCheck(template):
                if templateMK(SPORT, template) != None:
                    log(ctx.message.author) 
                    channel = self.client.get_channel(CHANNEL)
                    e = templateMK(SPORT, template)
                    await channel.send("<@&938291133690298389>") 
                    await channel.send(embed = e)
                elif templateMK(SPORT, template) == None:
                    await ctx.send("ERROR CHECK BET TYPE")
            elif not templateCheck(template):
                await ctx.send("ERROR CHECK TEMPLATE")
        elif password != PASSWORD:
            await ctx.send("ERROR CHECK PASSWORD")



    # whodat= {"fields" : 5, 
    # "bet_type" : "PROPS",
    #  "name0" : "Brad Marchand 2.5 Shots On Goal",
    #  "body0" : "✅OVER✅",
    #  "name1" : "Jacob Markstrom 27.5 Goalie Saves",
    #  "body1" : "✅UNDER✅",
    #  "name2" : "Philipp Grubauer 28.5 Goalie Saves",
    #  "body2" : "✅OVER✅",
    #  "name3" : "Mathew Barzal 2.5 Shots On Goal",
    #  "body3" : "✅OVER✅",
    #  "name4" : "Elias Lindholm 2.5 Shots On Goal",
    #  "body4" : "✅OVER✅",
    #  "name5" : "Results",
    #  "body5" : "5/5 —> 100%, x10 Via Prizepicks.com"}
    @commands.command()
    @commands.has_role("Analyst")
    async def recap(self, ctx, password, *,template : literal_eval):
        """
    {"fields" : 6, 
    "body0" : None,
    "body1" : None,
    "body2" : None,
    "body3" : None,
    "body4" : None,
    "body5" : None,
    "body6" : None}

        """
        ## Analyst Calls Sender for Football
        await ctx.channel.purge(limit = 1)
        CHANNEL = 946535729146781727
        TYPE = "***__~WEEKLY RECAP~__***"
        #Player props exception
        if password == PASSWORD:
            if templateCheckWK(template):
                log(ctx.message.author) 
                channel = self.client.get_channel(CHANNEL)
                e = weeklyMK(template, TYPE)
                await channel.send("<@&938291133690298389>") 
                await channel.send(embed = e)
            elif not templateCheckWK(template):
                await ctx.send("ERROR CHECK TEMPLATE")
        elif password != PASSWORD:
            await ctx.send("ERROR CHECK PASSWORD")


    @commands.command()
    @commands.has_role("Analyst")
    async def schedule(self, ctx, password, *,template : literal_eval):
        """
    {"fields" : 6, 
    "body0" : None,
    "body1" : None,
    "body2" : None,
    "body3" : None,
    "body4" : None,
    "body5" : None,
    "body6" : None}

        """
        ## Analyst Calls Sender for Football
        await ctx.channel.purge(limit = 1)
        CHANNEL = 945879710783643748
        TYPE = "***__~SCHEDULE~__***"
        #Player props exception
        if password == PASSWORD:
            if templateCheckWK(template):
                log(ctx.message.author) 
                channel = self.client.get_channel(CHANNEL)
                e = weeklyMK(template, TYPE)
                await channel.send("<@&938291133690298389>") 
                await channel.send(embed = e)
            elif not templateCheckWK(template):
                await ctx.send("ERROR CHECK TEMPLATE")
        elif password != PASSWORD:
            await ctx.send("ERROR CHECK PASSWORD")

    @commands.command()
    @commands.has_role("Analyst")
    async def winrate(self, ctx, password, *,template : literal_eval):
        """
    {"fields" : 2, 
    "body0" : None,
    "body1" : None,
    "body2" : None}

        """
        ## Analyst Calls Sender for Football
        await ctx.channel.purge(limit = 1)
        CHANNEL = 937931739089731595
        #Player props exception
        if password == PASSWORD:
            if templateCheckWK(template):
                log(ctx.message.author) 
                channel = self.client.get_channel(CHANNEL)
                e = winrateMK(template)
                await channel.send("<@&938291133690298389>") 
                await channel.send(embed = e)
            elif not templateCheckWK(template):
                await ctx.send("ERROR CHECK TEMPLATE")
        elif password != PASSWORD:
            await ctx.send("ERROR CHECK PASSWORD")

    @commands.command()
    @has_guild_permissions(administrator=True)
    async def test(self, ctx):
        await ctx.send("<@&938291133690298389>")


def setup(client):
    client.add_cog(Template(client))