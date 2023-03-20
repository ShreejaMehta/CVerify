from typing import Tuple, Union
from pathlib import Path
import fitz
from .anal import analyze


async def parser(path: str) -> Tuple[str, Union[str, None]]:
    """
    Parses the resume, uploads the parsed data into database
    and returns the database candidateId to access it 
    """
    p = Path(path)
    if not p.exists():
        return "-1", "Invalid path"

    if p.suffix != ".pdf":
        return "-1", "Invalid file type"

    # Synchronous code: Bad :(
    pdf_doc = fitz.open(path)
    pdf_text = ""

    # Stores all the text content of the pdf into `pdf_text` variable
    [pdf_text:= pdf_text + pdf_doc[page].get_text().replace("\n", "") for page in range(pdf_doc.page_count)]

    # TODO: Extract Image?
    # https://stackoverflow.com/questions/2693820/extract-images-from-pdf-without-resampling-in-python

    candidate_id, err = await analyze(pdf_text)

    return candidate_id, err
