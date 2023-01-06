import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sql.Column(sql.Integer, primary_key=True)
    email = sql.Column(sql.Text, unique=True)
    username = sql.Column(sql.Text, unique=True)
    password_hash = sql.Column(sql.Text)


class Operation(Base):
    __tablename__ = 'operations'

    id = sql.Column(sql.Integer, primary_key=True)
    user_id = sql.Column(sql.Integer, sql.ForeignKey('users.id'))
    date = sql.Column(sql.Date)
    kind = sql.Column(sql.String)
    amount = sql.Column(sql.Numeric(10, 2))
    description = sql.Column(sql.String, nullable=True)
