import asyncio
async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
async def main():
    urls = ['<https://example.com>', '<https://example.org>']
    tasks = [fetch_url(url) for url in urls]
    responses = await asyncio.gather(*tasks)
    for response in responses:
        print(response)
asyncio.run(main())

# The asyncio module in Python provides a 
# framework for asynchronous programming using coroutines. It allows you to 
# write asynchronous code that can efficiently handle I/O-bound operations without blocking the event loop.