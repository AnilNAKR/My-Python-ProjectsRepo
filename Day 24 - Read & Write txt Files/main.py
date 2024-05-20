# Write into the file
with open("myFile.txt", mode='w') as file:
    file.write("My full name is Anil")

# append content into the file
with open("myFile.txt", mode = 'a') as file:
    file.write("\nSorry My full name is Anil Kumar Reddy")

# this will create a new file, if the file is not present
with open("anil.txt", mode='w') as file:
    file.write("Hey, How are you!")


# Alternate method
# Reading the file

# file = open("myFile.txt")
# content = file.read()
# print(content)
# file.close()

# Below method is used to access the content and doesn't need to
#  worry about closing the file)

# with open("myFile.txt") as file:
#     print(file.read())


