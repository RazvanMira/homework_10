def prime_number(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
        if is_prime:
            return True
        else:
            return False

def next_prime(number):
    while True:
        number = number + 1
        if prime_number(number):
            print("Number", number, "is prime.")
            break
    return number

number = int(input("Type in a number: "))
print(next_prime(number))