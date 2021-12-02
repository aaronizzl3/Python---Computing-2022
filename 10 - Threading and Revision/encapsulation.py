class Student:
  __name = None

  def __init__(self, name):
    self.__name = name

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, value):
    self.__name = value


myObject = Student("Aaron")
print(myObject.name)

myObject.name = "Maximus"
print(myObject.name)

