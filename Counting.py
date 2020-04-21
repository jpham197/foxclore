async def double_count(message):
    # Check to see if message is in counting-channel
    if message.channel.name == 'test-buzz':
        print("Channel check works")
        last_num = int(message.content)
        await message.channel.send(last_num + 1)

def test():
    print('test')