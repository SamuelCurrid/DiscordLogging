import discord
from discord.ext import commands

gompei = commands.Bot(command_prefix=".")

@gompei.event
async def on_ready():
	"""
	Load state and update information since last run
	"""
	print("Logged on as {0}".format(gompei.user))

gompei.run("Njc0NjU2NTI5MzI4MzczNzcw.XoO-nA.rD0TxN2fI9kSTf1IinKD-NG6BHs")