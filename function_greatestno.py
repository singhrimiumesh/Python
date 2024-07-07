def greatest_no(a, b, c):
    greatest = a
    if b > greatest:
        greatest = b
    if c > greatest:
        greatest = c
    return greatest
a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))

print(greatest_no(a, b,c))