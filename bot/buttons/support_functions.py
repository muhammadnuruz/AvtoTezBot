import json

import requests


async def check_brand(brand: str):
    brands = json.loads(
        requests.get(url=f"http://127.0.0.1:8000/api/brands/").content
    )
    for name in brands['results']:
        if brand == name['name']:
            return 1
    return 0


async def check_spare_part(part: str):
    spare_parts = json.loads(
        requests.get(url=f"http://127.0.0.1:8000/api/spare_parts/").content
    )
    for name in spare_parts['results']:
        if part in [name['name'], name['ru_name']]:
            return 1
    return 0
