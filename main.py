# Work with Python 3.6
import discord
import re

TOKEN = 'Njg5MTY0MDk1NjAxMjQ2MjU2.Xm-9Gw.9oxlEQERe0bnVc7NOgP8YUHSp3o'

client = discord.Client()
mc_dico = {}

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    content = message.content
    
    if content.startswith('&hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        return
    
    if content.startswith('&minecraft'):
        """
        Send all the data in the dictionnary for minecraft coordinates
        """
        msg = '\n'.join([key+' : '+mc_dico[key] for key in mc_dico.keys() ])
        msg = msg.format(message)
        await client.send_message(message.channel, msg)
        return
    
    # check if message matches minecraft coordinates
    mc_coord = re.match('\d+\s\d+\s\d+\s\d+\s\d+\s\d+', content)    
    if mc_coord :
        span = mc_coord.span()
        coord = content[span[0]:span[1]]
        if coord in mc_dico.keys() :
              msg = coord+' : '+mc_dico[coord]
              msg = msg.format(message)
              await client.send_message(message.channel, msg)
        else :
            mc_dico[coord] = content[span[1]:]
        return
        
        
        

@client.event
async def on_ready():
    print('Connecté en tant que')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)