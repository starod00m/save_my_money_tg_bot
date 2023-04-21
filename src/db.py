from loguru import logger
from sqlalchemy.exc import DatabaseError
from sqlmodel import SQLModel, create_engine

from .models import *
from .settings import DB_PATH, DB_URL, settings

engine = create_engine(DB_URL, echo=settings.DEBUG)


def init_db():
    logger.info(f"Initializing db connection at {DB_URL}")
    if DB_PATH.exists() and settings.IS_DROP_DB:
        logger.warning(f"removing db at [{DB_PATH}]")
        DB_PATH.unlink()

    if DB_PATH.exists():
        logger.warning(f"db exists at [{DB_PATH}]")
    else:
        try:
            SQLModel.metadata.create_all(engine)
        except DatabaseError as e:
            logger.error(f"got error trying connect to db [{repr(e)}]")
            raise
