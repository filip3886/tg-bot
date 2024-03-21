import telebot
from telebot import types
import data_base as get_and_save_info


bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    get_and_save_info.create_table()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет!Я бот который розкажет тебе немного интересного о мемах", reply_markup=markup)
    get_and_save_info.insert_data_to_db(message.from_user.id,message.from_user.first_name,message.from_user.username)
@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.from_user.id,"Дякую за увагу!",parse_mode="Markdown")
    

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('потные девочки 18 плюс')
        btn2 = types.KeyboardButton('Топ самых популярных мемов')
        btn3 = types.KeyboardButton('История мемов')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) 
    

    elif message.text == 'потные девочки 18 плюс':
        get_and_save_info.show_db_info()
        bot.send_message(message.from_user.id, 'У нас есть твои данные ,грязный педофил', parse_mode='Markdown')
        bot.send_message(message.from_user.id,"", parse_mode='Markdown')
    
    
    elif message.text == '':
        bot.send_message(message.from_user.id, "", parse_mode='Markdown')

    elif message.text == 'История мемов':
        get_and_save_info.show_db_info()
        bot.send_message(message.from_user.id, '', parse_mode='Markdown')
       
bot.polling(none_stop=True, interval=0) 


