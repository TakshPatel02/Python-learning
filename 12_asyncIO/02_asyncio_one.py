import asyncio

# this is normal async function (coroutine)
async def brew_chai():
    print("brewing chai...")
    await asyncio.sleep(4)
    print("chai is ready!")

# to run the async function we have to use asyncio.run() method 
asyncio.run(brew_chai())