from src.db import init_db
from src.bot import init_bot
def start_app():
    init_db()

    application = init_bot()
    application.run_polling()

if __name__ == "__main__":
    start_app()
