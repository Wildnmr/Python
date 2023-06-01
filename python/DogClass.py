# Create class using camel casing uppercare of the begining of each word   OOP
# Attribute class
# and a method called speak

class Dog():

    specie = "Animal"  #<-- class level assigment

    def __init__(self,breed,name,size):   #<-- creating the arguments for attribute.(constructor)
        
        self.breed = breed            #<--- assigining attribute 
        self.name = name
        self.size = size

    # if to create a method to take action

    def speak(self,number):
        print(f'WOOF! my name is {self.name} and my number is {number}')


my_pet = Dog(breed = 'Golden Retriver', name = 'Roy', size = 200)    #<--- instatiating the class


# call the attribute for Dog class or the speak method

my_pet.size




     


    
