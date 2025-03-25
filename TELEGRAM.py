from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import ZETA_AI
import threading
from telegram import Bot
import time


def GetUsers():
    f = (open("./Brain/PERSONS.txt","r").read()).split("\n")
    x = 1
    y = []
    z =[]
    for i in f:
        z.append(i)
        if x == 2:
            y.append(z)
            z = []
            x = 0
        x +=1

    return y

def AddUser(id,name):
    f = open("./Brain/PERSONS.txt","a")
    f.write(f"\n{id}\n{name}")
    f.close()


        
ZETA = ZETA_AI.AI("AIzaSyDDdarIZF1rp-pvHyJxdKUK1Un6jVPwZFk")

class TelegramBOT:
    def __init__(self, TOKEN):
        # Bot için gerekli ayarları yap
        self.updater = Updater(TOKEN)
        self.bot = Bot(TOKEN)
        self.dispatcher = self.updater.dispatcher

        self.total_message = 0

        # Kullanıcı verilerini saklamak için bir liste
        self.user_data = GetUsers()
        print(GetUsers())
        # Komut ve mesaj işleyicilerini ekle
        self.add_handlers()

    def add_handlers(self):
        # Komutlar
        self.dispatcher.add_handler(CommandHandler("start", self.start))
        self.dispatcher.add_handler(CommandHandler("help", self.help_command))
        self.dispatcher.add_handler(CommandHandler("kayit", self.kayit))
        self.dispatcher.add_handler(CommandHandler("yetki", self.yetki))
        self.dispatcher.add_handler(CommandHandler("yetkiver", self.yetkiver))
        self.dispatcher.add_handler(CommandHandler("sahne", self.sahne))
        self.dispatcher.add_handler(CommandHandler("test", self.test))
        self.dispatcher.add_handler(CommandHandler("foto", self.foto))







        # Mesaj işleyici
        self.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.echo))
    def kayit(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text("----")
        ZETA.TESTAREA()
        update.message.reply_text("####")

    def test(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text("----")
        update.message.reply_text(ZETA.TESTPROMT())
        update.message.reply_text("####")


    def sahne(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text(ZETA.olayani())


    def foto(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text(ZETA.Photo())

    def yetki(self, update: Update, context: CallbackContext) -> None:
        chat_id = str(update.message.chat.id)
        if chat_id == "7933653406":
            update.message.reply_text("Merhabalar ErkamBey yetki vermek için aşağıdaki şablonu kopyalayarak kullabilirsiniz.")
            update.message.reply_text("/yetkiver id isim")



    def yetkiver(self, update: Update, context: CallbackContext) -> None:
            chat_id = str(update.message.chat.id)
            if chat_id == "7933653406":
                user_message = (update.message.text).split(" ")
                AddUser(user_message[1],user_message[2])
                update.message.reply_text(f"Kişiye [{user_message[2]}] yetki verilmiştir kodu : [{user_message[1]}]")
                self.user_data = GetUsers()


    def start(self, update: Update, context: CallbackContext) -> None:
        # Başlangıç mesajı
        update.message.reply_text("Merhaba!. Sana nasıl yardımcı olabilirim? 😊")

    def help_command(self, update: Update, context: CallbackContext) -> None:
        # Yardım mesajı
        update.message.reply_text("Kullanabileceğin komutlar:\n/start - Botu başlat\n/help - Yardım al")

    def echo(self, update: Update, context: CallbackContext) -> None:

        # Kullanıcı mesajını kaydet ve yanıtla
        user_message = update.message.text
        chat_id = str(update.message.chat.id)

        yetki = 0

        for user in self.user_data:
            if user[0] == chat_id:

                print(f"Kayıtlı Kullanıcı: {user[1]}")  # Kaydedilen veriyi konsolda göster

                # Mesaja yanıt ver
                promt = f" [KONUŞAN KİŞİ : {user[1]}] : {user_message}"
                yetki = 1

                cevap = ZETA.Ask(promt)
                #cevap = ZETA.questionitself()
                print(cevap)
                
                #CEVAP TUM OLAY

                try:
                    update.message.reply_text(cevap,parse_mode="MarkDown")
                except:
                    update.message.reply_text(cevap)


                self.total_message +=1
                if self.total_message >= 10:
                    thread = threading.Thread(target=ZETA.TESTAREA())
                    thread.daemon = True  # Program kapanırken thread'in kapanmasını sağlar
                    thread.start()
                    self.total_message  = 0
        

        if yetki == 0:
                print("Yetkisiz ERİŞİM")
                update.message.reply_text(f"ERİŞİM KODU. {chat_id}.")
                    



    def run(self):
        # Botu başlat
        print("Bot çalışıyor... Telegram'da botunuzu kontrol edin!")
        self.updater.start_polling()
        self.updater.idle()


    def sifirdancevap(self) -> None:
            while True:
                print("SORGU")
                time.sleep(1200)
                cvp = ZETA.questionitself()
                print(cvp)
                if cvp:
                    self.bot.send_message(chat_id=7933653406,text=cvp)

        

# Ana program
if __name__ == "__main__":
    # BotFather'dan aldığınız tokeni buraya ekleyin
    TOKEN = "7611812339:AAEkyEyCP2_-DZgopfPdNOY3e8xAh8thMno"

    # Botu oluştur ve çalıştır
    bot = TelegramBOT(TOKEN)
    thread = threading.Thread(target=bot.sifirdancevap)
    thread.daemon = True  # Program kapanırken thread'in kapanmasını sağlar
    thread.start()
    bot.run()

