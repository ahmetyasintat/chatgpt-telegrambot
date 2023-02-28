import openai
import sys
import telebot
import time 
import config

#openai api key 
openai.api_key = config.openai_api
#telegram bot api token
API_TOKEN = config.api_token

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=["start","help"])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am ChatGPT correct_standart_english.
I can put any sentence you want into a correct grammatical structure\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def correct_standart_english(message):
    start_time = time.time()
    
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Correct this to standard English:{message.text}",
    temperature=0.1,
    max_tokens=60,
    top_p=1.0,      
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    
    promt = response["choices"][0]["text"]
    
    bot.reply_to(message,promt)

    end_time = time.time()
    sys.stdout.write("request execution time (type of second) = " + str(int(((end_time - start_time)))%60)+"\n")
    sys.stdout.flush()


bot.infinity_polling()

