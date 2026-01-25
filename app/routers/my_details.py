from typing import List
from fastapi import FastAPI, Response, HTTPException, status,Depends,APIRouter
from .. import models,schemas,utils
from ..oauth2 import get_current_share_user, get_current_trade_user

router=APIRouter(
    prefix="/userDetails",
    tags=['My Details']
)

@router.get("/share",status_code=status.HTTP_200_OK, response_model=schemas.My_details_Out_Share)
def my_share_details(
        current_user: models.ShareUsers = Depends(get_current_share_user)):
   return current_user
@router.get("/trade",status_code=status.HTTP_200_OK, response_model=schemas.My_details_Out_Trade)
def my_trade_details(
        current_user: models.TradeUsers = Depends(get_current_trade_user)):
   return current_user

