import telebot
import random
import datetime
from telebot import types
with open ("token.txt", "r") as tok:
    bot_token = str(tok.readlines()[0])
temp_starta = True
temp_realno = False
bot = telebot.TeleBot(bot_token)
spisok = ['Какая фамилия у ректора МТУСИ?','По какому из этип хпредметов у нас в этом семестре зачёт?', 'Гипотенуза это?', 'За какую оценку на экзамене отправляют на пересдачу?', 'Как звали главного персонажа из мультфильма Лунтик?','в какое время суток необходимо выполнять лабораторные работы?','С каким наибольшим количеством ядер производила процессоры компания AMD','Сколько будет 2 + 2 = ?']
varianty_otvetov = [["/1 - Фролов", "/2 - Путин", "/3 - Кадыров", "/4 - Ерохин"],["/1 - Социология","/2 - Философия","/3 - ТОЭ","/4 - физика"], ['/1 - Наша однокурсница','/2 - Одна из прямых в прямоугольном треугольнике','/3 - Вид перелётных птиц','/4 - Вид колбасы'], ['/1 - 2','/2 - 3','/3 - 4','/4 - 5'],['/1 - Валерий','/2 - Сергей','/3 - Лунтик','/4 - Ахмэд'],['/1 - Дневное','/2 - Ночное','/3 - Вечернее','/4 - В любое время суок'],['/1 - 16','/2 - 32','/3 - 64','/4 - 128'],['/1 - 4', '/2 - 28','/3 - 46','/4 - 15']]
otvety = ['/4','/1', '/2','/1','/3','/2','/4', '/1']
otvet = ""
o4ki = 0
count = 1

def na4alo_viktotiny(message):
    global otvet
    global temp_realno
    n_voprosa = random.randint(0, len(spisok)-1)
    otvet = otvety[n_voprosa]
    vopros = spisok[n_voprosa]

    bot.send_message(message.chat.id, f'Внимание вопрос:\n{vopros}')
    temp_realno = True
    bot.send_message(message.chat.id, 'Варианты ответа:')
    for x in range(4):
        bot.send_message(message.chat.id, varianty_otvetov[n_voprosa][x])


@bot.message_handler(commands=['start'])
def start(message):
    global temp_starta
    temp_starta = True
    bot.send_message(message.chat.id, 'Ну дарова, я бот краоче, хочешь ссыль на МТУСИ?\nЕсли что - /help - помощь')


@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, 'Ну кароче:\n/Пятница? - проверяет состояние пятницы\n/Викторина - играть в викторину\n/Анекдот - рассказать анекдот')

@bot.message_handler(commands=['викторина'])
def viktorina(message):
    global count
    count = 1
    na4alo_viktotiny(message)

@bot.message_handler(commands=['пятница?'])
def pyatnitsa(message):
    den_nedely = datetime.datetime.now()
    den_nedely = den_nedely.timetuple().tm_wday+1
    if den_nedely == 5:
        bot.send_message(message.chat.id, 'Так она сегодня!')
    else:
        bot.send_message(message.chat.id, f'Она скоро!')

@bot.message_handler(commands=['анекдот'])
def anek(message):
    aneki = ['Хорошо, что сделали возможность дистанционно закрывать больничный лист.\nПлохо, что потом его надо распечатать, подписать у врача и поставить штамп в регистратуре.', '- Саррочка, какие у вас красивые зубы!\n- Это от мамы!\n- Как подошли!','Сын так часто спрашивал папу: "Мы приехали?", что не доехал до дачи сорок километров.','Слышу кто-то ходит в шкафу. Открываю - а там платья из моды выходят.']
    random_anek = random.randint(0, len(aneki) - 1)
    bot.send_message(message.chat.id, aneki[random_anek])

@bot.message_handler(content_types=['text'])
def answer(message):
    global temp_realno
    global o4ki
    global temp_starta
    global count

    msg = message.text.lower()

    if temp_starta == True:
        if message.text.lower() == "да":
            temp_starta = False
            bot.send_message(message.chat.id, 'Ну и иди сюда – https://mtuci.ru/')


        elif message.text.lower() != "да":
            if message.text.lower() == "нет":
                temp_starta = False
                bot.send_message(message.chat.id, "Ну лан(")

    if (temp_realno == True):
        if(msg.find('/stop') != -1):
            count = 5
            bot.send_message(message.chat.id, f'Викторина окончена досрочно!')
            bot.send_message(message.chat.id, f'У тебя, получается {o4ki*25}/100 о4ков)0)')
            o4ki = 0
        if(count <= 4):
            count+=1
            temp_realno = False
            if msg.find(otvet) != -1:
                bot.send_message(message.chat.id, 'Вна2ре правильно')
                o4ki += 1
                na4alo_viktotiny(message)

            else:
                bot.send_message(message.chat.id, f'Не, брат, ты не прав, правильный ответ:\n {otvet}')
                na4alo_viktotiny(message)
        else:
            temp_realno = False
            bot.send_message(message.chat.id, f'У тебя, получается {o4ki*25}/100 о4ков)0)')
            o4ki = 0

    if message.text.lower() == "GYM":
        bot.send_message(message.chat.id, 'GYM')
        bot.send_message(message.chat.id, 'GYM')

    if message.text.lower() == "-ping":
        bot.send_message(message.chat.id, 'Бот в норме')

    if message.text.lower() == "Кто победил ЧГК?":
        bot.send_message(message.chat.id, 'ЧГК победили GYM, а GYM - это империя')




bot.polling(none_stop=True)

