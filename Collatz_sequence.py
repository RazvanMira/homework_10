def collatz(number):
    if number % 2 == 0:
            print(number // 2)
            return number // 2
    elif number % 2 == 1:
            number = 3 * number + 1
            print(number)
            return number

def main() -> None:
    number = int(input("Type in a number: ")) 
    while number > 2:
        number = collatz(number)

if __name__ == "__main__":
    main()