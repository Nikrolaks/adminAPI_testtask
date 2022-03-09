import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    registration_date = sa.Column(sa.Date)
    last_login = sa.Column(sa.DateTime)
    age = sa.Column(sa.Integer)
    role = sa.Column(sa.String)
    login = sa.Column(sa.String)
    password = sa.Column(sa.String)