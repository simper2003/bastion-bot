import discord
import os
import random
import asyncio
import json
import time


from discord.ext import commands
from keep_alive import keep_alive
from discord.ext.commands import Bot


bot = discord.Client()

intents = discord.Intents(messages=True)

bot = commands.Bot(command_prefix = "/b ", intents = intents)



responses = ["hello there", "hi i am here for you", "What can i do for you?", "Type `/b_help` for more information!"]




@bot.command(aliases=["DFC"])
async def dfc(ctx):

	await ctx.send('https://tenor.com/view/dies-of-cringe-cringe-gif-20747133')





@bot.command(aliases=["logchannel, setlog"])
async def set_log(ctx, *args: discord.TextChannel):
    with open("configschannels.json", "r") as f:
        channels = json.load(f)
    channel = channels.get(str(ctx.guild.id), ctx.channel.id)
    if len(args) == 0:
        await ctx.send("Which channel should I set the logs? :thinking:")
    elif args[0] != discord.TextChannel:
        await ctx.send("That is not a valid channel!")
    elif args[0] == discord.TextChannel:
        with open("configs/channels.json", "w") as f:
            json.dump(channels, f, indent=4)
        embed = discord.Embed(title="Log channel set! :white_check_mark:",
                              description=f"**{channel}** has been set as logs channel!",
                              color=0x2f3136)
        await ctx.send(embed=embed)




@bot.event
async def on_member_join(member):
    with open('guilds.json', 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)

    channel_id = guilds_dict[str(member.guild.id)]
    await bot.get_channel(int(channel_id)).send(f'{member.mention} welcome to the Otay! Support server! Enjoy your stay!🎉')


@bot.command()
async def set_welcome_channel(ctx, channel: discord.TextChannel):
    with open('guilds.json', 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)

    guilds_dict[str(ctx.guild.id)] = str(channel.id)
    with open('guilds.json', 'w', encoding='utf-8') as f:
        json.dump(guilds_dict, f, indent=4, ensure_ascii=False)
    
    await ctx.send(f'Sent welcome channel for {ctx.message.guild.name} to {channel.name}')


# Optional:
# So if your bot leaves a guild, the guild is removed from the dict
@bot.event
async def on_guild_remove(guild):
    with open('guilds.json', 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)

    guilds_dict.pop(guild.id)
    with open('guilds.json', 'w', encoding='utf-8') as f:
        json.dump(guilds_dict, f, indent=4, ensure_ascii=False)


@bot.command()
async def pingtest(ctx):
    await ctx.send('ping test {0}'.format(round(bot.latency, 1)))



@bot.command(pass_context=True)
async def priest(ctx):
    moreoma = ctx.author.id
    message = await ctx.send("So you think you can be a priest,  oke do u beleave in god then?")

    emojis = ['✅', '❌']

    # Adds reaction to above message
    for emoji in (emojis):
        await message.add_reaction(emoji)

    def check(reaction, user):
        reacted = reaction.emoji
        return user.id == moreoma and str(reaction.emoji) in emojis

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=1, check=check)
    except asyncio.TimeoutError:
        await ctx.send("there is a time out dude just w8, you can't be a priest over and over again m8")
    else:
        if reaction.emoji ==  '✅':
            await ctx.send("alr i see you beleave, your now in the priest team!")
        elif reaction.emoji == '❌':
            await ctx.send("WOW you dont beleave? get out of my way!")

        
@bot.command()
async def slowmode(ctx, time:int):
	if (not ctx.author.guild_permissions.manage_messages):
		await ctx.send("This command requires ``Manage Messages`")
		return
	try:
		if time == 0:
			await ctx.send("Slowmode Off")
			await ctx.channel.edit(slowmode_delay = 0)
		elif time > 21600:
			await ctx.send("You can not set the slowmode above 6 hours")
			return
		else:
			await ctx.channel.edit(slowmode_delay = time)
			embed = discord.Embed(Tilte='Slowmode', description=f'slowmode set to {time}!')
			await ctx.send(embed=embed)
	except Exception:
		await print("oops!")




@bot.command(pass_context=True,aliases=['help imge','Help Image','Help image'])
async def image(ctx):
    embed = discord.Embed(
        title =None,#'🔹 Thanks for using my bot',url="http://wq.lt/UwBrZ",
        description = "➺ This bot is currently in beta. More commands will be added soon.",
        colour = 0x0af78a
    )

    embed.set_author(name='Fun commands',icon_url='https://cdn.discordapp.com/attachments/824378832206430209/843284078634860554/basterion.jpg')
    embed.set_footer(text="Bot still in beta and more commands are being added")
    embed.set_image(url='')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/824378832206430209/843291309916815390/sicter_nicker.jpeg')
    embed.add_field(name= "═─────────────────═", value='`/b`wanted\n`/b`rip\n`/b`roblox\n`/b`youtube\n`/b`vr\n`/b`jail\n`/b`floor\n`/b`spongebob\n`/b`fortnite\n`/b`unicorn\n`/b`deepfry\n`/b`ipad.', inline=False)
    await ctx.send(embed=embed)


@bot.command(pass_context=True,aliases=['help mod','Help Mod','Help mod'])
async def moderation(ctx):
    embed = discord.Embed(
        title =None,#'🔹 Thanks for using my bot',url="http://wq.lt/UwBrZ",
        description = "➺ This bot is currently in beta. More commands will be added soon.",
        colour = 0x0af78a
    )

    embed.set_author(name='Fun commands',icon_url='https://cdn.discordapp.com/attachments/824378832206430209/843284078634860554/basterion.jpg')
    embed.set_footer(text="Bot still in beta and more commands are being added")
    embed.set_image(url='')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/824378832206430209/843291309916815390/sicter_nicker.jpeg')
    embed.add_field(name= "═─────────────────═", value='`/b`new\n`/b`modmail\n`/b`kick\n`/b`ban\n`/b`warn\n`/b`mute\n`/b`unmute\n`/b`tempmute\n`/b`clear\n`/b`startg {upgraded giveaway}\n`/b`lock\n`/b`unlock\n`/b`setdelay\n`/b`dm\n`/b`giff{category}`.', inline=False)
    await ctx.send(embed=embed)

@bot.command(pass_context=True,aliases=['help fun','Help Fun','Help fun'])
async def fun(ctx):
    embed = discord.Embed(
        title =None,#'🔹 Thanks for using my bot',url="http://wq.lt/UwBrZ",
        description = "➺ This bot is currently in beta. More commands will be added soon.",
        colour = 0x0af78a
    )

    embed.set_author(name='Fun commands',icon_url='https://cdn.discordapp.com/attachments/824378832206430209/843284078634860554/basterion.jpg')
    embed.set_footer(text="Bot still in beta and more commands are being added")
    embed.set_image(url='')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/824378832206430209/843291309916815390/sicter_nicker.jpeg')
    embed.add_field(name= "═─────────────────═", value='`/b`8ball\n`/b`meme\n`/b`userinfo\n`/b`serverinfo\n`/b`imitate\n`/b`coinflip\n`/b`reminder\n`/b`Poll\n`/b`avatar\n`/b`Howgay\n`/b`chatbot\n`/b`guess\n`/b`beg\n`/b`pet\n`/b`hate\n`/b`quote\n`/b`Bug', inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def _help(ctx):
	embed=discord.Embed(title="Help!", description="click [here](https://discord.gg/293mD5Dn) for more support", color=0x109319)

	# Add author, thumbnail, fields, and footer to the embed


	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/824378832206430209/843284078634860554/basterion.jpg")

	embed.add_field(name=":hammer:`Moderation`", value="14 moderation commands.", inline=True) 
	embed.add_field(name=":smile:`Fun`", value="12 moderation commands.", inline=True)
	embed.add_field(name=":camera:`Image`", value="12 moderation commands.", inline=True)

	embed.set_footer(text='join the discord for more support')

	await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def create_emb(ctx):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    await ctx.send('Waiting for a title')
    title = await bot.wait_for('message', check=check)
  
    await ctx.send('Waiting for a description')
    desc = await bot.wait_for('message', check=check)

	

    embed = discord.Embed(title=title.content, description=desc.content, color=0x72d345)
    await ctx.send(embed=embed)




@bot.event
async def on_ready():
	
	await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('Bastion | !help'))


@bot.event
async def on_ready():
	print("The bot is ready")


for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')


@bot.event
async def on_message(message):
    if message.author.bot: return
    if message.content.lower() == "bastion":
        await message.channel.send(random.choice(responses))
    await bot.process_commands(message)



keep_alive()
bot.run("ODM4MDM1NTMyMTM0NzQ0MTM0.YI1PaA.9-RtpqaoE0jeOm7IbzwUwJW2oHY")