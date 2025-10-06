import asyncio
import time

async def brew(name):
    print(f"brewing {name}...")
    # await asyncio.sleep(2)
    time.sleep(2)
    print(f'{name} is ready!')

async def main():
    await asyncio.gather(
        brew("masala chai"),
        brew("green tea"),
        brew("black tea"),
    )

asyncio.run(main())
# here we are running multiple tasks concurrently using asyncio.gather() method which takes multiple coroutines as arguments and runs them concurrently.

# all the process run at the same time and we don't have to wait for each task to complete before starting the next one . this is the main advantage of asynchronous programming. This is a non blocking operation.

# Note : if we use time.sleep() instead of asyncio.sleep() then it will block the event loop and all the tasks will run sequentially one after another . so we should always use asyncio.sleep() in async functions to avoid blocking the event loop.