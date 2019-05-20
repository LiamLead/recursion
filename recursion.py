number = int(input("Number: "))


def recursion(m):
    if m <= 0:
        return 0
    else:
        return m + recursion(m - 1)

print(recursion(number))