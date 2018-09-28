from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from app import app

constr = "oracle+cx_oracle://%(user)s:%(pass)s@(DESCRIPTION = (LOAD_BALANCE=on)\
    (FAILOVER=ON) (ADDRESS = (PROTOCOL = TCP)(HOST = %(host)s)(PORT = 1521))\
    (CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = %(serv)s)))" % {
    'user': app.config['ORACLE_CONNECTION']['USER'],
    'pass': app.config['ORACLE_CONNECTION']['PASSWORD'],
    'host': app.config['ORACLE_CONNECTION']['HOST'],
    'serv': app.config['ORACLE_CONNECTION']['SERVICE_NAME'],
}

engine = create_engine(constr, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
conn = engine.raw_connection()

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()

    Base.metadata.create_all(bind=engine)
