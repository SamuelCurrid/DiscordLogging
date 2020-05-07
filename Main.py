import discord
import json
import os
from discord.ext import commands

from Logging import Logging

gompei = commands.Bot(command_prefix=".")
gompei.add_cog(Logging(gompei))

@gompei.event
async def on_ready():
	"""
	Load state and update information since last run
	"""
	print("Logged on as {0}".format(gompei.user))

gompei.run(json.load(open(os.path.join("config", "tokens.json")))["token"])