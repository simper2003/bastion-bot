import discord
from discord.ext import commands
import asyncio

emojis = ["\u2705", "\U0001F6AB", "\u274C"]


class Bug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bug(self, ctx, desc=None, rep=None):
        await ctx.channel.purge(limit=1)
        user = ctx.author
        await ctx.author.send('```Please explain the bug```')
        responseDesc = await self.client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
        description = responseDesc.content
        await ctx.author.send('```Please provide pictures/videos of this bug```')
        responseRep = await self.client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
        replicate = responseRep.content
        await ctx.author.send('Your bug report has been sent.')
        embed = discord.Embed(title='Bug Report', color=0x00ff00)
        embed.add_field(name='Description',
                        value=description, inline=False)
        embed.add_field(name='Replicate', value=replicate, inline=True)
        embed.add_field(name='Reported By', value=user, inline=True)
        adminBug = self.client.get_channel(822129196612059137)
        message = await adminBug.send(embed=embed)
        for emoji in emojis:
            await message.add_reaction(emoji)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        reaction_message = reaction.message
        message = await reaction_message.channel.fetch_message(reaction_message.id)
        my_embed = message.embeds[0]
        emoji = reaction.emoji

        if user.bot:
            return

        if emoji == "\u2705":
            fixed_channel = self.client.get_channel(840623430725271580)
            await fixed_channel.send(embed=my_embed)
        elif emoji == "\U0001F6AB":
            notBug = self.client.get_channel(840623612301017098)
            await notBug.send(embed=my_embed)
        elif emoji == "\u274C":
            notFixed = self.client.get_channel(840623640625807380)
            await notFixed.send(embed=my_embed)
        else:
            return




def setup(bot):
    bot.add_cog(Bug(bot))