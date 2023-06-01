# creating function to check multiple passing numbers  as a LIST and only return even


def check_even_num(number_list):
    for num in number_list:
        if num %2==0:
            print(f'these are your found even number {num}')
        
        


check_even_num([1,2,3,4,5,6,7,8,9])


            