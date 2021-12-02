"""
In this file, we are creating two objects from our classes and calling their methods.

The code works as you would expect; it waits for the first method to finish before starting the next.

Threading will give allow us to run things simultaneously.
"""


class Hello:
    def run(self):
        for i in range(5):
            print("Hello!")


class Goodbye:
    def run(self):
        for i in range(5):
            print("Goodbye!")

# Run Program
t1 = Hello()
t2 = Goodbye()

t1.run()
t2.run()