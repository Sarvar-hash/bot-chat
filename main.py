import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler
from handlers import start_command
import os
from dotenv import load_dotenv

load_dotenv()  # .env faylidan TOKEN ni yuklaydi

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    print("🤖 Bot ishga tushdi...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
