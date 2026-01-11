from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models
from app.database import get_db
from app.oauth2 import get_current_share_user

router = APIRouter(
    prefix="/share/portfolio",
    tags=['Portfolio']
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.PortfolioOut])
def get_portfolio(

    current_user: models.ShareUsers = Depends(get_current_share_user),
    db: Session = Depends(get_db)
):
    # portfolio = db.query(models.Portfolio).filter(current_user.id==id).all()
    #
    # if not portfolio:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail="Portfolio not found for this user"
    #     )
#user_query=db.query(models.ShareUsers).filter(models.ShareUsers.id==id).first()


    return current_user.portfolio