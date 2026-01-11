from sqlalchemy import Column, Integer, String,Boolean,ForeignKey,Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base
class ShareUsers(Base):
    __tablename__= "share_users"
    id=Column(Integer,primary_key=True,nullable=False)
    username=Column(String,primary_key=False,unique=True,nullable=False)
    email=Column(String,primary_key=False,unique=True,nullable=False)
    password=Column(String,primary_key=False,unique=True,nullable=False)
    #trade_account = relationship("TradeUsers", back_populates="share_owner", uselist=False)
    portfolio = relationship(
        "Portfolio",
        back_populates="owner",
        cascade="all, delete-orphan"
    )


class TradeUsers(Base):
    __tablename__="trade_users"
    id = Column(Integer, primary_key=True, nullable=False)
    #share_account_id = Column(
    #     Integer,
    #     ForeignKey("share_users.id", ondelete="CASCADE"),
    #     nullable=False
    # )
    username = Column(String, primary_key=False, unique=True, nullable=False)
    email = Column(String, primary_key=False, unique=True, nullable=False)
    password = Column(String, primary_key=False, unique=True, nullable=False)
    share_username=Column(String,primary_key=False,unique=True,nullable=False)
    #share_owner = relationship("ShareUsers", back_populates="trade_account")


class Portfolio(Base):
    __tablename__ = 'portfolio'

    id = Column(Integer, primary_key=True)
    name=Column(String,primary_key=False,nullable=False)
    current_balance=Column(Integer,primary_key=False,nullable=False)
    last_closing_price=Column(Float,primary_key=False,nullable=False)
    ltp=Column(Float,primary_key=False,nullable=False)

    # Foreign Key linking back to the User
    user_id = Column(Integer, ForeignKey('share_users.id', ondelete="CASCADE"), nullable=False)

    owner = relationship("ShareUsers", back_populates="portfolio")





