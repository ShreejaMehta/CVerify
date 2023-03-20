from fastapi import FastAPI, status, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import sqlalchemy
from src.router import router
import databases
from src.db_models import init_database

DBURL = "sqlite:///./candidate.db"

# TODO: get this `database` var in db.py
database = databases.Database(DBURL)
engine = sqlalchemy.create_engine(
    DBURL, connect_args={"check_same_thread": False}
)
init_database(engine, database)

app = FastAPI()

# Handles routing for the server
app.include_router(router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("startup")
async def shutdown():
    await database.disconnect()


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         # content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
#         content=jsonable_encoder({"detail": ""})
#     )
