import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.author == client.user:
            return
        elif message.content.startswith("$hello"):
            await message.channel.send("今日は")
        elif message.content.startswith("$?dev"):
            await message.channel.send("The only current dev is a baka named jackisapi on github.")



client = MyClient()
client.run('')
