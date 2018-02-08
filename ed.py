'''
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "!") #Initialise client bot


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
    if message.content == "Ed":
        await client.send_message(message.channel, "Ed Seykota bot at your service") #responds with Cookie emoji when someone says "cookie"

client.run("NDEwOTI3OTM4NDA2NzExMjk4.DV0SXQ.jg3aNg_yTIEJ2JCP7l7xDfriytU") #Replace token with your bots token
'''


import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random


real = "NDEwOTI3OTM4NDA2NzExMjk4.DV0SXQ.jg3aNg_yTIEJ2JCP7l7xDfriytU"
custom = "NDEwODY4NzAxOTM2NjE1NDQ0.DV0Wvg.bAamLwj3g8SzSuHrN0NCZjNuLy8"

Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "!") #Initialise client bot

'''
“If I am bullish, I neither buy on a reaction, nor wait for strength; I am already in. I turn bullish at the instant my buy stop is hit, and stay bullish until my sell stop is hit. Being bullish and not being long is illogical.”
“Fundamentalists figure things out and anticipate change. Trend followers join the trend of the moment. Fundamentalists try to solve their feelings. Trend followers join their feelings and observe them evolve and dis-solve.”
“The feelings we accept and enjoy rarely interfere with trading.”
“Systems don’t need to be changed. The trick is for a trader to develop a system with which he is compatible”
“It can be very expensive to try to convince the markets you are right.”
“There are old traders and there are bold traders, but there are very few old, bold traders.”
“I would add that I consider myself and how I do things as a kind of system which, by definition, I always follow.”
“Systems trading is ultimately discretionary. The manager still has to decide how much risk to accept, which markets to play, and how aggressively to increase and decrease the trading base as a function of equity change.”
“Trying to trade during a losing streak is emotionally devastating. Trying to play “catch up” is lethal.”
“The elements of good trading are: 1, cutting losses. 2, cutting losses. And 3, cutting losses. If you can follow these three rules, you may have a chance.”
“Losing a position is aggravating, whereas losing your nerve is devastating.”
“The markets are the same now as they were five to ten years ago because they keep changing – just like they did then.”
“Luck plays an enormous role in trading success. Some people were lucky enough to be born smart, while others were even smarter and got born lucky.”
“Having a quote machine is like having a slot machine at your desk – you end up feeding it all day long. I get my price data after the close each day.”
“A losing trader can do little to transform himself into a winning trader. A losing trader is not going to want to transform himself. That’s the kind of thing winning traders do.”
“If you can’t take a small loss, sooner or later you will take the mother of all losses.”
“It is a happy circumstance that when nature gives us true burning desires, she also gives us the means to satisfy them. Those who want to win and lack skill can get someone with skill to help them.”
“Risk no more that you can afford to lose, and also risk enough so that a win is meaningful.”
“Dramatic and emotional trading experiences tend to be negative. Pride is a great banana peel, as are hope, fear, and greed. My biggest slip-ups occurred shortly after I got emotionally involved with positions.”
“Be sensitive to subtle differences between ‘intuition’ and ‘into wishing’.”
“The trading rules I live by are: 1. Cut losses. 2. Ride winners. 3. Keep bets small. 4. Follow the rules without question. 5. Know when to break the rules.”
“I usually ignore advice from other traders, especially the ones who believe they are on to a “sure thing”. The old timers, who talk about “maybe there is a chance of so and so,” are often right and early.”
“I set protective stops at the same time I enter a trade. I normally move these stops in to lock in a profit as the trend continues. Sometimes, I take profits when a market gets wild. This usually doesn’t get me out any better than waiting for my stops to close in, but it does cut down on the volatility of the portfolio, which helps calm my nerves. Losing a position is aggravating, whereas losing your nerve is devastating.”
“I intend to risk below 5 percent on a trade, allowing for poor executions.”
“I don’t judge success, I celebrate it. I think success has to do with finding and following one’s calling regardless of financial gain.”
(On losing streaks and over-trading) “Acting out this drama could be exciting. However, it also seems terribly expensive. One alternative is to keep bets small and then to systematically keep reducing risk during equity drawdowns. That way you have a gentle financial and emotional touchdown.”
“In order of importance to me are: 1) the long term trend, 2) the current chart pattern, and 3) picking a good spot to buy or sell.”
“Win or lose, everybody gets what they want out of the market. Some people seem to like to lose, so they win by losing money.”
“Fundamentals that you read about are typically useless as the market has already discounted the price, and I call them “funny-mentals”. However, if you catch on early, before others believe, you might have valuable “surprise-a-mentals”.”
“If you can’t measure it, you probably can’t manage it… Things you measure tend to improve.”
“The key to long-term survival and prosperity has a lot to do with the money management techniques incorporated into the technical system.”
“If you want to know everything about the market, go to the beach. Push and pull your hands with the waves. Some are bigger waves, some are smaller. But if you try to push the wave out when it’s coming in, it’ll never happen. The market is always right”
“To avoid whipsaw losses, stop trading”
“Pyramiding instructions appear on dollar bills. Add smaller and smaller amounts on the way up. Keep your eye open at the top”
“Markets are fundamentally volatile. No way around it. Your problem is not in the math. There is no math to get you out of having to experience uncertainty.”
“Our work is not so much to treat or to cure feelings, as to accept and celebrate them. This is a critical difference.”
“Before I enter a trade, I set stops at a point at which the chart sours.”
“Trading requires skill at reading the markets and at managing your own anxieties.”
“The positive intention of fear is risk control.”
“Speculate with less than 10% of your liquid net worth. Risk less than 1% of your speculative account on a trade. This tends to keep the fluctuations in the trading account small, relative to net worth. This is essential as large fluctuations can engage {emotions} and lead to feeling-justifying drama.”
'''

quotes = ['If I am bullish, I neither buy on a reaction, nor wait for strength; I am already in. I turn bullish at the instant my buy stop is hit, and stay bullish until my sell stop is hit. Being bullish and not being long is illogical.',
          'Fundamentalists figure things out and anticipate change. Trend followers join the trend of the moment. Fundamentalists try to solve their feelings. Trend followers join their feelings and observe them evolve and dis-solve.',
          'The feelings we accept and enjoy rarely interfere with trading.',
          'Systems don’t need to be changed. The trick is for a trader to develop a system with which he is compatible',
          'It can be very expensive to try to convince the markets you are right.',
          'There are old traders and there are bold traders, but there are very few old, bold traders.',
          'I would add that I consider myself and how I do things as a kind of system which, by definition, I always follow.',
          'Systems trading is ultimately discretionary. The manager still has to decide how much risk to accept, which markets to play, and how aggressively to increase and decrease the trading base as a function of equity change.',
          'Trying to trade during a losing streak is emotionally devastating. Trying to play “catch up” is lethal.',
          'The elements of good trading are: 1, cutting losses. 2, cutting losses. And 3, cutting losses. If you can follow these three rules, you may have a chance.',
          'Losing a position is aggravating, whereas losing your nerve is devastating.',
          'The markets are the same now as they were five to ten years ago because they keep changing – just like they did then.',
          'Luck plays an enormous role in trading success. Some people were lucky enough to be born smart, while others were even smarter and got born lucky.',
          'Having a quote machine is like having a slot machine at your desk – you end up feeding it all day long. I get my price data after the close each day.',
          'A losing trader can do little to transform himself into a winning trader. A losing trader is not going to want to transform himself. That’s the kind of thing winning traders do.',
          'If you can’t take a small loss, sooner or later you will take the mother of all losses.',
          'It is a happy circumstance that when nature gives us true burning desires, she also gives us the means to satisfy them. Those who want to win and lack skill can get someone with skill to help them.',
          'Risk no more that you can afford to lose, and also risk enough so that a win is meaningful.',
          'Dramatic and emotional trading experiences tend to be negative. Pride is a great banana peel, as are hope, fear, and greed. My biggest slip-ups occurred shortly after I got emotionally involved with positions.',
          'Be sensitive to subtle differences between ‘intuition’ and ‘into wishing’.',
          'The trading rules I live by are: 1. Cut losses. 2. Ride winners. 3. Keep bets small. 4. Follow the rules without question. 5. Know when to break the rules.',
          'I usually ignore advice from other traders, especially the ones who believe they are on to a “sure thing”. The old timers, who talk about “maybe there is a chance of so and so,” are often right and early.',
          'I set protective stops at the same time I enter a trade. I normally move these stops in to lock in a profit as the trend continues. Sometimes, I take profits when a market gets wild. This usually doesn’t get me out any better than waiting for my stops to close in, but it does cut down on the volatility of the portfolio, which helps calm my nerves. Losing a position is aggravating, whereas losing your nerve is devastating.',
          'I intend to risk below 5 percent on a trade, allowing for poor executions.',
          'I don’t judge success, I celebrate it. I think success has to do with finding and following one’s calling regardless of financial gain.',
          'Acting out this drama could be exciting. However, it also seems terribly expensive. One alternative is to keep bets small and then to systematically keep reducing risk during equity drawdowns. That way you have a gentle financial and emotional touchdown.',
          'In order of importance to me are: 1) the long term trend, 2) the current chart pattern, and 3) picking a good spot to buy or sell.',
          'Win or lose, everybody gets what they want out of the market. Some people seem to like to lose, so they win by losing money.',
          'Fundamentals that you read about are typically useless as the market has already discounted the price, and I call them “funny-mentals”. However, if you catch on early, before others believe, you might have valuable “surprise-a-mentals.',
          'If you can’t measure it, you probably can’t manage it… Things you measure tend to improve.',
          'The key to long-term survival and prosperity has a lot to do with the money management techniques incorporated into the technical system.',
          'If you want to know everything about the market, go to the beach. Push and pull your hands with the waves. Some are bigger waves, some are smaller. But if you try to push the wave out when it’s coming in, it’ll never happen. The market is always right',
          'To avoid whipsaw losses, stop trading',
          'Pyramiding instructions appear on dollar bills. Add smaller and smaller amounts on the way up. Keep your eye open at the top',
          'Markets are fundamentally volatile. No way around it. Your problem is not in the math. There is no math to get you out of having to experience uncertainty.',
          'Our work is not so much to treat or to cure feelings, as to accept and celebrate them. This is a critical difference.',
          'Before I enter a trade, I set stops at a point at which the chart sours.',
          'Trading requires skill at reading the markets and at managing your own anxieties.',
          'The positive intention of fear is risk control.',
          'Speculate with less than 10% of your liquid net worth. Risk less than 1% of your speculative account on a trade. This tends to keep the fluctuations in the trading account small, relative to net worth. This is essential as large fluctuations can engage {emotions} and lead to feeling-justifying drama.']









@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
    if message.content == "!Ed":
        output = str(random.choice(quotes))
        await client.send_message(message.channel, output) #responds with Cookie emoji when someone says "cookie"
    if message.content == "!SingEd":
        output = "https://www.youtube.com/watch?v=LiE1VgWdcQM"
        await client.send_message(message.channel, output) #responds with Cookie emoji when someone says "cookie"
    

client.run(real) #Replace token with your bots token
