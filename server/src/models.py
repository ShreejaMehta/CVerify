from pydantic import BaseModel


class UserAuth(BaseModel):
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
    candidate_id: str
    message: str


class CandidateInfo(BaseModel):
    name: str
