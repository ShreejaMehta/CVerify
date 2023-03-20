from typing import Tuple, Union
from .extractors import *


async def analyze(pdf_text: str) -> Tuple[str, Union[str, None]]:
    """
    Analyses the given text, and extracts required data from the text
    inserts into the database and returns candidate id
    """

    name = await extract_name(pdf_text)
    number = await extract_mobile_number(pdf_text)
    email = await extract_email(pdf_text)
    skills = await extract_skills(pdf_text)
    education = await extract_education(pdf_text)
    github = await extract_github(pdf_text)
    linkedin = await extract_linkedin(pdf_text)

    return "", None
