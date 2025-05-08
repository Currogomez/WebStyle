import os, html, logging
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler, ContextTypes, filters
from openai import OpenAI

# Cargar .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

if not TOKEN or not OPENAI_KEY:
    raise RuntimeError("Faltan TELEGRAM_TOKEN u OPENAI_KEY en el archivo .env")

# Cliente OpenAI (OpenRouter)
client = OpenAI(
    api_key=OPENAI_KEY,
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "https://t.me/WwwebStylebot",
        "X-Title": "WebStyleBot"
    }
)

# Logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Estados de conversación
TYPE, COLOR1, COLOR2, COLOR3, STYLE, LAYOUT = range(6)

TYPE_KEYBOARD = [
    ["Corporativa", "Empresarial"],
    ["Tienda online", "Newsletter"],
    ["Portafolio", "Educativa"],
    ["Blog"]
]

# Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    kb = ReplyKeyboardMarkup(TYPE_KEYBOARD, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text("👋 ¡Bienvenido a WebStyle 2.0!\n¿Qué tipo de página web deseas crear?", reply_markup=kb)
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
    await update.message.reply_text("¿Estilo visual? (minimalista, moderno, clásico, creativo o libre)")
    return STYLE

async def style_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["style"] = html.escape(update.message.text)
    await update.message.reply_text("¿Layout? (one-page, secciones navegables, grid, menú lateral u otro)")
    return LAYOUT

async def layout_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["layout"] = html.escape(update.message.text)
    await update.message.reply_text("Generando tu plantilla con IA… ⏳")

    try:
        html_content, css_content, js_content = generate_html(context.user_data)

        with open("webstyle_template.html", "w", encoding="utf-8") as f:
            f.write(html_content)

        with open("style.css", "w", encoding="utf-8") as f:
            f.write(css_content)

        with open("script.js", "w", encoding="utf-8") as f:
            f.write(js_content)

        await update.message.reply_document(open("webstyle_template.html", "rb"))
        await update.message.reply_document(open("style.css", "rb"))
        await update.message.reply_document(open("script.js", "rb"))

        await update.message.reply_text("¡Tu web está lista con HTML, CSS y JavaScript!")
    except ValueError as ve:
        await update.message.reply_text(str(ve))
    except Exception as e:
        await update.message.reply_text("Error al generar la plantilla. Puede que la IA no devolviera los tres archivos esperados.")
        logging.error(f"Error: {e}")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Operación cancelada. Usa /start para reiniciar.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

# Generar HTML, CSS y JS desde IA
def generate_html(data: dict) -> tuple:
    prompt = (
        f"Actúa como un generador profesional de plantillas web. Devuélveme tres bloques: HTML, CSS y JS.\n\n"
        f"REQUISITOS:\n"
        f"- El HTML debe incluir header, menú lateral, secciones navegables, una galería funcional, enlaces correctos a style.css y script.js.\n"
        f"- El CSS debe tener diseño moderno y responsive usando estos colores: primario: {data['color1']}, secundario: {data['color2']}, terciario: {data['color3']}.\n"
        f"- El JavaScript debe incluir interacciones como mostrar/ocultar menú lateral y animación de scroll.\n\n"
        f"Tipo de web: {data['type']}\n"
        f"Estilo visual: {data['style']}\n"
        f"Layout: {data['layout']}\n\n"
        f"FORMATO EXACTO:\n"
        f"---HTML---\n<html>...</html>\n---END HTML---\n"
        f"---CSS---\n/* ... */\n---END CSS---\n"
        f"---JS---\n// ...\n---END JS---"
    )

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=2500,
    )

    content = response.choices[0].message.content

    try:
        html_part = content.split('---END HTML---')[0].split('---HTML---')[1].strip()
        css_part = content.split('---END CSS---')[0].split('---CSS---')[1].strip()
        js_part = content.split('---END JS---')[0].split('---JS---')[1].strip()
    except IndexError:
        raise ValueError("La IA no devolvió bien los tres bloques. Aquí tienes el contenido generado:\n\n" + content)

    return html_part, css_part, js_part

# Main
def main():
    app = Application.builder().token(TOKEN).build()
    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            TYPE: [MessageHandler(filters.TEXT & ~filters.COMMAND, type_handler)],
            COLOR1: [MessageHandler(filters.TEXT & ~filters.COMMAND, color1_handler)],
            COLOR2: [MessageHandler(filters.TEXT & ~filters.COMMAND, color2_handler)],
            COLOR3: [MessageHandler(filters.TEXT & ~filters.COMMAND, color3_handler)],
            STYLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, style_handler)],
            LAYOUT: [MessageHandler(filters.TEXT & ~filters.COMMAND, layout_handler)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv)
    logging.info("Bot iniciado – esperando mensajes…")
    app.run_polling()

if __name__ == "__main__":
    main()