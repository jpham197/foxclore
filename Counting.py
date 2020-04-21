async def double_count(message):
    # Check to see if message is in counting-channel
    if message.channel.name == 'test-buzz':
        print("Channel check works")
        if  is_number(message.content) : 
            last_num = int(message.content)
            await message.channel.send(last_num + 1)
        else: 
            await message.delete()

def test():
    print('test')

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False