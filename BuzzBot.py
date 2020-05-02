import discord
import json
import Counting as count
import Events as event
import updateUsers

# auth token from auth.json
token = json.load(open('auth.json', 'r'))['token']


class MyClient(discord.Client):
    async def on_ready(self):
        print("buzz-bot is on")
        # await updateUsers.first_time(self)

    async def on_member_join(self,member):
        await updateUsers.new_member(member)
    
    async def on_member_remove(self, member):
        await updateUsers.remove_member(member)

    async def on_message(self, message):
        await count.counting(message)

        if (message.content.split()[0] == "!event"):
            await event.events(message)

client = MyClient()
client.run(token)