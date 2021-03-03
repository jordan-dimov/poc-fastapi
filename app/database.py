import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.environ["DB_URI"]

connect_args = {}
if not os.environ.get("IS_LOCAL"):
    connect_args = {
        "aurora_cluster_arn": os.environ["DB_CLUSTER_ARN"],
        "secret_arn": os.environ["DB_SECRET_ARN"],
    }

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args=connect_args,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
