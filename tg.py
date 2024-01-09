from telethon import TelegramClient, events
from dotenv import dotenv_values

env_variables = dotenv_values(".env")

api_id = env_variables.get("API_ID")
api_hash = env_variables.get("API_HASH")
bot_token = env_variables.get("BOT_TOKEN")
client = TelegramClient('bot_session', api_id, api_hash)
client_token = env_variables.get("TOKEN")
client_name = env_variables.get("CLIENT_NAME")
number = env_variables.get("PHONE_NUMBER")


client.start(bot_token=bot_token)  

@client.on(events.NewMessage(pattern='/start')) 
async def start(event):
    await event.respond('Привіт! Я бот. Я відповім на ваші повідомлення.')

@client.on(events.NewMessage)  
async def echo(event):
    if event.is_private:  
        print(event.text)

client.run_until_disconnected()
