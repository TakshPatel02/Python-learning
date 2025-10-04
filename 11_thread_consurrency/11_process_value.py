from multiprocessing import Process , Value

def increment(counter):
    for _ in range(100000):
        with counter.get_lock():
            counter.value +=1

if __name__ =="__main__":
    counter = Value('i' , 0)
    processes = [Process(target=increment, args=(counter, )) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]

    print(f"Final counter value: {counter.value}")

# The use of Value allows multiple processes to share a single integer variable (counter in this case). Each process increments the counter 100,000 times. The get_lock() method ensures that only one process can modify the counter at a time, preventing race conditions and ensuring the final value is accurate. 