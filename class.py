class Restaurant:

    def  __init__(self, name, location, menu=None):
        self.name = name
        self.location = location
        self.menu = menu if menu is not None else[]
        self.orders = []
        self.TotalSales = 0

    def take_order(self, amount):
        if amount in self.menu:
            self.menu.order(amount)
            print(f"{amount} order taken")
        else:
            print('item not available')

    def prepared_food(self, food):
        if self.orders:
            print('preparing food')

    def serve_food(self):
        if self.orders:
            print('Food serve')
        else:
            print('No food serve')

    def generate_bill(self, orders):
        bill = 0
        for food in self.orders:
           bill += food['price'] * food['qty']
        return bill






class person:

    def __init__(self, name, age):
        self.name = name
        self.age = 24

    def introduce(self):
        print(f"may name is {self.name}, amd i am {self.age} years old")

p = person('el', 24)
p.introduce()









class product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} -$ {self.price}"

class cart:
    def __init__(self):
        self.product = []

    def  add_product(self, product):
        self.product.append(product)

    def total(self):
        return sum(product.price for product in self.product)

    def __str__(self):
        return "\n".join(product.price for product in self.product)

class customer:

    def __init__(self, name):
        self.name = name
        self.cart = cart()

    def add_to_card(self):
        self.cart.add_product(product)

    def checkout(self):
        total_price = self.cart.total()
        return f"Total amount dor {self.name}: ${total_price}"

laptop = product("Laptop", 2000)
phone = product("iPhone", 950)

customer = customer("john")
customer.add_to_card()
customer.add_to_card()

print(customer.cart)
print(customer.checkout())




class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    #@property
    #def width(self):
     #   return self.width

#    @width.setter
 #   def width(self, value):
  #      if value > 0:
   #         self.width = value
    #    else:
     #       print("width must be greater than 0")

rect = Rectangle(5, 2)
print(rect.area)

class MathOperation:

    @staticmethod
    def add(a, b):
        return a+b

    @staticmethod
    def multiply(a, b):
        return a*b

print(MathOperation.add(5, 7))
print(MathOperation.multiply(2, 9))


class MyClass:

    ClassVariable = "I'm a class variable"

    def __init__(self, InstanceVariable):
        self.InstanceVariable = InstanceVariable

    def InstanceMethod(self):
        return f"Instance variable: {self.InstanceVariable}"

    @classmethod
    def ClassMethod(cls):
        return f"I'm an instance variable "

obj = MyClass("I'm an instance variable")
print(obj.ClassMethod())
print(MyClass.ClassMethod())

class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} make sound."

class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} bark."

class Cow(Animal):
    def speak(self):
        return f"{self.name} moos."

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

dog = Dog("Buddy", "Beagle")
cat = Cat("Whiskers")
cow = Cow("MooMoo")

for animal in [dog, cat, cow]:
    print(animal.speak())


MyDog = Dog("Buddy", "Golden Retriever")
details = MyDog.speak()
print(details)


class car:


    wheels = 4

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.model} {self.year}"

MyCar = car("Toyota", "Corolla", 2021)
details = MyCar.description()
print(details)
print(MyCar.wheels)


class male:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} says woof!"

person = male("mosh", 29)
print(person.walk())





class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi i am {self.name}')

john = Person('mosh smith')
john.talk()

bob = Person('bob smith')
bob.talk()


class mammal:

    def walk(self):
        print('walk')

class dog(mammal):
    def bark(self):
        print('bark')

class cat(mammal):
    pass

dog1 = dog()
dog1.bark()



class Point:

    def __init__(self, x , y):
        self.x = x
        self.y = y


    def move (self):
        print('draw')

    def draw(self):
        print('draw')

point = Point(10, 20)
print(point.x)