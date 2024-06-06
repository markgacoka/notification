import os
import random
import requests

def send_telegram_message():
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    random_number = random.randint(1, 100)
    message = f'Random Number: {random_number}'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=data)
    return response.json()

if __name__ == "__main__":
    send_telegram_message()
