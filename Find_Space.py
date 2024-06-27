# Finding double spaces in the user entered string and replacing it by single space.

str = input("Enter the String: ")

print(str.find("  "))

str = str.replace("  ", " ")

print(str)