n = int(input("Enter the number of rows: "))

for i in range(0, n):
    print(" " * n-i, end= "")
    print("*"* (i*2-1))