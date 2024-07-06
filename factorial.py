n = int(input("Enter a number for it factorial: "))
fact = 1
i = 1
if n == 0 or n == 1:
    print("Factorial of", n, "is", 1)
while i <= n:
    fact *= i
    i += 1
print("Factorial of", n, "is", fact)