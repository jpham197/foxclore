async def counting(message):
    """
    manages the counting channel rules
    :param message: this is any message that was sent in the counting channel
    """
    # Check to see if message is in counting-channel
    if message.channel.name == 'test-buzz':
        # Checks to see if message is an int
        if  is_number(message.content) : 
            last_num = int(message.content)
            await message.channel.send(last_num + 1)
        else: 
            await message.delete()

def is_number(s):
    """
    Checks if the message can be an int
    :param s: the message as a string
    :returns: bool based on if the string to int conversion was successful
    """
    try:
        int(s)
        return True
    except ValueError:
        return False