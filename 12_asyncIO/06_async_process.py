import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt(data):
    return f"🔒 {data[::-1]}"

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool , encrypt , "credit_card_1234")
        print(result)

if __name__ == "__main__":
    asyncio.run(main())

# In this example, the blocking function encrypt is executed in a separate process using ProcessPoolExecutor. And the main function awaits its completion without blocking the event loop.

# for any processing task we have to put the function in __main__ block to avoid recursive spawning of subprocesses.
