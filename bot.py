import os
import random
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ─────────────────────────────────────────────
#  CONFIG – Token from environment variable
# ─────────────────────────────────────────────

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("❌ BOT_TOKEN environment variable set karo!")

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ─────────────────────────────────────────────
#  /start
# ─────────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "╔════════════════════════════╗\n"
        "      ⚡ 𝗚𝗔𝗠𝗘𝗥 𝗚𝗖 𝗕𝗢𝗧 ⚡\n"
        "╚════════════════════════════╝\n\n"
        "🎮 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗨𝗹𝘁𝗶𝗺𝗮𝘁𝗲 𝗚𝗮𝗺𝗲 𝗕𝗼𝘁!\n\n"
        "━━━━━━━━━━━━━━━━━━\n"
        "🎲 /dice  ➜ 𝗥𝗼𝗹𝗹 𝗗𝗶𝗰𝗲 (1-6)\n"
        "🪙 /flip  ➜ 𝗙𝗹𝗶𝗽 𝗖𝗼𝗶𝗻\n"
        "🎰 /random ➜ 𝗥𝗮𝗻𝗱𝗼𝗺 𝗚𝗮𝗺𝗲\n"
        "❓ /help ➜ 𝗛𝗲𝗹𝗽\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "✨ 𝗚𝗼𝗼𝗱 𝗟𝘂𝗰𝗸!\n"
        "⚡ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 𝗚𝗔𝗠𝗘𝗥 𝗚𝗖"
    )
    await update.message.reply_text(text)

# ─────────────────────────────────────────────
#  /help
# ─────────────────────────────────────────────
async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚡ 𝗚𝗔𝗠𝗘𝗥 𝗚𝗖 𝗕𝗢𝗧\n\n"
        "🎲 /dice – Roll Dice (1-6)\n"
        "🪙 /flip – Flip Coin\n"
        "🎰 /random – Random Game\n\n"
        "🚀 Enjoy!"
    )

# ─────────────────────────────────────────────
#  /dice – Animated dice + result value
# ─────────────────────────────────────────────
async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎲 𝗥𝗢𝗟𝗟𝗜𝗡𝗚 𝗗𝗜𝗖𝗘...")
    sent = await context.bot.send_dice(chat_id=update.effective_chat.id)
    value = sent.dice.value
    await update.message.reply_text(f"✨ 𝗥𝗲𝘀𝘂𝗹𝘁 : **{value}**", parse_mode='Markdown')

# ─────────────────────────────────────────────
#  /flip
# ─────────────────────────────────────────────
async def flip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = random.choice(["👑 𝗛𝗘𝗔𝗗𝗦", "🪙 𝗧𝗔𝗜𝗟𝗦"])
    await update.message.reply_text(
        "╔══════════════╗\n"
        "🪙 𝗖𝗢𝗜𝗡 𝗙𝗟𝗜𝗣\n"
        "╚══════════════╝\n\n"
        f"✨ {result}"
    )

# ─────────────────────────────────────────────
#  /random – randomly dice or flip
# ─────────────────────────────────────────────
async def random_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if random.choice([True, False]):
        await update.message.reply_text("🎰 𝗥𝗔𝗡𝗗𝗢𝗠 𝗚𝗔𝗠𝗘\n\n🎲 𝗦𝗲𝗹𝗲𝗰𝘁𝗲𝗱 : 𝗗𝗜𝗖𝗘")
        await dice(update, context)
    else:
        await update.message.reply_text("🎰 𝗥𝗔𝗡𝗗𝗢𝗠 𝗚𝗔𝗠𝗘\n\n🪙 𝗦𝗲𝗹𝗲𝗰𝘁𝗲𝗱 : 𝗖𝗢𝗜𝗡 𝗙𝗟𝗜𝗣")
        await flip(update, context)

# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("dice", dice))
    app.add_handler(CommandHandler("flip", flip))
    app.add_handler(CommandHandler("random", random_game))

    logger.info("⚡ GAMER GC BOT STARTED ⚡")
    print("⚡ GAMER GC BOT STARTED ⚡")

    app.run_polling()

if __name__ == "__main__":
    main()
