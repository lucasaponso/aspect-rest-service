import os
from dotenv import load_dotenv

load_dotenv()

"""
The following file (constants.py) loads the environment variables that were set in the Dockerfile. See the Dockerfile for more information.
We use the os library to access the value of the env variable. The remaining project files import these variables.
"""

ASPECT_SERVER_HOST = os.getenv('ASPECT_SERVER_HOST')
ASPECT_DB = os.getenv('ASPECT_DB')
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
ALGORITHM = os.getenv('ALGORITHM')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
