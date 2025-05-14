import telebot
from telebot import types

import gspread
from oauth2client.service_account import ServiceAccountCredentials

def maxdata(): # функция для выгрузки полученных данных в гугл таблицы

    global date, username, problem, segmentname, coursename

    scope = ['https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\79062\PycharmProjects\maxbot\maxbot-430608-2b2b254a2a6e.json', scope)

    client = gspread.authorize(creds)

    spreadsheet = client.open('maxbot') # открывает таблицу maxbot

    try: # Проверяет, есть ли лист с названием из переменной segmentname
        new_sheet = spreadsheet.worksheet(f'Лист {segmentname}')

        if new_sheet.acell('A1').value != 'Дата опечатки': # Проверяет, есть ли данные из dataname в листе
            dataname = [
                ['Дата опечатки', 'Кто прислал', 'Сегмент', 'Курс', 'Текст опечатки'],
            ]
            new_sheet.insert_row(dataname[0], 1)

    except gspread.exceptions.WorksheetNotFound: # создает новый лист, если листа не существует

        new_sheet = spreadsheet.add_worksheet(f'Лист {segmentname}', 1000, 5)
        dataname = [
            ['Дата опечатки', 'Кто прислал', 'Сегмент', 'Курс', 'Текст опечатки'],
        ]
        new_sheet.insert_row(dataname[0], 1)

    data = [
        [problem, date, segmentname, coursename, username],
    ]

    new_sheet.insert_row(data[0], 2) # загружает данные из (data) со второй строки

token = 'YOUR_TOKEN'
bot = telebot.TeleBot(token)

states = {} # словарь для определения номера сообщения в чате
def copy_problem(message): # копирует текст опечтки от пользователя

    global  problem
    problem = message.text

def copy_username(message): # копирует имя пользователя

    global username
    username = message.text

def copy_date(message): #копирует дату, которую вводит пользователь

    global date
    date = message.text

def changetext(callback): # отправляет новое сообщение, когда пользователь выбрал курс и сегмент

    bot.send_message(chat_id=callback.message.chat.id, text='опишите подробно где (в каком задании, в каком слове и т. д.) вы обнаружили ошибку')

def course(callback): # inline клавиатура для выбра курса

    Course_KeyBoard = types.InlineKeyboardMarkup(row_width=1)

    Course_Button_1 = types.InlineKeyboardButton(text= '8 класс', callback_data='Course_Button_1')
    Course_Button_2 = types.InlineKeyboardButton(text= '9 класс', callback_data='Course_Button_2')
    Course_Button_3 = types.InlineKeyboardButton(text='10 класс', callback_data='Course_Button_3')
    Course_Button_4 = types.InlineKeyboardButton(text='11 класс', callback_data='Course_Button_4')

    Course_KeyBoard.add(Course_Button_1, Course_Button_2, Course_Button_3, Course_Button_4)

    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='выберите курс, в котором была найдена опечатка', reply_markup=Course_KeyBoard)

@bot.message_handler (commands=['start'])
def start(message): # inline клавиатура для выбора сегмента

    chat_id = message.chat.id
    states[chat_id] = 1

    KeyBoard = types.InlineKeyboardMarkup(row_width = 1)

    Segment_Button_1 = types.InlineKeyboardButton(text=   'русский язык', callback_data='Segment_Button_1')
    Segment_Button_2 = types.InlineKeyboardButton(text=     'математика', callback_data='Segment_Button_2')
    Segment_Button_3 = types.InlineKeyboardButton(text=    'информатика', callback_data='Segment_Button_3')
    Segment_Button_4 = types.InlineKeyboardButton(text=         'физика', callback_data='Segment_Button_4')
    Segment_Button_5 = types.InlineKeyboardButton(text=        'история', callback_data='Segment_Button_5')
    Segment_Button_6 = types.InlineKeyboardButton(text= 'обществознание', callback_data='Segment_Button_6')
    Segment_Button_7 = types.InlineKeyboardButton(text='английский язык', callback_data='Segment_Button_7')
    Segment_Button_8 = types.InlineKeyboardButton(text=       'биология', callback_data='Segment_Button_8')
    Segment_Button_9 = types.InlineKeyboardButton(text=          'химия', callback_data='Segment_Button_9')

    DS_Main_button = types.InlineKeyboardButton(text=     'digital skills', callback_data='DS_Main_Button')

    KeyBoard.add(Segment_Button_1, Segment_Button_2, Segment_Button_3, Segment_Button_4, Segment_Button_5, Segment_Button_6, Segment_Button_7, Segment_Button_8, Segment_Button_9, DS_Main_button)

    bot.send_message(message.chat.id, 'Выберите сегмент, в котором была обнаружена опечатка:', reply_markup=KeyBoard)

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):

    global segmentname, coursename

    if callback.data == 'DS_Main_Button':

        DS_KeyBoard = types.InlineKeyboardMarkup(row_width=1)

        DS_Button_1 = types.InlineKeyboardButton(text=  'программирование', callback_data='DS_Button_1')
        DS_Button_2 = types.InlineKeyboardButton(text='графический дизайн', callback_data='DS_Button_2')
        DS_button_3 = types.InlineKeyboardButton(text=         'маркетинг', callback_data='DS_button_3')

        DS_KeyBoard.add(DS_Button_1, DS_Button_2, DS_button_3)

        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='выберите курс, в котором была найдена опечатка', reply_markup=DS_KeyBoard)

    elif callback.data == 'DS_Button_1':

        segmentname = 'программирование'
        course(callback)

    elif callback.data == 'DS_Button_2':

        segmentname = 'графический дизайн'
        course(callback)

    elif callback.data == 'DS_button_3':

        segmentname = 'маркетинг'
        course(callback)

    elif callback.data == 'Segment_Button_1':

        segmentname = 'русский язык'
        course(callback)

    elif callback.data == 'Segment_Button_2':

        segmentname = 'математика'
        course(callback)

    elif callback.data == 'Segment_Button_3':

        segmentname = 'информатика'
        course(callback)

    elif callback.data == 'Segment_Button_4':

        segmentname = 'физика'
        course(callback)

    elif callback.data == 'Segment_Button_5':

        segmentname = 'история'
        course(callback)

    elif callback.data == 'Segment_Button_6':

        segmentname = 'обществознание'
        course(callback)

    elif callback.data == 'Segment_Button_7':

        segmentname = 'английский язык'
        course(callback)

    elif callback.data == 'Segment_Button_8':

        segmentname = 'биология'
        course(callback)

    elif callback.data == 'Segment_Button_9':

        segmentname = 'химия'
        course(callback)

    if callback.data == 'Course_Button_1':

        coursename = '8 класс'
        changetext(callback)

    elif callback.data == 'Course_Button_2':

        coursename = '9 класс'
        changetext(callback)

    elif callback.data == 'Course_Button_3':

        coursename = '10 класс'
        changetext(callback)

    elif callback.data == 'Course_Button_4':

        coursename = '11 класс'
        changetext(callback)

@bot.message_handler(content_types=['text']) # срабатывает, когда пользователь отправляет сообщение
def handle_text(message):
    chat_id = message.chat.id
    copy_problem(message)

    if chat_id in states:
        state = states[chat_id]

        if state == 1:
            bot.send_message(chat_id, 'Введите ваши ФИО')
            states[chat_id] = 2

            copy_username(message)

        elif state == 2:
            bot.send_message(chat_id, 'Введите сегодняшнюю дату в формате ГГГГ-ММ-ДД')
            states[chat_id] = 3

            copy_date(message)

        elif state == 3:
            bot.send_message(chat_id, 'Информация об ошибке успешно отправлена. Если вы хотите отправить информацию еще об одной ошибке, перезапустите бота при помощи команды /start. ')
            states[chat_id] = 1

            maxdata()

    else: # отправляется пользователю, если он пытается отправить сообщение после заполнения всех данных или при ошибке работы бота
        bot.send_message(chat_id, 'Пожалуйста, перезапустите бота при помощи команды /start и побробуйте еще раз.')

bot.polling()