def greatest_common_divisor(a: int, b: int):
    d = min(a, b)
    for i in range (1, d+1):
        if a % i == 0 and b % i == 0:
            d = i
    return d

print("Introduce the numerator and denominator:")

def reduce_fraction_to_lowest_terms():
    numerator = int(input("numerator = "))
    denominator = int(input("denominator = "))
    lowest_numerator = numerator / greatest_common_divisor(numerator, denominator)
    lowest_denominator = denominator / greatest_common_divisor(numerator, denominator)
    print(lowest_numerator, lowest_denominator)

reduce_fraction_to_lowest_terms()