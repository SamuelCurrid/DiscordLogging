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
		the name, 
		:param member:
		:return:
		"""
		return

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		return

	@commands.Cog.listener()
	async def on_member_update(self, before, after):
		return

	@commands.Cog.listener()
	async def on_user_update(self, before, after):
		return

	@commands.Cog.listener()
	async def on_guild_update(self, before, after):
		return

	@commands.Cog.listener()
	async def on_guild_role_create(self, role):
		return

	@commands.Cog.listener()
	async def on_guild_role_delete(self, role):
		return

	@commands.Cog.listener()
	async def on_guild_role_update(self, before, after):
		return

	@commands.Cog.listener()
	async def on_guild_emojis_update(self, guild, before, after):
		return

	@commands.Cog.listener()
	async def on_voice_state_update(self, member, before, after):
		return

	@commands.Cog.listener()
	async def on_member_ban(self, guild, user):
		return

	@commands.Cog.listener()
	async def on_member_unban(self, guild, user):
		return

	@commands.Cog.listener()
	async def on_invite_create(self, invite):
		return

	@commands.Cog.listener()
	async def on_invite_delete(self, invite):
		return

	@commands.Cog.listener()
	async def on_group_join(self, channel, user):
		return
