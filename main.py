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
async def ping(ctx)

bot.run('NzM4MzY3MzAzNDg1MjI3MTA4.XyK4Iw.N1r6gm1yqkSpNpgRMfA4zfd4S1Y')