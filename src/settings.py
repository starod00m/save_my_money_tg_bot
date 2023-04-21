from pydantic import BaseSettings
from pathlib import Path

APP_HOME = Path(__file__).absolute().parent.parent
DB_NAME = 'smm.db'
DB_PATH = APP_HOME / DB_NAME
DB_URL = f"sqlite:///{DB_PATH}"

sqlite_file_name = "database.db"

class Settings(BaseSettings):
    class Config:
        underscore_attrs_are_private = True
        env_file = APP_HOME / ".env"

    TG_TOKEN: str
    DEBUG: bool = False
    IS_DROP_DB: bool = False

print(DB_PATH)
settings = Settings()  # type: ignore
