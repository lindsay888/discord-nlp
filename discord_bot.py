#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
from random import randint
import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
import re
import unidecode
pd.options.display.max_rows = 4000


# In[2]:


import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
#     message.channel.send('hey you!')
#     print('author')
    if message.author == client.user:
#         print('yes')
        return
        

    if message.content.startswith('$hello'):
#         print('this one')
        await message.channel.send('Hello!')
    
    if message.content.startswith('$thumb'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')
            
client.run('NzUyOTA2NDIzNzk2NzYwNjU3.X1ecvw.8Heqoke3Vw8X5S1i1SaFgPImAeg')




# In[ ]:




