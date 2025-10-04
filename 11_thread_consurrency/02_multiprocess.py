from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start of {name} chai brewing")
    time.sleep(3)
    print(f"End of {name} chai brewing")

# main method to create multiple processes
if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai , args=(f"ChaiMaker-{i+1}",))
        for i in range(3)
    ]

    # Starting all processes
    for p in chai_makers:
        p.start()

    # Waiting for all processes to complete
    for p in chai_makers:
        p.join()

    print("All chai is served.")

# In this example , we create multiple processes to brew chai simultaneously. Each process runs independently and can utilize multiple CPU cores , allowing true parallelism. This is different from multithreading where threads share the same memory space and may not run in parallel due to the Global Interpreter Lock (GIL) in Cpython. Here, each chai maker process brews chai independently, and the output will show that all chai makers start and finish their tasks around the same time, demonstrating true concurrency.

# Note : The output may vary in order due to the concurrent nature of processes. This is multiprocessing. Each process runs independently and can utilize multiple CPU cores, allowing true parallelism.