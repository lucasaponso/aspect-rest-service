from fastapi import status, HTTPException, Response
from fastapi import HTTPException, status, APIRouter
from schemas import TokenSchema
from deps import validate_database_creds
import sqlite3
from schemas import UserAuth, TokenSchema
from utils import (
    create_access_token,
)

router = APIRouter(
    prefix="/identity/auth"
)

@router.post('/request', tags=["user"], summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(user_creds: UserAuth, response: Response):
    if validate_database_creds(user_creds):
        access_token = create_access_token(user_creds.username)

        conn = sqlite3.connect('db/user.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO user (username, password) VALUES (?, ?)''', (user_creds.username,user_creds.password,))
        conn.commit()
        conn.close()



        return {"access_token": access_token}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Login Credentials")