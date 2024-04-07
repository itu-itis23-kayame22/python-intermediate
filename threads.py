#A thread is an entity within a process that can be scheduled for execution
from threading import Thread

def square_numbers():
    for i in range(1000):
        result = i * i

        
if __name__ == "__main__":        
    threads = []
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

# Sharing data ----------------------------------

from threading import Thread
import time

# global threads value
database_value = 0

def increase():
    global database_value 

    local_copy = database_value #have local copy
        
    local_copy += 1
    time.sleep(0.1)
        
    database_value = local_copy


if __name__ == "__main__":

    print('Start value: ', database_value)

    t1 = Thread(target=increase)
    t2 = Thread(target=increase)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End value:', database_value)

    print('end main')

#Using Locks --------------------------
from threading import Thread, Lock
import time
database_value = 0

def increase(lock):
    global database_value 
    lock.acquire()
    
    local_copy = database_value
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy

    # unlock 
    lock.release()


if __name__ == "__main__":

    lock = Lock()
    print('Start value: ', database_value)

    t1 = Thread(target=increase, args=(lock,)) #pass lock to target
    t2 = Thread(target=increase, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End value:', database_value)

    print('end main')

#Queue in multithreading --------------------------
from threading import Thread, Lock, current_thread
from queue import Queue

def worker(q, lock):
    while True:
        value = q.get() 

        with lock:
            print(f"in {current_thread().name} got {value}")# prevent printing at the same 
        #tasks
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    num_threads = 10
    lock = Lock()

    for i in range(num_threads):
        t = Thread(name=f"Thread{i+1}", target=worker, args=(q, lock))
        t.daemon = True  # dies when the main thread dies
        t.start()
    
    for x in range(20):
        q.put(x)

    q.join()  # Blocks until all processed.

    print('main done')