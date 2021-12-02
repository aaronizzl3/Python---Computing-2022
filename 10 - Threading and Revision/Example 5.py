"""
Our program itself runs on its own thread; we can identify this as the MAIN thread.

No matter how many other threads we make, this main thread will always be running.

We can't forget about it, and we can use join() to make our program wait before continuing.
"""

from time import sleep
from threading import *


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello!")
            sleep(2)


class Goodbye(Thread):
    def run(self):
        for i in range(5):
            print("Goodbye!")
            sleep(2)


# Run Program
t1 = Hello()
t2 = Goodbye()

t1.start()
t2.start()

t1.join()
t2.join()

print("Where is this thread going to go?")
