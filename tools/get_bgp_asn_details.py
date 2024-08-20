import requests
import os
import aiohttp

async def get_bgp_asn_details(arguments):
    asn = arguments['asn']
    url = f"{os.getenv('BGPVIEW_BASE_URL')}/asn/{asn}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()
