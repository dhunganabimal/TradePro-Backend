from fastapi import FastAPI, Response, HTTPException, status,Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import  get_db
from .. import models, schemas, utils, oauth2
from ..models import CollateralAmount, Portfolio
from ..oauth2 import get_current_trade_user
from ..schemas import TradeUsers, AddCollateral

router=APIRouter(
    prefix="/tradeUsers",
    tags=['TradeUsers']
)
#Creating a user for registration
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Users_Out)
def create_trade_user(user:schemas.TradeUsers,db: Session = Depends(get_db)):

    # hash the password
    hashed_pass=utils.hash(user.password)
    user.password=hashed_pass
    new_user = models.TradeUsers(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return  new_user



@router .get("/{id}",response_model=schemas.Users_Out)
def get_user(id:int,db: Session = Depends(get_db)):
     user=db.query(models.TradeUsers).filter(models.TradeUsers.id==id).first()
     if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"The Message you are looking for id {id}  is not found on the server")
     return user

@router.post("/funds/load-collateral")
def load_collateral( data: AddCollateral,current_user: models.TradeUsers = Depends(get_current_trade_user),db: Session = Depends(get_db)):
    collateral=CollateralAmount(
        amount=data.amount,
        payment_method=data.payment_method,
        remarks=data.remarks,
        trade_users_id=current_user.id
    )

    db.add(collateral)
    db.commit()
    db.refresh(collateral)
    return {"message": "Collateral Added Sucessfully"}
@router.get("/getcollateral",response_model=schemas.CollateralOut)
def get_collateral(db: Session = Depends(get_db),current_user: models.TradeUsers = Depends(get_current_trade_user)):
    data=db.query(models.CollateralAmount).filter(models.CollateralAmount.id==current_user.id).first()
    if not data:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="The data is not available.")
    return data
# @router.post("/share/orders")
# def order_stock(stock:schemas.StockOrder,current_user: models.TradeUsers = Depends(get_current_trade_user),db: Session = Depends(get_db)):
#     stock_data=Portfolio(
#
#     )





