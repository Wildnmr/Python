

#create the place holder first before the fun

even = []

def check_even(number_list):
    
    for num in number_list:
        if num %2==0:
            even.append(num)
            print(f'The found even numbers are: {even}') 
        
       
                  
    else:
        print(f'number is not even {num}')




check_even([1,2,3,4,5])