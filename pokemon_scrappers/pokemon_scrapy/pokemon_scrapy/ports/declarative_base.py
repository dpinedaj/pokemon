from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

metadata = MetaData(schema='data')
DeclarativeBase = declarative_base(metadata=metadata)