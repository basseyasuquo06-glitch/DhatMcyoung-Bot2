from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Professional branding
TOKEN = "8668969527:AAGmWkKGCF5s02aFNvByPqEo3sW7kVr9lRA"
ADMIN_ID = 1128630065  

# 1. The Start Menu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["✅ Available Trades", "⏳ Running Trades"],
        ["💰 Close Trades", "📊 Monthly Performance"],
        ["🏧 Deposit", "▶️ Goto MT5"],
        ["📚 MT5 Training", "📚 Mentorship"],
        ["👨🏽‍💻 Channel", "👨🏽‍💻 Support"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Welcome to DHATMCYOUNG Signals 👩🏽‍💻📈\nChoose an option:",
        reply_markup=reply_markup
    )

# 2. Manual Update Commands (Admin Only)
async def update_trades(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Only allow YOU to change the trades
    if update.effective_user.id != ADMIN_ID:
        return

    text = " ".join(context.args)
    if not text:
        await update.message.reply_text("Usage: /setavailable GBPAUD SELL 📉")
        return
    
    command = update.message.text.split()[0]
    
    if command == "/setavailable":
        context.bot_data['available'] = text
        await update.message.reply_text("✅ Available Trades Updated!")
    elif command == "/setrunning":
        context.bot_data['running'] = text
        await update.message.reply_text("⏳ Running Trades Updated!")
    elif command == "/setclose":
        context.bot_data['close'] = text
        await update.message.reply_text("💰 Close Trades Updated!")

# 3. Handling Button Clicks
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == "✅ Available Trades":
        # Pulls the text you set manually
        msg = context.bot_data.get('available', "No active signals. Awaiting entry... 👨🏽‍💻")
        await update.message.reply_text(f"🔥 *AVAILABLE TRADES* 🔥\n\n{msg}", parse_mode="Markdown")

    elif text == "⏳ Running Trades":
        msg = context.bot_data.get('running', "No trades currently running. 📉")
        await update.message.reply_text(f"⏳ *RUNNING TRADES* ⏳\n\n{msg}", parse_mode="Markdown")

    elif text == "💰 Close Trades":
        msg = context.bot_data.get('close', "No recently closed trades. ✅")
        await update.message.reply_text(f"💰 *CLOSED TRADES* 💰\n\n{msg}", parse_mode="Markdown")

    elif text == "🏧 Deposit":
        await update.message.reply_text("Fund your account on Exness here:\nhttps://my.exness.com/")

    elif text == "▶️ Goto MT5":
        await update.message.reply_text("Launch MetaTrader 5:\nhttps://metatrader5.com/download")

    elif text == "📚 Mentorship":
        await update.message.reply_text("Level up your skills. Contact me for 1-on-1 Mentorship:\n@dhatmcyoung")

    elif text == "👨🏽‍💻 Channel":
        await update.message.reply_text("Join the official DHATMCYOUNG Channel:\nhttps://t.me/+RWV4PadJa4YxYjA8")

    elif text == "📊 Monthly Performance":
        performance_report = "📈 *Performance*\n\n• Trades Closed: 7\n• Total RR: +24RR"
        await update.message.reply_text(performance_report, parse_mode="Markdown")

    elif text == "📚 MT5 Training":
        await update.message.reply_text("Master MT5 here:\nhttps://youtu.be/uTudeCn2VaE?si=fk9H61A7bJOW4LW5")

    elif text == "👨🏽‍💻 Support":
        await update.message.reply_text("Contact Support: @dhatmcyoung")

# 4. Starting the Bot
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("setavailable", update_trades))
    app.add_handler(CommandHandler("setrunning", update_trades))
    app.add_handler(CommandHandler("setclose", update_trades))
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("DHATMCYOUNG Bot is live!")
    app.run_polling()