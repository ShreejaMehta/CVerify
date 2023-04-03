# Install spacy stuff
import os

os.system("pipenv install")
os.system("pipenv run spacy download en_core_web_sm")

print("Make sure to check 'config.toml' file before running the server")
