async def counting(message):
    """
    manages the counting channel rules
    :param message: this is any message that was sent in the counting channel
    """
    # Check to see if message is in counting-channel
    try:
        message.channel.name
        if message.channel.name == 'test-buzz':
            if message.author.name != "buzz-bot":
                m = await message.channel.history().get(author__name='buzz-bot')
                if is_number(message):
                    if in_order(message, m):
                        last_num = int(message.content)
                        await message.channel.send(last_num + 1)
                    else:
                        await message.author.send("stop it")
                        await message.delete()
                else: 
                    await message.delete()
    except AttributeError:
        pass

            
        

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
    """
    Checks if the message is the correct number
    :param message: the message that is sent by user
    :oaram last_message: the message sent by the bot
    :returns: bool based on if the number is the next number in the sequence
    """
    if int(message.content) == int(last_message.content) + 1:
        return True
    else:
        return False
