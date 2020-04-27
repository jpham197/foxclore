import discord
import json
import Counting as count
import pymongo
from pymongo import MongoClient

# Connecting to database and declaring the collection
cluster = MongoClient("mongodb+srv://buzzbot:neJPIzxDGax66NqI@buzzbot-" 
+ "gesgl.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["discord"]
collection = db["users"]

token = json.load(open('auth.json', 'r'))['token']
class MyClient(discord.Client):
    async def on_ready(self):
        """
        Adds all users of servers that the bot is in to the database
        :param self: this is our bot
        """
        # Shows that the login worked
        print('Logged on as', self.user)

        # x is a list created by the method get_all_members()
        x = self.get_all_members()
        for member in x:
            post = {
            "_id": member.id, 
            "name": member.name,
            "joined at": member.joined_at,
            "server": member.guild.name, 
            "isBot": member.bot
            }
            collection.insert_one(post)
    
    
    async def on_member_join(self,member):
        """
        Adds newly joined memebers while bot is on to the database
        :param self: this is our bot
        :param member: this is the memeber that has just joined
        """
        post = {
            "_id": member.id, 
            "name": member.name,
            "joined at": member.joined_at,
            "server": member.guild.name, 
            "isBot": member.bot
            }
        collection.insert_one(post)


    async def on_message(self, message):
        """
        Adds newly joined memebers while bot is on to the database
        :param self: this is our bot
        :param message: this is any message that was sent in any server
        """
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

        await count.counting(message)

client = MyClient()
client.run(token)