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
class My_details_Out_Share(BaseModel):
    username:str
    email:EmailStr

    class Config:
        from_attributes = True
class CollateralOut(BaseModel):
    amount:float
    class Config:
        from_attributes = True
class My_details_Out_Trade(BaseModel):
    username:str
    email:EmailStr
    collateral_amount: CollateralOut | None

    class Config:
        from_attributes = True
class AddCollateral(BaseModel):
    amount: float
    payment_method:str
    remarks:str
    class Config:
        from_attributes = True
# class StockOrder(BaseModel):
#     symbol:str
#     quantity:int
#     price:float
#     remarks:Optional[str]=None
