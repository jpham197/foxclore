"""
This class handles the updating of users with the database
"""
from pymongo import MongoClient

# Connecting to database and declaring the collection
cluster = MongoClient("mongodb+srv://buzzbot:neJPIzxDGax66NqI@buzzbot-"
                      + "gesgl.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["discord"]
collection = db["users"]


async def first_time(self):
    """
    Adds all users of servers that the bot is in to the database
    :param self: this is our bot
    """
    # x is a list created by the method get_all_members()
    member_list = self.get_all_members()
    for member in member_list:
        post = {
            "_id": member.id,
            "name": member.name,
            "joined at": member.joined_at,
            "server": member.guild.name,
            "isBot": member.bot
        }
        collection.insert_one(post)


async def new_member(member):
    """
    Adds newly joined members while bot is on to the database
    :param member: this is the member that has just joined
    """
    post = {
        "_id": member.id,
        "name": member.name,
        "joined at": member.joined_at,
        "server": member.guild.name,
        "isBot": member.bot
    }
    collection.insert_one(post)


async def remove_member(member):
    """
    Removes member from database when they leave the server
    :param member: member that left
    """
    leaving_member = {"_id": member.id}
    collection.delete_one(leaving_member)


async def remove_channel(guild):
    """
    Removes member from database when they leave the server
    :param guild: server that removed the bot
    """
    leaving_server = {"server": guild.name}
    collection.delete_one(leaving_server)
