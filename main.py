import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import datetime
import random
import Nugget
from random import randint
import youtube_dl

from gtts import gTTS
import schedule
import time
import wikipedia
import sys


#INVITE LINK: https://discordapp.com/api/oauth2/authorize?client_id=607761606788644876&permissions=8&scope=bot


client = commands.Bot(command_prefix = '-')

owner_id = 352478596289396737
channel_id = 597492274775195660


@client.event
async def on_ready():
    time = datetime.datetime.now()
    print("Online at {}".format(time))

    acts = client.guilds
    mem = 0

    print("\nServers:")
    for s in acts:
        print(str(s.name))
        
    if str(s.name) == "Discord Bot List":
        return

    for a in acts:
        mem += len(a.members)

    print("\nMembers:", mem)
    
    await client.change_presence(activity=discord.Game(name='-help || Version 2.4'.format(mem)))

client.remove_command("help")

    
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def prefix(ctx):
    await ctx.send("My prefix is -")


@client.command()
async def tts(ctx):
    await voice.tts(ctx, discord, os)



@client.command()
async def shutdowntime(ctx):
    await ctx.send("Scheduled shutdown is at 9:00PM EDT")
  
        
    await ctx.send(content=None, embed=work)
    await Nugget.daily(ctx.author.id, os)

@client.command()
async def nuggets(ctx):
    await Nugget.bal(ctx)

@client.command()
async def terminate(ctx):
    if ctx.author.id == owner_id:
        await ctx.send(":wave:")
        await client.logout()
    else:
        await ctx.send("**HEY!** You do not have permission to use this command")

@client.command()
async def announce(ctx):
    await ctx.send("Scheduled Shutdown In 30 Minutes!")
    await asyncio.sleep(900)
    await ctx.send("Scheduled Shutdown In 15 Minutes!")
    await asyncio.sleep(600)
    await ctx.send("Scheduled Shutdown in 5 Minutes!")
    await asyncio.sleep(180)
    await ctx.send("Scheduled Shutdown in 2 Minutes!")
    await asyncio.sleep(60)
    await ctx.send("Scheduled Shutdown in 3 Seconds!")
    await asyncio.sleep(1)
    await ctx.send("Scheduled Shutdown in 2 Seconds!")
    await asyncio.sleep(1)
    await ctx.send("Scheduled Shutdown in 1 Seconds!")
    await asyncio.sleep(1)
    await ctx.send(":wave:")
    await client.logout()

@client.command()
async def invite(ctx):
    invite = discord.Embed(title="Invite Nugget2.0", description="invite link for Nugget2.0")
    invite.add_field(name="Link", value="https://discordapp.com/api/oauth2/authorize?client_id=607761606788644876&permissions=8&scope=bot", inline=False)
      
    await ctx.send(content=None, embed=invite)

@client.command()
async def help(ctx):
     help = discord.Embed(title="Help", description="You can also open sub-categories like [-helpmusic|-helputiles|-helpcurrency]", colour=discord.Colour.purple())
     help.add_field(name="`PING`", value="Shows client latency in ms.", inline=True)
     help.add_field(name="`MEME`", value="Sends random memes into the specified channel :P", inline=True,)
     help.add_field(name="`INVITE`", value="Sends an invite link for Nugget2.0", inline=True)
     help.add_field(name="`SUMMON`", value="Joins your voice channel", inline=True)
     help.add_field(name="`DISCONNECT`", value="Leaves your voice channel", inline=True)
     help.add_field(name="`PLAY`", value="plays specified song or song link", inline=True)
     help.add_field(name="`PAUSE`", value="Pauses the current song", inline=True)
     help.add_field(name="`resume`", value="resumes playing the current song", inline=True)
     help.add_field(name="`SKIP`", value="skips to the next song in the queue", inline=True)
     help.add_field(name="`QUEUE`", value="shows all songs in the current queue", inline=True)
     help.add_field(name="`CLEAN`", value="cleans up messages send by Nugget2.0", inline=True)
     help.add_field(name="`SHUTDOWNTIME`", value="Shows the scheduled shutdown time", inline=True)
     help.add_field(name="`USER`", value="Sends an embed with information about a user", inline=True)
     help.add_field(name="`SLOTS`", value="Buy a scratch off ticket for $50 each")
     help.add_field(name="`SHOP`", value="buy xp boosters and ohter items with your nuggets", inline=True)
     help.add_field(name="`BUY`", value="Used to buy things from the shop", inline=True)
     help.add_field(name="`BAL`", value="check how many nuggets you have", inline=True)
     help.add_field(name="`BAG`", value="see your current inventory", inline=True)
     help.add_field(name="`ADDFUNDS(admin)`", value="adds 30 nuggets into your account", inline=True)
     help.add_field(name="`LEVEL`", value="check your current xp and level(earn from talking in chat)", inline=True)
     help.add_field(name="`WORK`", value="used to earn nuggets. You can earn more depending on your xp level", inline=True)
     help.add_field(name="`CLEAR`", value="Deletes one page of messages in the channel", inline=True)
     help.add_field(name="`CLEARALL`", value="Deletes multiple pages of messages in the channel", inline=True)
     help.add_field(name="\u200b", value="Type -help to see more information on a command", inline=True)
     help.add_field(name="\u200b", value="You can also type -help (category) to see more information on a category", inline=True)
     help.set_footer(text=f"Requested By: {ctx.author.name}")

     second = discord.Embed(title="HEY!", description="You can also open sub categories like -helpmusic or -helputils", colour=discord.Colour.purple())
     await ctx.send(content=None, embed=help)
     

@client.command()
async def helpmusic(ctx):
    emb = discord.Embed(title=":musical_note: Music Commands", description=None, colour=discord.Colour.purple())
    emb.add_field(name="`Summon`", value="Joins your voice channel", inline=True)
    emb.add_field(name="`disconnect`", value="Leaves your voice channel", inline=True)
    emb.add_field(name="`play`", value="plays specified song or song link", inline=True)
    emb.add_field(name="`pause`", value="Pauses the current song", inline=True)
    emb.add_field(name="`resume`", value="resumes playing the current song", inline=True)
    emb.add_field(name="`skip`", value="skips to the next song in the queue", inline=True)
    emb.add_field(name="`queue`", value="shows all songs in the current queue", inline=True)
    emb.add_field(name="`clear`", value="clears the current queue", inline=True)
    emb.add_field(name="`restart`", value="Having trouble or not working? Try this", inline=True)
    emb.set_footer(text=f"Requested By: {ctx.author.name}")
    await ctx.send(content=None, embed=emb)



@client.command()
async def helputils(ctx):
    util = discord.Embed(title=":gear: Utility Commands", description=None, colour=discord.Colour.purple())
    util.add_field(name="`PING`", value="Make sure Nugget is working and test client latency", inline=True)
    util.add_field(name="`USER`", value="Get detailed information on a specified user", inline=True)
    util.add_field(name="`LEVEL`", value="Check your current level and amount of XP", inline=True)
    util.add_field(name="`ADDFUNDS(admin)`", value="adds 30 nuggets into a specified account", inline=True)
    util.add_field(name="`INVITE`", value="Sends an invite link for Nugget2.0", inline=True)
    util.add_field(name="`RESTART`", value="Having trouble or not working? Try this", inline=True)
    util.set_footer(text=f"Requested By: {ctx.author.name}")
    await ctx.send(content=None, embed=util)


@client.command()
async def helpcurrency(ctx):
    curr = discord.Embed(title=":moneybag: Currency Commands", description=None, colour=discord.Colour.purple())
    curr.add_field(name="`WORK`", value="Work a day job for nuggets - 100N/Hr", inline=True)
    curr.add_field(name="`BAL`", value="Check how much nuggets you have", inline=True)
    curr.add_field(name="`SHOP`", value="Spend your nuggets on stupid shit you will never use XD. Oh come on I know you want to :smirk:", inline=True)
    curr.add_field(name="`BUY`", value="Usage: -buy(number of listing)", inline=True)
    curr.add_field(name="`BAG`", value="Look to see what stuff you got", inline=True)
    await ctx.send(content=None, embed=curr)




@client.command()
async def meme(ctx):
    num = randint(0, 41)
    try:
        await ctx.send(file = discord.File("MEMES/{}.jpg".format(num))) 
    except:
        await ctx.send(file = discord.File("MEMES/{}.png".format(num)))

@client.command()
async def slots(ctx):
    scratch = discord.Embed(title="Spinning...", description="\u200b")
    scratch.add_field(name="|:cherries:|:banana:|:grapes:|:carrot:|", value ="\u200b", inline=False)
    scratch.add_field(name="|:banana:|:carrot:|:cherries:|:grapes:|", value="\u200b", inline=False)
    await ctx.send(content=None, embed=scratch)
    time.sleep(3)
        
    rand = randint(0, 4800)
    if rand < 2000:
        await ctx.send(":slot_machine: YOU WON **{}!!**:slot_machine:".format(rand))
    else:
        await ctx.send(":x: **YOU LOSE**")

@client.command()
async def smack(ctx):
    var = randint(0, 1)
    if var == 1:
        await ctx.send(f"Ouch! {ctx.author.name} smacked a hoe!")
        await ctx.send(file = discord.File("GIF/0.gif"))
    else:
        await ctx.send(f"**DAMN!** {ctx.author.name} clocked a bitch!")
        await ctx.send(file = discord.File("GIF/1.gif"))

@client.command()
async def attack(ctx):
    List = [f"FUCK! {msg.author.name} stepped on a lego! Watch your step buddy.",f"{msg.author.name} swung, but missed and busted their ass"]
    await ctx.send(random.choice(List))



@client.command()
async def detailedon(ctx):
    ctx.send("Enabling detailed view of Wiki searches")
    
@client.command()
async def detailedoff(ctx):
    ctx.send("Disabling detailed view of Wiki searches")





client.run("NjY4OTg4MTI0NTY2NzgxOTg0.XiZTPA.DoQvauT72a2gtO7JulL9hUifmSQ")
