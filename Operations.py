num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

Add = float(num1) + float(num2)

sub = float(num1) - float(num2)

mul = float(num1) * float(num2)

div = float(num1) / float(num2)

mod = float(num1) % float(num2)

exp = float(num1) ** float(num2)

print('The Addition of {0} and {1} is {2}' .format(num1,num2,Add))
print('The Subtraction of {0} and {1} is {2}' .format(num1,num2,sub))
print('The Multiplication of {0} and {1} is {2}' .format(num1,num2,mul))
print('The Division of {0} and {1} is {2}' .format(num1,num2,div))
print('The Modules of {0} and {1} is {2}'.format(num1,num2,mod))
print('The Exponent of {0} and {1} is {2}'.format(num1,num2,exp))