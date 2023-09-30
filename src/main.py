from fastapi import FastAPI
from sqlalchemy.exc import NoResultFound

from .exception_handler import sqlalchemy_no_result_handler
from .routers.user import router as user_router

app = FastAPI()
app.include_router(user_router)
app.add_exception_handler(NoResultFound, sqlalchemy_no_result_handler)
