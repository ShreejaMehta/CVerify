from typing import Tuple, Union

from src.models import CandidateInfo
from .extractors import *


async def analyze(pdf_text: str) -> Tuple[CandidateInfo, Union[str, None]]:
    """
    Analyses the given text, and extracts required data from the text
    returns `CandidateInfo` and an error message
    """

    name = await extract_name(pdf_text)
    number = await extract_mobile_number(pdf_text)
    email = await extract_email(pdf_text)
    skills = await extract_skills(pdf_text)
    education = await extract_education(pdf_text)
    github = await extract_github(pdf_text)
    linkedin = await extract_linkedin(pdf_text)
    urls = await extract_urls(pdf_text)

    return CandidateInfo(
        name=name,
        number=number,
        email=email,
        skills=skills,
        education=education,
        github=github,
        linkedin=linkedin,
        urls=urls
    ), None
