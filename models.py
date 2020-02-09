from sqlalchemy import ARRAY, Column, DateTime, Integer
from tornado_sqlalchemy import SQLAlchemy

db = SQLAlchemy(url='localhost')


class TableItem(db.Model):
    __tablename__ = 'table'

    id = Column(Integer, primary_key=True)
    raw_array = Column(ARRAY(Integer))
    sorted_array = Column(ARRAY(Integer))
    created_at = Column(DateTime)

    class Meta:
        database = db
