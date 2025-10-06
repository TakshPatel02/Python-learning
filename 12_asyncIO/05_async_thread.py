import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Checking the stock for {item}...")
    time.sleep(3) # blocking operation
    return f"{item} is in the stock."

async def main():
    # get_running_loop() is a loop for threading
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool , check_stock , "Masala chai")
        print(result)

asyncio.run(main())

# In this example, the blocking function check_stock is executed in a separate thread using ThreadPoolExecutor. And the main function awaits its completion without blocking the event loop.

