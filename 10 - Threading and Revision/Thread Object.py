"""
Rather than use the Thread class, we can create a Thread() object and target a method and their run time.

We are essentially saying, run this function, wait for it to finish, then return to the main thread.

The main thread will not run if we've told it previous threads need to have joined.
"""

from threading import *
from time import sleep


def example():
    for x in range(5):
        print(current_thread().getName())
        sleep(1)


t1 = Thread(target=example)
t2 = Thread(target=example)
print("Starting...")
t1.start()
t2.start()
t1.join()
t2.join()
print("All threads closed.")