from typing import Optional

from pydantic import BaseModel, conint, EmailStr
from datetime import datetime
class Users_Out(BaseModel):
    id:int
    username:str
    class Config:
        from_attributes = True

class TradeUsers(BaseModel):
    username:str
    email:EmailStr
    password:str
    share_username:str
    class Config:
        from_attributes = True
class ShareUsers(BaseModel):
    username: str
    email: EmailStr
    password: str
    class Config:
        from_attributes = True
class Users_Login(BaseModel):
    username:str
    password:str
    class Config:
        from_attributes = True
class Token(BaseModel):
    access_token:str
    token_type:str
class TokenData(BaseModel):
    id:Optional[str]=None
class Portfolio(BaseModel):
    name:str
    current_balance:int
    last_closing_price:float
    ltp:float
    user_id:int
class PortfolioOut(BaseModel):
    name: str
    current_balance: int
    last_closing_price: float
    ltp: float

class My_details_Out(BaseModel):
    username:str
    email:EmailStr
    class Config:
        from_attributes = True
