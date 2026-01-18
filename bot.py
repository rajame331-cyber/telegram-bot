from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8194510013:AAGVxJ_KLl6TuoOhFu4bc7Y3rTVraGD9rM4"

CHANNEL_USERNAME = "@tiktokvairalvideo2026"
CHANNEL_LINK = "https://t.me/tiktokvairalvideo2026"

MONETAG_LINK = "https://otieu.com/4/10482308"

VIDEOS = [
    "BAACAgUAAxkBAAFA3b5pbNtyAAFPAAGNerzjQAz7ryPOTZ9BAALgGQACNqNoV6dw8ZudC7eBOAQ",
    "BAACAgUAAxkBAAFA3d9pbN5zPub4wQalsGSdawp46H4ZiAACtBoAAjajaFeT0dKlY_xgEDgE",
    "BAACAgUAAxkBAAFA3edpbN8WSg0JCx251ELpr7fg1a5m4gACtRoAAjajaFcx2bhvwbL11TgE",
    "BAACAgUAAxkBAAFA3fNpbN-Fbouz3AnLgmUVrbDyDLIyhAACthoAAjajaFfCVuRqR5_WVDgE"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    try:
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if member.status not in ["member", "administrator", "creator"]:
            raise Exception()
    except:
        keyboard = [[InlineKeyboardButton("🔔 Join Channel", url=CHANNEL_LINK)]]
        await update.message.reply_text(
            "❌ আগে Channel Join করো",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    buttons = []
    for i in range(len(VIDEOS)):
        buttons.append(
            [InlineKeyboardButton(f"🔓 Unlock Video {i+1}", url=MONETAG_LINK)]
        )

    await update.message.reply_text(
        "🎯 প্রতিটা ভিডিও দেখতে হলে আগে Ad দেখতে হবে 👇",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

async def unlock(update: Update, context: ContextTypes.DEFAULT_TYPE):
    idx = int(context.args[0])
    await context.bot.send_video(
        chat_id=update.effective_chat.id,
