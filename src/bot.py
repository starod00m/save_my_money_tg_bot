from telegram import Update
from telegram.ext import Application, ApplicationBuilder, CommandHandler, ContextTypes

from .settings import settings


def init_bot() -> Application:
    app = ApplicationBuilder().token(settings.TG_TOKEN).build()
    app.add_handler(CommandHandler("hello", hello))
    return app


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"Hello {update.effective_user.first_name}"
    )
