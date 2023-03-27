from dataclasses import dataclass
from pydantic import BaseModel


class ServerResponse(BaseModel):
    """
    A response from the server
    """
    message: str
    code: int


class ErrorResponse(BaseModel):
    """
    Error message model
    """
    message: str
    code: int


class UserAuth(BaseModel):
    """
    stored as `credentials` in db_model
    """
    username: str
    password: str


class AuthResponse(BaseModel):
    logged_in: bool
    message: str
    sessionId: str


class ParseRequest(BaseModel):
    path: str


class ParseResponse(BaseModel):
    """
    if candidate_id is "-1", then parsing failed
    check `message` for more details
    """
    candidate_id: int
    message: str


class CandidateInfo(BaseModel):
    """
    stored as `candidate_info` in db_model
    """
    id: int = -1
    name: str
    number: str
    email: str
    skills: list[str]
    education: list[str]
    github: str
    linkedin: str
    urls: list[str]

    status: str = "processing"
    # compatibility_rate
    # photo?
