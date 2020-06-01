import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '-')

@client.command()
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount)

client.run("NjA3NzYxNjA2Nzg4NjQ0ODc2.XUeYOQ.bCLYLYdrONpYpSULd8M_flnISeE")
