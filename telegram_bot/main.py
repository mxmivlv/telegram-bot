import telebot
from telebot import types
import config

bot = telebot.TeleBot(token=config.token)
keyBoards = types.ReplyKeyboardMarkup(True, row_width=2)
item1 = types.KeyboardButton("Мои работы")
item2 = types.KeyboardButton("Контактная информация")
keyBoards.add(item1, item2)
sticker_welcome = open("sticker/welcomeStick.webp", "rb")
sticker_contact_info = open("sticker/contactInfoStick.webp", "rb")
sticker_eror = open("sticker/erorStick.webp", "rb")

#Функция ответа на команду
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_sticker(message.chat.id, sticker_welcome)
    bot.send_message(message.chat.id, "Привет. Я Максим Романович.\n"
                                      "Начинающий программист в области GameDev.\n"
                                      "Изучаю языки программировани: C#, Python.", reply_markup=keyBoards)

#Функция ответа на текстовые сообщения
@bot.message_handler(content_types=['text'])
def answer(message):
    match message.text:
        case "Мои работы":
            bot.send_message(message.chat.id, f"Мои работы опубликованны в репозиториях GitHub.\n"
                                              f"Ссылка: https://github.com/mxmivlv.\n"
                                              f"Приятного просмотра {message.from_user.first_name} {message.from_user.last_name}")
        case "Контактная информация":
            bot.send_sticker(message.chat.id, sticker_contact_info)
            bot.send_message(message.chat.id, f"Меня можно найти в социальных сетях:\n"
                                              f"Телеграм: https://t.me/mxmivlv\n"
                                              f"Инстаграмм: https://www.instagram.com/mxmivlv/\n"
                                              f"Вконтакте: https://vk.com/mxmivlv\n"
                                              f"Почта: mxmivlv@yandex.ru\n")
        case _:
            bot.send_sticker(message.chat.id, sticker_eror)
            bot.send_message(message.chat.id, f"Извините, {message.from_user.first_name} {message.from_user.last_name},"
                                              f" но на ваш запрос я не могу ответить.")

#Запись данных в фаил на диск
    file = open("logs.txt", "a")
    file.writelines(f"[{message.from_user.first_name} {message.from_user.last_name}] {message.text}\n")
#Работа бота
bot.polling(none_stop = True)
