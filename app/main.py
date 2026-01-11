from fastapi import FastAPI,APIRouter
from . import models
from .database import engine
from .routers import share_users, auth, trade_users, portfolio, my_details
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)
app=FastAPI()
app.include_router(share_users.router)
app.include_router(trade_users.router)
app.include_router(auth.router)
app.include_router(portfolio.router)
app.include_router(my_details.router)
origins = [

    "http://localhost:8080",
    "http://localhost:3000",
    "http://192.168.0.123:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home_page():
    return "Hello World"