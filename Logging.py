# TODO: Implementation
# IDEA: Track which invite a user joined off of

import discord
from discord.ext import commands

class Logging(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message_delete(self, message):
		"""
		Sends a logging message containing
		author, location (channel and placement), content, and time of the deleted message
		:param message:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_raw_message_delete(self, payload):
		"""
		Sends a logging message containing
		location (channel), and ID of the message deleted
		:param payload:
		:return:
		"""
		# Remember to only send this message if there is no cached message
		return

	@commands.Cog.listener()
	async def on_raw_bulk_message_delete(self, payload):
		"""
		Sends a logging message containing
		author, location (channel and placement), content, and time of the deleted messages
		May be limited if message is not in the cache
		:param payload:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_message_edit(self, before, after):
		"""
		Sends a logging message containing
		the content of the message before and after the edit
		:param before:
		:param after:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_raw_message_edit(self, payload):
		"""
		Sends a logging message containing
		the content of the message after the edit
		:param payload:
		:return:
		"""
		# Remember to only send this message if there is no cached message
		return

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
