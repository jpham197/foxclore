"""
Module holding all event logic
"""

async def create(message):
    """
    Reads following format: !event [create/delete (id)] [date format MM/DD/YYYY:HH:MM on 24hr scale] [description]

    :param message: The message object typed in from user
    :return: confirmation of event creation / deletion
    """
    
    action = message.content.split()[1]
    print(action)
    if (action == "create"):
        return ""
    elif (action == "delete"):
        return ""
    else:
        return "Actions allowed: create, delete"