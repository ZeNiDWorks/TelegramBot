import telebot
from telebot import types

# Qui sotto dovrai inserire il tuo token generabile da BotFather
# Metti il token fra le due ""
TOKEN = "Inserisci il tuo token"

bot = telebot.TeleBot(TOKEN)

# Quando un utente farà /start o /help il bot invierà un testo con sotto dei bottoni
@bot.message_handler(commands=['start', 'help'])
def comando_start(message):
    markup = types.InlineKeyboardMarkup()

    # Qui invece sono presenti i bottoni e sono in tutto 3 
    # Dovrai inserire il testo che vedranno gli utenti sui bottoni
    # dove c'è 'url=', inserisci il link dove vuoi che il bottone reindirizzi gli utenti (ad esempio un canale telegram)
    # Metti il testo e il link sempre fra le due ""
    bottone1 = types.InlineKeyboardButton("Inserisci il tuo Testo", url="Inserisci il tuo Link")
    bottone2 = types.InlineKeyboardButton("Inserisci il tuo Testo", url="Inserisci il tuo Link")
    bottone3 = types.InlineKeyboardButton("Inserisci il tuo Testo", url="Inserisci il tuo Link")

    # Qui trovi l'ordine dei bottoni in questo caso il bottone1 si trova sopra e gli altri due sotto nella stessa riga
    # Puoi riordina i bottoni come vuoi tu, metterli tutti anche su una stessa riga
    markup.row(bottone1)
    markup.row(bottone2, bottone3)
    
    # Qui è presente il testo che sarà inviato sopra i bottoni
    # Metti il testo sempre fra le due ""
    bot.send_message(message.chat.id, "Inserisci il tuo Titolo", parse_mode="Markdown", reply_markup=markup)

# Questo è un comando che ti ho aggiunto in più
# Appena un utente fa /id il bot manda l'id dell'esecutore del comando
@bot.message_handler(commands=['id'])
def comando_id(message):
    bot.send_message(message.chat.id, "Il tuo ID » " + str(message.from_user.id) + ".")

# Se desideri lasciarmi i crediti non toccare questo parte di comando sotto altrimenti eliminala
@bot.message_handler(commands=['info'])
def comando_id(message):
    bot.send_message(message.chat.id, "Il Bot è stato creato da @Impallinare in Python 3.")


#Non toccare la parte di codice qui sotto o il Bot non partirà mai.
print("Bot Correttamente Avviato!")
bot.polling(none_stop=True)
