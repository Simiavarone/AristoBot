# Work with Python 3.6
import discord

TOKEN = 'Njg5MTY0MDk1NjAxMjQ2MjU2.Xm-9Gw.9oxlEQERe0bnVc7NOgP8YUHSp3o'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('&hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Connecté en tant que')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)