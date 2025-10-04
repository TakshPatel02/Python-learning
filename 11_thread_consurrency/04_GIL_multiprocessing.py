from multiprocessing import Process
import time

def crunch_number():
    print(f"start the count process...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"ended the count process...")

if __name__ == "__main__":
    start = time.time()

    p1 = Process(target=crunch_number)
    p2 = Process(target=crunch_number)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time taken : {end - start:.2f} seconds")

# In this code , we are using the multiprocessing module to create two separate processes that run the crunch_number function concurrently. Each process has its own Python interpreter and memory space, so they can run truly in parallel on multi-core processors, efficiently utilizing CPU resources and bypassing the GIL limitation.
# Note : The if __name__ == "__main__": guard is necessary when using multiprocessing in Windows to prevent recursive spawning of subprocesses.