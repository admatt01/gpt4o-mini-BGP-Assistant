import aiohttp
import os

async def view_ip_address_details(arguments):
    """
    Retrieve details for a specific IP address using the BGPView API asynchronously.
    
    Args:
    arguments (dict): A dictionary containing 'ip_addr'
    
    Returns:
    dict: A dictionary containing the API response with IP address details
    """
    ip_addr = arguments['ip_addr']
    url = f"{os.getenv('BGPVIEW_BASE_URL')}/ip/{ip_addr}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()

# Example usage:
# import asyncio
# result = asyncio.run(view_ip_address_details({"ip_addr": "8.8.8.8"}))
# print(result)