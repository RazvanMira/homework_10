def median_of_three_values():
    print("Type in 3 numbers.")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    if ((a >= b) and (b >= c)) or ((c >= b) and (b >= a)):
        print("The median value is", b)
    elif ((b >= a) and (a >= c)) or ((c >= a) and (a >= b)):
        print("The median value is", a)
    elif ((a >= c) and (c >= b)) or ((b >= c) and (c >= a)):
        print("The median value is", c)

median_of_three_values()