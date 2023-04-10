def prime_number(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
        if is_prime:
            return True
        else:
            return False

n = int(input("Type in a number: "))            
print(prime_number(n))