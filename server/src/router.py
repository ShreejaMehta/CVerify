from typing import Union
from fastapi import APIRouter, UploadFile, File
from src.db import check_credentials, get_candidate, get_candidate_range, update_candidate_status
from src.pdfanal.parser import parser
from .models import ErrorResponse, ServerResponse, UserAuth, AuthResponse, ParseRequest, ParseResponse, CandidateInfo
from .auth import check_login, create_user
import tempfile

router = APIRouter()


# Nothing here
@router.get("/")
async def index_redirect():
    # TODO: Redirect to index page
    # return RedirectResponse("https://google.com")
    return {"status": "alive"}


# Login
@router.post("/auth/login", include_in_schema=True)
async def login(info: UserAuth) -> AuthResponse:
    user = info.username
    password = info.password
    # Check login and give user a token, add that token to the db
    logged_in, id = await check_credentials(user, password)

    return AuthResponse(logged_in=logged_in, message="", sessionId=id)


register_descrption = """
    Returns 1 for successfull registration
    0 for failed registration
"""
# Register
# TODO: Security
@router.post("/auth/register", include_in_schema=True, description=register_descrption)
async def register(info: UserAuth, api_key: str) -> Union[ServerResponse, ErrorResponse]:
    """
    Returns 1 for successfull registration
    0 for failed registration
    """
    return (await create_user(info, api_key))


# Parser
parser_description = """
> Used for parsing Resume

## Required Parameters
- path: local path where the resume is stored
"""

@router.post("/parse", description=parser_description, include_in_schema=False)
async def parse(req: ParseRequest) -> ParseResponse:
    """
    TODO: Handle validation errors
    TODO: Handle emptpy body: 422 Unprocessable Entity

    NOTE: This is deprecated as of now, use /upload api
    """
    path = req.path

    # TODO: Include path boundary checking
    id, msg = await parser(path)

    return ParseResponse(candidate_id=id, message=msg if msg else "")

# File uploader
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)) -> ParseResponse:
    """
    takes in a resume parses it and returns the candidate id stored in the database

    TODO: Add file validation
    """

    # Save the file in temp dir 
    with tempfile.NamedTemporaryFile(mode="wb", suffix=".pdf") as temp:
        temp.write(await file.read())
        path = temp.name

        print(path)
        id, msg = await parser(path)
        return ParseResponse(candidate_id=id, message=msg if msg else "")


# Get Candidate info
@router.get("/candidate/{candidate_id}")
async def get_details(candidate_id: int) -> Union[CandidateInfo, ErrorResponse]:
    cand = await get_candidate(candidate_id)

    if not cand:
        return ErrorResponse(message="Candidate id not found", code=1)

    return cand

@router.get("/candidate/{candidate_id}/{status}")
async def get_status(candidate_id: int, status: bool) -> Union[ServerResponse, ErrorResponse]:
    success: bool = await update_candidate_status(candidate_id, status)

    if not success:
        return ErrorResponse(message="Candidate id not found", code=-1)

    return ServerResponse(message="Success", code=1)


@router.get("/summary/{limit}")
async def candidate_range(limit: int = 10) -> list[CandidateInfo]:
    """
    Returns first `limit` candidates from the DB
    """
    candidates = await get_candidate_range(limit)
    return candidates
