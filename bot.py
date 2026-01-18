from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8194510013:AAHRV_sRBmxMWB-SV617MsBDJWvIfGRmGrM"

VIDEOS = [
    "BAACAgUAAxkBAAFA3b5pbNtyAAFPAAGNerzjQAz7ryPOTZ9BAALgGQACNqNoV6dw8ZudC7eBOAQ",
    "BAACAgUAAxkBAAFA3d9pbN5zPub4wQalsGSdawp46H4ZiAACtBoAAjajaFeT0dKlY_xgEDgE",
    "BAACAgUAAxkBAAFA3edpbN8WSg0JCx251ELpr7fg1a5m4gACtRoAAjajaFcx2bhvwbL11TgE",
    "BAACAgUAAxkBAAFA3fNpbN-Fbouz3AnLgmUVrbDyDLIyhAACthoAAjajaFfCVuRqR5_WVDgE"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for v in VIDEOS:
        await context.bot.send_video(
            chat_id=update.effective_chat.id,
            video=v
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
