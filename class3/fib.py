limit = int(input("enter the limit: "))

first = 0
second = 1

next = first + second

while next < limit:
    print(next)
    first = second
    second = next
    next = first + second