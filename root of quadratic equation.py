import cmath

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

discriminant = (num2**2) - (4*num1*num3)

a = (-num2-cmath.sqrt(discriminant))/(2*num1)
b = (-num2+cmath.sqrt(discriminant))/(2*num1)
print('The solution are {0} and {1}'.format(a,b))