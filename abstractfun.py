from abc import ABC , abstractmethod

class Animal(ABC):
    def __init__(self,name,habitat):
        self.name = name
        self.habitat = habitat

    def display(self):
        print(f"Name :{self.name} stays {self.habitat}")
    
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def __init__ (self,name,habitat,breed):
        super().__init__(name,habitat)
        self.breed = breed
    def speak(self):
        print(f"{self.name} is saying {self.breed} ")
class Sparrow(Animal):
    def __init__(self,name,habitat,phrase):
        super().__init__(name,habitat)
        self.phrase = phrase
    def speak (self):
        print(f"{self.name} is saying  {self.phrase}")
class Whale(Animal):
    def __init__(self,name,habitat,sentence):
        super().__init__(name,habitat)
        self.sentence = sentence
    def speak(self):
        print(f"{self.name} is telling {self.sentence} ")

dog = Dog("Dogesh" , "Kennel", "Bhau Bhau")
sparrow = Sparrow("Chintu" , "Nest" , "Chii Chii")
whale = Whale("Bablu", "Sea", "hmm")


print("-----Animal-----")
print()

for Animal in [dog , sparrow , whale]:
    Animal.display()
    Animal.speak()
    print()