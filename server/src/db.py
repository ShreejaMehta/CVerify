from typing import Tuple, Union
from databases import Database
from src.models import CandidateInfo
from .db_models import convert_into_candidate_model, sessions, credentials, candidate_info, get_db

# 3 tables
#   + candidate: stores candiate information
#   + credentials: stores username and hashed password
#   + sessions: stores current user sessions


async def check_credentials(username: str, password: str) -> Tuple[bool, str]:
    query = credentials.select().where(credentials.c.username == username)
    resp = await get_db().fetch_one(query)

    # TODO: Implement user sessions
    if not resp:
        return False, "-1"

    pissword = resp[1]
    if password == pissword:
        return True, "1"

    return False, "-1"


async def insert_credentials(username: str, password: str):
    query = credentials.insert().values(
        username=username,
        password=password
    ) 
    id = await get_db().execute(query)
    return id


async def insert_candidate(info: CandidateInfo):
    query = candidate_info.insert().values(
        name=info.name,
        number=info.number,
        email=info.email,
        skills=",".join(info.skills),
        education=",".join(info.education),
        github=info.github,
        linkedin=info.linkedin,
        status=info.status
    )
    insert_record_id = await get_db().execute(query)
    return insert_record_id


async def get_candidate(id: int) -> Union[None, CandidateInfo]:
    query = candidate_info.select().where(candidate_info.c.id == id)
    resp = await get_db().fetch_one(query)
    if not resp:
        return None
    return convert_into_candidate_model(resp)


async def get_candidate_range(limit: int) -> list[CandidateInfo]:
    query = candidate_info.select().limit(limit)
    resp = await get_db().fetch_all(query)

    return [
        convert_into_candidate_model(info)
        for info in resp
    ]
