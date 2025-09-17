import os
from telegram.ext import Application, CommandHandler

TOKEN = os.getenv("8279732556:AAHxlcyvnvVyZalanYTKXrxL2LFx_Ls7s-c")

# دستور start
async def start(update, context):
    await update.message.reply_text("سلام! 👋")

def main():
    app = Application.builder().token(TOKEN).build()

    # اضافه کردن هندلر برای دستور /start
    app.add_handler(CommandHandler("start", start))

    # اجرای ربات با polling
    app.run_polling()

if __name__ == "__main__":
    main()
