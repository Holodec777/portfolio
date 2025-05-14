import telebot
from telebot import types
import json
import os

API_TOKEN = 'YOUR TOKEN'
bot = telebot.TeleBot(API_TOKEN)

password = 'enter password'
student_password = 'enter password'

EVENTS_FILE = 'events.json'
TEACHERS_FILE =  'teachers_data.json'
STUDENTS_FILE = 'students_data.json'

events = {}

teachers = []
students = []

global name, description

def load_events():
    global events
    if os.path.exists(EVENTS_FILE):
        with open(EVENTS_FILE, 'r') as file:
            events = json.load(file)

def save_events():
    with open(EVENTS_FILE, 'w') as file:
        json.dump(events, file)

#ДАННЫЕ УЧИТЕЛЕЙ
def load_teachers_data():
    global teachers
    if os.path.exists(TEACHERS_FILE):
        with open(TEACHERS_FILE, 'r') as file:
            teachers = json.load(file)

def save_teachers_data():
    with open(TEACHERS_FILE, 'w') as file:
        json.dump(teachers, file)

#ДАННЫЕ УЧАЩИХСЯ
def load_students_data():
    global students
    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, 'r') as file:
            students = json.load(file)

def save_students_data():
    with open(STUDENTS_FILE, 'w') as file:
        json.dump(students, file)

#РЕГИСТРАЦИЯ УЧИТЕЛЕЙ
def process_teacher_password(message):
    password_input = message.text

    if password_input == password:
        login_success_teacher(message)
    else:
        login_failed_teacher(message)

def login_success_teacher(message):
    if message.chat.id not in teachers:

        teachers.append(message.chat.id)
        save_teachers_data()

    bot.send_message(message.chat.id, 'Вы вошли в систему как учитель.')
    event_panel_teachers(message)

def login_failed_teacher(message):
    bot.send_message(message.chat.id, 'Неверный пароль. Попробуйте еще раз.')
    bot.register_next_step_handler(message, process_teacher_password)

#ВИДЖЕТЫ УЧИТЕЛЕЙ
def event_panel_teachers(message):
    event_keyboard = types.InlineKeyboardMarkup(row_width=1)

    event_btn_1 = types.InlineKeyboardButton(text='Создать мероприятие', callback_data='create_event')

    event_keyboard.add(event_btn_1)

    bot.send_message(message.chat.id, 'Теперь вы можете управлять мероприятиями!', reply_markup=event_keyboard)

def create_event_start(message):
    bot.send_message(message.chat.id, 'Введите имя мероприятия:')
    bot.register_next_step_handler(message, process_event_name)

def process_event_name(message):
    global name
    name = message.text

    bot.send_message(message.chat.id, 'Введите описание мероприятия, прикрепите ссылку на регистрацию:')
    bot.register_next_step_handler(message, process_event_description)

def process_event_description(message):

    send_keyboard = types.InlineKeyboardMarkup(row_width=1)
    send_btn = types.InlineKeyboardButton(text='отправить', callback_data = 'send')

    send_keyboard.add(send_btn)

    global description
    description = message.text
    bot.send_message(message.chat.id, f'Приглашение будет выглядеть так: \nВы были приглашены на мероприятие! \n {name} \n {description}')
    bot.send_message(message.chat.id, f'отправить приглашение: ', reply_markup=send_keyboard)

def send_event(message):
    for user_id in students:
        try:
            bot.send_message(user_id, f"Вы были приглашены на мероприятие \n \n {name} \n \n {description}")

        except Exception as e:
            bot.reply_to(message, f"Отправлено")

#РЕГИСТРАЦИЯ УЧАЩИХСЯ
def process_student_password(message):
    password_input = message.text

    if password_input == student_password:
        login_success_student(message)
    else:
        login_failed_student(message)

def login_success_student(message):
    if message.chat.id not in students:
        students.append(message.chat.id)
        save_students_data()

    bot.send_message(message.chat.id, 'Вы вошли как учащийся')
    event_panel_students(message)

def login_failed_student(message):
    bot.send_message(message.chat.id, 'Неверный пароль. Попробуйте еще раз.')
    bot.register_next_step_handler(message, process_teacher_password)

#ВИДЖЕТЫ УЧАЩИХСЯ
def event_panel_students(message):

    student_panel_keyboard = types.InlineKeyboardMarkup(row_width=1)
    student_panel_button = types.InlineKeyboardButton(text = 'Посмотреть доступные мероприятия', callback_data='show_events')

    student_panel_keyboard.add(student_panel_button)

    bot.send_message(message.chat.id, 'Теперь вы будете получать уведомления о новых мероприятиях. Также вы можете посмотреть доступные мероприятия.',
                     reply_markup= student_panel_keyboard)

@bot.message_handler(commands=['start'])
def start(message):
    register_keyboard = types.InlineKeyboardMarkup(row_width=1)

    register_btn_1 = types.InlineKeyboardButton(text='Я преподаватель', callback_data='register_teacher')
    register_btn_2 = types.InlineKeyboardButton(text='Я учащийся', callback_data='register_student')

    register_keyboard.add(register_btn_1, register_btn_2)

    bot.send_message(message.chat.id, 'Для начала работы войдите в систему:', reply_markup=register_keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    if call.data == 'register_teacher':
        bot.send_message(call.message.chat.id, 'Введите пароль (если у вас нет пароля обратитесь за ним к админимтратору):')
        bot.register_next_step_handler(call.message, process_teacher_password)

    elif call.data == 'register_student':

        bot.send_message(call.message.chat.id, 'Введите пароль (если у вас нет пароля обратитеь за ним к преподавателю)')
        bot.register_next_step_handler(call.message, process_student_password)

    elif call.data == 'create_event':
        create_event_start(call.message)

    elif call.data == 'send':
        send_event(call.message)
        events.update({name:description})
        save_events()

    elif call.data == 'show_events':

        if events:

            for key, value in events.items():
                print(key, value)
                bot.send_message(call.message.chat.id, f'{key} \n \n{value}')

        else:
            bot.send_message(call.message.chat.id, f'Для вас пока нет дооступных мероприятий')

load_students_data()
load_teachers_data()

load_events()

bot.polling()