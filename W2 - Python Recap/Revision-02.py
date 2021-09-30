# Lists
myList = ["Apple", "Banana", "Plum"]
print(myList[0])

myList.append("Orange")
myList[0] = "Pear"

# Dictionaries
myDict = {
    "Name": "Aaron",
    "Colour": "Blue",
    1: True
}

print(myDict["Name"])

myDict["Job"] = "Lecturer"
myDict["Colour"] = "Green"

print(myDict.get("Name"))


# Iterative Techniques
for x in range(10):
    print(x)


while True:
    print("Menu is alive.")
    break


myList = [4, 1, 5, 10, 6]

for index, value in enumerate(myList):
    print(f"Index: {index} - Value: {value}")
    myList[index] += 1

print(myList)

n = 0

while n < 10:
    n += 1
    print(n)


# Functions
def SayHello(n="Slim Shady"):
    n += "Zzz"
    print(f"Hi! My name is {n}.")
    return n


newName = SayHello("Aaron")
print(newName)

SayHello()


def RectangleArea(w, l=5):
    area = w * l
    return area


print(RectangleArea(10))
print(RectangleArea(5, 10))


# Logical Operators
# AND, OR, NOT

role = "Admin"
password = "Password"

if role == "Admin" and password == "Password":
    print("Logged in")


if role == "Admin":
    if password == "Password":
        print("Logged in")


x = True
y = True

if x == True and not(y == True):
    print("True")


