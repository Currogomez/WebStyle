import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler, ConversationHandler, filters, ContextTypes
)

# Configuración de logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Token del bot de Telegram
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

    # Recopilando toda la información para generar la respuesta
    web_type = context.user_data.get("web_type", "No especificado")
    colors = context.user_data.get("colors", "No especificado")
    style = context.user_data.get("style", "No especificado")
    details = context.user_data.get("details", "No especificado")
    header = context.user_data.get("header", "No especificado")
    body = context.user_data.get("body", "No especificado")
    footer = context.user_data.get("footer", "No especificado")

    # Resumen de la web
    summary = (
        f"📜 **Resumen de tu página web:**\n"
        f"🔹 **Tipo de web:** {web_type}\n"
        f"🎨 **Colores principales:** {colors}\n"
        f"🖌 **Estilo de diseño:** {style}\n"
        f"🔍 **Detalles adicionales:** {details}\n"
        f"📌 **Header:** {header}\n"
        f"📜 **Body:** {body}\n"
        f"📎 **Footer:** {footer}\n\n"
        "🚀 **Generando tu diseño web basado en buenas prácticas...**"
    )

    # Código HTML con estructura estricta
    html_code = f"""```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{web_type}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <section class="page">
        <header class="page__header">
            <h1>{header}</h1>
        </header>
        <article class="page__content">
            <div class="page__info">
                <p>{body}</p>
            </div>
        </article>
        <footer class="page__footer">
            <p>{footer}</p>
        </footer>
    </section>
</body>
</html>
```"""

    # Código CSS usando BEM con especificidad 010
    css_code = """```css
/* Estilos basados en BEM con especificidad 010 */
.page {
    font-family: Arial, sans-serif;
    color: #333;
    background-color: #f9f9f9;
    padding: 20px;
}

.page__header {
    background-color: #007BFF;
    color: white;
    padding: 20px;
    text-align: center;
}

.page__content {
    background-color: white;
    padding: 20px;
    margin: 20px 0;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.page__info {
    font-size: 1.2em;
    line-height: 1.5;
}

.page__footer {
    background-color: #333;
    color: white;
    text-align: center;
    padding: 15px;
}
```"""

    # Enviar respuestas al usuario
    await update.message.reply_text(summary)
    await update.message.reply_text("📜 **Aquí tienes tu plantilla HTML:**\n" + html_code)
    await update.message.reply_text("🎨 **Aquí tienes tu plantilla CSS:**\n" + css_code)

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

    logging.info("✅ Bot en ejecución...")
    app.run_polling()

if __name__ == "__main__":
    main()