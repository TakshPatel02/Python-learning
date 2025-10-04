import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1
    
threads = [threading.Thread(target=increment) for _ in range(5)]
[t.start() for t in threads] # comphrehension way of writing the loop
[t.join() for t in threads] # comphrehension way of writing the loop

print(f"Final counter value : {counter}")

# without lock the counter value will be inconsistent 