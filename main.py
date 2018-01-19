# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, JobQueue
import logging
import utilities as utils
import msg
from datetime import datetime, time


token = utils.readToken()

logging.basicConfig (format = '%(asctime)s - %(levelname)s - %(message)s',level = logging.INFO)
logger = logging.getLogger (__name__)

def start (bot, update):
    """Recibe el comando /start"""
    bot.send_message(chat_id = update.message.chat_id, text = msg.infoStartBot)

def error (bot, update, error):
    """Logea los errores causados por los updates"""
    logger.warning ('Update "%s" caused error "%s"', update, error)

def main ():

    updater = Updater(token = token)
    dp = updater.dispatcher
    dp.add_handler (CommandHandler ('start', start))
    dp.add_error_handler (error)
    
    jb = JobQueue(updater.bot)
    jb.run_daily(utils.sendUpdate, time(hour=12, minute=0, second=0))
    jb.start()

#   job_queue.run_repeating(utils.sendUpdate, 5)

    updater.start_polling()
    updater.idle() 

    



if __name__ == "__main__":
    main()
	
