# ***
# **
# *

def pattern(n):
    for i in range(0, n):
        print("*"*(n-i))

n = int(input("Enter number: "))
pattern(n)