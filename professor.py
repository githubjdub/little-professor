import random

# Randomly generates ten (10) math problems formatted as X + Y =,
# wherein each of X and Y is a non-negative integer with n digits.
def main():
    L = get_level()
    score = 10
    for _ in range(10):
        a = generate_integer(L)
        b = generate_integer(L)
        mistakes = 0
        while True:
            try:
                print(f"{a} + {b} = ", end="")
                answer = int(input())
                #
                if answer == a + b:
                    break
                elif answer != a + b:
                    mistakes += 1
                    print("EEE")
                    if mistakes > 2:
                        print(f"{a} + {b} = {a+b}")
                        score -= 1
                        break

            except ValueError:
                mistakes += 1
                print("EEE")
                if mistakes > 2:
                    print(f"{a} + {b} = {a+b}")
                    score -= 1
                    break

    # The program should ultimately output the user’s score, a number out of 10.
    print("Score:", score)


# Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0 and n < 4:
                break
        except ValueError:
            pass
    return n


# Allows program to generate a random integer, using the level previously defined, from 0 to 9.
def generate_integer(level):
    num = ""
    for _ in range(level):
        num += str(random.randint(0, 9))
    return int(num)


if __name__ == "__main__":
    main()
