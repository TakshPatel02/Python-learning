import threading

chai_stock = 0

def restock():
    global chai_stock
    for _ in range(100000):
        chai_stock += 1

threads = [threading.Thread(target=restock) for _ in range(2)]

for t in threads: t.start()
for t in threads: t.join()

# This code is race condition prone because multiple threads are modifying the shared variable chai_stock simultaneously without any synchronization mechanism. This can lead to inconsistent or incorrect results.

print("Final chai stock:" , chai_stock) #The final chai stock may not be 200000