

# functions use snake_casing

# func takes 1 argument ONLY Numberic

def myfunc(n):
    if n %2==0:
        print(f'your number is even {n}') 
    else:
        print(f'not even {n}')


myfunc(4)


# when use return we need to assign the func call and print the assigment to get the result
def add_number(x,y):
    return x+y

result = add_number(5,3)*2

print(result)

# Another return func

def greet(name):
    return(f'Hello {name}')

say = greet("Sam")

print(say)





# creating function to check MULTIPLE PASSING NUMBERS as a LIST and only return even


def check_even_num(number_list):
    for num in number_list:
        if num %2==0:
            print(f'these are your found even number {num}')
        
        


check_even_num([1,2,3,4,5,6,7,8,9])

    


# creating function that takes only 1 argument numeric

def user_input(msg):
    inp = input(msg)
    try:
        return int(inp) if inp.isnumeric() else float(inp)
    except ValueError as e:
        return user_input("Please enter a numeric value")


m1=int(user_input("\nWhat was your first marking period percentage?"))
w1=float(user_input("\nWhat is the weighting of the first marking period? (in decimal)"))
m2=int(user_input("\nWhat was your second marking period percentage?"))
w2=int(user_input("\nWhat is the weighting of the second marking period? (in decimal)"))

print(m1)
print(w1)




# creating function that accepts multiple argument using *

def greet(*names):
    for name in names:
        print("Hello", name)
        
        
greet('Tony', 'Justin')


# creating function that takes only 2 arguments numeric 

def myfunc(a,b):
    return sum((a,b))*.05

result2 = myfunc(40,60)

print(result2)






# creating function that takes multiple argument numeric use tuple for arguments

def myfunc1(a=0,b=0,c=0,d=0,e=0): # notice the tuple style
    return sum((a,b,c,d,e))*.05

result1 = myfunc1(40,60,20,20)

print(result1)




# *args
# USE of *args for multipl numeric arugment postions USE *args 
# You can use any word instead of args as long as you use * in front of it example *numbers

def myfunc2(*args):
    return sum(args)*.05

result = myfunc2(40,60,20)

print(result)




# creat function that take 1 character string argument ONLY

def greet1(name, str):
    return(f'Hello {name}')

say = greet1("Buddy")

print(say)

# creating function that takes only 2 arguments str

def greet2(name1,name2):
    return(f'Hello {name1} {name2}')

say = greet2("Tommy","Manny")

print(say)

# **kwargs creating function that takes multiple argument and return dictionary **Kwargs
# When a function has the **kwargs parameter, it can accept a variable number of keyword arguments as a dictionary.
# returns the results as dictionary

def mymarket(**kwargs):
    print(kwargs)
    
mymarket(apple = 5, name = 'rocky', day ='tomorrow')


    
#note difference between an argument and a keyword argument

# argument is a value  when passing in a func also called non keyword argument

# keyword argument is when passing a value along with the variable of it
# mainly for dict{} see above func as an example







