import os
import nacl
import discord
from discord.ext import commands
my_secret = os.environ['TOKEN']

bot = commands.Bot(command_prefix='n!')

@bot.event
async def on_ready():
    print(f'Logado como {bot.user}')

cogs = []
for i in range(len(cogs)):
  cogs[i].setup(bot)

bot.run(my_secret)