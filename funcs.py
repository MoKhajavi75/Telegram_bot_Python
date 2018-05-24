def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="")


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="الان داری می سوزی احسان؟")


def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)


def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


def callback_minute(bot, job):
    bot.sendMessage(chat_id=78858954, text='One message every minute')

