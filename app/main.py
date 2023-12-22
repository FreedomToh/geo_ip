import sys

from app.settings import logging

from fastapi import FastAPI, Request, Response

from app.backends.auth_backend import auth_handler
from app.backends.geoip_backend import GeoipBackend
from app.response_handlers import response403, response404, response200

app = FastAPI(title='geoip')
geoip = GeoipBackend().init_db()
logging.info('API is starting up')


@app.get("/ip_info/{ip}/")
async def ip_info(ip: str, request: Request, response: Response):
    logging.info(f"Start {ip}")
    r = await auth_handler(request.headers)
    if not r:
        response.status_code = 403
        return response403(response)

    result = geoip.check_ip(ip)
    if "error" in result:
        return response404(response)
    return response200(response, data=result)
