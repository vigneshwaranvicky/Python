import cmath

def discriminant(a, b, c):
  return b**2 - 4*a*c

a = int(input("Enter the a of x^2: "))
b = int(input("Enter the b of x: "))
c = int(input("Enter the c: "))

result = discriminant(a, b, c)

print(f"Results for equation, {a} x**2 + {b} x+ {c} =0, are:- ",result)

if result > 0:
  print("The equation has two Real Roots.")
elif result == 0:
  print("The equation has one Real Root.")
else:
  print("The equation has no Real Roots.")
