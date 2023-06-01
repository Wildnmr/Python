# create an input

# Enter a string or a number

print(input("Enter your name here: "))

#Input accepts only number

print(int(input("enter a number here: ")))



# while the number is NOT IN the list keep asking and if the number is good confirm

import os
import sys
import random


def select_choice(num):
    choice = 'Wrong'
    acceptable_range = [1,2,3]
    within_range = False
    
    while choice.isdigit() == False or within_range == False:
        choice = print('Enter a number 1,2 or 3: ')
        
        if choice.isdigit() == False:
            print('Wrong number try again')
            
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('Sorry you are out of range try again')
                within_range = False
    return int(choice)

select_choice(5)








            
            
            



            
    

 
    
    
  
    
     
    
    
        
     
          
    
    
    


    
    


    
        
        
        
   
        
    


    



     
         
             
        
         
             
         


   

    






   

 



     
     
    
    
        
     

    
    
    



