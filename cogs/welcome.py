import discord
import asyncio 
import datetime
from discord.ext import commands

colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]



class WelcomeCog(commands.Cog):

	def __init__(self, bot):
		self.bot = bot


	@commands.Cog.listener()
	async def on_member_join(self, member):
		channel = discord.utils.get(member.guild.text_channels, name='welcome')
		if channel:
			embed = discord.Embed(description='Welcome to our Discord Server!')
			embed.set_thumbnail(url=member.avatar_url)
			embed.set_author(name=member.name, icon_url=member.avatar_url)
			embed.set_footer(text=member.guild, icon_url=member.guild.icon_url)
			embed.timestamp = datetime.datetime.utcnow()

			await channel.send(embed=embed)
		
def setup(bot):
	bot.add_cog(WelcomeCog(bot))