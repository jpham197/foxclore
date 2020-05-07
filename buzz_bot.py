"""Main file for the discord bot"""
import json
import discord
import counting_logic as count
import update_users

# auth token from auth.json
token = json.load(open('auth.json', 'r'))['token']


class MyClient(discord.Client):
    """Our main discord bot class"""
    async def on_ready(self):
        """Stuff that happens when the bot is turned on"""
        print("buzz-bot is on")
        await update_users.first_time(self)

    async def on_member_join(self, member):
        """Stuff that happens when there is a new member"""
        await update_users.new_member(member)

    async def on_member_remove(self, member):
        """Stuff that happens when a member leaves"""
        await update_users.remove_member(member)

    async def on_message(self, message):
        """Stuff that happens when there is a new message"""
        await count.counting(message)

    async def on_guild_join(self):
        """Stuff that happens when the bot joins a server"""
        await update_users.first_time(self)

    async def on_guild_remove(self, guild):
        """Stuff that happens when bot is removed from a server"""
        await update_users.remove_channel(guild)

    async def on_user_update(self, after):
        await update_users.update_member(after)


client = MyClient()
client.run(token)
