"""This file manages the rules and logic for the counting channel"""


async def counting(message):
    """
    manages the counting channel rules
    :param message: this is any message that was sent in the counting channel
    """
    # Check to see if message is in counting-channel
    try:
        if message.channel.name == 'test':
            if message.author.name != "buzz-bot":
                last_message = await message.channel.history().get(author__name='buzz-bot')
                if is_number(message):
                    if in_order(message, last_message):
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
    :param message: the message sent by non-bot user
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
    :param last_message: the message sent by the bot
    :param message: the message that is sent by user
    :returns: bool based on if the number is the next number in the sequence
    """
    return int(message.content) == int(last_message.content) + 1
