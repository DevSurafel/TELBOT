import time
import telebot

# Replace with your bot's token
TOKEN = '6673603433:AAE01kdnAPBySpX421ZX5kf3VudealyWLf4'

# Create the bot instance
bot = telebot.TeleBot(TOKEN)

# Replace with your group chat ID
CHAT_ID = '-1002033347065'

# Function to send a message to the group every 10 minutes
def send_message():
    while True:
        bot.send_message(CHAT_ID, "Hello Everyone")
        time.sleep(600)  # Wait for 10 minutes (600 seconds)

if __name__ == "__main__":
    send_message()
