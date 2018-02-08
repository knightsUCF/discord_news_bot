import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

from cleverwrap import CleverWrap

cw = CleverWrap("CC74d-BTvojAsdOPDst7CX3tkiA")

real = "NDEwOTI3OTM4NDA2NzExMjk4.DV0SXQ.jg3aNg_yTIEJ2JCP7l7xDfriytU"
custom = "NDEwODY4NzAxOTM2NjE1NDQ0.DV0Wvg.bAamLwj3g8SzSuHrN0NCZjNuLy8"

Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "!") #Initialise client bot

username = "wizardsprite"
password = "7haso6kSRiv4RL0cjK1-NChQ0-U"

import praw
import re

reddit = praw.Reddit(user_agent = "News", client_id = "aVWoqAzFdmvQWw", client_secret = password)

quotes = ['You are erratic. Conflicted. Disorganised. Every decision is debated, every action questioned, every individual entitled to their own small opinion. You lack harmony, cohesion, greatness. It will be your undoing.',
          'I understand the concept of humour. It may not be apparent, but I am often amused by Human behaviour.',
          'Acquiring knowledge is a worthy objective. But its pursuit has obviously not elevated you.',
          'Fun will now commence.',
          'The Borg have prevailed',
          'You are a frustrating opponent',
          'We are Borg',
          'You will be assimiliated. Resistance is futile.',
          'Curious sensation...',
          'The end result has no use, no necessary task has been accomplished.',
          'So this is human freedom.',
          'The Borg believes otherwise.',
          'My parents were assimilated. Obviously their tactics were flawed.',
          'Your plan is ambitious.',
          'I have regained full contact with the collective.',
          'Your appeal to my humanity is pointless',
          'I am not overwhelmed. I simply do not wish to live among humans.',
          'I will survive -- on what, Borg perfection -- precisely.',
          'I wish to play again.',
          'Impossible is a word humans use far too often',
          'Intriguing but implausible',
          'Intuition is a human fallacy',
          'You are fatigued and concerned that I will defeat you.',
          'We are Borg',
          'Inefficient.',
          'You are individuals. You are small and you think in small terms.',
          'We must analyze the bioship -- your data',
          'Do not engage in further irrelevant discourse.',
          'Comfort is irrelevant.',
          'This activity is truly unproductive.',
          'The Borg believe otherwise.']


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):

    '''
    if message.content == "!Ed":
        output = str(random.choice(quotes))
        await client.send_message(message.channel, output) #responds with Cookie emoji when someone says "cookie"
    if message.content == "!SingEd":
        output = "https://www.youtube.com/watch?v=LiE1VgWdcQM"
        await client.send_message(message.channel, output) #responds with Cookie emoji when someone says "cookie"
    '''
    if message.content == "!Seven":
        output = 'Hi, I am Seven. Here are a few helpful commands you can use to communciate with me: \n\n'
        command_one = '*  !7"talk to me"\n'
        command_four = '*  !7of9\n'
        command_two = '*  !7fxposts\n'
        command_three = '*  !7investingposts\n'
        output = output + command_one + command_two + command_three
        await client.send_message(message.channel, output)
    if message.content.startswith('!7'):
        if message.content[2] == "\"" and message.content[-1] == "\"":
            input_conversation = message.content[3:-1]
            output = cw.say(input_conversation)
            await client.send_message(message.channel, output)         
        if message.content == "!7fxposts":
            output = 'Top 10 threads in https://www.reddit.com/r/forex : \n \n \n'
            number = 0
            for submission in reddit.subreddit('forex').hot(limit=10):
                number += 1
                output += (str(number) + '.' + ' ' + submission.title + '\n\n')
            await client.send_message(message.channel, output)
        if message.content == "!7investingposts":
            output = 'Top 10 threads in https://www.reddit.com/r/investing : \n \n \n'
            number = 0
            for submission in reddit.subreddit('forex').hot(limit=10):
                number += 1
                output += (str(number) + '.' + ' ' + submission.title + '\n\n')
            await client.send_message(message.channel, output)
    if message.content == "!7of9":
        output = str(random.choice(quotes))
        await client.send_message(message.channel, output)



client.run(real) #Replace token with your bots token
