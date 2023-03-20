from databases import Database
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

# Database instance: BAD CODING
database: Database
def get_db():
    global database
    return database


credentials_metadata = MetaData()
sessions_metadata = MetaData()
candidate_info_metadata = MetaData()

credentials = Table(
    "credentials",
    credentials_metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String, unique=True),
    Column("password", String),
)

sessions = Table(
    "sessions",
    sessions_metadata,
    Column("username", String, ForeignKey(credentials.c.username), nullable=False),
    Column("session_id", String)
)

candidate_info = Table(
    "candidate_info",
    candidate_info_metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String),
    Column("number", String),
    Column("email", String),
    Column("skills", String),
    Column("education", String),
    Column("github", String),
    Column("linkedin", String),
    Column("status", String)
)


# Create tables :)
def init_database(engine, db):
    credentials_metadata.create_all(engine)
    sessions_metadata.create_all(engine)
    candidate_info_metadata.create_all(engine)

    global database
    database = db
