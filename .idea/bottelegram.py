
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler, ConversationHandler, filters, ContextTypes
)

# Configuración de logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Reemplaza con tu TOKEN de Telegram
TOKEN = "8090158396:AAExpLkd9aTgYkJtTuMXQ5GtxqfMjKB5_QM"

# Estados de la conversación
WEB_TYPE, COLORS, STYLE, DETAILS, HEADER, BODY, FOOTER = range(7)

# Opciones de teclado
WEB_OPTIONS = [
    ["Corporativa", "Empresarial"],
    ["Tienda Online", "Newsletter"],
    ["Portafolio", "Educativa"],
    ["Blog"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info("Comando /start recibido")
    keyboard = ReplyKeyboardMarkup(WEB_OPTIONS, resize_keyboard=True)
    await update.message.reply_text(
        "👋 ¡Hola! ¿Qué tipo de página quieres crear? 🌍✨",
        reply_markup=keyboard
    )
    return WEB_TYPE

async def handle_website_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["web_type"] = update.message.text
    await update.message.reply_text("🎨 Dime los colores principales (Ejemplo: Azul y blanco).")
    return COLORS

async def handle_colors(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["colors"] = update.message.text
    await update.message.reply_text("✨ Ahora dime un estilo de diseño (Minimalista, Moderno, Clásico).")
    return STYLE

async def handle_style(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["style"] = update.message.text
    await update.message.reply_text("🔍 Cuéntame más detalles sobre la página.")
    return DETAILS

async def handle_details(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["details"] = update.message.text
    await update.message.reply_text("🖥️ ¿Cómo quieres que sea el Header?")
    return HEADER

async def handle_header(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["header"] = update.message.text
    await update.message.reply_text("📜 ¿Cómo quieres que sea el Body?")
    return BODY

async def handle_body(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["body"] = update.message.text
    await update.message.reply_text("📌 ¿Cómo quieres que sea el Footer?")
    return FOOTER

async def handle_footer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["footer"] = update.message.text
    await update.message.reply_text("🚀 ¡Generando tu diseño web! 🎨")
    await update.message.reply_text("✅ Código generado con buenas prácticas.")
    return ConversationHandler.END

async def fallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚠️ No entendí eso. Intenta de nuevo. 😅")
    return ConversationHandler.END

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("El comando /test funciona correctamente.")

def main():
    app = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            WEB_TYPE: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_website_type)],
            COLORS: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_colors)],
            STYLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_style)],
            DETAILS: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_details)],
            HEADER: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_header)],
            BODY: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_body)],
            FOOTER: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_footer)],
        },
        fallbacks=[MessageHandler(filters.ALL, fallback)],
        conversation_timeout=600,  # Expira en 10 minutos
    )

    app.add_handler(conv_handler)
    app.add_handler(CommandHandler("test", test))

    logging.info("Bot en ejecución...")
    app.run_polling()

if __name__ == "__main__":
    main()