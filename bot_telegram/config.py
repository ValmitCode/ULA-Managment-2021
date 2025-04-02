#const texts
START_COMMAND="""Привіт я УАЛ бот для збирання осередкової статистики. Для того щоб почати тобі необхідно зареєструватися за допомогою цієї форми https://forms.gle/EVhuuBsY7xdGFjXs6"""
INFORMATION_COMMAND="""Цей бот був розроблений для автоматизації збору міжосередкової статистики"""
COLLECT_RUN="""Скільки сьогодні км бігу?"""
COLLECT_BOOK="""Скільки книжок прочитано?"""
COLLECT_VOLUNTEER="""Скільки хвилин волонтерства?"""
COLLECT_INSITE="""Скільки написаних інсайтів?"""
COLLECT_END="""Дякую за твій вклад в осередкову статистику)"""
GET_UP_MESSAGE="""Добрий ранок! За 15 хвилин буде ранкова збірка"""
GOODNIGHT_MESSAGE="""Добраніч, завтра важкий день, отже висипайся"""
PROFILE_REMIND_MESSAGE="""Не забувай заповнювати профайл будь ласка). /profile"""


### Bot setting ###
import telebot
BOT_TOKEN=os.getenv("BOT_TOKEN")
from telebot.types import Contact
bot=telebot.TeleBot(BOT_TOKEN)
#Dev id
DEV_ID=os.getenv("DEV_ID")

### Database setting & base funcs ###
from pymongo import MongoClient
DATABASE_LINK=os.getenv("DATABASE_LINK")
clientDB=MongoClient(DATABASE_LINK)
db=clientDB.ualDB
students=db.students
mentors=db.mentors
contacts=db.contacts
centers=db.centers
#const Tokens, link, e.t.c
DATABASE_NAME="ualDB"

### Google sheets setting ###
from oauth2client.service_account import ServiceAccountCredentials
import gspread
SCOPES = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
clientGoogle = gspread.authorize(ServiceAccountCredentials.from_json_keyfile_name('bot_telegram/ula-digital.json', SCOPES))
# Sheet links
USER_REGISTER_LINK=os.getenv("USER_REGISTER_LINK")
MENTOR_REGISTER_LINK=os.getenv("MENTOR_REGISTER_LINK")
CONTACTS_LINK=os.getenv("CONTACTS_LINK")
    

    



