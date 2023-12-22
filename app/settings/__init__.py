import dotenv
import os

if os.path.exists(".env"):
    dotenv.load_dotenv(".env")

from app.settings.external import AUTH_SERVER, FS_API_INIT_CALL_URI
from app.settings.geoip import DB_PATH
from app.settings.logs import logging
