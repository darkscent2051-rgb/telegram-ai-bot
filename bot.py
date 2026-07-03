import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model=genai.GenerativeModel("gemini-2.5-flash")
async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your AI bot.")
async def chat(update:Update,context:ContextTypes.DEFAULT_TYPE):
    r=model.generate_content(update.message.text)
    await update.message.reply_text(r.text)
app=Application.builder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start",start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,chat))
app.run_polling()
