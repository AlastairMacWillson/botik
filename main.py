import telebot
from telebot import types

#import wolframalpha
#client = wolframalpha.Client('pypi-AgEIcHlwaS5vcmcCJGI4ZTQ0ZTJlLTI4MDgtNGRjMi1iZWVkLWU4ZDA1YmZkNjIyNwACJXsicGVybWlzc2lvbnMiOiAidXNlciIsICJ2ZXJzaW9uIjogMX0AAAYgG0k2KSN-ho-EeQJ-NtnKIkaXWpkkn5Kh1BilogvZtdQ')
#res = client.query(query)
#print(next(res.results).text)

bot = telebot.TeleBot('2016351506:AAGV9AKm7i6d39ggcPsnDTEGQPYcaQiKFcs')
name = ''
surname = ''
age = 0
def get_age(message):
    global age
    while age == 0:  # проверяем что возраст изменился
        try:
            age = int(message.text)  # проверяем, что возраст введен корректно
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
    keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)  # следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id,'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_name(message):  # получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

#def inlinequery(update, context):
    #"""Handle the inline query."""
    #query = update.inline_query.query
    #print(query)
    #res = client.query(query)
    #results = [
    #    InlineQueryResultArticle(
    #        id=uuid4(),
    #        title="Magic answer is here!",
    #        input_message_content=InputTextMessageContent(
    #            "{} => *{}*".format(query, next(res.results).text),
    #            parse_mode=ParseMode.MARKDOWN))]
    #update.inline_query.answer(results)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":  # call.data это callback_data, которую мы указали при объявлении кнопки
        # код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'Запомню : )')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Запомню specially')
        # переспрашиваем




bot.polling(none_stop=True, interval=0)
