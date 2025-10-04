import threading
import time

def take_order():
    for i in range(1 , 4):
        print(f"Taking order for #{i}")
        time.sleep(1)

def brew_chai():
    for i in range(1 , 4):
        print(f"Brewing chai for #{i}")
        time.sleep(2)

# Creating the threads
order_thread = threading.Thread(target=take_order)
brew_thread = threading.Thread(target=brew_chai)

# Starting the threads
order_thread.start()
brew_thread.start()

# Waiting for both threads to complete
order_thread.join()
brew_thread.join()

print("All orders taken and chai brewed.")

# Note : The output may vary in order due to the concurrent nature of threads. This is multithreadings. Threads swithing happens so fast that it appears that both tasks are happening simultaneously. Both the tasks are not running at the same time but they are interleaved.