"""
Programs run so quickly, it can be hard to see what is happening.

Sometimes they run too fast, and we need to try and prevent collisions.

We can use the time module to do this, but we still have some collisions.
"""

from time import sleep
from threading import *


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello!")
            sleep(1)


class Goodbye(Thread):
    def run(self):
        for i in range(5):
            print("Goodbye!")
            sleep(1)


# Run Program
t1 = Hello()
t2 = Goodbye()

t1.start()
t2.start()