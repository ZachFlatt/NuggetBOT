import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import datetime
import random
from random import randint
import wikipedia


client = commands.Bot(command_prefix = '-')

owner_id = 352478596289396737
channel_id = 597492274775195660

client.remove_command("help")

@client.event
async def on_ready():
    time = datetime.datetime.now()
    print("Wiki Search online at {}".format(time))

def wiki_summary(arg):

    definition = wikipedia.summary(arg, sentences=3, chars=1000, 
    auto_suggest=True, redirect=True)
    return definition

@client.event
async def on_message(message):
        words = message.content.split()
        important_words = words[1:]
            
        if message.content.startswith('-define'):
                words = message.content.split()
                important_words = words[1:]
                search = discord.Embed(title='Searching...', description=wiki_summary(important_words), colour=discord.Colour.purple())
                await message.channel.send(content=None, embed=search)
                #await message.channel.send(wiki_summary(important_words))

client.run("NjY4OTg4MTI0NTY2NzgxOTg0.XiZTPA.DoQvauT72a2gtO7JulL9hUifmSQ")
