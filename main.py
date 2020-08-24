import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='p/')

@bot.event
async def on_ready():
   print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
   channel = bot.get_channel(653534069061320714)
   await channel.send(f'@{member} join!') 

@bot.command()
async def ping(ctx):
   await ctx.send(bot.latency)

bot.run('NzM4MzY3MzAzNDg1MjI3MTA4.XyK4Iw.S8_I19ddLmUamFhtoZMy00CDN3c')