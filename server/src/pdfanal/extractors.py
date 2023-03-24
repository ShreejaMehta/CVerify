# Note: All the functions defined here are purely synchronous,
#       and implementing a async version "might" be a herculean task
# Yes, I know. This code sucks
# TODO: try converting from purely synchronous to async
import re
import spacy
from spacy.matcher import Matcher
import pandas as pd
import validators


# NLP based
nlp = spacy.load("en_core_web_sm") # bootstrapping first time might take time
async def extract_name(text: str) -> str:
    matcher = Matcher(nlp.vocab)
    nlp_text = nlp(text)

    # First name and Last name are always Proper Nouns
    pattern = [{"POS": "PROPN"}, {"POS": "PROPN"}]
    # pattern = [{"POS": "PROPN"}, {"POS": "PROPN"}, {"POS": "PROPN"}] # For First Middle last

    matcher.add("NAME", [pattern])

    matches = matcher(nlp_text)

    for match_id, start, end in matches:
        span = nlp_text[start:end]
        return span.text
    return ""



async def extract_skills(text: str) -> list[str]:
    nlp_text = nlp(text)

    # removing stop words and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]
    
    # reading the csv file
    data = pd.read_csv("skills.csv") 
    
    # extract values
    skills = list(data.columns.values)
    
    skillset = []
    
    # check for one-grams (example: python)
    for token in tokens:
        if token.lower() in skills:
            skillset.append(token)
    
    # check for bi-grams and tri-grams (example: machine learning)
    for token in nlp_text.noun_chunks:
        token = token.text.lower().strip()
        if token in skills:
            skillset.append(token)
    
    return [i.capitalize() for i in set([i.lower() for i in skillset])]


async def extract_education(text: str) -> list[str]:
    #TODO: Extract education
    return []


# ReGeX based
async def extract_email(text: str) -> str:
    email = re.findall(r"([^@|\s]+@[^@]+\.[^@|\s]+)", text)
    if email:
        try:
            return email[0].split()[0].strip(';') # IDK what this does
        except IndexError:
            pass
    return ""


async def extract_mobile_number(text: str) -> str:
    phone = re.findall(re.compile(r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'), text)

    if phone:
        number = ''.join(phone[0])
        if len(number) > 10:
            return '+' + number
        return number
    return ""


async def extract_github(text: str) -> str:
    pat = re.compile(r"github.com/([^\s^/]+)")
    matches = pat.findall(text)

    if len(matches) == 0:
        return ""
    return matches[0]  # Return the first occurance


async def extract_linkedin(text: str) -> str:
    pat = re.compile(r"((?:(?:[\w]+\.)?linkedin\.com\/(?:pub|in|profile)\/(?:[-a-zA-Z0-9]+)\/*))")
    matches = pat.findall(text)

    if len(matches) == 0:
        return ""
    return matches[0]  # Return the first occurance


async def extract_urls(text: str) -> list[str]:
    text = "".join(letter for letter in text if letter.isascii())
    pat = re.compile(r"(https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*))")
    matches = pat.findall(text)
    return matches
