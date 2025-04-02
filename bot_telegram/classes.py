from bot_telegram.config import *

class Student:
    def __init__ (self, chatId):
        self.chatId=chatId
        self.name=students.find_one({ "chatId": self.chatId })["name"]
        self.surname=students.find_one({ "chatId": self.chatId })["surname"]
        self.access=students.find_one({"chatId": self.chatId})["access"]
        self.mentorId=students.find_one({ "chatId": self.chatId })["mentorId"]
        self.center=students.find_one({ "chatId": self.chatId })["center"]
        self.position=students.find_one({ "chatId": self.chatId })["position"]
        self.access=students.find_one({ "chatId": self.chatId })["access"]
        self.run=students.find_one({ "chatId": self.chatId })["run"]
        self.volunteer=students.find_one({ "chatId": self.chatId })["volunteer"]
        self.book=students.find_one({ "chatId": self.chatId })["book"]
        self.insite=students.find_one({ "chatId": self.chatId })["insite"]

class Mentor:
    def __init__ (self, chatId):
        self.chatId=chatId
        self.name=mentors.find_one({ "chatId": self.chatId })["name"]
        self.surname=mentors.find_one({ "chatId": self.chatId })["surname"]
        self.mentorId=mentors.find_one({ "chatId": self.chatId })["mentorId"]
        self.center=mentors.find_one({ "chatId": self.chatId })["center"]
        self.position=mentors.find_one({ "chatId": self.chatId })["position"]
        self.access=mentors.find_one({ "chatId": self.chatId })["access"]
        self.room=mentors.find_one({ "chatId": self.chatId })["room"]
#position (studadmin, onduty)
class Contact:
    def __init__ (self, chatId):
        self.chatId=chatId
        self.name=contacts.find_one({ "chatId": self.chatId })["name"]
        self.surname=contacts.find_one({ "chatId": self.chatId })["surname"]
        self.mentorId=contacts.find_one({ "chatId": self.chatId })["mentorId"]
        self.center=contacts.find_one({ "chatId": self.chatId })["center"]
        self.position=contacts.find_one({ "chatId": self.chatId })["position"]
        self.access=contacts.find_one({ "chatId": self.chatId })["access"]
        self.room=contacts.find_one({ "chatId": self.chatId })["room"]