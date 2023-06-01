# Dice Roll 

import random

dice = [1,2,3,4,5,6]

random.shuffle(dice)

print(dice)


number = range(0,7)

print(list(number))

print(random.choice(number))

# shuffle func

from random import shuffle

my_dice = [1,2,3,4,5,6]

def shuffle_dice(my_dice):
    
    shuffle(my_dice)    #to shuffle
    print(random.choice(my_dice))  # to random select a nunber from a list
    
    
    
    print(my_dice)
    


shuffle_dice(my_dice)

















 









