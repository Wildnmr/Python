#two.py
# this is a script/module that is importing another script and calling its function

import one

one.my_func()

if __name__ == '__main__':
    
    print("I am direct func from two.py")
else:
    
    print("I am imported function from a different module one.py")





  
  



