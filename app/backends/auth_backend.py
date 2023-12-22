import asyncio
import logging

import aiohttp
from fastapi import Header

from app.settings import AUTH_SERVER

logger = logging.getLogger(__name__)


async def auth_handler(headers: Header):
    headers = {
        "Authorization": headers.get("Authorization", "")
    }
    return {"status": True}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(AUTH_SERVER, headers=headers) as response:
                status_code = response.status
                data = await asyncio.wait_for(response.json(), timeout=20)
                if status_code != 200:
                    logger.debug(f"auth_handler fail: {data}")
                    return None

                if "c2c" not in data.get("allowed_services", {}):
                    return None
                return data
    except asyncio.TimeoutError:
        print(f"Timeout reached while fetching {AUTH_SERVER}")
        return None
    except Exception as e:
        print(f"An error occurred while fetching {AUTH_SERVER}: {str(e)}")
        return None