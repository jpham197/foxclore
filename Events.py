"""
Module holding all event logic
"""
import datetime
import pymongo
from pymongo import MongoClient

# Connecting to database and declaring the collection
cluster = MongoClient("mongodb+srv://buzzbot:neJPIzxDGax66NqI@buzzbot-" 
+ "gesgl.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["discord"]
collection = db["events"]

async def events(message):
    """
    Reads following format: !event [create (name) (date format YYYY-MM-DD HH:MM on 24hr scale indexing from 0) (description) / delete (name) / read(name)]

    :param message: The message object typed in from user
    :return: confirmation of event creation / deletion
    """
    splitMessage = message.content.split()
    action = splitMessage[1]
    if (action == "create"):
        try:
            dateArg = splitMessage[3].split("-")
            timeArg = splitMessage[4].split(":")

            year = int(dateArg[0])
            month = int(dateArg[1])
            day = int(dateArg[2])

            hour = int(timeArg[0])
            mins = int(timeArg[1])

            date = datetime.datetime(year, month, day, hour, mins)

            event = {
                "_id": splitMessage[2],
                "date": date,
                "description": splitMessage[5]
            }
            print(event)
            collection.insert_one(event)
        except:
            raise Exception("Incorrect date format")
        finally:
            print("Incorrect syntax for event creation")
    elif (action == "delete"):
        id = splitMessage[2]
        return ""
    elif (action == "read"):
        id = splitMessage[2]
        return ""
    else:
        return "Actions allowed: create, delete"