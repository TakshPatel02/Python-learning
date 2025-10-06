# Async-await : asynchronous programming , in this we can run multiple tasks concurrently without waiting for each task to complete before starting the next one . for this we have to write async def instead of def and await keyword is used to call an asyncs function.

# Event loop : it is a core of every asyncio application , it runs in the background and manages the execution of asynchronous tasks . it schedules and executes tasks , handles I/O operations and manages coroutines . 

# Event Queue : it is a data structure that holds the tasks that are waiting to be executed by the event loop . when a task is created , it is added to the event queue and the event loop picks up tasks from the queue and executes them . 
