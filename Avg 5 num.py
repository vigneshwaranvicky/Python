#def is a keyword in Python that is used to define a function. avg is the name of the function.
#The purpose of the avg function it's likely that the function calculates the average of some set of numbers.

def average_of_five_numbers(num1, num2, num3, num4, num5):
    average = (num1 + num2 + num3 + num4 + num5) / 5
    return average

#the return statement is used to return the avg of five numbders to the calling function.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
num5 = int(input("Enter fifth number: "))

result = average_of_five_numbers(num1, num2, num3, num4, num5)
print("The average of", num1, ",", num2, ",", num3, ",", num4, num5, "is", result)
