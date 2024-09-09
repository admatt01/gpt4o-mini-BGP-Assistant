import aiohttp
import os

async def view_prefix_details(arguments):
    """
    Retrieve details for a specific IP prefix using the BGPView API asynchronously.
    Args:
    arguments (dict): A dictionary containing 'ip_addr' and 'cidr'
    Returns:
    dict: A dictionary containing the API response with prefix details
    """
    ip_addr = arguments['ip_addr']
    cidr = arguments['cidr']
    url = f"{os.getenv('BGPVIEW_BASE_URL')}/prefix/{ip_addr}{cidr}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()

# Example usage:
# import asyncio
# result = asyncio.run(view_prefix_details({"ip_addr": "192.209.63.0", "cidr": "/24"}))
# print(result)