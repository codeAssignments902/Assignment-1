def main():
    n = int(input("Enter N: "))

    numbers = []
    for i in range(n):
        numbers.append(int(input("Enter a number: ")))

    x = int(input("Enter X: "))

    if x in numbers:
        print(numbers.index(x) + 1)
    else:
        print(-1)


main()