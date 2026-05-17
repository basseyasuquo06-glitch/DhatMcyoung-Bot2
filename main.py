import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- CONFIGURATION ---
TOKEN = "8668969527:AAGO6Cf69SBpDSrMem9xhGNsIj1eOK_GdLE"  # Your active Bot Token
ADMIN_ID = 1128630065  # Your verified Admin Telegram ID

# Temporary storage for your trades
current_trades = {
    "available": "No active trade setups at the moment. Stay tuned!",
    "running": "No running trades currently.",
    "close": "All recent trades are closed. Check Monthly Performance for stats!"
}

# --- HANDLERS ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends the premium welcome banner with inline buttons."""
    photo_url = "https://i.ibb.co/6R0D5VpS/premium-dark-crypto-forex-trading-gold-coin-chart-aesthetic-illustration-phone-wallpaper-banner.jpg"
    
    caption_text = (
        "| **DHATMCYOUNG BOT - TRADING SIGNALS**\n"
        "📈 *Your Path to consistent Risk-to-Reward (RR) gains.*\n\n"
        "Welcome to the official command center. Use the menu below "
        "to view live setups, check performance reports, and access resources."
    )
    
    # Premium stacked button layout with all your updated details
    keyboard = [
        [InlineKeyboardButton("📢 Join Main Channel", url="https://t.me/+MydiesYR63MxODMx")], 
        [InlineKeyboardButton("🚀 Crypto Only", url="https://t.me/+MydiesYR63MxODMx")], 
        [InlineKeyboardButton("✅ Available Trades", callback_data="view_available")],
        [InlineKeyboardButton("🏃‍♂️ Running Trades", callback_data="view_running")],
        [InlineKeyboardButton("📊 Monthly Performance", callback_data="view_performance")],
        [InlineKeyboardButton("📚 Free MT5 Training", url="https://youtu.be/uTudeCn2VaE?si=fk9H61A7bJOW4LW5")], # Replace with your training link if needed
        [InlineKeyboardButton("👩🏽‍💻 Mentorship (@DhatMcyoung)", url="https://t.me/DhatMcyoung")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_photo(
        photo=photo_url,
        caption=caption_text,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the action when users click the inline buttons."""
    query = update.callback_query
    await query.answer()  # Stops the loading wheel on Telegram
    
    if query.data == "view_available":
        await query.message.reply_text(f"✅ **Available Trades:**\n\n{current_trades['available']}", parse_mode="Markdown")
    
    elif query.data == "view_running":
        await query.message.reply_text(f"🏃‍♂️ **Running Trades:**\n\n{current_trades['running']}", parse_mode="Markdown")
        
    elif query.data == "view_performance":
        performance_text = (
            "📊 **PERFORMANCE REPORT**\n"
            "• Month: April 2026\n"
            "• Net Performance: +36.33RR 🔥\n\n"
            "Consistency is key. Risk managed, profits secured."
        )
        await query.message.reply_text(performance_text, parse_mode="Markdown")

# --- ADMIN COMMANDS FOR DHATMCYOUNG ---

async def set_available(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    if not context.args:
        await update.message.reply_text("Format: /setavailable [trade details]")
        return
    current_trades["available"] = " ".join(context.args)
    await update.message.reply_text("✅ Available trades updated successfully!")

async def set_running(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    if not context.args:
        await update.message.reply_text("Format: /setrunning [trade details]")
        return
    current_trades["running"] = " ".join(context.args)
    await update.message.reply_text("🏃‍♂️ Running trades updated successfully!")
async def set_close(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    if not context.args:
        await update.message.reply_text("Format: /setclose [details]")
        return
    current_trades["close"] = " ".join(context.args)
    current_trades["available"] = "No active trade setups at the moment. Stay tuned!"
    await update.message.reply_text("🔒 Trade status closed and updated!")

# --- MAIN ENGINE ---
def main():
    application = Application.builder().token(TOKEN).build()

    # Base commands
    application.add_handler(CommandHandler("start", start))
    
    # Inline button listener
    application.add_handler(CallbackQueryHandler(button_click))
    
    # Admin commands
    application.add_handler(CommandHandler("setavailable", set_available))
    application.add_handler(CommandHandler("setrunning", set_running))
    application.add_handler(CommandHandler("setclose", set_close))

    print("DHATMCYOUNG Premium Bot is running live...")
    application.run_polling()

if __name__ == "__main__":
    main()
