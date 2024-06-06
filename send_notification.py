import os
import random
import requests

def send_telegram_message(message):
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=data)
    return response.json()

if __name__ == "__main__":
    random_number = random.randint(1, 100)
    message = f'Random Number: {random_number}'
    send_telegram_message(message)
