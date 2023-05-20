class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name + " says bark!")


my_dog = Animal("tomy");
my_dog.speak();
