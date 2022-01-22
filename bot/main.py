
import random
import os
import time
import server
import discord
import ctypes
import server
from discord.ext import commands
from cogs.musiccog import Music,Fun

find_opus = ctypes.util.find_library('opus')
discord.opus.load_opus(find_opus)
TOKEN = os.getenv("DISCORD_TOKEN")

# Silence useless bug reports messages


bot = commands.Bot(command_prefix='!')
bot.add_cog(Music(bot))
bot.add_cog(Fun(bot))


@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))
    

server.server()
bot.run(TOKEN)