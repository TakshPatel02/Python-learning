import threading
import time

def monitoring():
    while True:
        print("Monitoring the system health 🕰️")
        time.sleep(2)

t = threading.Thread(target=monitoring ,daemon=True)
t.start()

print("Main thread is running...")

# The main thread will finish after this sleep, and since the monitoring thread is a daemon, it will not prevent the program from exiting.

# The daemon thread will automatically terminate when the main program exits. 