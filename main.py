o# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHanddler, Filters
import logging
import utilities as utils

token = utils.readToken()

logging.basicConfig (format = '%(asctime)s - %(levelname)s - %(message)s',level = logging.INFO)
logger = logging.getLogger (__name__)

def start (bot, update):
	"""Recibe el comando star"""

	bot.send_message (chat_id = update.message.chat_id, text = "argo")


def unknown (bot, update):
	"""Manda un mensaje en el caso de que no conozca el comando"""
	
	bot.send_message (chat_id = update.message.chat_id, text = "ja")


def error (bot, update, error):
	"""Logea los errores causados por los updates"""

	logger.warning ('Update "%s" caused error "%s"', update, error)

def main ():

	updater = Updater(token = token)

	dp = updater.dispatcher

	dp.add_handler (CommandHandler ('start', start))

	dp.add_error_handler (error)

	dp.add_handler (MessageHandler (Filters.command, unknown))

	updater.start_polling()
	updater.idle()

if __name__ == "__main__":
	main()
	
