from fastapi import Response, HTTPException


def response403(response: Response, data: dict | str | int = None):
    response.status_code = 403
    return HTTPException(status_code=response.status_code, detail="Access denied" if not data else data)


def response404(response: Response, data: dict | str | int = None):
    response.status_code = 404
    return HTTPException(status_code=response.status_code, detail="Bad request" if not data else data)


def response200(response: Response, data: dict | str | int = None):
    response.status_code = 200
    return "Success" if not data else data
