# Class Inheritance Example
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

if __name__ == "__main__":
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    print(dog.speak())
    print(cat.speak())
