import os
from app.settings import logging
import IP2Location

if not __name__ == "__main__":
    from app.settings import DB_PATH
else:
    DB_PATH = "../../db/IP2LOCATION-LITE-DB3.BIN"


logger = logging.getLogger(__name__)


class GeoipDBException(Exception):
    ...


ERROR_IP = "INVALID IP ADDRESS"

class GeoipBackend:
    db_file = None
    database = None

    def __init__(self, db: str = DB_PATH):
        self.db_file = db
        if not self.db_file:
            raise GeoipDBException("No db configured")

    def init_db(self):
        if not self.db_file:
            raise GeoipDBException("No db configured")

        logger.info(f"init db {self.db_file}")
        self.database = IP2Location.IP2Location(self.db_file)
        return self

    def check_ip(self, ip: str):
        rec = self.database.get_all(ip)
        if rec.city == ERROR_IP:
            return {"error": ERROR_IP}
        return {
            "ip": rec.ip,
            "country": rec.country_long,
            "region": rec.region,
            "city": rec.city
        }


if __name__ == "__main__":
    a = GeoipBackend(db="../../db/IP2LOCATION-LITE-DB3.BIN").init_db()
    print(a.check_ip("195.238.246.203"))
