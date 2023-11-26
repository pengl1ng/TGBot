import telebot
from telebot import types

api_token = '6730965952:AAEGGvnWQ6QYR83vNnKMGp4SN5hhqs0iCo4'
bot = telebot.TeleBot(api_token)
eq_list = ()
mdl = ""


def models_markup(call, names):
    markup_model = types.InlineKeyboardMarkup()
    for i in range(len(names)):
        button = types.InlineKeyboardButton(f'{names[i]}', callback_data=f'{names[i]}')
        markup_model.add(button)
    bot.send_message(call.message.chat.id, text="Выберите модель автомобиля",
                     reply_markup=markup_model)


def models_eq(call, equipments):
    markup_eq = types.InlineKeyboardMarkup()
    for i in range(len(equipments)):
        button = types.InlineKeyboardButton(f'{equipments[i]}', callback_data=f'{equipments[i]}')
        markup_eq.add(button)
    bot.send_message(call.message.chat.id, text="Выберите комплектацию автомобиля:",
                     reply_markup=markup_eq)


@bot.message_handler(commands=['start', 'restart'])
def mark(message):
    markup_mark = types.InlineKeyboardMarkup()
    button_kia = types.InlineKeyboardButton("Kia", callback_data="Kia")
    button_ford = types.InlineKeyboardButton("Ford", callback_data="Ford")
    markup_mark.add(button_kia, button_ford)
    bot.send_message(message.chat.id, text="Добро пожаловать!\nВыберите марку автомобиля",
                     reply_markup=markup_mark)


@bot.callback_query_handler(func=lambda call: True)
def model(call):
    global eq_list
    global mdl
    if call.data == 'Kia':
        cars_models = ('Kia Sorento',
                       'Kio Sportage',
                       'Kio Stinger')
        models_markup(call, cars_models)
    elif call.data == 'Ford':
        cars_models = ('Ford EcoSport',
                       'Ford Flex',
                       'Ford Focus (Mk3)')
        models_markup(call, cars_models)
    elif call.data == 'Kia Sorento':
        eq_list = ('Luxe 2.5 / 180 л. с. 6AT 4WD',
                   'Premium 2.5 / 180 л. с. 6AT 4WD')
        models_eq(call, eq_list)
        mdl = call.data
    elif call.data == 'Kio Sportage':
        eq_list = ('Comfort 2.0 / 150 л. с. 6AT 2WD Бензин',
                   'Comfort 2.0 / 150 л. с. 6AT 4WD Бензин',
                   'Luxe 2.0 / 150 л. с. 6AT 2WD')
        models_eq(call, eq_list)
        mdl = call.data
    elif call.data == 'Kio Stinger':
        eq_list = ('GT Line 2.0T / 247 л. с. 8AT AWD',
                   'Luxe 2.0T / 247 л. с. 8AT AWD',
                   'Luxe 2.0T / 247 л. с. 8AT RWD')
        models_eq(call, eq_list)
        mdl = call.data
    elif call.data == 'Ford EcoSport':
        eq_list = ('1.5 л, 123 л.с., бензин, МКПП, передний привод',
                   '1.5 л, 123 л.с., бензин, АКПП, передний привод',
                   '2.0 л, 148 л.с., бензин, АКПП, полный привод (4WD)')
        models_eq(call, eq_list)
        mdl = call.data
    elif call.data == 'Ford Flex':
        eq_list = ('3.5 л, 287 л.с., бензин, АКПП, передний привод',
                   '3.5 л, 287 л.с., бензин, АКПП, полный привод (4WD)',
                   '3.5 л, 365 л.с., бензин, АКПП, полный привод (4WD)')
        models_eq(call, eq_list)
        mdl = call.data
    elif call.data == 'Ford Focus (Mk3)':
        eq_list = ('1.5 л, 150 л.с., бензин, АКПП, передний привод',
                   '1.6 л, 105 л.с., бензин, МКПП, передний привод',
                   '1.6 л, 105 л.с., бензин, робот, передний привод',
                   '1.6 л, 125 л.с., бензин, МКПП, передний привод',
                   '1.6 л, 125 л.с., бензин, робот, передний привод')
        models_eq(call, eq_list)
        mdl = call.data
    elif str(call.data) in eq_list and mdl != "":
        bot.send_message(call.message.chat.id, text=f"Вы выбрали машину: {mdl}, комплектация: {call.data}\n"
                                                    f"Для перезапуска введите команду /restart")


bot.polling(none_stop=True)
