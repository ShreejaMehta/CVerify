from collections import defaultdict
import databases
from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import sqlalchemy
import uvicorn

from src.db_models import init_database
from src.router import router
from src.utils import get_config


# Get the config
CONFIG = get_config("./config.toml")

# TODO: get this `database` var in db.py
database = databases.Database(CONFIG.DBURL)
engine = sqlalchemy.create_engine(
    CONFIG.DBURL, connect_args={"check_same_thread": False}
)
init_database(engine, database)

app = FastAPI()

# Accept CORS requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"]
)

# Handles routing for the server
app.include_router(router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("startup")
async def shutdown():
    await database.disconnect()


@app.exception_handler(RequestValidationError)
async def custom_form_validation_error(request, exc):
    reformatted_message = defaultdict(list)
    for pydantic_error in exc.errors():
        loc, msg = pydantic_error["loc"], pydantic_error["msg"]
        filtered_loc = loc[1:] if loc[0] in ("body", "query", "path") else loc
        field_string = ".".join(filtered_loc)  # nested fields with dot-notation
        reformatted_message[field_string].append(msg)

    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {"detail": "Invalid request", "errors": reformatted_message}
        ),
    )

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=CONFIG.PORT, log_level="info")
