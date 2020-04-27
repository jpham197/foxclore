async def counting(message):
    """
    manages the counting channel rules
    :param message: this is any message that was sent in the counting channel
    """
    # Check to see if message is in counting-channel
    if message.channel.name == 'test-buzz':
        if message.author.name != "buzz-bot":
            m = await message.channel.history().get(author__name='buzz-bot')
            # Checks to see if message is an int
            if is_number(message):
                if in_order(message, m):
                    last_num = int(message.content)
                    await message.channel.send(last_num + 1)
                else:
                    await message.delete()

            else: 
                await message.delete()

            
        

def is_number(message):
    """
    Checks if the message can be an int
    :param s: the message as a string
    :returns: bool based on if the string to int conversion was successful
    """
    try:
        int(message.content)
        return True
    except ValueError:
        return False

def in_order(message, last_message):
    if int(message.content) == int(last_message.content) + 1:
        return True
    else:
        return False
