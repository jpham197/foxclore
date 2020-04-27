import discord
import json
import Counting as count
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://buzzbot:neJPIzxDGax66NqI@buzzbot-gesgl.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["discord"]
collection = db["chat logs"]

token = json.load(open('auth.json', 'r'))['token']
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
       
        #adds all the members to teh database on start of bot across all servers the bot is in
        x = self.get_all_members()
        for member in x:
            post = {"_id": member.id, "name": member.name,"joined at": member.joined_at, 
            "server": member.guild.name, "isBot": member.bot}
            collection.insert_one(post)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

        await count.double_count(message)

client = MyClient()
client.run(token)