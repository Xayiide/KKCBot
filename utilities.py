import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, JobQueue



release = datetime.date(2020, 8, 20)

def readToken ():
	with open ('token.txt', 'r') as f:
		return f.readline().strip("\n")

def calculateDays():
    today = datetime.date.today()
    return release - today

def days(numDays):
    return str(numDays) + " days left until 2020.20.8!"


def sendUpdate(bot, job):
    bot.send_message(chat_id='@KKCRelease', text=days(calculateDays().days))
