from typing import List

from fastapi import FastAPI, Response, HTTPException, status,Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import  get_db
from .. import models,schemas,utils
from ..oauth2 import get_current_share_user

router=APIRouter(
    prefix="/shareUsers",
    tags=['ShareUsers']
)
#Creating a user for registration
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Users_Out)
def create_share_user(user:schemas.ShareUsers,db: Session = Depends(get_db)):

    # hash the password
    hashed_pass=utils.hash(user.password)
    user.password=hashed_pass
    new_user = models.ShareUsers(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return  new_user



@router .get("/{id}",response_model=schemas.Users_Out)
def get_user(id:int,db: Session = Depends(get_db)):
     user=db.query(models.ShareUsers).filter(models.ShareUsers.id==id).first()
     if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"The Message you are looking for id {id}  is not found on the server")
     return user
@router.get("/share/me",status_code=status.HTTP_200_OK, response_model=List[schemas.Users_Out])
def my_details(
        current_user: models.ShareUsers = Depends(get_current_share_user)):
    return current_user
