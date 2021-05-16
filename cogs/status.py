import discord
from discord.ext import commands, tasks
import datetime, time
import asyncio
import random
from itertools import cycle



class Status(commands.Cog):


    def __init__(self, client, *args, **kwargs):
        self.client = client
        client.uptime = datetime.datetime.utcnow()


    @tasks.loop(seconds=12)
    async def change_status(self):
        statuses = cycle([f"on {len(self.client.guilds)} Guilds | /b_help", "v2.0 | /bhelp | /binv", "Invite Me! | /binv", "Help! | /b_help"])

        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=next(statuses)))

    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()

        print("Mystify is Online!")

def setup(client):
    client.add_cog(Status(client))
    print('[+] Status Event Loaded!')