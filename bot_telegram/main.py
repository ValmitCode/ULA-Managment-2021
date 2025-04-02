from concurrent.futures import thread
import threading
from bot_telegram.funcs import *
from bot_telegram.config import *
import bot_telegram.config

@bot.message_handler(commands=["start"])
def start_command(message):
    bot.send_message(message.chat.id, config.START_COMMAND)

@bot.message_handler(commands=["passcode"])
def passcode_send(message):
    bot.send_message(message.chat.id, message.chat.id)

@bot.message_handler(commands=["petition"])
def petition(message):
    #bot.register_next_step_handler(message, send_petition)
    bot.register_next_step_handler(message, message_to_mentor, "petition")
    #bot.send_message(message.chat.id, config.START_COMMAND)

@bot.message_handler(commands=["conversation"])
def conversation_request(message):
    bot.register_next_step_handler(message, message_to_mentor, "conversation_request")

@bot.message_handler(commands=["department"])
def application_department(message):
    bot.register_next_step_handler(message, message_to_mentor, "application_department")

@bot.message_handler(commands=["profile"])
def statistics_collect(message):
    send_statistic_collect(message)

#Mentor functional

@bot.message_handler(commands=["changeStatus"])
def statistics_colect(message):
    send_statistic_collect(message)

@bot.message_handler(func=lambda m:True)
def noncommand_message(message):
    bot.send_message(message.chat.id, "Я не розумію цієї команди(")
    

#room clear
#oseredkovi cili na modul
#modul zakinchivsya
#work with contact collector

if __name__== '__main__':
    
    p1=threading.Thread(target=bot.infinity_polling)
    p2=threading.Thread(target=scheduler)
    
    p1.start()
    p2.start()
