from fastapi import FastAPI, status, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from src.router import router


app = FastAPI()

app.include_router(router)


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         # content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
#         content=jsonable_encoder({"detail": ""})
#     )
