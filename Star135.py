n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    print(" "*(n-i), end= "")
    print("*"*(i*2-1))
#   *
#  ***
# *****
print("------------")
for i in range(1, n+1):
    print("*"*(i))
# *
# **
# ***
print("------------")
for i in range(1, n+1):
    if i == 1 or i == n:
        print("*"*n)
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*")