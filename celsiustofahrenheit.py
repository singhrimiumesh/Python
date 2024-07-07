def Fahrenheit(c):
    f = (9/5)*c + 32
    return f
c = int(input("Enter the temperature in celsius: "))
print("Fahrenheit: ", Fahrenheit(c))