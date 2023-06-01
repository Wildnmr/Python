# Insert, replace, remove, delete.

list = [1,2,3,4,5,6,7]

# quick way to INSERT an int to a position in a list
list[0] = 9

print(list)

#using INSERT method in position 5 insert 100
list.insert(5,100)

print(list)

#using REPLACE method is used for string object

text = "I am number One, Two, Three, Four, and Five"

replace_text = text.replace('One', '1')

print(replace_text)

# REPLACE an int in a position by a different int or value
my_list = [1,2,3,4]

my_list[0]= "ONE"

print(my_list)

# to REMOVE a int from a list use REMOVE method

my_list.remove(4)
print(my_list)

# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']

# 'rabbit' is removed
animals.remove('rabbit')

print(animals)


# to delete a string from a string

# use either replace() with blanks "" OR use del(objectname(position))

font = "My font and colors are too much good"

print(font.replace("My", ""))


      
      

























