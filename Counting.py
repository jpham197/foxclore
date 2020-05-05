import random

async def counting(message):
    """
    manages the counting channel rules
    :param message: this is any message that was sent in the counting channel
    """
    # Check to see if message is in counting-channel
    if message.channel.name == 'test-buzz':
        if message.author.name != "buzz-bot":
            last_message = await message.channel.history(limit=2).flatten()

            if is_number(message):
                if in_order(message, last_message[1]):
                    await double_count(message)
                else:
                    await message.delete()

            else: 
                await message.delete()

async def double_count(message):
    """
    Make buzz-bot count one more time after user counts, only happens sometimes

    :param message: the discord message the user sent
    :returns: no return value
    """

    chance = 50

    if random.randint(1, 100) < chance:
        last_num = int(message.content)
        await message.channel.send(last_num + 1)

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
    Checks if the message was correct

    :param s: the message as a string
    :returns: bool based on if the message is one greater than the last
    """
    print(f'Last Message is {last_message.content}')
    if int(message.content) == int(last_message.content) + 1:
        return True
    else:
        return False
