# Factory Pattern Example
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def get_pet(pet="dog"):
    pets = dict(dog=Dog(), cat=Cat())
    return pets.get(pet, ValueError("Invalid pet type"))

if __name__ == "__main__":
    d = get_pet("dog")
    print(d.speak())
    c = get_pet("cat")
    print(c.speak())
