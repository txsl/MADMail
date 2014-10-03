import sqlsoup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = sqlsoup.SQLSoup('mysql://DB_STUFF_HERE')

erp_engine = create_engine('mssql+pymssql://username:pass@host:port/db_name', schema_name='dbo')
erp_session = sessionmaker(bind=erp_engine)
newerpol = erp_session()

SECRET_KEY = 'Make me more secret'

EMAIL= {
    'MAIL_SERVER': None,  # default ‘localhost’
    'MAIL_PORT': None,  # default 25
    'MAIL_USE_TLS': None,  # default False
    'MAIL_USE_SSL': None,  # default False
    'MAIL_DEBUG': None,  # default app.debug
    'MAIL_USERNAME': None,  # default None
    'MAIL_PASSWORD': None,  # default None
    'DEFAULT_MAIL_SENDER': None,  # default None. Probably ("Mums and Dads", "mumsanddads@imperial.ac.uk")
    'MAIL_MAX_EMAILS': None,  # default None
    'MAIL_SUPPRESS_SEND': None, # default app.testing
    'MAIL_ASCII_ATTACHMENTS': None, #  default False
}