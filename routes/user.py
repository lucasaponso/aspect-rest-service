from fastapi import Response
from fastapi.responses import JSONResponse
from fastapi import APIRouter, HTTPException, status
from deps import validate_database_creds
import sqlite3
import bcrypt
from schemas import UserAuth, SuccessLogin, FailLogin
from utils import (
    create_access_token,
)

router = APIRouter(
    prefix="/identity/auth"
)

@router.post('/request', tags=["user"], summary="Create access and refresh tokens for user")
async def login(user_creds: UserAuth):
    if validate_database_creds(user_creds):

        access_token = create_access_token(user_creds.username)

        conn = sqlite3.connect('db/user.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO user (username, password) VALUES (?, ?)''', (user_creds.username,user_creds.password,))
        conn.commit()
        conn.close()

        status_code = status.HTTP_200_OK
        login_attempt = SuccessLogin(username=user_creds.username, token=access_token, status=True, msg="User has been login successfully")
    else:
        status_code = status.HTTP_401_UNAUTHORIZED
        login_attempt = FailLogin(username=user_creds.username, status=False, msg=f"Incorrect login credentials, thw following user was unable to login successfully: {user_creds.username}")

    return JSONResponse(status_code=status_code, content=login_attempt.dict())