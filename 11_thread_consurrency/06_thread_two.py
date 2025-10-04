# passing args in the threads
import threading
import time

def prepare_chai(type_ , wait_time):
    print(f"{type_} brewing...")
    time.sleep(wait_time)
    print(f"{type_} is ready.")

t1 = threading.Thread(target=prepare_chai, args=("Masala chai" , 2))
t2 = threading.Thread(target=prepare_chai, args=("Ginger chai" , 3))

t1.start()
t2.start()
t1.join()
t2.join()

