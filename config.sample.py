import sqlsoup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = sqlsoup.SQLSoup('mysql://DB_STUFF_HERE')

erp_engine = create_engine('mssql+pymssql://username:pass@host:port/db_name', schema_name='dbo')
erp_session = sessionmaker(bind=erp_engine)
newerpol = erp_session()
