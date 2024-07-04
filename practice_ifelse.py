# 4 inputs from user and display the greatest

print("Want to find the greatest number")

n1 = int(input("Enter the number 1: "))
n2 = int(input("Enter the number 2: "))
n3 = int(input("Enter the number 3: "))
n4 = int(input("Enter the number 4: "))
greatest = n1
if n2 > greatest:
    greatest = n2
if n3 > greatest:
    greatest = n3
if n4 > greatest:
    greatest = n4
print(f"Greatest number: {greatest}")



