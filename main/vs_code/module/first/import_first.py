from first import calculator
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
op = input("Enter the operator : ")
obj = calculator(num1,num2,op)
print(obj.calc())