import os       #importing the OS module

directory_path = '/'        #Selecting the directory    
files = os.listdir(directory_path)          #Listing the files from the Specified directory

# Printing Each files
for file in files:
    print(file)
