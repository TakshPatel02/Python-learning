import asyncio
import aiohttp

async def fetch(session , url):
    async with session.get(url) as response:
        print(f"Fetching the {url} and status is {response.status}")

async def main():
    urls = ["https://httpbin.org/delay/1"] * 3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session , url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())

# in this code we get the response in 1 second as all the three requests are made concurrently . 
# *tasks is used to unpack the list of tasks and pass them as separate arguments to asyncio.gather()
