from multiprocessing import Process , Queue
import time

def prepare_chai(queue):
    queue.put("Boil water")

if __name__ == "__main__":
    queue = Queue()

    p = Process(target=prepare_chai, args=(queue, ))
    p.start()
    p.join()
    print(queue.get())

# In this example, we create a Queue to facilitate communication between the main process and the child process. The child process executes the prepare_chai function, which puts a message into the queue. After the child process completes, the main process retrieves and prints the message fromt the queue.