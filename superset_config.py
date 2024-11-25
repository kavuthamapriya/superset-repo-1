import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database connection URI 
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

# Secret Key
SECRET_KEY = os.getenv('SUPERSET_SECRET_KEY')

# Admin Credentials 
SUPERSET_ADMIN_USERNAME = os.getenv('SUPERSET_ADMIN_USERNAME')
SUPERSET_ADMIN_PASSWORD = os.getenv('SUPERSET_ADMIN_PASSWORD')
SUPERSET_ADMIN_EMAIL = os.getenv('SUPERSET_ADMIN_EMAIL')

# Enable proxy fix
ENABLE_PROXY_FIX = True

# Additional configurations
SUPERSET_WEBSERVER_PORT = 8088


