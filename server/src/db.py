from typing import Union
from databases import Database
from src.models import CandidateInfo
from .db_models import sessions, credentials, candidate_info, get_db

# 3 tables
#   + candidate: stores candiate information
#   + credentials: stores username and hashed password
#   + sessions: stores current user sessions


async def check_credentials(username: str, password: str):
    pass


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
    return CandidateInfo(
        id=resp[0],
        name=resp[1],
        number=resp[2],
        email=resp[3],
        skills=resp[4].split(","),
        education=resp[5].split(","),
        github=resp[6],
        linkedin=resp[7],
        status=resp[8]
    )


async def get_candidate_range(limit: int) -> list[CandidateInfo]:
    return []
