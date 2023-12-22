import logging
import os

logging.basicConfig(
    filename=os.getenv("LOG_PATH", "./geoip.log"),
    level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
)
