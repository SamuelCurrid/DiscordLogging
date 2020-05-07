# TODO: Implementation
# IDEA: Track which invite a user joined off of

import discord
import json
import os
from datetime import datetime
from discord.ext import commands


class Logging(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.embed = discord.Embed()
		self.logs = None

	async def update_guilds(self):
		savedGuilds = []
		for guildID in self.logs:
			savedGuilds.append(guildID)

		guilds = []
		for guild in self.bot.guilds:
			guilds.append(str(guild.id))

		addGuilds = [x for x in guilds if x not in savedGuilds]
		removeGuilds = [x for x in savedGuilds if x not in guilds]

		# Add new guilds
		for guildID in addGuilds:
			self.logs[str(guildID)] = {"channel": None}

		# Remove disconnected guilds
		for guildID in removeGuilds:
			self.logs.pop(str(guildID))

		await self.update_state()

	@commands.Cog.listener()
	async def on_ready(self):
		print("Loading logging cog...")

		await self.load_state()
		await self.update_guilds()

		print("Logging cog loaded")

	@commands.command(pass_context=True, name="logging")
	async def change_logging(self, ctx):
		if ctx.message.author.guild_permissions.administrator:
			for channel in ctx.message.channel_mentions:
				if self.logs[str(ctx.message.guild.id)]["channel"] != int(channel.id):
					self.logs[str(ctx.message.guild.id)]["channel"] = int(channel.id)

					print("Updating guild " + str(ctx.message.guild.id) + " to use logging channel " + str(channel.id))

					await self.update_state()
					print("Finished updating logging channel")

	async def load_state(self):
		with open(os.path.join("config", "logging.json"), "r+") as loggingFile:
			logs = loggingFile.read()
			self.logs = json.loads(logs)

	async def update_state(self):
		with open(os.path.join("config", "logging.json"), "r+") as loggingFile:
			loggingFile.truncate(0)
			loggingFile.seek(0)
			json.dump(self.logs, loggingFile, indent=4)

	@commands.Cog.listener()
	async def on_message_delete(self, message):
		"""
		Sends a logging message containing
		author, location (channel and placement), content, and time of the deleted message
		:param message:
		:return:
		"""
		if not message.author.bot:
			if self.logs[str(message.guild.id)]["channel"] is not None:
				loggingChannel = message.guild.get_channel(int(self.logs[str(message.guild.id)]["channel"]))
				channel = message.channel

				self.embed = discord.Embed()
				self.embed.colour = discord.Colour(0xbe4041)
				self.embed.set_author(name=message.author.name + "#" + message.author.discriminator, icon_url=message.author.avatar_url)
				self.embed.title = "Message deleted in " + "#" + channel.name
				self.embed.description = message.content
				self.embed.set_footer(text="ID: " + str(message.author.id))
				self.embed.timestamp = datetime.utcnow()

				await loggingChannel.send(embed=self.embed)

	@commands.Cog.listener()
	async def on_raw_message_delete(self, payload):
		"""
		Sends a logging message containing
		location (channel), and ID of the message deleted
		:param payload:
		:return:
		"""
		guild = self.bot.get_guild(payload.guild_id)

		if self.logs[str(guild.id)]["channel"] is not None and payload.cached_message is None:

			loggingChannel = guild.get_channel(int(self.logs[str(guild.id)]["channel"]))
			channel = guild.get_channel(payload.channel_id)

			self.embed = discord.Embed()
			self.embed.colour = discord.Colour(0xbe4041)
			self.embed.title = "Message deleted in " + "#" + channel.name
			self.embed.set_footer(text="Uncached message")
			self.embed.timestamp = datetime.utcnow()

			await loggingChannel.send(embed=self.embed)

	@commands.Cog.listener()
	async def on_raw_bulk_message_delete(self, payload):
		"""
		Sends a logging message containing
		author, location (channel and placement), content, and time of the deleted messages
		May be limited if message is not in the cache
		:param payload:
		:return:
		"""
		guild = self.bot.get_guild(payload.guild_id)

		if self.logs[str(guild.id)]["channel"] is not None:

			loggingChannel = guild.get_channel(int(self.logs[str(guild.id)]["channel"]))
			channel = guild.get_channel(payload.channel_id)
			content = ""

			for message in payload.cached_messages:
				content += "[" + message.author.name + "#" + message.author.discriminator + "]: " + message.content + "\n"

			self.embed = discord.Embed()
			self.embed.colour = discord.Colour(0xbe4041)
			self.embed.title = "Messages bulk deleted in " + "#" + channel.name
			self.embed.description = content
			self.embed.timestamp = datetime.utcnow()

			await loggingChannel.send(embed=self.embed)

	@commands.Cog.listener()
	async def on_message_edit(self, before, after):
		"""
		Sends a logging message containing
		the content of the message before and after the edit
		:param before:
		:param after:
		:return:
		"""
		if not before.author.bot:
			if self.logs[str(before.guild.id)]["channel"] is not None:
				loggingChannel = before.guild.get_channel(int(self.logs[str(before.guild.id)]["channel"]))
				channel = before.channel

				self.embed = discord.Embed()
				self.embed.colour = discord.Colour(0x8899d4)
				self.embed.set_author(name=before.author.name + "#" + before.author.discriminator, icon_url=before.author.avatar_url)
				self.embed.title = "Message edited in " + "#" + channel.name
				self.embed.description = "**Before:** " + before.content + "\n**+After:** " + after.content
				self.embed.set_footer(text="ID: " + str(before.author.id))
				self.embed.timestamp = datetime.utcnow()

				await loggingChannel.send(embed=self.embed)



	@commands.Cog.listener()
	async def on_raw_message_edit(self, payload):
		"""
		Sends a logging message containing
		the content of the message after the edit
		:param payload:
		:return:
		"""
		# FIXME: Cannot get guild from payload
		# guild = self.bot.get_guild(payload.guild_id)
		#
		# if self.logs[str(guild.id)]["channel"] is not None and payload.cached_message is None:
		# 	loggingChannel = guild.get_channel(int(self.logs[str(guild.id)]["channel"]))
		# 	channel = guild.get_channel(payload.channel_id)
		# 	message = channel.fetch_message(payload.message_id)
		#
		# 	self.embed = discord.Embed()
		# 	self.embed.colour = discord.Colour(0x8899d4)
		# 	self.embed.set_author(name=message.author.name + "#" + message.author.discriminator, icon_url=message.author.avatar_url)
		# 	self.embed.title = "Message edited in " + "#" + channel.name
		# 	self.embed.description = "\n**+After:** " + message.content
		# 	self.embed.set_footer(text="ID: " + str(message.author.id))
		# 	self.embed.timestamp = datetime.utcnow()
		#
		# 	await loggingChannel.send(embed=self.embed)

	@commands.Cog.listener()
	async def on_guild_channel_create(self, channel):
		"""
		Sends a logging message containing
		the name, category, and permissions of the channel
		:param channel:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_guild_channel_delete(self, channel):
		"""
		Sends a logging message containing
		the name and category of the channel
		:param channel:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_guild_channel_update(self, before, after):
		"""
		Sends a logging message containing
		the updated properties of the channel
		:param before:
		:param after:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_guild_channel_pins_update(self, channel, last_pin):
		"""
		Sends a logging message containing
		the name of the channel, the content of the pinned message, and a link to the message
		:param channel:
		:param last_pin:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_guild_integrations_update(self, guild):
		"""
		WTF are guild integrations???
		:param guild:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_webhooks_update(self, channel):
		"""
		WTF are webhooks???
		:param channel:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_member_join(self, member):
		"""
		Sends a logging message containing
		the name, avatar, id, join position, account age
		:param member:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		"""
		Sends a logging message containing
		the name, avatar, id, time spent on the server
		:param member:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_member_update(self, before, after):
		"""
		Sends a logging message containing
		the property of the member updated before and after
		:param before:
		:param after:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_user_update(self, before, after):
		"""
		Sends a logging message containing
		the property of the user updated before and after
		:param before:
		:param after:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_guild_update(self, before, after):
		"""
		Sends a logging message containing
		the property of the guild updated before and after
		:param before:
		:param after:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_guild_role_create(self, role):
		"""
		Sends a logging message containing
		the id, name, color, mentionable, and hoisted properties of the role
		:param role:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_guild_role_delete(self, role):
		"""
		Sends a logging message containing
		the id, name, color, mentionable, and hoisted properties of the role
		:param role:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_guild_role_update(self, before, after):
		"""
		Sends a logging message containing
		the property of the role updated before and after
		:param before:
		:param after:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_guild_emojis_update(self, guild, before, after):
		"""
		Sends a logging message containing
		the id, name, and picture of the emoji
		:param guild:
		:param before:
		:param after:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_voice_state_update(self, member, before, after):
		"""
		Sends a logging message containing
		the id, name, and updated voice properties of the member
		:param member:
		:param before:
		:param after:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_member_ban(self, guild, user):
		"""
		Sends a logging message containing
		the id, name, and join date of the member
		:param guild:
		:param user:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_member_unban(self, guild, user):
		"""
		Sends a logging message containing
		the id and name of the member
		:param guild:
		:param user:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_invite_create(self, invite):
		"""
		Sends a logging message containing
		the invite code, inviter name, inviter id, expiration time
		:param invite:
		:return:
		"""

		return

	@commands.Cog.listener()
	async def on_invite_delete(self, invite):
		"""
		Sends a logging message containing
		the invite code, inviter name, and expiration time
		:param invite:
		:return:
		"""
		return
