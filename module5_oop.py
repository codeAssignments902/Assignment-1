class NumberList:
    def __init__(self):
        self.numbers = []

    def insert(self, number):
        self.numbers.append(number)

    def search(self, x):
        if x in self.numbers:
            return self.numbers.index(x) + 1
        return -1


def main():
    n = int(input("Enter N: "))

    number_list = NumberList()
    for i in range(n):
        number_list.insert(int(input("Enter a number: ")))

    x = int(input("Enter X: "))
    print(number_list.search(x))


main()
