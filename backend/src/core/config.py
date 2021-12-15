import os
from dotenv import load_dotenv

load_dotenv(os.path.abspath(__file__ + "/../../../../.env"))

API_V1_PREFIX = os.environ.get('API_V1_PREFIX', '/api/v1')
PROJECT_NAME = os.environ.get('PROJECT_NAME', 'React App Backend')

JWT_SECRET = os.environ.get('JWT_SECRET')
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
