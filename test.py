class Person:
    def display(self):      #creating methods (functions inside classes)
        print("I am a person")

    def greet(self):
        print("Hello, how are you doing?")

p1 = Person() #instatitating the class
p2 = Person()

#now call methods
p1.greet()
p2.display()