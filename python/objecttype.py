# Python objects and data structure types

'''
Object types (list,tuple,sets,dictionary)
Object data types or elements ( int, float, strings,boolean)

'''

# Create a list changeable (mutable) you can use indexing to change elements and slice to output element

my_list = [1,2,3,4,5,6]

#index  ( to call, change, run methods, and run addition, subtraction or multiplication)
print(my_list[1])
my_list[1] = 'one'
my_list[1].upper()
my_list[5]= my_list[5] +10

#slice to grap a section from a string or list of elements
print(my_list[::-1])

# add to a list

my_list = my_list + [7]

# to double the element in a list
print(my_list * 2)



# Create a set 
# returns unique elements from a data type and cast inside {}
# sets cast a list with multiple repeat elements to a set to get the unique elements.
# 

list1 = [1,2,2,2,3,4,3,5,5,6,4,3,5,7,8,9,8,7,9,10,10,10]

# to add elements to an empty set

x = set()
x.add(70)
print(x)
x.add(80)
print(x)





# create a tuple same like list but are not mutable Not Changeable

my_t = (1,2,3,4,5,6,7,8,9)

# create a dictionary (Mappings are a collection of objects that are stored by a key, and changeable)

my_dict = {'furit': 200, 'Milk': 300, 'bread': 100}

# Boolean True or False


a = True

print(1 > 2)

print(a)
print(my_dict['furit'])
print(my_list)
print(my_t)
print(my_dict)
print(set(list1)) 








