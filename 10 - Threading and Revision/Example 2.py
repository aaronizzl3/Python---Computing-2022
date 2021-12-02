"""
This file extends our previous example.

We will import the Thread class and apply it to our classes.

Remember you have a choice; create a thread object or run threads on classes.
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

t1.run()
t2.run()