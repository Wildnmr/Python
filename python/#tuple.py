#tuple unpacking

my_t = (1,2,3,4,5,6,7,8,9,10)


for num in my_t:
    print(f'This is every number in the tuple {num}')
    
print(len(my_t))
print(type(my_t))

#Unpacking

my_list = [(2,4),(5,6),(7,8)]
 
print(my_list)
'''
for a,b in my_list:
    print(a)
    print(b)
''' 

for a,b in my_list:
    
    if a and b %2==0:
        
        print(a,b)
else:
    print("not divisiable ")
    
    
        
  
        
        
    
           
        
        
        
    
    
    




    
    