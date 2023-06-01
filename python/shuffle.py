# Dice Roll 

import random

dice = [1,2,3,4,5,6]

random.shuffle(dice)

print(dice)


number = range(0,7)

print(list(number))

print(random.choice(number))


#### using a function ####

number = range(0,7)

def  diceroll_random(number):
    
    print(random.choice(number))
    
    
diceroll_random(number)











 









