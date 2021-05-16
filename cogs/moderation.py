import discord
import datetime
import asyncio

from discord.ext import commands


class ModCog(commands.Cog):

	def __init__(self, bot):
		self.bot = bot


	@commands.command()
	@commands.has_permissions(administrator=True)
	async def purge(self, ctx, *, number:int=None):
			if ctx.message.author.guild_permissions.manage_messages:
				try:
					if number is None:
						await ctx.send("please input a number!")
					else:
						deleted = await ctx.message.channel.purge(limit=number)
						await ctx.send(f"Message purged by{ctx.message.author.mention}: `{len(deleted)}`")
				except:
					await ctx.send("I cant Purge here!")				
			else:
				await ctx.send("You do not have Permissions to use this command.")	



	@commands.command()
	@commands.has_permissions(administrator=True)
	async def kick(self, ctx, user: discord.Member, *, reason=None):
		if user.guild_permissions.manage_messages:
			await ctx.send("I cant't kick the user because they are an admin/moderator.")
		elif ctx.message.author.guild_permissions.kick_members:
			if reason is None:
				await ctx.guild.kick(user=user, reason=reason)
				await ctx.send(f"{user} has been kicked for {reason}")
			else:
				await ctx.send("You do not have the permissions to use this command")

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def ban(self, ctx, user: discord.Member, *, reason=None):
		if user.guild_permissions.manage_messages:
			await ctx.send("i can't ban this user because they are an admin/moderator.")
		elif ctx.message.author.guild_permissions.ban_members:
			if reason is None:
				await ctx.guild.ban(user=user, reason=reason)
				await ctx.send(f"{user} has been banned for {reason}")
			else:
				await ctx.send("You do not have the permissions to use this command!")




def setup(bot):
	bot.add_cog(ModCog(bot))
	print('Moderation is loaded')