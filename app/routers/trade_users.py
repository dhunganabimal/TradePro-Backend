from fastapi import FastAPI, Response, HTTPException, status,Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import  get_db
from .. import models,schemas,utils
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