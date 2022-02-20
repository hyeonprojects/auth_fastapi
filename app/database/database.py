from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

SQLALCHEMY_DATABASE_URL = 'mysql+mysqldb://hyeonproject:hyeonproject@127.0.0.1/auth'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True, future=True, pool=QueuePool, pool_size=10
)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()
