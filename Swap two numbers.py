
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("Before Swapping")
print(f'First number {a}, Second Number{b}')

temp = a
a = b
b = temp

print("After Swapping")
print(f'First number {a}, Second Number{b}')