import os

DB_PATH = os.getenv("DB_PATH", "")
if not os.path.exists(DB_PATH):
    raise Exception("No geoip database")

