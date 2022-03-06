import platform

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

SQLALCHEMY_DATABASE_URL_1 = 'mysql+mysqldb://hyeonproject:hyeonproject@127.0.0.1/auth'
SQLALCHEMY_DATABASE_URL_2 = 'postgresql+psycopg2://auth:authproject@127.0.0.1:5432/auth'

os_name = platform.system()

if os_name == 'Windows':
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL_2, echo=True, future=True, pool=QueuePool, pool_size=10
    )
else:
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL_1, echo=True, future=True, pool=QueuePool, pool_size=10
    )


session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()
