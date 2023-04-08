from typing import Tuple, Union
from src.models import CandidateInfo
from .db_models import convert_into_candidate_model, sessions, credentials, candidate_info, get_db

# 3 tables
#   + candidate: stores candiate information
#   + credentials: stores username and hashed password
#   + sessions: stores current user sessions (Didn't use it yet)


async def check_credentials(username: str, password: str) -> Tuple[bool, str]:
    """
    Checks for user credential in the db and returns
    [success/failure, reason]
    -1: no use found
    0: Valid User!
    1: "Invalid password"
    Note: This shouldn't be exposed in the API, but only for the programmers refernce
    """
    query = credentials.select().where(credentials.c.username == username)
    resp = await get_db().fetch_one(query)

    # TODO: Implement user sessions
    if not resp:
        return False, "-1"

    pissword = resp[1]
    if password == pissword:
        return True, "0"

    return False, "1"


async def insert_credentials(username: str, password: str) -> int:
    """
    Inserts candidate and returns user id or -1 if already exists
    """
    query = credentials.insert().values(
        username=username,
        password=password
    ) 
    try:
        id = await get_db().execute(query)
    except:
        return -1
    return id


async def insert_candidate(info: CandidateInfo) -> int:
    '''
    Inserts the candidate into the db
    returns the inserted unique candidate key
    '''
    query = candidate_info.insert().values(
        name=info.name,
        number=info.number,
        email=info.email,
        skills=",".join(info.skills),
        education=",".join(info.education),
        github=info.github,
        linkedin=info.linkedin,
        status=info.status,
        urls=",".join(info.urls)
    )
    insert_record_id = await get_db().execute(query)
    return insert_record_id


async def get_candidate(id: int) -> Union[None, CandidateInfo]:
    """
    gets the candidate with his id
    """
    query = candidate_info.select().where(candidate_info.c.id == id)
    resp = await get_db().fetch_one(query)
    if not resp:
        return None
    return convert_into_candidate_model(resp)


async def get_candidate_range(limit: int) -> list[CandidateInfo]:
    """
    Returns list of candidates
    """
    query = candidate_info.select().limit(limit)
    resp = await get_db().fetch_all(query)

    return [
        convert_into_candidate_model(info)
        for info in resp
    ]


async def update_candidate_status(id: int, status: bool) -> bool:
    """
    Updates the current candidate acceptance status
    """
    query = candidate_info.update().where(candidate_info.c.id == id).values(status="Accepted" if status else "Rejected")
    res = await get_db().execute(query)
    print(res)

    return True
