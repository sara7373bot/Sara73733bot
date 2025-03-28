import telebot
import requests
import os

TOKEN = os.getenv("TOKEN")  # دریافت توکن از متغیر محیطی
bot = telebot.TeleBot(TOKEN)

def get_crypto_price(crypto_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    response = requests.get(url).json()
    return response.get(crypto_id, {}).get("usd", "نامشخص")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 سلام! برای دریافت قیمت ارزها از /price [نام_ارز] استفاده کن.")

@bot.message_handler(commands=['price'])
def send_price(message):
    try:
        crypto_id = message.text.split()[1].lower()
        price = get_crypto_price(crypto_id)
        bot.reply_to(message, f"💰 قیمت {crypto_id}: {price} دلار")
    except IndexError:
        bot.reply_to(message, "❌ لطفاً نام ارز را بعد از /price وارد کنید.")

bot.polling(none_stop=True)
