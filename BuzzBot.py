import discord
import json

import Counting as count

token = json.load(open('auth.json', 'r'))['token']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

        await count.double_count(message)

client = MyClient()
client.run(token)