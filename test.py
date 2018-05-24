import telegram
from telegram.ext import Updater, MessageHandler, Filters
import logging
from telegram.ext import CommandHandler
import funcs
from telegram.ext import Job


bot = telegram.Bot(token='361666590:AAHdyKInEQqDWXinRqDfGiUulKuC1wpJcGA')
updater = Updater(token='361666590:AAHdyKInEQqDWXinRqDfGiUulKuC1wpJcGA')
dispatcher = updater.dispatcher
j = updater.job_queue

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


print(bot.getMe())
print("\n\n\n")


start_handler = CommandHandler('start', funcs.start)
dispatcher.add_handler(start_handler)

updater.start_polling()

echo_handler = MessageHandler(Filters.text, funcs.echo)
dispatcher.add_handler(echo_handler)


caps_handler = CommandHandler('caps', funcs.caps, pass_args=True)
dispatcher.add_handler(caps_handler)


# job_minute = Job(funcs.callback_minute, 5.0)
# j.put(job_minute, next_t=0.0)


# job_minute.enabled = False  # Temporarily disable this job ------ if bezaram, age kanal khali bood chizi nade


# MUST BE at the end of the commands!
unknown_handler = MessageHandler(Filters.command, funcs.unknown)
dispatcher.add_handler(unknown_handler)

#updater.idle()

#bot.sendMessage(chat_id=78858954, text="I'm sorry Dave I'm afraid I can't do that.")


