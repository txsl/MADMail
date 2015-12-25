# -*- coding: utf-8 -*-

import sqlsoup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = sqlsoup.SQLSoup('mysql://root:pass@localhost/mad2k14')

erp_engine = create_engine('mssql+pymssql://su_dotorglink:hjkfhue2348905wdg@icsqlk.cc.ic.ac.uk/SU_NEWERPOL')
erp_session = sessionmaker(bind=erp_engine)
newerpol = erp_session()