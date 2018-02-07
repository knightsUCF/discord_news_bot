# https://discordapp.com/api/webhooks/410500270553038858/chgMvQCOxcIj_3wqy2PT1QXW2scv20YDtzSKc4gnTGfoDQc1VsRqskL_VLbSFx-Qe2aA


import time


# discord_bitcoin_price_bot.py
import requests  # pip install requests

# Provide the webhook URL that Discord generated
discord_webhook_url = 'https://discordapp.com/api/webhooks/410500270553038858/chgMvQCOxcIj_3wqy2PT1QXW2scv20YDtzSKc4gnTGfoDQc1VsRqskL_VLbSFx-Qe2aA'

# Get the BTC price from CoinDesk
bitcoin_price_url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'





while True:
    time.sleep(10800)
    data = requests.get(bitcoin_price_url).json()
    price_in_usd = data['bpi']['USD']['rate']
    # Post the message to the Discord webhook
    data = {
    "content": "Current Bitcoin price: $" + price_in_usd + " USD"
    }
    requests.post(discord_webhook_url, data=data)
    # print(data)
    
