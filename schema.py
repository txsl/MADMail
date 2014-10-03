# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Float, Index, Integer, LargeBinary, Numeric, String, Table, Text, Unicode
from sqlalchemy.dialects.mssql.base import BIT, MONEY
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

t_MumsandDadsAllocation = Table(
    'MumsandDadsAllocation', metadata,
    Column('PeopleID', Integer, nullable=False),
    Column('DepOCID', Integer, nullable=False),
    Column('ChildName', Unicode(511)),
    Column('ChildFname', Unicode(255)),
    Column('ChildSurname', Unicode(255)),
    Column('ParentNames', Unicode(1025)),
    Column('FirstParent', Unicode(511)),
    Column('FirstParentFName', Unicode(255)),
    Column('FirstParentSurname', Unicode(255)),
    Column('SecondParent', Unicode(511)),
    Column('SecondParentFName', Unicode(255)),
    Column('SecondParentSurname', Unicode(255)),
    Column('YearID', Integer, nullable=False),
    Column('Login', Unicode(50)),
    Column('dataStatus', Integer, nullable=False),
    Column('FirstParentLogin', Unicode(50)),
    Column('SecondParentLogin', Unicode(50)),
    Column('OCDesc', Unicode(50), nullable=False),
    Column('CurrentYear', BIT),
    Column('OCNameTypeName', Unicode(255), nullable=False),
    schema='dbo'
)


class MumsandDadsChildren(Base):
    __tablename__ = 'MumsandDadsChildren'
    __table_args__ = (
        Index('IX_MumsandDadsChildren', 'PeopleID', 'CoupleID', 'YearID', 'DepOCID', unique=True),
        {u'schema': 'dbo'}
    )

    ID = Column(Integer, primary_key=True)
    PeopleID = Column(Integer, nullable=False)
    CoupleID = Column(Integer, nullable=False)
    YearID = Column(Integer, nullable=False)
    DepOCID = Column(Integer, nullable=False)
    ConcRV = Column(DateTime, nullable=False)
    metaLadderId = Column(Integer)
    dataStatus = Column(Integer, nullable=False)


class MumsandDadsCouple(Base):
    __tablename__ = 'MumsandDadsCouples'
    __table_args__ = (
        Index('IX_MumsandDadsCouples', 'FirstParentID', 'SecondParentID', 'YearID', 'DepOCID', unique=True),
        {u'schema': 'dbo'}
    )

    ID = Column(Integer, primary_key=True)
    FirstParentID = Column(Integer, nullable=False)
    SecondParentID = Column(Integer, nullable=False)
    YearID = Column(Integer, nullable=False)
    DepOCID = Column(Integer, nullable=False)
    ConcRV = Column(DateTime, nullable=False)
    metaLadderId = Column(Integer)
    dataStatus = Column(Integer, nullable=False)


class MumsandDadsFinish(Base):
    __tablename__ = 'MumsandDadsFinish'
    __table_args__ = {u'schema': 'dbo'}

    ID = Column(Integer, primary_key=True)
    DepOCID = Column(Integer, nullable=False)
    YearID = Column(Integer, nullable=False)
    Finished = Column(BIT, nullable=False)
    FinishedBy = Column(Integer)
    FinishedWhen = Column(DateTime)
    ConcRV = Column(DateTime, nullable=False)
    metaLadderId = Column(Integer)
    dataStatus = Column(Integer, nullable=False)


t_MumsandDadsParentDetails = Table(
    'MumsandDadsParentDetails', metadata,
    Column('DepOCID', Integer, nullable=False),
    Column('YearID', Integer, nullable=False),
    Column('ParentName', Unicode(511)),
    Column('Login', Unicode(50)),
    Column('ID', Integer, nullable=False),
    Column('ParentID', Integer, nullable=False),
    schema='dbo'
)

