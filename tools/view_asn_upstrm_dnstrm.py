import requests
import os
import aiohttp

async def view_asn_upstreams(arguments):
    asn = arguments['asn']
    url = f"{os.getenv('BGPVIEW_BASE_URL')}/asn/{asn}/upstreams"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()

async def view_asn_downstreams(arguments):
    asn = arguments['asn']
    url = f"{os.getenv('BGPVIEW_BASE_URL')}/asn/{asn}/downstreams"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()