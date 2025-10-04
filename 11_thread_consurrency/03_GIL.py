# GIL (Global Interpreter Lock) in Python:
# When two or more threads are running in a python program , if they want to access the same resource at the same time , it can lead to data corruption or inconsistent results.  To prevent this , Python uses a mechanism called the Global Interpreter Lock (GIL) . The GIl is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once. This means that even in a multi-threaded program, only one thread can execute Python code at a time.  After completing a certain number of bytecode instructions , the GIL is released and another thread can acquire it and run. This switching happens very quickly , giving the illusion of parallelism , but in reality , only one thread is executing at any given moment.

import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} starting chai brewing")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} fininshed chai brewing")

thread1 = threading.Thread(target=brew_chai, name="ChaiMaker-1")
thread2 = threading.Thread(target=brew_chai, name="Chaimaker-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

print(f"Total time taken: {end - start:.2f} seconds")