from typing import Iterator, Optional

from pydantic import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker


class DBSettings(BaseSettings):
    db_uri: str
    is_local: Optional[bool]
    db_cluster_arn: Optional[str]
    db_secret_arn: Optional[str]


settings = DBSettings()

connect_args = {}
if not settings.is_local:
    connect_args = {
        "aurora_cluster_arn": settings.db_cluster_arn,
        "secret_arn": settings.db_secret_arn,
    }

engine = create_engine(settings.db_uri, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Iterator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
