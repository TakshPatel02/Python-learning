import asyncio
import time
import threading

def background_worker():
    while True:
        time.sleep(1)
        print(f"Logging the system health 🕰️")

async def fetch_order():
    await asyncio.sleep(3)
    print("Order fetched 🍽️")

threading.Thread(target=background_worker , daemon=True).start()

asyncio.run(fetch_order())

# In this example, the background_worker function runs in a separate daemon thread, continuously logging system health every second. Meanwhile , the main asyncio event loop runs the fetch_order coroutine, which simulates fetching an order with a 3-second delay. The background worker thread does not block the main event loop, allowing both tasks to run concurrently.