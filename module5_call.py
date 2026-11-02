from module5_mod import NumberList


def main():
    n = int(input("Enter N: "))

    number_list = NumberList()
    for i in range(n):
        number_list.insert(int(input("Enter a number: ")))

    x = int(input("Enter X: "))
    print(number_list.search(x))


main()
