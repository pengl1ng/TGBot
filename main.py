import telebot
from telebot import types

api_token = '6730965952:AAEGGvnWQ6QYR83vNnKMGp4SN5hhqs0iCo4'
bot = telebot.TeleBot(api_token)
eq_list = ()
mdl = ""


def models_markup(message, names):
    markup_model = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(len(names)):
        button = types.KeyboardButton(f'{names[i]}')
        markup_model.add(button)
    button_exit = types.KeyboardButton('Вернуться к производителям')
    markup_model.add(button_exit)
    bot.send_message(message.chat.id, text="Выберите модель автомобиля",
                     reply_markup=markup_model)


def models_eq(message, equipments):
    markup_eq = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(len(equipments)):
        button = types.KeyboardButton(f'{equipments[i]}')
        markup_eq.add(button)
    button_exit = types.KeyboardButton('Вернуться к моделям')
    markup_eq.add(button_exit)
    bot.send_message(message.chat.id, text="Выберите комплектацию автомобиля:",
                     reply_markup=markup_eq)


@bot.message_handler(commands=['start', 'restart'])
def mark(message):
    markup_mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_kia = types.KeyboardButton("Kia")
    button_ford = types.KeyboardButton("Ford")
    markup_mark.add(button_kia, button_ford)
    bot.send_message(message.chat.id, text="Добро пожаловать!\nВыберите марку автомобиля",
                     reply_markup=markup_mark)


@bot.message_handler(content_types=['text'])
def model(message):
    global eq_list
    global mdl
    if message.text == 'Kia':
        cars_models = ('Kia Sorento',
                       'Kio Sportage',
                       'Kio Stinger')
        models_markup(message, cars_models)
    elif message.text == 'Ford':
        cars_models = ('Ford EcoSport',
                       'Ford Flex',
                       'Ford Focus (Mk3)')
        models_markup(message, cars_models)
    elif message.text == 'Kia Sorento':
        eq_list = ('Luxe 2.5 / 180 л. с. 6AT 4WD',
                   'Premium 2.5 / 180 л. с. 6AT 4WD')
        models_eq(message, eq_list)
        mdl = message.text
    elif message.text == 'Kio Sportage':
        eq_list = ('Comfort 2.0 / 150 л. с. 6AT 2WD Бензин',
                   'Comfort 2.0 / 150 л. с. 6AT 4WD Бензин',
                   'Luxe 2.0 / 150 л. с. 6AT 2WD')
        models_eq(message, eq_list)
        mdl = message.text
    elif message.text == 'Kio Stinger':
        eq_list = ('GT Line 2.0T / 247 л. с. 8AT AWD',
                   'Luxe 2.0T / 247 л. с. 8AT AWD',
                   'Luxe 2.0T / 247 л. с. 8AT RWD')
        models_eq(message, eq_list)
        mdl = message.text
    elif message.text == 'Ford EcoSport':
        eq_list = ('1.5 л, 123 л.с., бензин, МКПП, передний привод',
                   '1.5 л, 123 л.с., бензин, АКПП, передний привод',
                   '2.0 л, 148 л.с., бензин, АКПП, полный привод (4WD)')
        models_eq(message, eq_list)
        mdl = message.text
    elif message.text == 'Ford Flex':
        eq_list = ('3.5 л, 287 л.с., бензин, АКПП, передний привод',
                   '3.5 л, 287 л.с., бензин, АКПП, полный привод (4WD)',
                   '3.5 л, 365 л.с., бензин, АКПП, полный привод (4WD)')
        models_eq(message, eq_list)
        mdl = message.text
    elif message.text == 'Ford Focus (Mk3)':
        eq_list = ('1.5 л, 150 л.с., бензин, АКПП, передний привод',
                   '1.6 л, 105 л.с., бензин, МКПП, передний привод',
                   '1.6 л, 105 л.с., бензин, робот, передний привод',
                   '1.6 л, 125 л.с., бензин, МКПП, передний привод',
                   '1.6 л, 125 л.с., бензин, робот, передний привод')
        models_eq(message, eq_list)
        mdl = message.text
    elif message.text in eq_list and mdl != "":
        bot.send_message(message.chat.id, text=f"Вы выбрали машину: {mdl}, комплектация: {message.text}\n"
                                               f"Для перезапуска введите команду /restart")


bot.polling(none_stop=True)