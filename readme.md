# About :

This is just a basic telegram bot to get the current price for a stock. It uses botfather for telegram bot creation and telegram api handling is done via telebot library.
It use alpha vantage free api for getting stock price information.

# Purpose :
The only purpose of this bot is to show my basic python skills.

# How to use :
1. Start with installing python & pip and the packages in requirements.txt file.
For pip install
```
pip install -r requirements.txt

```

2. create a bot using telegram botfather and get the bot token

3. Get a free api key from alpha vantage free api

4. Create credentials.json file and set those values as
```
{
    "telegram_api_token" : "",
    "alpha_api_token" : ""
}
```

5. Run bot with running 
```
python botScript.py
```
