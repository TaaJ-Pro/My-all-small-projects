import discord

token = ("ODg3NjEwNjgzNTk0ODAxMTkz.YUGp3Q.YgLG87RkISzNj6Ec6GQLQQbHPFE")
client = discord.Client()

@client.event

async def on_message(message): # every time a message is posted, mod-bot will check to see if it contains any banned words
    if message.content.startswith('!test'):
        await message.channel.send(message.content)
        print(message.content)
    elif message.author == client.user:
        return


client.run(token)