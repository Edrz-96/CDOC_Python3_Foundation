# Process = program thats running, a container of Threads
# Thread = a discreet bit of processing


# Threading
# Python has a concept called GIL, essentially locking the interpreter on a single thread
# This means that only one thread can be in a state of execution at any point in time.
# The Thread class represents an activity that is run in a separate thread of control.
# There are two ways to specify the activity:by passing a callable object to the constructor,
# or by overriding the run() method in a subclass.


COUNT = 50000000
from threading import Thread
import time


def my_func(*args):
    print("From thread", args)

time.sleep(2)
th1 = Thread(target=my_func, args="1")
th2 = Thread(target=my_func, args="2")
# Once a thread object is created, its activity must be started by calling the thread’s start() method.
# This invokes the run() method in a separate thread of control.
th1.start()
th2.start()
print("From main")
# Wait until the thread terminates. This blocks the calling thread until the thread whose join() method
# is called terminates – either normally or through an unhandled exception – or until the optional timeout occurs.
th1.join()
th2.join()


# Join returns None, so when actually checking a thread, use isAlive.
# th1.isAlive()
# th2.isAlive()

# Threading
# multi_threaded.py
def countdown_one(n):
    while n > 0:
        n -= 1


t1 = Thread(target=countdown_one, args=(COUNT // 2,))
t2 = Thread(target=countdown_one, args=(COUNT // 2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken in seconds -', end - start)

# Multiprocessing
from multiprocessing import Pool


def countdown(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(countdown, [COUNT // 2])
    r2 = pool.apply_async(countdown, [COUNT // 2])
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken in seconds -', end - start)


## Look up aysncIO, concurrentFutures
