import discord
from discord.ext import commands
import requests

class FunCog(commands.Cog):

	def __init__(self, bot):
		self.bot = bot  

	@commands.command()
	async def minecraft(self, ctx, arg):
		r = requests.get('https://api.minehut.com/server/' + arg + '?byName=true')
		json_data = r.json()

		description = json_data["server"]["motd"]
		online = str(json_data["server"]["online"])
		playerCount = str(json_data["server"]["playerCount"])

		embed = discord.Embed(
			title=arg + " Server Info",
			description='Description: ' + description + '\nOnline: ' + online + '\nPlayers: ' + playerCount,
			color=discord.Color.dark_green()
		)
		embed.set_thumbnail(url="https://i1.wp.com/www.craftycreations.net/wp-content/uploads/2019/08/Grass-Block-e1566147655539.png?fit=500%2C500&ssl=1")

		await ctx.send(embed=embed)





	
def setup(bot):
	bot.add_cog(FunCog(bot))

