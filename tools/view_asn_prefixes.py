import requests
import os
import aiohttp

async def view_asn_prefixes(arguments):
    asn = arguments['asn']
    url = f"{os.getenv('BGPVIEW_BASE_URL')}/asn/{asn}/prefixes"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()