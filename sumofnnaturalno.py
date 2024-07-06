# find the sum of 1st n natural numbers.
n = int(input("Enter a natural number: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print(f"Sum of first {n} natural numbers: {sum}")