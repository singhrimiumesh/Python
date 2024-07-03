# dic = {
#     "save": "apple",
#     "kela": "banana",
#     "aam": "mango"
# }

# item = input("Enter the hindi word for its english version: ")

# print(dic[item])




# # set - display only once
# s = set()
# for i in range(6):
#     s.add(int(input(f"Enter number {i+1}: ")))
# print(f"Unique numbers: {s}")



# add items in a dictionary
# d = {}
# for i in range(5):
#     k = input("Enter name: ")
#     v = input("Enter age: ")
#     d.update({k : v})

# print(d)


d = {}
for i in range(5):
    d.update({input("Enter k:"): input("Enter v: ")})

print(d)