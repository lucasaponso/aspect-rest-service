import pymssql
from fastapi import Depends
from deps import get_current_user
from typing import Generator
from schemas import UserAuth
from constants import (
    ASPECT_SERVER_HOST,
    ASPECT_DB
)

"""
The following function returns a db connection to an endpoint.
The endpoint must pass the users credentials, to then connect to the DB.

Parameters:
- user: UserAuth (depends on the output of get_current_user)

Returns:
- DB object
"""

def get_db(user: UserAuth = Depends(get_current_user)) -> Generator[pymssql.Connection, None, None]:
    db: pymssql = pymssql.connect(server=ASPECT_SERVER_HOST, user=user.username, password=user.password, database=ASPECT_DB)
    try:
        yield db
    finally:
        db.close()