import aiohttp
import os

async def search_org_details(arguments):
    """
    Search for organization details using the BGPView API asynchronously.
    Args:
    arguments (dict): A dictionary containing 'query_term'
    Returns:
    dict: A dictionary containing the API response with organization details
    """
    query_term = arguments['query_term']
    url = f"{os.getenv('BGPVIEW_BASE_URL')}/search?query_term={query_term}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()

# Example usage:
# import asyncio
# result = asyncio.run(search_org_details({"query_term": "cloudplus"}))
# print(result)
