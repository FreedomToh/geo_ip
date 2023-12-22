import dotenv
import os
import logging

if os.path.exists(".env"):
    dotenv.load_dotenv(".env")

logging.basicConfig(
    filename=os.getenv("LOG_PATH", "./geoip.log"),
    level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
)

DB_PATH = os.getenv("DB_FILE", "")
if not os.path.exists(DB_PATH):
    raise Exception("No geoip database")

NEED_AUTH = os.getenv("NEED_AUTH", True) in ["True", "true", True]
AUTH_SERVER = os.getenv("AUTH_SERVER", "")

logger = logging.getLogger(__name__)
if not NEED_AUTH:
    print("Auth doesn't work!")
    logger.warning("Auth doesn't work!")



