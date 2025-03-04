class Person:
    def set_details(self,name,age): #self refers to the current instance
        self.name = name #instance variables
        self.age = age
# self.age and self.name are 2 instance variables that can be used anywhere in the class
# name and age in line 2 are parameters of the method local variables that can only be used in method

    def display(self):      #creating methods (functions inside classes)
        print("My name is ",self.name)

    def greet(self):
        if self.age<80:
            print("Hello, kindly tell me your name and how I may help you")
        else:
            print("Name please and what do you need")
        self.display()
p1 = Person() #instatitating the class
p2 = Person()

p1.set_details("Bob",32) #each instance has it's own copy of instance variables
p2.set_details("Rob",30)

#now call methods
p1.greet()
p2.greet()

