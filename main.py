from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import routes.user as user
import routes.data as data
import sqlite3


"""
The following file (main.py) is the entry point to the following API. We first start by initialising the fastAPI application.
Then we include two routes (user and data). The user route includes the endpoint to login. The data route includes the endpoint to get all inventory data.
Following this we initialise our in file database, by using sqllite3. We first connect to the db/user.db file. Following this we create a table that stores username and password.
This table is used to keep track of users that have logged in.
"""

app = FastAPI()

app.include_router(user.router)
app.include_router(data.router)

conn = sqlite3.connect('db/user.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS user (username text, password text)''')
conn.commit()


"""
The following endpoint is the root endpoint for this application.

Returns: Access to the docs page
"""
@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url='/docs')