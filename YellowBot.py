#5626050890:AAG6afiS6Zzwf7vlB41n_Z11na_b1uhvVAU#ТОКЕН(уникальное имя бота)
import telebot    #импортируем необходимую библиотеку
from telebot import types   #импортировали библиотеку для создания кнопок в телеботе
from PIL import Image,ImageFilter
token = '5626050890:AAG6afiS6Zzwf7vlB41n_Z11na_b1uhvVAU'#здесь имя, полученное у @BotFather
bot = telebot.TeleBot(token) #объект класса Telebot
#Приветственная надпись
@bot.message_handler(commands=['start'])#Обработчик, который отвечает любое входящее сообщение.Для обработки команд нам потребуется message_handler, с помощью которого и будет реализован весь функционал обработки команд для старта и завершения
def welcome (message):
    first_message = bot.send_message(message.chat.id, "Как я могу к Вам обращаться?")
    bot.register_next_step_handler(first_message,hello) #Функция register_next_step_handler, принимающая в аргументы объект отправленного сообщения и имя следующей функции def hello отвечает за то, что следующее сообщение от пользователя будет обработано функцией hello.
def hello(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # класс кнопок #количество кнопок в одной строке 1
    second_message = bot.send_message(message.chat.id,'Здравствуйте, <b><i>{name}</i></b>. Я Александра, администратор детской IT-школы Yellow Club \u263a\ufe0f'.format(name=message.text),parse_mode="html")#выведи имя пользователя в формате текста и reply_markup означает то, что после этого сообщения пользователь обязательно должен на что-то кликнуть из кнопок
    website = types.KeyboardButton("Посетить наш сайт")
    programma = types.KeyboardButton("Программа на первый учебный год")
    price = types.KeyboardButton("Узнать стоимость занятий")
    make_an_appointment = types.KeyboardButton("Записаться на пробное занятие")
    markup.add(website, programma, price, make_an_appointment) #кнопка Посетить сайт в переменной site)#  в класс кнопок добавляем созданную кнопку "site"
    third_message = bot.send_message(message.chat.id, "Чем могу Вам помочь?", reply_markup = markup)
    bot.register_next_step_handler(third_message, choice)
def choice(message):
    if message.text =="Посетить наш сайт":
        bot.send_message(message.chat.id,"Добро пожаловать в <b>YellowClub</b> https://yellowclub.by/",parse_mode="html")
        fouth_message = bot.send_message(message.chat.id, "Чем я еще могу помочь?")
        bot.register_next_step_handler(fouth_message, choice)
    elif message.text =="Программа на первый учебный год":
        bot.send_photo(message.chat.id, photo=open('D:\Новый сайт\программа учебного года.jpg', 'rb'))
        fouth_message = bot.send_message(message.chat.id, "Чем я еще могу помочь?")
        bot.register_next_step_handler(fouth_message, choice)
    elif message.text =="Узнать стоимость занятий":
        bot.send_message(message.chat.id,"Занятия проходят <b>1 раз в неделю</b>, длится занятие <b>1,5 часа</b> с возможностью перерыва на отдых.\nВ группах <b>до 5 учеников</b>.\nСтоимость абонемента на месяц(4 занятия) составляет <b>190 BYN</b>",parse_mode="html")
        fouth_message = bot.send_message(message.chat.id, "Чем я еще могу помочь?")
        bot.register_next_step_handler(fouth_message, choice)
    elif message.text == "Записаться на пробное занятие":
        bot.send_message(message.chat.id,"Напишите <b> фамилию, имя, возраст</b> ребенка,\n выберите учебный класс: <b>Коласа,3</b> или <b>Мстиславца,6</b>,\n номер для связи: ",parse_mode="html")
        fouth_message = bot.send_message(message.chat.id, "Чем я еще могу помочь?")
        bot.register_next_step_handler(fouth_message,choice)
    else:
        bot.send_message(message.chat.id,
                         "Если у Вас остались еще вопросы - оставьте Ваш контактный номер")

@bot.message_handler(content_types=['text'])
def number (message):
    if message.text.isdigit():
        bot.send_message(message.chat.id, "Cпасибо, мы с Вами свяжемся\n                    /start")
    else:
        bot.send_message(message.chat.id, "Хорошего Вам дня \n          /start")

bot.polling(none_stop=True)
