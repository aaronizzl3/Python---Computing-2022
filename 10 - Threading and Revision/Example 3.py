"""
Start() calls whichever method we've identified as run() inside of our class. Almost like a constructor.

We identify the method we want to activate whenever we create a thread of the class.

In this file, we're creating two threads.
"""

from threading import *


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello!")


class Goodbye(Thread):
    def run(self):
        for i in range(5):
            print("Goodbye!")


# Run Program
t1 = Hello()
t2 = Goodbye()

t1.start()
t2.start()