"""
WebStyle 2.0 – Bot de Telegram con IA (OpenRouter)
Usando python-telegram-bot v20+, python-dotenv y OpenRouter para generar plantillas HTML/CSS.
"""

import os, html, logging
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler, ContextTypes, filters
import openai

# — Seguridad: carga variables de entorno —
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
# Clave de OpenRouter
OPENAI_KEY = "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"

if not TOKEN:
    raise RuntimeError("Define TELEGRAM_TOKEN en .env")

# — Configura OpenRouter —
openai.api_key = OPENAI_KEY
openai.api_base = "https://openrouter.ai/api/v1"
openai.api_type = "openai"
openai.api_version = "v1"

# — Logging —
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# — Estados de la conversación —
TYPE, COLOR1, COLOR2, COLOR3, STYLE, LAYOUT = range(6)

# — Teclado de opciones para tipo de web —
TYPE_KEYBOARD = [
    ["Corporativa", "Empresarial"],
    ["Tienda online", "Newsletter"],
    ["Portafolio", "Educativa"],
    ["Blog"]
]

# — Handlers —
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    kb = ReplyKeyboardMarkup(TYPE_KEYBOARD, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text(
        "👋 ¡Bienvenido a WebStyle 2.0 con IA!\n¿Qué tipo de página web deseas crear?", reply_markup=kb
    )
    return TYPE

async def type_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["type"] = html.escape(update.message.text)
    await update.message.reply_text("¿Color primario? (hex o nombre)", reply_markup=ReplyKeyboardRemove())
    return COLOR1

async def color1_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["color1"] = html.escape(update.message.text)
    await update.message.reply_text("¿Color secundario?")
    return COLOR2

async def color2_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["color2"] = html.escape(update.message.text)
    await update.message.reply_text("¿Color terciario?")
    return COLOR3

async def color3_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["color3"] = html.escape(update.message.text)
    await update.message.reply_text(
        "¿Estilo visual? (minimalista, moderno, clásico, creativo o libre)"
    )
    return STYLE

async def style_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["style"] = html.escape(update.message.text)
    await update.message.reply_text(
        "¿Layout? (one-page, secciones navegables, grid, menú lateral u otro)"
    )
    return LAYOUT

async def layout_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["layout"] = html.escape(update.message.text)
    await update.message.reply_text("Generando tu plantilla con IA… ⏳")
    html_content = generate_html(context.user_data)
    filename = "webstyle_template.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    await update.message.reply_document(open(filename, "rb"), caption="¡Tu web está lista!")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Operación cancelada. Usa /start para reiniciar.", reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

# — Función de IA con OpenRouter —
def generate_html(data: dict) -> str:
    prompt = (
        f"Genera un HTML completo para un sitio '{data['type']}' "
        f"con colores primaria '{data['color1']}', secundaria '{data['color2']}', terciaria '{data['color3']}', "
        f"estilo '{data['style']}', layout '{data['layout']}'. "
        "Incluye header, navegación, secciones de ejemplo y footer, con CSS limpio y accesible."
    )
    response = openai.ChatCompletion.create(
        model="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",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1500
    )
    return response.choices[0].message.content

# — Configuración de la aplicación —
def main():
    app = Application.builder().token(TOKEN).build()
    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            TYPE:    [MessageHandler(filters.TEXT & ~filters.COMMAND, type_handler)],
            COLOR1:  [MessageHandler(filters.TEXT & ~filters.COMMAND, color1_handler)],
            COLOR2:  [MessageHandler(filters.TEXT & ~filters.COMMAND, color2_handler)],
            COLOR3:  [MessageHandler(filters.TEXT & ~filters.COMMAND, color3_handler)],
            STYLE:   [MessageHandler(filters.TEXT & ~filters.COMMAND, style_handler)],
            LAYOUT:  [MessageHandler(filters.TEXT & ~filters.COMMAND, layout_handler)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv)
    logging.info("Bot iniciado en MacBook – esperando mensajes…")
    app.run_polling()

if __name__ == "__main__":
    main()
