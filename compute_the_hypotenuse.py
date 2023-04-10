import math

def hypotenuse():
    side_one = float(input("The first side of the triangle is: "))
    side_two = float(input("The second side of the triangle is: "))
    hypotenuse = math.sqrt(side_one ** 2 + side_two ** 2)
    print("The hypotenuse is: ", hypotenuse)

hypotenuse()
