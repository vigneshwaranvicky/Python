print("1.Rectangle, 2.Square, 3.Triangle or 4.Circle")
# Initialization variable value is 0
area = 0.0

while (1):
    choice = int(input("Enter your Choice: "))

    if choice == 1:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width

        print(f"The area of the Rectangle is {area}")

    elif choice == 2:
        side = float(input("Enter the side of the square: "))
        area = side * side

        print(f"The area of the square is {area}")

    elif choice == 3:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 1/2 * base * height

        print(f"The area of the Triangle is {area}")

    elif choice == 4:
        radius = float(input("Enter the radius of the circle: "))
        # The pi value is 3.4
        area = 3.4 * radius * radius

        print(f"The area of the circle is {area}")

    else:

        print("Invalid shape entered. Try again...")