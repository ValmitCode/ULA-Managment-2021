import smtplib
import bot_telegram.config as config
from bot_telegram.config import *
import schedule
import time
from bot_telegram.classes import Student
import matplotlib.pyplot as plt
#import pandas

###DEVELOPER FUNCS
def bug_report(err):
    bot.send_message(config.DEV_ID, "New bug:" + err)
    
def log(msg=""):
    f = open("log.txt", "a")
    f.write(str(time.time())+msg+"\n")
    f.close()

def notification(msg, group="all"):
    chats=students.distinct("chatId")
    for chatId in chats:
        bot.send_message(chatId, msg)

def mentor_permission(message):
    if mentors.find_one({"chatId": message.chat.id}) != None:
        return True
    else: 
        return False
###USERS FUNCS###

def report (funcname, name, surname, msg):
    return (funcname+" від "+name+" "+surname+": "+msg)
    log(funcname+" від "+name+" "+surname+": "+msg)

def send_statistic_collect(message):
    bot.send_message(message.chat.id, config.COLLECT_RUN)
    bot.register_next_step_handler(message, ask_for_run) 

def ask_for_run(message):
    if students.find_one({"chatId": message.chat.id}) != 0:
        students.update_one(
        { "chatId": message.chat.id },
        { '$inc': { "run": int(message.text) } }
        ) 
    bot.send_message(message.chat.id, config.COLLECT_BOOK)
    bot.register_next_step_handler(message, ask_for_book)

def ask_for_book(message):
    if students.find_one({"chatId": message.chat.id}) != 0:
        students.update_one(
        { "chatId": message.chat.id },
        { '$inc': { "book": int(message.text) } }
        ) 
    bot.send_message(message.chat.id, config.COLLECT_INSITE)
    bot.register_next_step_handler(message, ask_for_insite)

def ask_for_insite(message):
    if students.find_one({"chatId": message.chat.id}) != 0:
        students.update_one(
        { "chatId": message.chat.id },
        { '$inc': { "insite": int(message.text) } }
        ) 
    bot.send_message(message.chat.id, config.COLLECT_VOLUNTEER)
    bot.register_next_step_handler(message, ask_for_volunteer)

def ask_for_volunteer(message):
    if students.find_one({"chatId": message.chat.id}) != 0:
        students.update_one(
        { "chatId": message.chat.id },
        { '$inc': { "volunteer": int(message.text) } }
        ) 
    bot.send_message(message.chat.id, config.COLLECT_END)

def send_statistics_report(message):
    user = Student(message.chat.id)
    print(user)
    totalRun = students.aggregate([ { "$group": { "_id": "$center", "total": { "$sum": "$run" } } } ] )
    totalBook = students.aggregate([ { "$group": { "_id": "$center", "total": { "$sum": "$book" } } } ] )
    totalInsite = students.aggregate([ { "$group": { "_id": "$center", "total": { "$sum": "$insite" } } } ] )
    totalVolunteer = students.aggregate([ { "$group": { "_id": "$center", "total": { "$sum": "$volunteer" } } } ] )
    for i in totalRun:
        centers.update_one(
        { "city": user.center },
        { '$set': { "run": i["total"]} }
        )
    for i in totalBook:
        centers.update_one(
        { "city": user.center },
        { '$set': { "book": i["total"]} }
        ) 
    for i in totalInsite:
        centers.update_one(
        { "city": user.center },
        { '$set': { "insite": i["total"]} }
        ) 
    for i in totalVolunteer:
        centers.update_one(
        { "city": user.center },
        { '$set': { "volunteer": i["total"]} }
        )   
    
#petition
def message_to_mentor(message, reason):
    user = Student(message.chat.id)
    if reason=="petition":
        textSend=report("Петиція", user.name, user.surname, message.text)
    elif reason=="conversation_request":
        textSend=report("Запит на менторську розмову", user.name, user.surname, message.text)
    elif reason=="application_department":
        textSend=report("Заявка в департамент", user.name, user.surname, message.text)
    else:
        log("unknown reason")
    bot.send_message(user.mentorId, textSend)
    log(textSend)

def scheduler():
    schedule.every().day.at('06:45').do(notification, config.GET_UP_MESSAGE)
    schedule.every().day.at('20:00').do(notification, config.PROFILE_REMIND_MESSAGE)
    schedule.every().day.at('23:00').do(notification, config.GOODNIGHT_MESSAGE)
    schedule.every().day.at('03:00').do(users_register_form)
    schedule.every().day.at('04:00').do(mentors_register_form)
    schedule.every().day.at('05:00').do(contacts_collector)
    while True:
        schedule.run_pending()
        time.sleep(1)


###GOOGLE SHEETS FUNCS###
def users_register_form():
    sheet=clientGoogle.open_by_url(config.USER_REGISTER_LINK)
    sheetlist=sheet.get_worksheet(0)
    j=2
    while sheetlist.cell(row=j, col=2).value!=None:
        if students.find_one({"chatId": sheetlist.cell(row=j, col=6).value})==None:
            students.insert_one({
                "name": sheetlist.cell(row=j,col=2).value,
                "surname": sheetlist.cell(row=j, col=3).value,
                "access": "user",
                "center": sheetlist.cell(row=j, col=4).value,
                "chatId": sheetlist.cell(row=j, col=6).value,
                "position": sheetlist.cell(row=j, col=5).value,
                "mentorId": sheetlist.cell(row=j, col=7).value,
                "book": 0,
                "insite": 0,
                "run": 0,
                "volunteer": 0
                })
        j+=1

def mentors_register_form():
    print("Build")
def contacts_collector():
    print("Build")

###CONTACT SPAMMERS###
def send_email(msg="", emailFrom="", emailFromPass="", accName="eu",emailList=[]):
    import smtplib
    BODY = "\r\n".join((
        "From: %s" % "",
        "To: %s" % "",
        "Subject: %s" % accName,
        "",
        msg
    ))
    try:
        server=smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(emailFrom, emailFromPass)
        server.sendmail(emailFrom, emailList, BODY) 
        server.close()
    except Exception as e:
        print(e)
        log(str(e))
        pass
def email_spammer(contactsLink=config.CONTACTS_LINK, column=0, msg=""):
    sheet=clientGoogle.open_by_url(contactsLink)
    sheetlist=sheet.get_worksheet(0)
    receivers=[i for i in sheetlist.col_values(12) if i!=None]
    receivers.pop(0)
    receivers.extend("developmentual@gmail.com")
    send_email(msg, emailList=receivers)

