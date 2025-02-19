class Person:
    def set_details(self):
        self.name = "John" #instance variables
        self.age = 20

    def display(self):      #creating methods (functions inside classes)
        print("I am a person")

    def greet(self):
        print("Hello, how are you doing?")

p1 = Person() #instatitating the class
p2 = Person()

p1.set_details() #each instance has it's own copy of instance variables
p2.set_details()

#now call methods
p1.greet()
p1.display()

p2.greet()
p2.display()
