import discord
import json
import Counting as count
import updateUsers

# auth token from auth.json
token = json.load(open('auth.json', 'r'))['token']


class MyClient(discord.Client):
    # Our main discord bot class
    async def on_ready(self):
        # Stuff that happens when the bot is turned on
        print("buzz-bot is on")
    
    async def on_member_join(self,member):
        # Stuff that happens when there is a new member
        await updateUsers.new_member(member)
    
    async def on_member_remove(self, member):
        # Stuff that happens when a member leaves
        await updateUsers.remove_member(member)

    async def on_message(self, message):
        # Stuff that happens when there is a new message
        await count.counting(message)
    
    async def on_guild_join(self,guild):
        # Stuff that happens when the bot joins a server
        await updateUsers.first_time(self)

client = MyClient()
client.run(token)