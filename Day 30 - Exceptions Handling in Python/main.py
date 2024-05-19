# File not found

try:
    file = open("file.txt")
    my_dict = {'key1': 'value1'}
    print(my_dict['key1'])
except FileNotFoundError:
    # print("There was an error")
    file = open("file.txt", 'w')
    file.write("Write something")
except KeyError as error_message:
    print(f"That {error_message} is not available")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")
