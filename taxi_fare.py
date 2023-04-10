def taxi_fare():
    distance = float(input("Type in the distance in km: "))
    fixed_cost = 4.00
    variable_cost = 0.25
    fare_cost = fixed_cost + variable_cost * distance / 0.14
    print("The taxi fare for", distance, "km is $" + "{:.2f}".format(fare_cost))

taxi_fare()