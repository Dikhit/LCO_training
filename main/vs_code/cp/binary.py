def check(string) :  
    p = set(string)  
    s = {'0', '1'}  
    
    if s == p or p == {'0'} or p == {'1'}: 
        return True
    else : 
        return False

num_test_case = int(input("Enter the number of test case : "))
while num_test_case > 0:
    binary_number = 0
    input_number = input("Enter the number : ")
    power = len(input_number)
    if check(input_number):
        for index,value in enumerate(input_number):
            power = power - 1
            binary_number = binary_number +  ( (2**power) * int(value))
        print(binary_number)
    num_test_case -= 1 