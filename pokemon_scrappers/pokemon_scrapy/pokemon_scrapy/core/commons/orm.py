from scrapy.utils.project import get_project_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


def db_session():
    
    engine = create_engine(get_project_settings().get("CONNECTION_STRING"))

    session = scoped_session(
        sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=False
        )
    )
    return session